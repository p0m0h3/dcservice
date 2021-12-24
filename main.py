from containers import service

task_id = service.start_task("helloworld")
for line in service.stream_task_log(task_id):
    print(line.decode("utf-8"))
