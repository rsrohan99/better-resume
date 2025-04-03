from typing import Annotated, List


from llama_index.core.workflow import Context


async def save_research_result(
    ctx: Context,
    key_skills: Annotated[List[str], "Key skills required for the job"],
    qualifications: Annotated[List[str], "Qualifications required for the job"],
    responsibilities: Annotated[List[str], "Main responsibilities of the job"],
    experiences: Annotated[List[str], "Experiences required for the job"],
    keywords: Annotated[List[str], "Keywords to be used in the resume"],
):
    """
    Useful for saving the extracted key skills, responsibilities, experiences
    and qualifications required for a job after thoroughly analysing the
    jop posting. Use the tools to gather content and identify and categorize
    the requirements for a job. This saved info will be used by
    other agents later.
    """
    current_state = await ctx.get("state")
    current_state["job_requirements"] = {
        "key_skills": key_skills,
        "qualifications": qualifications,
        "responsibilities": responsibilities,
        "experiences": experiences,
        "keywords": keywords,
    }
    await ctx.set("state", current_state)
    return "Job Research result saved successfully."
