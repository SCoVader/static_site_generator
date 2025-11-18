from textnode import (TextNode, TextType)
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered list"
    OLIST = "ordered list"


def markdown_to_blocks(markdown):
    candidates = markdown.split("\n\n")
    blocks = []
    for block in candidates:
        if block == '': continue
        blocks.append(block.strip())
    return blocks

def block_to_block_type(block):
    block_type = BlockType.PARAGRAPH
    if block[0] == '#':
        n = 1
        while block[n] == '#':
            n += 1
        if n <= 6 and block[n] == ' ': 
            return BlockType.HEADING
    if block[0: 3] == "```" and block[-1: -4: -1] == "```":
        return BlockType.CODE
        
    lines = block.split("\n")

    if lines[0].startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if lines[0].startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if lines[0].startswith("1. "):
        n = 1
        for line in lines:
            if not line.startswith(f"{n}. "):
                return BlockType.PARAGRAPH
            n += 1
        return BlockType.OLIST
    return block_type