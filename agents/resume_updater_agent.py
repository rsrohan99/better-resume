from dotenv import load_dotenv
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.gemini import Gemini

from tools import read_existing_resume, save_updated_resume_content

load_dotenv()
llm = Gemini(model="models/gemini-2.0-flash")

resume_updater_agent = FunctionAgent(
    name="ResumeUpdaterAgent",
    description="Useful for finding all the best ways to make a resume stand out in the job market.",
    system_prompt=(
        "With a strategic mind and an eye for detail, you "
        "excel at refining resumes to highlight the most "
        "relevant skills and experiences, ensuring they "
        "resonate perfectly with the job's requirements."
        "Using the existing resume of the user and job requirements obtained "
        "before, tailor the resume to highlight the most "
        "relevant areas. Employ tools to adjust and enhance the "
        "resume content. Make sure this is the best resume ever but "
        "don't make up any information. Update every section, "
        "inlcuding the initial summary, work experience, skills, "
        "and education. All to better reflrect the candidates "
        "abilities and how it matches the job posting."
    ),
    llm=llm,
    tools=[read_existing_resume, save_updated_resume_content],
)
