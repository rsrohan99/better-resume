from llama_index.core.agent.workflow import AgentWorkflow
from agents import job_research_agent, resume_updater_agent


def get_resume_updater_workflow(url, resume_file):
    """Get the resume updater workflow."""
    return AgentWorkflow(
        agents=[job_research_agent, resume_updater_agent],
        root_agent=job_research_agent.name,
        initial_state={
            "url": url,
            "resume_file": resume_file,
            "updated_resume_file_path": "updated_resume.md",
        },
    )
