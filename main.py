import argparse
import http.client
from src.api import get_events


def main():
    connection = http.client.HTTPSConnection("api.github.com")
    user = ""
    events = get_events(connection, user)
    repo_events = {}
    for event in events:
        if event["repo"]["name"] in repo_events.keys():
            repo_events[event["repo"]["name"]].append(event["type"])
            continue
        repo_events[event["repo"]["name"]] = [event["type"]]

    for repo_name, events in repo_events.items():
        if "CreateEvent" in events:
            print(f" - Created {repo_name}")

        if "DeleteEvent" in events:
            print(f" - Deleted {repo_name}")
        
        if "DiscussionEvent" in events:
            discussions_len = events.count("DiscussionEvent")
            print(f" - Created {discussions_len} discussions in {repo_name}")
        
        if "ForkEvent" in events:
            print(f" - Forked {repo_name}")
        
        if "PushEvent" in events:
            commits_len = events.count("PushEvent")
            print(f" - Pushed {commits_len} commits to {repo_name}")

        if "WatchEvent" in events:
            print(f" - Starred {repo_name}")

    connection.close()


if __name__ == "__main__":
    main()
