import pytest

from flunt.localization.flunt_regex_patterns import FluntRegexPatterns
from tests.mocks.entity.sample_entity import SampleEntity


@pytest.fixture(scope="module")
def entity_mock() -> SampleEntity:
    """Fixture to return a SampleEntity instance."""
    return SampleEntity()


@pytest.fixture(scope="module")
def regex() -> FluntRegexPatterns:
    """Fixture to return a FluntRegexPatterns instance."""
    return FluntRegexPatterns()
