from typing import Annotated


async def read_file(
    file: Annotated[str, "The file to read, either 'html' or 'css'"],
) -> str:
    """
    Useful for getting the contents of either the html or css file.
    """

    try:
        print(f"\nGetting contents from file: {file}...\n")
        file_to_read = "resume.html" if file == "html" else "style.css"
        with open(file_to_read, "r") as f:
            contents = f.readlines()
            return "\n".join(
                [f"{i + 1} | {line.strip()}" for i, line in enumerate(contents)]
            )
    except FileNotFoundError:
        return "File not found."
