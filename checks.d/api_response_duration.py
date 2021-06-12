from datadog_checks.base import AgentCheck

__version__ = "1.0.0"

import requests

class CheckValue(AgentCheck):
  def check(self, instance):
    response = requests.get("https://codefun.vn/api/logs")
    json = response.json()
    data = list(filter(
      lambda event:
        event["Content"]["url"] != "/judge/ping" and event["Content"]["url"] != "/logs" and event["Content"]["url"] != "/judge/logs",
      json["data"]
    ))
    self.gauge('codefun.api.duration', data[0]["Content"]["duration"])