import pytest

from datetime import datetime
from datetime import timedelta

from app.task import Task
from app.task import DueDateError

###########################

# funcion para "skipif"

def is_available_to_skip():
    return True
###########################

# FIXTURES: son funciones que se ejecutan antes de las pruebas unitarias.
# Su objetivo es proveer datos a dichas pruebas

@pytest.fixture
def username():
    print('>>>Ejecutamos el codigo antes de la prueba')
    yield 'Cody'
    print('>>>Ejecutamos el codigo despues de la prueba')

@pytest.fixture
def password():
    return 'Password'

def test_username(username):
    print(username)
    assert username == 'Cody'

def test_username_and_password(username, password):
    print(username)
    print(password)
    assert username == 'Cody'
    assert password == 'Password'

##########################

class TestTask():

    
    @pytest.mark.news
    def test_task(self):
        assert True
    
    # PARAMETRIZACION DE PRUEBAS: una prueba unitaria puede ejecutarse una N cant de veces a partir de diferentes valores.
    
    @pytest.mark.news
    @pytest.mark.parametrize(
        'title, description, assigned_to, due_date',
        [
            ('Title 1','Description 1', 'User 1', datetime.now() + timedelta(days=1)),
            ('Title 2','Description 2', 'User 2', datetime.now() + timedelta(days=1)),
            ('Title 3','Description 3', 'User 3', datetime.now() + timedelta(days=1)),
            ('Title 4','Description 4', 'User 4', datetime.now() + timedelta(days=1)),
            ('Title 5','Description 5', 'User 5', datetime.now() + timedelta(days=1))
        ]
    )
    def test_new_task(self, title, description, assigned_to, due_date):
        due_date = datetime.now() + timedelta(days=1)
        task = Task(title, description, assigned_to, due_date)

        assert task.title == title
        assert task.description == description
        assert task.assigned_to == assigned_to
        assert task.due_date == due_date
    
    # Marcadores para pruebas: pytest app/test/test_task.py -v -m due_date
    # Para eliminar los warning cuando lanzamos pruebas con marcadores: cramos un archivo "pytest.ini" y confiuramos los "markers"
    # Pueden ponerse varios marcadores para una prueba

    @pytest.mark.due_date
    def test_due_date_error(self):
        with pytest.raises(DueDateError):
            due_date = datetime.now() - timedelta(days=1)
            Task('Title', 'Description', 'diega_ga', due_date)

    @pytest.mark.due_date
    def test_due_date(self):
        due_date = datetime.now() + timedelta(days=1)
        task = Task('Title', 'Description', 'diega_ga', due_date)
        assert task.due_date > datetime.now()
    
    #######################

    # skip
    # skipIf

    @pytest.mark.skip(reason='Lo siento, la pruba no cumple con los requerimientos')
    def test_skip_1(self):
        pass

    @pytest.mark.skipif(is_available_to_skip(), reason='Lo siento, la pruba no cumple con los requerimientos')    # si la funcion da FALSE, la prueba se ejecutara
    def test_skip_2(self):
        pass
    
    #######################