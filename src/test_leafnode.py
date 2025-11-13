import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node  = LeafNode("a", "link", {"href": "https://google.com", "target": "_blank"})
        node2 = LeafNode("a", "link", {"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_prop_conversion(self):
        node = LeafNode("a", "some", {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')
    
    def test_childfree(self):
        node = LeafNode("a", "some link", {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.children, None)

    def test_no_tag(self):
        node = LeafNode(None, "Some boring text without any features.", {"style": "color: red;"})
        self.assertEqual(node.to_html(), "Some boring text without any features.")

    def test_no_value(self):
        node = LeafNode("img", None, {"src": "static/cat1.png", "alt": "there is a cat", "width": "400", "height": "300"})
        self.assertEqual(node.to_html(), '<img src="static/cat1.png" alt="there is a cat" width="400" height="300" />')

if __name__ == "__main__":
    unittest.main()