import pytest
from tests.blogRepositorioMock import BlogRepositorioMock
from tests.blogRepositorioMock import ExcecaoUserIdNaoEncontrado

def test_busca_todos_posts():
    blogRepositorio = BlogRepositorioMock()
    blog = blogRepositorio.posts()

    assert blog == [{
                        "userId": 1,
                        "id": 1,
                        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
                    },
                    {
                        "userId": 1,
                        "id": 2,
                        "title": "qui est esse",
                        "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
                    },
                    {
                        "userId": 1,
                        "id": 3,
                        "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
                        "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
                    },]

def test_busca_post_por_id():
    blogRepositorio = BlogRepositorioMock()
    blog = blogRepositorio.post_by_user_id(1)

    assert blog['id'] == 1
    assert blog['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'
    assert blog['body'] == 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'

def test_busca_post_id_inexistente_gera_excecao():
    with pytest.raises(ExcecaoUserIdNaoEncontrado):
        blogRepositorio = BlogRepositorioMock()
        blogRepositorio.post_by_user_id(4)

@pytest.fixture
def post():
    return [{'userId' : 1,
            'Id' : 1,
            'title' : 'Titulo teste 1',
            'body' : 'Conteudo do blog 1'},
            {'userId' : 2,
            'Id' : 2,
            'title' : 'Titulo teste 2',
            'body' : 'Teste de conteudo do blog 2'}]

def test_busca_todos_posts_fixture(post):
    assert post == [{'userId' : 1,
            'Id' : 1,
            'title' : 'Titulo teste 1',
            'body' : 'Conteudo do blog 1'},
            {'userId' : 2,
            'Id' : 2,
            'title' : 'Titulo teste 2',
            'body' : 'Teste de conteudo do blog 2'}]