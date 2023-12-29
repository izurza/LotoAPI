class ErrorResponse:
    def __init__(self, success:bool = False, message:str = ""):
        self.success = success
        self.message = message
    