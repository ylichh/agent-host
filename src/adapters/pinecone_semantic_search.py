from ..domain.services.tools.i_tool import ITool
from langchain_core.tools import tool


class PineconeSemanticSearch(ITool):

    @tool
    def execute(self, a: int, b: int):
        """Executes a semantic search using Pinecone."""
        print("Executing Pinecone Semantic Search Tool")


if __name__ == "__main__":
    pinecone_tool = PineconeSemanticSearch()
    print(pinecone_tool.execute.name)
    print(pinecone_tool.execute.description)
    print(pinecone_tool.execute.args)

    pinecone_tool.execute()
