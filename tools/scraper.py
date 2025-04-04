from llama_index.readers.web import UnstructuredURLLoader
from llama_index.core.workflow import Context

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    + "(KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
)


async def scrape_url(ctx: Context) -> str:
    """
    Useful for getting the contents of a URL and saving them.
    """
    current_state = await ctx.get("state")
    url = current_state["url"]
    print(f"\nGetting contents from url: {url}...\n")
    loader = UnstructuredURLLoader(
        urls=[url],
        continue_on_failure=False,
        headers={
            "User-Agent": USER_AGENT,
        },
    )
    data = loader.load_data()
    current_state["job_posting_data"] = data[0].text
    # print(f"\nJob Data: {data[0].text}\n")
    await ctx.set("state", current_state)
    return (
        f'Contents from the URL "{url}" saved'
        if data
        else 'Failed to get contents from the URL "{url}"'
    )
