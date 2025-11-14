

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag # string representing tag name: "a"
        self.value = value # string: "Example.com"
        self.children = children # list of HTMLNodes
        self.props = props # dictionary: {"href": "https://www.example.com"}

    def to_html(self):
        raise NotImplementedError("Method must be implemented by children")

    def props_to_html(self):
        if not self.props: return ""
        result=""
        for key in self.props:
            result += f"{key}=\"{self.props[key]}\" "
        
        return result[0:-1]

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        return self.tag == other.tag and \
            self.value == other.value and \
            self.children == other.children and \
            self.props == self.props


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.tag and not self.value: 
            raise ValueError("LeafNode must have tag and/or value")

        if not self.value: 
            string = f"<{self.tag}"
            if self.props: 
                string += f" {self.props_to_html()}"
            string += " />"
            return string

        if not self.tag: 
            return self.value

        string = f"<{self.tag}"
        if self.props: 
            string += f" {self.props_to_html()}"

        string += ">"
        return f"{string}{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if not self.tag: raise ValueError("Container node must have a tag!")
        if not self.children: raise ValueError("Container node must have children!")

        string = f"<{self.tag}>"
        for child in self.children:
            string += child.to_html()

        string+=f"</{self.tag}>"
        return string
        