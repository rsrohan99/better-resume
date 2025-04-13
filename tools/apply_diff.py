from typing import Annotated
import os
import time


async def apply_diff(
    file: Annotated[str, "The file to apply diff, either 'html' or 'css'"],
    search_content: Annotated[
        str,
        "The exact code to replace within start_line and end_line of the file. The code must match exactly including proper indendation.",
    ],
    replace_content: Annotated[str, "The new code to replace the old code with."],
    start_line: Annotated[int, "The start line of the diff to apply, indexed from 1."],
    end_line: Annotated[int, "The end line of the diff to apply, indexed from 1."],
) -> str:
    """
    Useful for applying a diff to a file using search and replace. use exact code in the search_content, if unsure use read_file first.
    """

    try:
        time.sleep(3)
        print(f"\nApplying diff to {file} file...\n")
        base_dir = "html_resume"
        file_to_read = os.path.join(
            base_dir, "resume.html" if file == "html" else "style.css"
        )
        with open(file_to_read, "r") as f:
            lines = f.readlines()
            start_line = int(start_line)
            end_line = int(end_line)
            # Check if the search content matches the specified lines
            if (
                search_content.strip()
                in "".join(lines[start_line - 1 : end_line]).strip()
            ):
                content_to_replace = "".join(lines[start_line - 1 : end_line]).replace(
                    search_content.strip(), replace_content.strip()
                )
                # Replace the specified lines with the new content
                lines[start_line - 1 : end_line] = content_to_replace.splitlines(
                    keepends=True
                )
                with open(file_to_read, "w") as f:
                    f.writelines(lines)
                return f"Diff applied successfully to {file} file."
            else:
                return "Search content does not match the specified lines. Diff not applied. Please use the read_file tool and make sure to use the exact code."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {str(e)}. Try again..."
