from datadog_checks.base import AgentCheck

__version__ = "1.0.0"

import requests
from datetime import datetime, timedelta

class CheckValue(AgentCheck):
  def check(self, instance):
    interval = 15
    if "min_collection_interval" in instance:
        interval = instance["min_collection_interval"]

    response = requests.get("https://codefun.vn/api/judge/logs")
    data = response.json()["data"]
    data = list(map(
        lambda event: { "Time": datetime.fromisoformat(event["Time"].split(".")[0]), "Content": event["Content"] },
        data
    ))
    time_limit = datetime.now() - timedelta(seconds=interval)
    self.count("codefun.submissions.scored", sum(1 for event in data if event["Time"] > time_limit and "scored" in event["Content"]))
    self.count("codefun.submissions.sent_to_judge", sum(1 for event in data if event["Time"] > time_limit and "Sent" in event["Content"]))