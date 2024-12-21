from src.processing import filter_by_state, sort_by_date


# filter_by_state
def test_filter_by_state(fixture_processing):
    assert filter_by_state(fixture_processing)


def test_filter_by_state_no_state():
    assert filter_by_state([]) == []


def test_filter_by_state_different_value_of_state(fixture_processing):
    assert filter_by_state(fixture_processing, "CANCELED")
    assert filter_by_state(fixture_processing, "EXECUTED")
    assert filter_by_state(fixture_processing, "something") == []
    assert filter_by_state(fixture_processing, "") == []


# sort_by_date
def test_sort_by_date_no_sort_order(fixture_processing):
    assert sort_by_date(fixture_processing)


def test_sort_by_date_set_sort_order(fixture_processing):
    assert sort_by_date(fixture_processing, True)
    assert sort_by_date(fixture_processing, False)
    assert sort_by_date(fixture_processing, "smth")
