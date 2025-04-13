async def read_resume_markdown() -> str:
    """
    Useful for getting the contents of the resume markdown file that will be used to populate the html template.
    """

    try:
        print("\nGetting contents from markdown resume file...\n")
        with open("updated_resume.md") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."
