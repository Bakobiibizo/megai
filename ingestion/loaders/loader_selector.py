from ingestion.loaders.pypdf_loader import PyPDFLoader
from pydantic import BaseModel


class LoaderSelector(BaseModel):
    def __init__(self):
        self.loader = None
        self.loader_list = []
         
    def add_loader(self, loader, name):
        if self.loader[name] not in self.loader_list:
            self.loader_list.append({self.loader_list[name]: loader})

    def loader_selector(self, name):
        self.loader = self.loader_list[name]
        return self.loader
            
    def load_and_split(self, path):
        self.loader.load_and_split(path)
        
    def load(self, path):
        self.loader.load(path)
    
class PDFLoader(LoaderSelector):
    def __init__ (self):
        super.__init__(self, PyPDFLoader, "PyPDFLoader")
        self.add_loader(PyPDFLoader, "PyPDFLoader")


if __name__ == "__main__":
    PDFLoader = PDFLoader()
    
    
    loader = LoaderSelector()
    loader = loader.pdf_loader("PyPDFLoader")
    loader.load_and_split("in/orca.pdf")
