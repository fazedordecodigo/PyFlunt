import pytest

from tests.mocks.entity.sample_entity import SampleEntity


@pytest.fixture(scope='module')
def entityMock():
    return SampleEntity()
