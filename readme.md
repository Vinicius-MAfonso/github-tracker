# GitHub Activity Tracker

A command-line tool to fetch and display the recent activity of any GitHub user using the GitHub API.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Output Examples](#output-examples)
- [Error Handling](#error-handling)
- [Advanced Features](#advanced-features)

## Features

- Fetch recent activity from any GitHub user
- Display activity in a readable terminal format
- Support for various event types (pushes, issues, stars, etc.)
- Graceful error handling for invalid users and API failures
- No external dependencies required

## Requirements

- A modern programming language of your choice
- Internet connection to access GitHub API
- **No external libraries or frameworks** for API calls (pure language built-ins only)

## Installation

1. Clone this repository
2. Navigate to the project directory
3. Follow language-specific setup instructions for your chosen implementation

## Usage

Run the CLI with a GitHub username as an argument:

```bash
github-activity <username>
```

### Example

```bash
github-activity kamranahmedse
```

## API Reference

### GitHub Events Endpoint

The tool uses the GitHub API events endpoint to fetch user activity:

```
GET https://api.github.com/users/<username>/events
```

Example:
```
https://api.github.com/users/kamranahmedse/events
```

For more details, see the [GitHub API documentation](https://docs.github.com/en/rest/activity/events?apiVersion=2022-11-28).

## Output Examples

```
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
```

## Error Handling

The application handles the following error scenarios gracefully:

- **Invalid username**: Displays a user-friendly error message if the GitHub user doesn't exist
- **API failures**: Handles network errors and rate limiting appropriately
- **Empty activity**: Handles users with no recent public activity

## Advanced Features

Consider these enhancements for a more sophisticated implementation:

- **Filter by event type**: Allow users to filter activity by specific event types (push, pull_request, issues, etc.)
- **Structured output**: Display activity in formats like JSON or tables
- **Caching**: Cache fetched data to improve performance and reduce API calls
- **Additional endpoints**: Explore other GitHub API endpoints for repository information or user statistics
- **Date filtering**: Show activity within a specific date range
- **Sorting options**: Sort activity by date, type, or repository