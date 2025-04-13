from typing import Annotated


# apply_diff: Replace code in a file using a search and replace block. Must match existing content exactly. Use read_file first if unsure.
# Parameters: file (required) - which file to read, either html or css, search_content(required) - the exact code to replace within start_line and end_line of the file, replace_content (required) - the new code to replace the old code with, start_line (required), end_line (required)
async def apply_diff(
    file: Annotated[str, "The file to apply diff, either 'html' or 'css'"],
    search_content: Annotated[
        str, "The exact code to replace within start_line and end_line of the file."
    ],
    replace_content: Annotated[str, "The new code to replace the old code with."],
    start_line: Annotated[int, "The start line of the diff to apply."],
    end_line: Annotated[int, "The end line of the diff to apply."],
) -> str:
    """
    Useful for applying a diff to a file using search and replace. use exact code in the search_content, if unsure use read_file first.
    """

    try:
        print(f"\nApplying diff to {file} file...\n")
        file_to_read = "resume.html" if file == "html" else "style.css"
        with open(file_to_read, "r") as f:
            lines = f.readlines()
            # Check if the search content matches the specified lines
            if lines[start_line - 1 : end_line] == search_content.splitlines(
                keepends=True
            ):
                # Replace the specified lines with the new content
                lines[start_line - 1 : end_line] = replace_content.splitlines(
                    keepends=True
                )
                with open(file_to_read, "w") as f:
                    f.writelines(lines)
                return f"Diff applied successfully to {file} file."
            else:
                return "Search content does not match the specified lines. Diff not applied. Please use the read_file tool and make sure to use the exact code."
    except FileNotFoundError:
        return "File not found."
