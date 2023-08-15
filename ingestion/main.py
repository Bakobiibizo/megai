from loaders import loader_selector

loader = loader_selector.PyPdfLoader()

loader.load_and_split("in/orca.pdf")
