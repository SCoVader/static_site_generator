import unittest
from block_markdown import (
    markdown_to_blocks, 
    block_to_block_type, 
    BlockType
    )


class TestBlockMarkdown(unittest.TestCase):
    def test_block_markdown(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]
        
        self.assertListEqual(expected, markdown_to_blocks(md))

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Must be heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("####### Must be heading"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("```\ncounter += 1\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("##Must be heading"), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
