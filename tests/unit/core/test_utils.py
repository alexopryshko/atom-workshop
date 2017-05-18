import pytest


# from core.utils import dev


def dev(a, b):
    if b == 0:
        return
    return a / b


class TestDev:
    @pytest.yield_fixture()
    def gen_5(self):
        yield 5

    @pytest.fixture(params=[1, 2, 3])
    def gen_1_2_3(self, request):
        return request.param

    @pytest.fixture()
    def gen_0(self):
        return 0

    def test_zero(self, gen_5, gen_1_2_3):
        result = dev(gen_5, gen_1_2_3)
        assert result == gen_5 / gen_1_2_3

    def test_success(self, gen_5):
        result = dev(gen_5, 2)
        assert result == 2.5
