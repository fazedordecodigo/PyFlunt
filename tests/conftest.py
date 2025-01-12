import pytest

from flunt.localization.flunt_regex_patterns import get_pattern
from tests.mocks.entity.sample_entity import SampleEntity


@pytest.fixture(scope="module")
def entity_mock() -> SampleEntity:
    """Fixture to return a SampleEntity instance."""
    return SampleEntity()


@pytest.fixture(scope="module")
def regex() -> get_pattern:
    """Fixture to return a get_pattern instance."""
    return get_pattern()
