import pytest


@pytest.fixture
def fixture_card_number():
    return [
        "1234567890123",
        "12345678901234",
        "123456789012345",
        "1234567890123456",
        "12345678901234567",
        "123456789012345678",
        "1234567890123456789",
    ]


@pytest.fixture
def fixture_account_number():
    return [
        "12345678901234567890",
        "51758524928291403976",
        "34263820582001592812",
        "89272095094888418968",
        "44001588067172575292",
    ]


@pytest.fixture
def fixture_processing():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def fixture_date():
    return [
        "2024-01-01",
        "2019-07-03T18:35:29.512364",
        "2012-09-28T02:08:58.425572",
        "2018-09-12T21:27:25.241689",
        "2018-10-14T08:21:33.419441",
    ]


@pytest.fixture
def fixture_invalid_date():
    return ["", "2025-25-01", "24-01-01", "2024-01-32", "no date"]
