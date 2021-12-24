from containers import service

task_id = service.start_task("amass", args={'domain': 'owasp.org'})
for line in service.stream_task_log(task_id):
    print(line.decode("utf-8"))
