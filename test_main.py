import pytest
from main import validate_user_input

def test_validate_user_input():
    empty_input=""
    with pytest.raises(ValueError, match="No input"):
        validate_user_input(empty_input)
    