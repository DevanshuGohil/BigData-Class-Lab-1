from docling.document_converter import DocumentConverter

# Initialize converter
converter = DocumentConverter()

# Convert a PDF file or URL
source = "RAG Information.pdf"
result = converter.convert(source)

# Export to markdown
print(result.document.export_to_markdown())
