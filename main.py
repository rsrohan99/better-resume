import asyncio

from workflows.update_resume_workflow import update_resume_workflow
from utils.verbose import log_events


async def main():
    handler = update_resume_workflow.run(
        user_msg="tailor my resume for the provided job application",
    )

    # Log events from the handler
    await log_events(handler)

    resp = await handler
    print(resp)


if __name__ == "__main__":
    asyncio.run(main())
