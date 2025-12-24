class Comment:
    def __init__(self, text, author):
        # Initialize the comment with text, author, and an empty list of replies
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        # Add a reply object to the list of replies for this comment
        self.replies.append(reply)

    def remove_reply(self):
        # Perform a "soft delete": change text and set the deletion flag
        # We do not remove the object from the list to preserve the hierarchy
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, prefix="", is_last=True, is_root=True):
        """
        Recursively displays the comment tree using ASCII graphics.

        :param prefix: The string prefix for indentation (lines and spaces).
        :param is_last: Boolean indicating if this is the last reply in the current list.
        :param is_root: Boolean indicating if this is the root comment (no prefix needed).
        """

        # Select emoji based on deletion status
        marker = "👻" if self.is_deleted else "💬"

        # Prepare the text to display based on deletion status
        if self.is_deleted:
            display_text = f"{marker} {self.text}"
        else:
            display_text = f"{marker} {self.author}: {self.text}"

        if is_root:
            # The root comment is printed without any prefix
            print(display_text)
            new_prefix = ""
        else:
            # Choose the connector: └── for the last item, ├── for others
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{display_text}")

            # Update the prefix for the children of this comment
            # If this was the last child, we add spaces (no vertical line needed)
            # Otherwise, we add a vertical line (|) to continue the tree structure
            new_prefix = prefix + ("    " if is_last else "│   ")

        # Iterate over replies to display them
        count = len(self.replies)
        for i, reply in enumerate(self.replies):
            # Check if this specific reply is the last one in the list
            is_last_child = (i == count - 1)
            reply.display(prefix=new_prefix, is_last=is_last_child, is_root=False)


def main() -> None:
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    reply2_1 = Comment("А що чудового в тобі?! Ти й такої не напишеш...", "Бодя")
    reply2.add_reply(reply2_1)

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1_1_1 = Comment("Ну тоді використай цю купу паперу замість туалетного) \
може твоя дупа трохи порозумнішає )))", "Бодя")
    reply1_1.add_reply(reply1_1_1)
    reply1.add_reply(reply1_1)

    # Remove the reply (soft delete)
    reply1.remove_reply()

    # Display the comment tree
    root_comment.display()


if __name__ == "__main__":
    main()