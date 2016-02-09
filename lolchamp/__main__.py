from requests_futures.sessions import FuturesSession

def main():
    session = authorize_user()

def authorize_user():
    """
    Opens up an async requests session to persist the connection to the
    endpoint. Validates the API key and returns the session.
    """
    def validate_api_key(session, key):
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

    valid_key = False
    while not valid_key:
        api_key = input("Enter the API key: ")
        valid_key = validate_api_key(session, api_key)

    return session

if __name__ == '__main__':
    main()
