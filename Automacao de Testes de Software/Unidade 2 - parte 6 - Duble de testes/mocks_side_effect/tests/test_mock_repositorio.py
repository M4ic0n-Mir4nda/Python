from datetime import date
from tests.livroRepositorioMock import LivroRepositorioMock 
from tests.livroRepositorioMock import ExcecaoLivroNaoEncontrado
from src.livro import Livro 
import pytest
from unittest.mock import Mock

class ExcecaoLivroNaoEncontrado(Exception):
    pass

@pytest.fixture
def livro():
    l1 = Livro('111', 'Python para iniciantes', 50.0, date.today)
    return l1

def test_busca_livro_por_id(livro):
    livroRepositorio = Mock()
    livroRepositorio.obter_livro.return_value = livro
    livroRepositorio.numero_de_chamadas.return_value = 1
    resultado = livroRepositorio.obter_livro('111')

    assert resultado.id == '111'
    assert resultado.titulo == 'Python para iniciantes'
    assert livroRepositorio.numero_de_chamadas() == 1


def test_busca_livro_por_id_inexistente_gera_excecao(livro):
    livroRepositorio = Mock()
    livroRepositorio.obter_livro.side_effect = ExcecaoLivroNaoEncontrado

    with pytest.raises(ExcecaoLivroNaoEncontrado):
        livroRepositorio.obter_livro('222')
