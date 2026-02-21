class InvalidURLException(Exception):
    def __init__(self, message: str = "The provided URL is invalid."):
        self.message = message
        super().__init__(self.message)
    """Raised when the provided URL is invalid."""