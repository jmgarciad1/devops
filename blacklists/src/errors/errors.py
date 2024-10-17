class ApiError(Exception):
    code = 422
    description = "Default message"

class IncompleteParams(ApiError):
    code = 400
    description = "Bad request"


class InvalidParams(ApiError):
    code = 400
    description = "Bad request"


class Unauthorized(ApiError):
    code = 401
    description = "Unauthorized"


class NotFoundError(ApiError):
    code = 404
    description = "Item does not exist"
