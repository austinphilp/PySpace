from uuid import uuid4 as uuid


class IdentityMixin(object):
    @property
    def object_id(self):
        if not hasattr(self, '_object_id'):
            self._object_id = uuid().hex[:8]
        return self._object_id
