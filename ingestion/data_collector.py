import json
import os
from vectorstore.vectorstore import VectorStore
from loaders import loader_selector
from loguru import logger


class DataCollector:
    """
    This class represents a DataCollector object, which is responsible for collecting and processing data.

    Attributes:
    - vectordb: An instance of the VectorStore class, used for storing document vectors.
    - loader: An instance of the LoaderSelector class, used for selecting and loading PDF files.

    Methods:
    - load_pdf(path): Loads a PDF file located at the specified path, splits it into individual documents,
      adds the documents to the vectordb, and saves them as text files. It also logs information about the
      loaded documents.

    Note:
    - The class assumes that a "docs" directory exists in the current working directory, where the text files
      will be saved.
    """

    def __init__(self):
        logger.info("data_collector initialized")
        self.vectordb = VectorStore()
        self.loader = loader_selector.LoaderSelector(loader_name="pdf")

    def load_pdf(self, path):
        logger.info("loading pdf")
        docs = self.loader.pdf_loader().load_and_split(path)
        self.vectordb.add_document(docs)
        name = os.path.basename(path).replace(".pdf", ".txt")
        with open("docs/" + name, "a", encoding="utf-8") as file:
            for doc in docs:
                logger.debug(f"writing doc:\n{doc}")
                doc_chunk = file.write(doc.text["documents"][0]["text"] + "\n\n")
                logger.debug(f"Document chunk written to {name}:\n{doc_chunk}")
            doc_info = json.loads(doc)["documents"][0]["metadata"]
            doc_info["path"] = path
        self.vectordb.add()


if __name__ == "__main__":
    collector = DataCollector()
    collector.load_pdf("in/orca.pdf")
