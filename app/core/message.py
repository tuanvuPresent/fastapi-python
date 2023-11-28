from enum import Enum


class ErrorMessage(Enum):
    def __new__(cls, code, message):
        obj = object.__new__(cls)
        obj._value_ = code
        obj.code = code
        obj.message = message
        return obj
    
    
    SERVER_ERROR = (10001, 'An error occurred, please try again')
    NOT_FOUND = (10002, 'Not found')
    INVALID_AUTH = (10003, 'Not authenticated')
    NOT_PERMISSION = (10004, 'Not permission denied')
    BOOK_NAME_MAX_LENGTH = (10005, 'Max length not than 63')
