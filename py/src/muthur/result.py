from typing import Generic, TypeVar, Optional, overload, Union

T = TypeVar("T")


class Result(Generic[T]):
    @overload
    @staticmethod
    def ok() -> "Result[None]": ...

    @overload
    @staticmethod
    def ok(data: T) -> "Result[T]": ...

    @staticmethod
    def ok(data: Optional[T] = None) -> "Result[Union[T, None]]":
        return Result(status=0, data=data)

    @staticmethod
    def error(error: str) -> "Result[None]":
        return Result(status=1, error=error)

    @staticmethod
    def not_found() -> "Result[None]":
        return Result(status=404)

    def is_ok(self) -> bool:
        return self.status == 0

    def is_not_found(self) -> bool:
        return self.status == 404

    def __init__(
        self, status: int, error: Optional[str] = None, data: Optional[T] = None
    ):
        self.status = status
        self.error = error
        self.data = data

    def __repr__(self):
        return f"Result(status={self.status}, error={self.error}, data={self.data})"


ResultType = Result[Union[T, None]]
