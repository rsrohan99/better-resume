# Better-Resume

In this tutorial, we will use AgentWorkflow, the new multi-agent framework from LlamaIndex, to build a multi-agent system that takes your existing resume and a job posting URL, and generates a tailored resume exclusively for that job posting.

It also has a nice chat interface to iteratively improve the resume, including updating the resume with various styles and colorschemes.

Full tutorial 👇

[![]()]()

## How to use

- Clone the repo

```bash
git clone git@github.com:rsrohan99/better-resume.git
```

- Install dependencies

```bash
uv sync
```

- Create `.env` file and add the necessary api keys from `.env.example`

```bash
cp .env.example .env
```

- Run the workflow with the topic to research

```bash
uv run main.py
```

- provide the existing resume file and the job posting url in the chat interface
- open the `resume.html` file in the browser to see the rendered resume
- print the rendered resume using `ctrl+p'
