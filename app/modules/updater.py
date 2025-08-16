import logging
import requests
from packaging.version import parse as parse_version

class Updater:
    """
    Handles checking for new application versions from a GitHub repository.
    """
    def __init__(self, current_version, github_repo_url):
        """
        Initializes the Updater.
        :param current_version: The current version of the application (e.g., "1.0.0").
        :param github_repo_url: The URL to the GitHub repository's latest release API.
                                (e.g., "https://api.github.com/repos/user/repo/releases/latest")
        """
        self.current_version = parse_version(current_version)
        self.api_url = github_repo_url
        logging.info(f"Updater initialized with current version {self.current_version}")

    def check_for_updates(self):
        """
        Checks for a newer version on GitHub.
        Returns a dictionary with update info if a new version is found, otherwise None.
        """
        logging.info(f"Checking for updates at {self.api_url}")
        try:
            response = requests.get(self.api_url, timeout=5)
            response.raise_for_status()  # Raise an exception for bad status codes
            latest_release = response.json()

            latest_version_str = latest_release.get('tag_name', '0.0.0').lstrip('v')
            latest_version = parse_version(latest_version_str)

            logging.info(f"Latest version found: {latest_version}")

            if latest_version > self.current_version:
                logging.info(f"New version {latest_version} is available.")
                return {
                    "latest_version": str(latest_version),
                    "release_notes": latest_release.get('body', 'No release notes provided.'),
                    "download_url": latest_release.get('html_url', '#')
                }
        except requests.exceptions.RequestException as e:
            logging.error(f"Update check failed due to a network error: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred during update check: {e}")

        return None
