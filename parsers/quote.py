from locators.quote_locators import QuoteLocators
"""
Given one of the specific quote divs, find out more details about the
quote (content, author, and tags)
"""
class QuoteParser:
    def __init__(self, parent):
        self.parent = parent # we receive bs4 quote tag

    def __repr__(self):
        return f'<Quote: {self.content} by {self.author}><Tags: {self.tags}>'
    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string
    
    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return [e.string for e in self.parent.select(locator)]