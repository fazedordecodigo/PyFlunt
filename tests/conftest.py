from __future__ import annotations

import pytest
from faker import Faker

from tests.mocks.entity.sample_entity import SampleEntity

fake = Faker()


@pytest.fixture(scope="module")
def entity_mock() -> SampleEntity:
    """Fixture to return a SampleEntity instance."""
    return SampleEntity()
