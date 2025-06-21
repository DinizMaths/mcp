from fastmcp import Client

async def main():
    async with Client("http://localhost:8000/sse") as client:
        tools = await client.list_tools()

        print(f"Tools: {tools}")

        resources = await client.list_resources()

        print(f"Resources: {resources}")

        prompts = await client.list_prompts()

        print(f"Prompts: {prompts}")

        response = await client.call_tool("get_weather", {"location": "New York"})

        print(f"Responses: {response}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())