FROM datadog/agent:7

COPY conf.d/http_check.d/site.yml /etc/datadog-agent/conf.d/http_check.d/site.yml
