# 1472. Design Browser History
class BrowserHistory:
    # initialize history and current_page for remember the history of visted page and remember the index of active page respectively
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_page = 0

    # Time complexity: O(m - n): m mean length of history, n is a index of current page in history
    # Space complexity: O(1): 
    # visit the new page url
    def visit(self, url: str) -> None:
        # check the current page is the newest visited page if not the remove all after page of this current page
        if self.current_page != len(self.history):
            for i in range(len(self.history) - self.current_page - 1):
                self.history.pop()
        # add new url to the history
        self.history.append(url)
        # set current page to new page
        self.current_page = len(self.history) - 1

    # Time complexity: O(1):
    # Space complexity: O(1):
    # back to n steps previous page
    def back(self, steps: int) -> str:
        # check the current page subtract with steps that can't not lower than zero and move the current page to index subtract with steps 
        # if the value of this operation is less than equal zero return the first index of history
        if self.current_page - steps > 0:
            self.current_page -= steps 
            return self.history[self.current_page]
        else:
            self.current_page = 0
            return self.history[0]

    # Time complexity: O(1):
    # Space complexity: O(1):
    # forward to n steps next page
    def forward(self, steps: int) -> str:
        # check the current page add with steps that can't not greater than length of history and move the current page to index add with steps
        # if the value of this operation is greater than length of history return the last index of history
        if self.current_page + steps <= len(self.history) - 1:
            self.current_page += steps
            return self.history[self.current_page]
        else:
            self.current_page = len(self.history) - 1
            return self.history[-1]
