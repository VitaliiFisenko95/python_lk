# Custom errors


class BaseCustomException(Exception):
    pass


class TriangleValidationError(BaseCustomException):
    def __init__(self, *args, **kwargs):
        # some operations
        msg = f'{args} {kwargs}'
        super().__init__(msg)
