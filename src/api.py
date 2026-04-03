import json


def get_events(connection, user: str) -> dict:
    headers={
        'X-GitHub-Api-Version': '2026-03-10',
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'github-tracker',
    }
    connection.request("GET", f"/users/{user}/events", headers=headers)
    response = connection.getresponse()
    data = response.read()
    return json.loads(data.decode("utf-8"))