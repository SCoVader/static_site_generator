from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text" # text
    BOLD = "bold" # **bold**
    ITALIC = "italic" # _italic_
    CODE = "code" # `code`
    LINK = "link" # [anchor text](url)
    IMAGE = "image" # ![alt text](url)


class TextNode():
    
    def __init__(self, text, text_type, url = None):
        self.text=text
        self.text_type=text_type
        self.url=url

    def __eq__(self, other):
        return self.text == other.text and \
            self.text_type == other.text_type and \
            self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_to_html_node(textnode):
    htmlnode = None
    match textnode.text_type:
        case TextType.TEXT:
            htmlnode = LeafNode(None, textnode.text)
        case TextType.BOLD:
            htmlnode = LeafNode("b", textnode.text)
        case TextType.ITALIC:
            htmlnode = LeafNode("i", textnode.text)
        case TextType.CODE:
            htmlnode = LeafNode("code", textnode.text)
        case TextType.LINK:
            htmlnode = LeafNode("a", textnode.text, {"href": textnode.url})
        case TextType.IMAGE:
            htmlnode = LeafNode("img", None, {"src": textnode.url, "alt": textnode.text})
        case _:
            raise ValueError("Unknown text node")

    return htmlnode
