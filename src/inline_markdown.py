import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\) ]*)\)", text)
    #return re.findall(r"!\[([\w ]*)\]\((\S*.\w*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        delim_tuples = extract_markdown_images(old_node.text)
        split_nodes = []
        new_string = old_node.text
        substrings = []
        for i in range(len(delim_tuples)):
            delim = f"![{delim_tuples[i][0]}]({delim_tuples[i][1]})"
            substrings = new_string.split(delim, 1)
            if len(substrings) < 1:
                continue
            if substrings[0] != '': 
                split_nodes.append(TextNode(substrings[0], TextType.TEXT))
            split_nodes.append(TextNode(delim_tuples[i][0], TextType.IMAGE, delim_tuples[i][1]))
            if substrings[1] != '': 
                new_string = substrings[1]
        if len(substrings) > 1 and substrings[1] != '': 
            split_nodes.append(TextNode(substrings[1], TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_links(text):
    return re.findall(r"\[([^\[\]]*)\]\(([^\(\) ]*)\)", text)
    #return re.findall(r"\[([\w ]*)\]\((\S*)\)", text)

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        delim_tuples = extract_markdown_links(old_node.text)
        split_nodes = []
        new_string = old_node.text
        substrings = []
        for i in range(len(delim_tuples)):
            delim = f"[{delim_tuples[i][0]}]({delim_tuples[i][1]})"
            substrings = new_string.split(delim, 1)
            if len(substrings) < 1:
                continue
            if substrings[0] != '': 
                split_nodes.append(TextNode(substrings[0], TextType.TEXT))
            split_nodes.append(TextNode(delim_tuples[i][0], TextType.LINK, delim_tuples[i][1]))
            if substrings[1] != '': 
                new_string = substrings[1]
        if len(substrings) > 1 and substrings[1] != '': 
            split_nodes.append(TextNode(substrings[1], TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes