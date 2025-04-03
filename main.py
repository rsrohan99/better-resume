import sys
import asyncio

from dotenv import load_dotenv

from llama_index.utils.workflow import draw_all_possible_flows
from llama_index.llms.gemini import Gemini

from workflows.workflow import LlamaWorkflow


async def main():
    load_dotenv()
    llm = Gemini(model="models/gemini-2.0-flash")
    workflow = LlamaWorkflow(llm=llm, verbose=True, timeout=240.0)
    # draw_all_possible_flows(workflow, filename="workflow.html")
    topic = sys.argv[1]
    await workflow.run(query=topic)


if __name__ == "__main__":
    asyncio.run(main())
