from typing import Annotated

from llama_index.core.workflow import Context


async def save_updated_resume_content(
    ctx: Context,
    updated_resume_in_markdown: Annotated[
        str,
        "Full updated resume in markdown format with all the sections like Full name of the candidate, headline, summary, experiences, projects, skills, contact info extracted from previous resume like email, phone number, website, github, linkedin url etc. The headline must reflect the job title and include relevant keywords from the job posting. The summary must be tailored to highlight the most relevant skills, experience, and achievements that match the job posting. The summary must be under 35 words. The experiences and projects must be rewritten to emphasize achievements and responsibilities that align with the job requirements. Extract all information for experiences and projects like start end year, job title, workplace etc. The description of the experiences and projects must be Rewritten list of bullet points to emphasize achievements and responsibilities of this experience that align with the job requirements. The skills must be grouped by relevant and similar skills, sorted by relevance and importance to the job.",
    ] = "",
) -> str:
    """
    Useful for saving the updated resume content after thoroughly analyzing
    the job requirements and the user's previous resume. This updated resume
    is tailored to highlight the most relevant skills, experience,
    and achievements that match the job posting. The info saved by this tool
    will be used by other agents later to create the final updated resume.
    """
    current_state = await ctx.get("state")
    current_state["resume_content"] = updated_resume_in_markdown
    updated_resume_file_path = current_state.get("updated_resume_file_path")
    with open(updated_resume_file_path, "w") as f:
        f.write(updated_resume_in_markdown)
    await ctx.set("state", current_state)
    return "Job Research result saved successfully."
