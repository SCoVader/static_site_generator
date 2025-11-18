from textnode import (TextNode, TextType)
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


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
            block_type = BlockType.HEADING
    if block[0: 3] == "```" and block[-1: -4: -1] == "```":
        block_type = BlockType.CODE
        
    # UNFINISHED
    if block[0] == '>':
        block_type = BlockType.QUOTE
    if block[0:2] == '- ':
        block_type = BlockType.UNORDERED_LIST
    if block[0:3] =='1. ':
        block_type = BlockType.ORDERED_LIST
    return block_type