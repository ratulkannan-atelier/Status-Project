import requests
from datetime import datetime, timezone


def check_response(url):
    results = {}
    results["url"] = url
    response = requests.get(url, timeout=5)
    results["status"] = response.status_code  # Should print 200

    ms = round(response.elapsed.total_seconds() * 1000, 3)
    results["response_time"] = ms

    timestamp = datetime.now(timezone.utc)
    results["timestamp"] = timestamp
    return results


# print(check_response("https://api.githhub.com"))


print(check_response("https://api.github.com"))
print(check_response("https://www.youtube.com"))
print(check_response("https://www.netflix.com/"))
print(check_response("https://httpbin.org/status/404"))
