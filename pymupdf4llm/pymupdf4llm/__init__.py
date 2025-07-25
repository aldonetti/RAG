from .helpers.pymupdf_rag import IdentifyHeaders, TocHeaders, to_markdown

__version__ = "0.0.25"
version = __version__
version_tuple = tuple(map(int, version.split(".")))


def LlamaMarkdownReader(*args, **kwargs):
    from .llama import pdf_markdown_reader

    return pdf_markdown_reader.PDFMarkdownReader(*args, **kwargs)
