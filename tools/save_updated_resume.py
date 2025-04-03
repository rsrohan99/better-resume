from typing import List, Optional, Annotated

from llama_index.core.workflow import Context

from pydantic import BaseModel, Field


class ResumeExperience(BaseModel):
    workplace: Optional[str] = Field(description="Name of the workplace")
    title: Optional[str] = Field(description="Job title")
    start_year: Optional[str] = Field(description="Start year of the job, optional")
    end_year: Optional[str] = Field(
        description='End year of the job or "present" if still working, optional'
    )
    description: List[str] = Field(
        description="Rewritten list of bullet points to emphasize achievements and responsibilities of this experience that align with the job requirements"
    )


class ResumeProjects(BaseModel):
    title: Optional[str] = Field(description="Title of the project")
    start_year: Optional[str] = Field(
        description="The year when started working on this project, optional."
    )
    end_year: Optional[str] = Field(
        description='Year when the project was completed or "present" if still working on it, optional'
    )
    description: List[str] = Field(
        description="Rewritten list of bullet points to emphasize achievements and responsibilities of this project that align with the job requirements"
    )


class ResumeContent(BaseModel):
    headline: str = Field(
        description="Updated headline to reflect the job title and include relevant keywords from the job posting."
    )
    summary: str = Field(
        description="Tailored summary to highlight the most relevant skills, experience, and achievements that match the job posting."
    )
    website: Optional[str] = Field(
        description="Link to the personal website or portfolio, extracted from the user's previous resume, optional"
    )
    linkedin: Optional[str] = Field(
        description="Link to the LinkedIn profile, extracted from the user's previous resume, optional"
    )
    github: Optional[str] = Field(
        description="Link to the GitHub profile, extracted from the user's previous resume, optional"
    )
    email: Optional[str] = Field(
        description="Email address, extracted from the user's previous resume, optional"
    )
    phone: Optional[str] = Field(
        description="Phone number, extracted from the user's previous resume, optional"
    )
    experiences: List[ResumeExperience] = Field(
        description="List of experiences most relevant to the position to be applied for."
    )
    projects: Optional[List[ResumeProjects]] = Field(
        description="List of projects most relevant to the position to be applied for."
    )
    skills: List[List[str]] = Field(
        description="List of groups of skills, grouped by relevant and similar skills. sorted by relevance and importance to the job."
    )


async def save_updated_resume_content(
    ctx: Context,
    resume_content: Annotated[
        ResumeContent,
        "Updated resume specifically tailored to the given job posting so that it stands out.",
    ],
) -> str:
    """
    Useful for saving the updated resume content after thoroughly analyzing
    the job requirements and the user's previous resume. This updated resume
    is tailored to highlight the most relevant skills, experience,
    and achievements that match the job posting. The info saved by this tool
    will be used by other agents later to create the final updated resume.
    """
    current_state = await ctx.get("state")
    current_state["resume_content"] = resume_content
    await ctx.set("state", current_state)
    return "Job Research result saved successfully."
