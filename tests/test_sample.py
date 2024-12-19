import pytest

from sample import reverse_string


@pytest.mark.parametrize("string, expected_result", [
	("hello", "olleh"),
	("world", "dlrow"),
	("12345", "54321"),
	("", ""),
])
def test_reverse_string(string, expected_result):
	assert reverse_string(string) == expected_result
