# from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.util.retry import Retry

# # Define retry strategy
# retry_strategy = Retry(
#     total=3,  # Retry up to 3 times
#     backoff_factor=1,  # Wait 1 second between retries
#     status_forcelist=[429, 500, 502, 503, 504]  # Retry on these status codes
# )

# # Mount the adapter to the session
# session = requests.Session()
# adapter = HTTPAdapter(max_retries=retry_strategy)
# session.mount("https://", adapter)

# try:
#     response = session.get("https://jsonplaceholder.typicode.com/posts")
#     response.raise_for_status()
#     print("Data fetched successfully:", response.json()[:2])
# except requests.exceptions.RequestException as e:
#     print("An error occurred:", e)
