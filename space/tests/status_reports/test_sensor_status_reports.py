from space.components import Sensor


def test_integrity_status_report():
    reactor = Sensor(base_range=2000, focus=90, pitch=90, yaw=90)
    assert reactor.status_report["integrity"] == reactor.integrity, \
        "Sensor integrity is innacurately reported"


def test_lor_integrity_status_report():
    reactor = Sensor(base_range=2000, focus=90, pitch=90, yaw=90)
    reactor.degrade(0.5)
    assert reactor.status_report["integrity"] == reactor.integrity, \
        "Sensor integrity is innacurately reported"


def test_is_active_status_report():
    reactor = Sensor(base_range=2000, focus=90, pitch=90, yaw=90)
    assert reactor.status_report["is_active"] == reactor.is_active, \
        "Sensor is_active is innacurately reported"


def test_is_active_status_report_no_integrity():
    reactor = Sensor(base_range=2000, focus=90, pitch=90, yaw=90)
    reactor.degrade(1)
    assert reactor.status_report["is_active"] == reactor.is_active, \
        "Sensor is_active is innacurately reported"


def test_is_active_status_report_no_power():
    reactor = Sensor(base_range=2000, focus=90, pitch=90, yaw=90)
    reactor.powered_on = False
    assert reactor.status_report["is_active"] == reactor.is_active, \
        "Sensor is_active is innacurately reported"


def test_powered_on_status_report():
    reactor = Sensor(base_range=2000, focus=90, pitch=90, yaw=90)
    reactor.powered_on = False
    assert reactor.status_report["powered_on"] == reactor.powered_on, \
        "Sensor powered_on is innacurately reported"


def test_focus_status_report():
    r = Sensor(base_range=2000, focus=90, pitch=90, yaw=90)
    assert r.status_report["focus"] == r.focus, \
        "Sensor focus is innacurately reported"


def test_focus_status_report_narraow():
    r = Sensor(base_range=2000, focus=10, pitch=90, yaw=90)
    assert r.status_report["focus"] == r.focus, \
        "Sensor focus is innacurately reported"


def test_focus_status_report_wide():
    r = Sensor(base_range=2000, focus=180, pitch=90, yaw=90)
    assert r.status_report["focus"] == r.focus, \
        "Sensor focus is innacurately reported"


def test_base_range_status_report_short():
    r = Sensor(base_range=100, focus=10, pitch=90, yaw=90)
    assert r.status_report["base_range"] == r.base_range, \
        "Sensor base_range is innacurately reported"


def test_base_range_status_report():
    r = Sensor(base_range=2000, focus=10, pitch=90, yaw=90)
    assert r.status_report["base_range"] == r.base_range, \
        "Sensor base_range is innacurately reported"


def test_base_range_status_report_long():
    r = Sensor(base_range=20000, focus=180, pitch=90, yaw=90)
    assert r.status_report["base_range"] == r.base_range, \
        "Sensor base_range is innacurately reported"


def test_current_range_status_report_short():
    r = Sensor(base_range=100, focus=10, pitch=90, yaw=90)
    assert r.status_report["current_range"] == r.range, \
        "Sensor range is innacurately reported"


def test_current_range_status_report():
    r = Sensor(base_range=2000, focus=10, pitch=90, yaw=90)
    assert r.status_report["current_range"] == r.range, \
        "Sensor range is innacurately reported"


def test_current_range_status_report_long():
    r = Sensor(base_range=20000, focus=180, pitch=90, yaw=90)
    assert r.status_report["current_range"] == r.range, \
        "Sensor range is innacurately reported"


def test_pitch_degrees_status_report_neg():
    r = Sensor(base_range=100, focus=10, pitch=90, yaw=90)
    assert r.status_report["pitch_degrees"] == r.pitch_degrees, \
        "Sensor pitch_degrees is innacurately reported"


def test_pitch_degrees_status_report():
    r = Sensor(base_range=100, focus=10, pitch=-90, yaw=90)
    assert r.status_report["pitch_degrees"] == r.pitch_degrees, \
        "Sensor pitch_degrees is innacurately reported"


def test_yaw_degrees_status_report_neg():
    r = Sensor(base_range=100, focus=10, pitch=90, yaw=90)
    assert r.status_report["yaw_degrees"] == r.yaw_degrees, \
        "Sensor yaw_degrees is innacurately reported"


def test_yaw_degrees_status_report():
    r = Sensor(base_range=100, focus=10, pitch=-90, yaw=90)
    assert r.status_report["yaw_degrees"] == r.yaw_degrees, \
        "Sensor yaw_degrees is innacurately reported"
