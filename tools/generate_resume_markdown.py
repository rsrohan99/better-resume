import shutil
import os
from typing import Annotated
from workflows.update_resume_workflow import get_resume_updater_workflow
from utils.verbose import log_events


async def generate_resume_markdown(
    resume_file_path: Annotated[
        str,
        'The path to the user\'s existing resume file, use "resume.pdf" if the user has not provided a file path.',
    ],
    job_posting_url: Annotated[str, "The URL of the job posting. Required."],
) -> str:
    """
    Useful for generating the resume markdown file from user's existing resume and job posting url.
    Only use this tool if user explicitly asks to generate the resume markdown file.
    """

    try:
        update_resume_workflow = get_resume_updater_workflow(
            job_posting_url, resume_file_path
        )
        handler = update_resume_workflow.run(
            user_msg="tailor my resume for the provided job application",
        )

        await log_events(handler)
        await handler

        if os.path.exists("html_resume"):
            shutil.rmtree("html_resume")
        shutil.copytree("html_resume_template", "html_resume")
        print("\nDeleting old html_resume folder and copying the new one...\n")
        return "Resume markdown file generated successfully."

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {str(e)}. Try again..."
