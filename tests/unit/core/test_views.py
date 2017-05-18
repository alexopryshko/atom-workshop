import pytest
import mock
from core.models import Todo
from tests.base.utils import authenticate


class TestIndex:
    @pytest.fixture()
    def todo1(self, db):
        return Todo.objects.create(title='todo1')

    @mock.patch('core.views.network')
    def test_index(self, network_mock, http, todo1):
        network_mock.return_value = None
        with authenticate(user):
            response = http.get('/')
        assert response.status_code == 200
        assert 'todo' in response.content.decode('utf-8')


class TestCreate:
    @pytest.fixture()
    def todo1(self, db):
        return Todo.objects.create(title='todo1')

    @pytest.fixture(params=[
        'todo1',
        'todo1\'',
        'todo2'
    ])
    def todos(self, db, request):
        return Todo.objects.create(title=request.param)

    @pytest.mark.parametrize('todo', [
        'todo1',
        'todo1\'',
        'todo2'
    ])
    def test_success_create(self, db, todo, http):
        response = http.post('/create', data={'title': todo})
        assert response.status_code == 302
        assert Todo.objects.filter(title=todo).exists()

    def test_error_unique(self, http, todo1):
        response = http.post('/create', data={'title': todo1.title})
        assert response.status_code == 400
