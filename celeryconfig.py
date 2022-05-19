# global Celery options that apply to all configurations
# enable the json serializer
task_serializer = "pickle"
result_serializer = "pickle"
accept_content = ["pickle", "json"]

task_routes = {"web.*": {"queue": "web"}}

enable_utc = False
