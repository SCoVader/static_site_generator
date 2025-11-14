import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    # HTMLNode tests
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

    # LeafNode tests
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
    
    # ParentNode tests
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()