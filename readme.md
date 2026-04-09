# GitHub Tracker

A simple command-line tool to display your recent GitHub activity in an easy-to-read format.

## Features

- Fetches your recent GitHub events from the GitHub API
- Groups events by repository
- Displays a summary of your activities including:
  - Created repositories
  - Deleted repositories
  - Created discussions
  - Forked repositories
  - Pushed commits
  - Starred repositories

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/github-tracker.git
cd github-tracker
```

2. No external dependencies required (uses only Python standard library)

## Usage

Run the tracker with a GitHub username:

```bash
python main.py <username>
```

### Example

```bash
python main.py torvalds
```

This will display output similar to:

```
 - Pushed 5 commits to linux
 - Starred torvalds/kernel
 - Created 2 discussions in linux
```

## Project Structure

```
github-tracker/
├── main.py           # Entry point with CLI argument parsing and event processing
├── src/
│   ├── __init__.py   # Package initialization
│   └── api.py        # GitHub API interaction module
└── readme.md         # This file
```

## How It Works

1. **API Connection**: Connects to the GitHub API (`api.github.com`)
2. **Event Fetching**: Retrieves the latest events for the specified user
3. **Event Organization**: Groups events by repository name
4. **Output Formatting**: Displays a human-readable summary of activities

## API Details

Uses the GitHub REST API endpoint:
```
GET /users/{user}/events
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License

Based on: https://roadmap.sh/projects/github-user-activity