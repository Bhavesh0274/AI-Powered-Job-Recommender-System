from mcp.server.fastmcp import FastMCP
from src.job_api import fetch_linkedin_jobs, fetch_naukri_jobs

mcp = FastMCP("Job Recommender MCP")

@mcp.tool()
async def fetchlinkedin(list_of_keywords):
    return fetch_linkedin_jobs(list_of_keywords)

@mcp.tool()
async def fetchlinkedin(list_of_keywords):
    return fetch_linkedin_jobs(list_of_keywords)

if __name__ == "__main__":
    mcp.run(transport='stdio')