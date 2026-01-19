from concurrent.futures import ThreadPoolExecutor


class PreFetcher:
    def __init__(self, api_client):
        self.api = api_client

    def fetch_all(self, endpoints):
        with ThreadPoolExecutor(max_workers=3) as executor:
            tenants_future = executor.submit(self.api.get, endpoints["tenants"])
            vs_future = executor.submit(self.api.get, endpoints["virtual_services"])
            se_future = executor.submit(self.api.get, endpoints["service_engines"])

            tenants = tenants_future.result()
            virtual_services = vs_future.result()
            service_engines = se_future.result()

        print(f"Pre-Fetcher: Tenants fetched = {len(tenants.get('results', []))}")
        print(f"Pre-Fetcher: Virtual Services fetched = {len(virtual_services.get('results', []))}")
        print(f"Pre-Fetcher: Service Engines fetched = {len(service_engines.get('results', []))}")

        return virtual_services
