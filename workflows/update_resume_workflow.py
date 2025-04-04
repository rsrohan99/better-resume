from llama_index.core.agent.workflow import AgentWorkflow
from agents import job_research_agent, resume_updater_agent


update_resume_workflow = AgentWorkflow(
    agents=[job_research_agent, resume_updater_agent],
    root_agent=job_research_agent.name,
    initial_state={
        "url": "https://www.linkedin.com/jobs/view/full-stack-software-engineer-l5-platform-engineering-at-netflix-4049838471",
        "resume_file": "resume.pdf",
        "updated_resume_file_path": "updated_resume.md",
    },
)
