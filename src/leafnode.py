from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.tag and not self.value: 
            raise ValueError("LeafNode must have tag and/or value")

        if not self.value: 
            return f"<{self.tag} {self.props_to_html()} />"

        if not self.tag: 
            return self.value

        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
    