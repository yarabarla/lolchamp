from requests_futures.sessions import FuturesSession

def main():
    session, api_key = authorize_user()

def authorize_user():
    """
    Opens up an async requests session to persist the connection to the
    endpoint. Validates the API key and returns the session.
    """
    def validated_api_key(session, key):
        """
        Connects to endpoint to check status code. Returns a boolean depending
        on whether access is valid or not
        """
        url = 'http://api.champion.gg/champion?api_key=' + key
        res = session.get(url)
        status_code = res.result().status_code

        if status_code == 403:
            print("Invalid API key--")
            return False
        return True

    session = FuturesSession()

    key_validated = False
    while not key_validated:
        api_key = input("Enter the API key: ")
        key_validated = validated_api_key(session, api_key)

    return session, api_key

if __name__ == '__main__':
    main()
