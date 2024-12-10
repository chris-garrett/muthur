## Files

```muthur/result.py
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

```

```muthur/__init__.py
def main() -> None:
    print("Hello from muthur!")

```

````muthur/llm/prompt.py
import os
from typing import List

from muthur.result import Result


def files_to_markdown(files: List[str], relative_root: str = None) -> Result[str]:
    #
    # Build markdown from a list of files
    #
    try:
        contents = []
        for file in files:
            with open(file, "r") as file_content:
                file_name = (
                    file
                    if relative_root is None
                    else os.path.relpath(file, relative_root)
                )

                content = file_content.read()
                contents.append(f"""```{file_name}\n{content}\n```""")

        content = f"## Files\n\n{'\n\n'.join(contents)}"
        return Result.ok(content)
    except Exception as e:
        return Result.error(f"Error building markdown: {e}")


def files_to_markdown_file(
    files: List[str], markdown_file: str, relative_root: str = None
) -> Result:
    #
    # Write the content of the files to a markdown file
    #
    try:
        content = files_to_markdown(files, relative_root=relative_root)
        with open(markdown_file, "w") as f:
            f.write(content.data)

        return Result.ok()
    except Exception as e:
        return Result.error(f"Error writing to file: {e}")

````

```muthur/llm/__init__.py

```
