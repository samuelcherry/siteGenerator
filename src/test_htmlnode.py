import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>",
        )


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


    def test_to_html_with_multiple_children(self):
        child_one = LeafNode("b", "bold")
        child_two = LeafNode("i", "italic")
        child_three = LeafNode("span", "normal")

        parent_node = ParentNode(
            "div",
            [child_one, child_two, child_three],
        )

        self.assertEqual(
            parent_node.to_html(),
            "<div><b>bold</b><i>italic</i><span>normal</span></div>",
        )


    def test_to_html_with_text_children(self):
        child_one = LeafNode(None, "Hello ")
        child_two = LeafNode("b", "world")

        parent_node = ParentNode(
            "p",
            [child_one, child_two],
        )

        self.assertEqual(
            parent_node.to_html(),
            "<p>Hello <b>world</b></p>",
        )


    def test_to_html_with_props(self):
        child = LeafNode("span", "Hello")
        parent_node = ParentNode(
            "div",
            [child],
            {"class": "container"},
        )

        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>Hello</span></div>',
        )


    def test_to_html_with_nested_props(self):
        child = LeafNode(
            "a",
            "Click me",
            {"href": "https://example.com"},
        )

        parent_node = ParentNode(
            "div",
            [child],
            {"class": "links"},
        )

        self.assertEqual(
            parent_node.to_html(),
            '<div class="links"><a href="https://example.com">Click me</a></div>',
        )


    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])

        self.assertEqual(
            parent_node.to_html(),
            "<div></div>",
        )


    def test_to_html_missing_tag(self):
        parent_node = ParentNode(
            None,
            [LeafNode("span", "child")],
        )

        with self.assertRaises(ValueError):
            parent_node.to_html()


    if __name__ == "__main__":
        unittest.main()
