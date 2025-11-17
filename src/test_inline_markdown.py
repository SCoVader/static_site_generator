import unittest
from textnode import TextNode, TextType
from inline_markdown import (
    split_nodes_delimiter, 
    extract_markdown_images, 
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_image_extraction(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), 
            [
                ('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), 
                ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')
            ]
        )

    def test_link_extraction(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), 
            [
                ('to boot dev', 'https://www.boot.dev'), 
                ('to youtube', 'https://www.youtube.com/@bootdotdev')
            ]
        )

    def test_split_images_complex(self):
        node = TextNode("This is huge text node with multiple images ![first image](https://example.com/image1.png), some text between them ![second image](https://example.com/image2.jpg), some more text ![third image](https://example.com/image3.gif) and final few words", TextType.TEXT)
        expected = [
            TextNode('This is huge text node with multiple images ', TextType.TEXT),
            TextNode('first image', TextType.IMAGE, 'https://example.com/image1.png'),
            TextNode(', some text between them ', TextType.TEXT),
            TextNode('second image', TextType.IMAGE, 'https://example.com/image2.jpg'),
            TextNode(', some more text ', TextType.TEXT),
            TextNode('third image', TextType.IMAGE, 'https://example.com/image3.gif'),
            TextNode(' and final few words', TextType.TEXT)
        ]
        self.assertListEqual(split_nodes_image([node]), expected)

    def test_split_images_no_dangling_nodes(self):
        node = TextNode("This is huge text node with multiple images ![first image](https://example.com/image1.png)", TextType.TEXT)
        expected = [
            TextNode('This is huge text node with multiple images ', TextType.TEXT),
            TextNode('first image', TextType.IMAGE, 'https://example.com/image1.png'),
        ]
        self.assertListEqual(split_nodes_image([node]), expected)

    def test_split_images_no_dangling_nodes(self):
        node = TextNode("![first image](https://example.com/image1.png), some text between them ", TextType.TEXT)
        expected = [
            TextNode('first image', TextType.IMAGE, 'https://example.com/image1.png'),
            TextNode(', some text between them ', TextType.TEXT),
        ]
        self.assertListEqual(split_nodes_image([node]), expected)

    def test_split_links_complex(self):
        node = TextNode("This is huge text node with multiple links [first image](https://example.com/image1.png), some text between them [second image](https://example.com/image2.jpg), some more text [third image](https://example.com/image3.gif) and final few words", TextType.TEXT)
        expected = [
            TextNode('This is huge text node with multiple links ', TextType.TEXT),
            TextNode('first image', TextType.LINK, 'https://example.com/image1.png'),
            TextNode(', some text between them ', TextType.TEXT),
            TextNode('second image', TextType.LINK, 'https://example.com/image2.jpg'),
            TextNode(', some more text ', TextType.TEXT),
            TextNode('third image', TextType.LINK, 'https://example.com/image3.gif'),
            TextNode(' and final few words', TextType.TEXT)
        ]
        self.assertListEqual(split_nodes_link([node]), expected)

if __name__ == "__main__":
    unittest.main()
