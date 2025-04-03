from llama_index.readers.web import UnstructuredURLLoader

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    + "(KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
)


def scrape_url(url: str) -> str:
    """
    Useful for getting the contents of a URL.
    """
    loader = UnstructuredURLLoader(
        urls=[url],
        continue_on_failure=False,
        headers={
            "User-Agent": USER_AGENT,
        },
    )
    data = loader.load_data()
    return (
        f'Contents from the URL "{url}": \n{data[0].text}'
        if data
        else 'Failed to get contents from the URL "{url}"'
    )
