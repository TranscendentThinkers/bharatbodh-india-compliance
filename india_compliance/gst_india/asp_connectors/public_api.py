from .base_api import BaseAPI


class PublicAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.api_endpoint = "commonapi"
        self.api_key = self.settings.get_password("api_secret")

    def get_gstin_info(self, gstin):
        return self.get(
            endpoint="search",
            params={"action": "TP", "gstin": gstin},
        )

    def get_returns_info(self, gstin, fy):
        if len(fy) == 9:
            start, end = fy.split("-")
            fy = f"{start}-{end[-2:]}"

        return self.get(
            endpoint="returns",
            params={"action": "RETTRACK", "gstin": gstin, "fy": fy},
        )
