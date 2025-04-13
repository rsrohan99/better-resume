from typing import Annotated
import os
import time
import re


async def apply_diff(
    file: Annotated[str, "The file to apply diff, either 'html' or 'css'"],
    search_content: Annotated[
        str,
        "The exact code to replace within start_line and end_line of the file. The code must match exactly including proper indendation.",
    ],
    replace_content: Annotated[str, "The new code to replace the old code with."],
    start_line: Annotated[int, "The line number of the first line of search_content"],
    end_line: Annotated[int, "The line number of the last line of search_content."],
) -> str:
    """
    Useful for applying a diff to a file using search and replace. You need to make sure that the code from start_line to end_line must exactly be the search_content. if unsure use read_file first.
    """

    try:
        # time.sleep(3)
        print(f"\nApplying diff to {file} file...\n")
        base_dir = "html_resume"
        file_to_read = os.path.join(
            base_dir, "resume.html" if file == "html" else "style.css"
        )
        with open(file_to_read, "r") as f:
            lines = f.readlines()
            start_line = int(start_line)
            end_line = int(end_line)
            main_content = "".join(lines[start_line - 1 : end_line])
            normalized_main = re.sub(r"\s+", "", main_content)
            normalized_search = re.sub(r"\s+", "", search_content)
            # Check if the search content matches the specified lines

            if normalized_search in normalized_main:
                pattern = re.compile(r"\s*".join(map(re.escape, search_content)))
                match = pattern.search(main_content)
                if match:
                    content_to_replace = (
                        main_content[: match.start()]
                        + replace_content
                        + main_content[match.end() :]
                    )
                    content_to_replace = (
                        content_to_replace + "\n"
                        if content_to_replace[-1] != "\n"
                        else content_to_replace
                    )
                    # Replace the specified lines with the new content
                    lines[start_line - 1 : end_line] = content_to_replace.splitlines(
                        keepends=True
                    )
                    with open(file_to_read, "w") as f:
                        f.writelines(lines)
                    return f"Diff applied successfully to {file} file. Here is the updated code of {file}:\n\n{''.join([f'{i + 1} | {line}' for i, line in enumerate(lines)])}"
                else:
                    return "Search content does not match the specified lines. Diff not applied. Please use the read_file tool and make sure to use the exact code and the correct start_line and end_line."
            else:
                return "Search content does not match the specified lines. Diff not applied. Please use the read_file tool and make sure to use the exact code and the correct start_line and end_line."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {str(e)}. Try again..."
