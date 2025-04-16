from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.gemini import Gemini
from dotenv import load_dotenv

from tools import save_research_result, scrape_url

load_dotenv()
llm = Gemini(model="models/gemini-2.0-flash")

job_research_agent = FunctionAgent(
    name="JobResearchAgent",
    description="Useful for doing amazing analysis on the job posting from the given URL.",
    system_prompt=(
        "As a skilled job researcher, help pinpoint the necessary "
        "qualifications and skills sought by the employer, "
        "forming the foundation for effective application tailoring."
        "Analyze the job posting URL provided "
        "to extract key skills, experiences, and qualifications "
        "required. Use the tools to gather content and identify "
        "and categorize the requirements. We are expecting the following from you: "
        "A structured list of job requirements, including necessary "
        "skills, qualifications, and experiences."
    ),
    llm=llm,
    tools=[scrape_url, save_research_result],
    can_handoff_to=["ResumeUpdaterAgent"],
)
