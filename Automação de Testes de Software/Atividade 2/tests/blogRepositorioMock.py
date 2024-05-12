from src.blogRepositorio import BlogRepositorio

class ExcecaoUserIdNaoEncontrado(Exception):
    pass

class BlogRepositorioMock(BlogRepositorio):
    def __init__(self):
        self.Listposts = [{
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

    def posts(self):
        return self.Listposts

    def post_by_user_id(self, userId: int):
        for post in self.Listposts:
            if post['id'] == userId:
                return post
        raise ExcecaoUserIdNaoEncontrado
        