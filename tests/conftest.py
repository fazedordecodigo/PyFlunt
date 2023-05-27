import pytest

from flunt.localization.flunt_regex_patterns import FluntRegexPatterns
from tests.mocks.entity.sample_entity import SampleEntity


@pytest.fixture(scope="module")
def entityMock() -> SampleEntity:
    return SampleEntity()


@pytest.fixture(scope="module")
def regex() -> FluntRegexPatterns:
    return FluntRegexPatterns()
