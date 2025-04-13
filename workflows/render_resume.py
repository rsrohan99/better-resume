from dotenv import load_dotenv
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.llms.gemini import Gemini

from tools import apply_diff, read_file, read_resume_markdown, generate_resume_markdown
from prompts.updater import updater_system_prompt


load_dotenv()
llm = Gemini(model="models/gemini-2.0-flash")
RenderResumeWorkflow = AgentWorkflow.from_tools_or_functions(
    tools_or_functions=[
        generate_resume_markdown,
        read_file,
        read_resume_markdown,
        apply_diff,
    ],
    llm=llm,
    system_prompt=updater_system_prompt,
)
