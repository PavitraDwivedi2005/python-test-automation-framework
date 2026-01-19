import yaml

from framework.auth import login
from framework.api_client import APIClient
from framework.executor import TestExecutor
from framework.mocks import mock_ssh, mock_rdp


def load_yaml(path):
    with open(path, "r") as file:
        return yaml.safe_load(file)


def main():
    # Load configurations
    api_config = load_yaml("config/api.yaml")
    testcase_config = load_yaml("config/testcases.yaml")

    base_url = api_config["base_url"]
    credentials = api_config["credentials"]

    # Authenticate and get token
    token = login(
    base_url,
    api_config["auth"]["login_endpoint"],
    credentials["username"],
    credentials["password"]
)


    # Initialize API client
    api_client = APIClient(base_url, token)

    # Mock integrations (as required by assessment)
    mock_ssh()
    mock_rdp()

    # Execute test workflow
    executor = TestExecutor(api_client, api_config, testcase_config)
    executor.execute()


if __name__ == "__main__":
    main()
