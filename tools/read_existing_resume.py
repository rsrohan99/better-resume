from llama_index.core.workflow import Context
from llama_index.core import SimpleDirectoryReader


async def read_existing_resume(ctx: Context):
    """
    Read the existing resume from the context.
    """
    current_state = await ctx.get("state")
    try:
        resume_file = current_state.get("resume_file")
        print(f"\nReading resume contents from {resume_file}...\n")
        docs = SimpleDirectoryReader(
            input_files=[resume_file],
        ).load_data()
        current_state["resume"] = docs[0].text
        await ctx.set("state", current_state)
        return "Resume read successfully."
    except FileNotFoundError:
        return "Resume file not found."
