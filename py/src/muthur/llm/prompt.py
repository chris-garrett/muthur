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
