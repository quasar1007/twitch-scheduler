## Twitch Scheduler

### Purpose

The purpose of this project is to have a script that will open up Twitch streams when they go live - primarily useful
for drops.

### Prerequisites

- Python 3.12+ 
- Pip
- Twitch account

### Install

1. Optionally create a venv (can be user installed as well) and activate it
    - To create a venv run `python -m venv .venv`
2. Run `pip install .` to install all the relevant dependencies

### Configure

- Examine `config.yaml` and add entries to the `streamers` list as needed
- Create the following environment variables. See [Twitch Authentication](#twitch-authentication) for more details on how to get these values
  - `TwitchClientId`: This is the client id related to your Twitch account
  - `TwitchSecret`: This is the secret for Twitch authentication

### Run

- From the base directory run `python src/main.py` to just run the script manually
- Alternatively, set up a Windows or Linux service that calls the script on startup or on a schedule

### Twitch Authentication

This section explains how to create a client id and secret for Twitch authentication

#### Register an OAuth Application

- Navigate to [Twitch Developer Console](https://dev.twitch.tv/console)
- Click `Applications`
- Click `Register Your Application` and fill out the form
  - Name can be anything as long as it makes sense to you
  - Put `http://localhost` for the OAuth Redirect URL. This value also is not used, but is required for the form
  - Make sure `Client Type` is set to `Confidential`
- Click `Create`

#### Get Client Id

- Navigate to the application you want to use for authentication
- The `Client ID` field is what you are looking for

#### Create a Secret

- Navigate to the application you want to use for authentication
- Click `New Secret`
- Save this value somewhere as after you create it, you cannot access the value again
