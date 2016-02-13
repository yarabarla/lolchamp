class Champion(object):
    session, api_key = get_credentials()
    def __init__(self, name):
         self.name = name
         self.data = self.get_data()

    @staticmethod
    def get_credentials(self, session, api_key):
        return session, api_key     

    def get_data():
        url = "http://api.champion.gg/champion?api_key=" + api_key
        res = session.get(url)
        return res

    def items():
        try:
            items = self.data["items"]["highestWinPercent"]["items"]
            items = [item["name"] for item in items]
        except e:
            print("Error getting items.")
            raise

        items.map(lambda item: print(item))
