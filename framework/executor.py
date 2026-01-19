from framework.prefetcher import PreFetcher
from framework.validators import find_virtual_service, validate_enabled_state


class TestExecutor:
    def __init__(self, api_client, api_config, testcase_config):
        self.api = api_client
        self.api_config = api_config
        self.testcase = testcase_config

    def execute(self):
        # Pre-Fetcher
        prefetcher = PreFetcher(self.api)
        vs_list = prefetcher.fetch_all(self.api_config["endpoints"])

        # Pre-Validation
        target_name = self.testcase["virtual_service"]["target_name"]
        target_vs = find_virtual_service(vs_list, target_name)

        if not target_vs:
            raise Exception("Target Virtual Service not found")

        print("Pre-Validation: Checking enabled state")
        validate_enabled_state(
            target_vs,
            self.testcase["validation"]["pre_enabled"]
        )

        # Task / Trigger
        uuid = target_vs["uuid"]
        print(f"Task: Disabling Virtual Service {target_name}")

        self.api.put(
            f"/api/virtualservice/{uuid}",
            self.testcase["task"]["payload"]
        )

        # Post-Validation
        print("Post-Validation: Verifying disabled state")
        updated_vs = self.api.get(f"/api/virtualservice/{uuid}")
        validate_enabled_state(
            updated_vs,
            self.testcase["validation"]["post_enabled"]
        )

        print("TEST RESULT: Virtual Service disabled successfully")
