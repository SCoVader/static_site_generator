from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def preview_nodes():
    tn1 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    hn1 = HTMLNode("a", "some", [HTMLNode("b", "link")], {"href": "https://www.google.com", "target": "_blank",})
    ln0 = LeafNode("p", "some text")
    ln1 = LeafNode(None, "normal text")
    ln2 = LeafNode("b", "bold text")
    pn0 = ParentNode("div", [ln0, ln1, ln2], {"class": "mt-3 mb-3", "id": "inner_box"})
    pn1 = ParentNode("div", [pn0], {"class": "pl-4 pr-4 gray-400", "id": "outer_box"})
    print(repr(tn1))
    print(repr(hn1))
    print(repr(ln1))
    print(repr(pn1))

def main():
    text_nodes=[
        TextNode("Plain text node. Just some text", TextType.TEXT),
        TextNode("Bold text", TextType.BOLD),
        TextNode("Italic text", TextType.ITALIC),
        TextNode("list = [1, 2, 3, 4, 5, 6]", TextType.CODE),
        TextNode("Buy your music!", TextType.LINK, "https://www.bandcamp.com"), 
        TextNode("Cat in a bush", TextType.IMAGE, "cat_pic1.png")
    ]
    
    for node in text_nodes:
        print(text_to_html_node(node).to_html())


if __name__ == "__main__":
    main()
    