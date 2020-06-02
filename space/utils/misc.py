class ExpirableAttribute(object):
    def __init__(self, expires_in=3):
        self.expires_in = expires_in
        self._value = None

    def is_expired(self, instance):
        return (
            instance._expirable_attr_expiry.get(id(self), 0)
            < instance.system.time()
        )

    def value(self, instance):
        return instance._expirable_attr_vals.get(id(self))

    def _init_expirable_attrs(self, instance):
        instance._expirable_attr_vals = {}
        instance._expirable_attr_expiry = {}

    def __get__(self, instance, owner):
        if not hasattr(instance, '_expirable_attrs'):
            self._init_expirable_attrs(instance)
        if not self.is_expired(instance):
            return self.value(instance)

    def __set__(self, instance, value):
        self.expires_on = instance.system.time() + self.expires_in
        self._value = value


class CacheMap(object):
    def __init__(self, expiry=3):
        self._data = {}
        self._expiry_map = {}
        self._expiry = expiry
        self._tick = 0

    def __setitem__(self, key, val):
        if key not in self._data or self._expiry_map[key] <= self._tick:
            self._data[key] = val()
            self._expiry_map[key] = self._tick + self._expiry

    def __getitem__(self, key):
        return self._data[key]

    def tick(self):
        self._tick += 1


class GameClock(object):
    instance = None

    class __GameClock(object):
        def __init__(self):
            self.tick = 0

        def __str__(self):
            return repr(self) + self.val

    def __init__(self):
        if not GameClock.instance:
            GameClock.instance = GameClock.__GameClock()

    @classmethod
    def time(cls):
        return cls.instance.tick

    @classmethod
    def next(cls):
        cls.instance.tick += 1

    def __getattr__(self, name):
        return getattr(self.instance, name)


GameClock()
