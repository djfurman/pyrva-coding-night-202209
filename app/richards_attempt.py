class Page:
    def __init__(self, max_pages: int) -> None:
        self.current_page: int = 1
        self.max_pages = max_pages

        self.display: str = self.build_pagination()

    def pagination_action(self, action) -> None:
        if action == "next":
            self.current_page += 1
        if action == "previous":
            self.current_page -= 1

        self.display = self.build_pagination()

    def build_pagination(self) -> str:
        output = []

        for i in range(self.max_pages):
            if i == self.current_page:
                output.append(f"({i})")
            else:
                output.append(str(i))

        return " ".join(output)
