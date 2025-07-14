from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio"
            },
            "playwright": {
                "command": "npx",
                "args": ["@playwright/mcp@latest"],
                "transport": "stdio"
            }
        }
    )

    tools = await client.get_tools()
    llm = ChatGroq(model="qwen-qwq-32b")
    agent = create_react_agent(llm, tools)
    
    try:
        while True:
            query = input("Enter a query: ")
            if query.lower() in ["exit", "quit", "bye"]:
                print("Exiting...")
                break
            if query.lower() in ["clear", "cls"]:
                # Clear conversation by creating a new agent
                agent = create_react_agent(llm, tools)
                print("Conversation history cleared")
                continue
            
            try:
                result = await agent.ainvoke({"messages": [{"role": "user", "content": query}]})

                print(f"\nResult: {result['messages'][-1].content}")
            except Exception as e:
                print(f"\nError: {e}")
                print("Please try again.")
                continue
    finally:
        pass



asyncio.run(main())


# if __name__ == "__main__":
#     asyncio.run(main())



