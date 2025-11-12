from textnode import TextNode, TextType

def main():
    tn1=TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    tn2=TextNode("This is a bold dummy", TextType.BOLD)

    print(repr(tn1))
    print(repr(tn2))

if __name__ == "__main__":
    main()
    