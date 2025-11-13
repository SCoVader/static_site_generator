import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "some", [HTMLNode("b", "link")], {"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode("a", "some", [HTMLNode("b", "link")], {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node, node2)

    def test_prop_conversion(self):
        node = HTMLNode("a", "some", [HTMLNode("b", "link")], {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')
    
    def test_non_val(self):
        node = HTMLNode("br")
        self.assertEqual(node.value, None)
        

if __name__ == "__main__":
    unittest.main()