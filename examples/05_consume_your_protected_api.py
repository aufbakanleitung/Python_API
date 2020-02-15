# https://docs.thecatapi.com/
import requests
import json
import argparse
from requests.auth import HTTPBasicAuth

# -= Assignment =-
# Access your http server through your protected API

def run(user, password):
    api_url = ""
    headers = {"Accept": "application/json"}

    auth = HTTPBasicAuth(username=user, password=password)

    response = requests.get(api_url, headers=headers, auth=auth)

    print("code:" + str(response.status_code))
    print("******************")

    if response.status_code == 200:
        print("headers:" + str(response.headers))
        print("******************")
        print("content:" + str(response.text))
        print("******************")

        print("pretty content:" + json.dumps(json.loads(response.text), indent=2))

    elif response.status_code == 401:
        print("headers:" + str(response.headers))
        print("******************")
        print("Oh no!!! You are not authorized:")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a simple API Call")
    parser.add_argument(
        "-u",
        "--user",
        default="",
        help="Specify the User",
    )

    parser.add_argument(
        "-p",
        "--password",
        default="",
        help="Specify the Password",
    )

    parser.print_help()

    args = parser.parse_args()
    run(user=args.user, password=args.password)
