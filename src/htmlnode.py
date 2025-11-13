

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
