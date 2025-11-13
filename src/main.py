from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    tn1 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    hn1 = HTMLNode("a", "some", [HTMLNode("b", "link")], {"href": "https://www.google.com", "target": "_blank",})
    ln1 = LeafNode("p", "some text")
    print(repr(tn1))
    print(repr(hn1))
    print(repr(ln1))


if __name__ == "__main__":
    main()
    