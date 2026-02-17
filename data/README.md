# Data Directory

This directory is for storing documents that will be ingested into the RAG system.

## Supported Formats

- PDF files (`.pdf`)
- Text files (`.txt`)
- Markdown files (`.md`)
- Word documents (`.docx`)

## Usage

1. Place your documents in this directory
2. Run the ingestion script to process and index the documents
3. The documents will be chunked, embedded, and stored in the vector database

## Notes

- Large documents will be automatically chunked
- Ensure documents are readable and properly formatted
- Remove any sensitive information before adding documents


