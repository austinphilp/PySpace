from space.components import Reactor


def test_integrity_status_report():
    reactor = Reactor(max_output=20)
    assert reactor.status_report["integrity"] == reactor.integrity, \
        "Reactor integrity is innacurately reported"


def test_lor_integrity_status_report():
    reactor = Reactor(max_output=20)
    reactor.degrade(0.5)
    assert reactor.status_report["integrity"] == reactor.integrity, \
        "Reactor integrity is innacurately reported"


def test_is_active_status_report():
    reactor = Reactor(max_output=20)
    assert reactor.status_report["is_active"] == reactor.is_active, \
        "Reactor is_active is innacurately reported"


def test_is_active_status_report_no_integrity():
    reactor = Reactor(max_output=20)
    reactor.degrade(1)
    assert reactor.status_report["is_active"] == reactor.is_active, \
        "Reactor is_active is innacurately reported"


def test_is_active_status_report_no_power():
    reactor = Reactor(max_output=20)
    reactor.powered_on = False
    assert reactor.status_report["is_active"] == reactor.is_active, \
        "Reactor is_active is innacurately reported"


def test_powered_on_status_report():
    reactor = Reactor(max_output=20)
    reactor.powered_on = False
    assert reactor.status_report["powered_on"] == reactor.powered_on, \
        "Reactor powered_on is innacurately reported"


def test_current_output_status_report():
    r = Reactor(max_output=20)
    assert r.status_report["current_output"] == r.current_output, \
        "Reactor current_output is innacurately reported"


def test_max_output_status_report():
    r = Reactor(max_output=20)
    assert r.status_report["max_output"] == r.initial_max_output, \
        "Reactor max_output is innacurately reported"


def test_max_output_status_report_lor_integrity():
    r = Reactor(max_output=20)
    r.degrade(0.2)
    assert r.status_report["max_output"] == r.initial_max_output, \
        "Reactor max_output is innacurately reported"
