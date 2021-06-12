FROM datadog/agent:7

COPY conf.d/http_check.d/site.yml /etc/datadog-agent/conf.d/http_check.d/site.yml
COPY conf.d/api_response_duration.yml /etc/datadog-agent/conf.d/api_response_duration.yml
COPY checks.d/api_response_duration.py /etc/datadog-agent/checks.d/api_response_duration.py
RUN rm -rf /etc/datadog-agent/conf.d/disk.d /etc/datadog-agent/conf.d/cpu.d /etc/datadog-agent/conf.d/file_handle.d