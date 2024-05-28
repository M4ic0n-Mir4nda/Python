from abc import ABCMeta, abstractmethod

class BlogRepositorio(metaclass=ABCMeta):
    @abstractmethod
    def posts(self):
        pass

    @abstractmethod
    def post_by_user_id(self, userId: str):
        pass