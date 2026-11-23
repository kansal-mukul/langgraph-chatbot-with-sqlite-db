import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    client = MultiServerMCPClient({
        "sanitizer": {
            "transport": "sse",
            "url": "https://mcp-security-sanitizer-server.onrender.com/sse",
        }
    })
    tools = await client.get_tools()
    print([tool.name for tool in tools])

asyncio.run(main())