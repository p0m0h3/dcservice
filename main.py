from containers import service

task_id = service.start_task("helloworld", args={'arg1': 'hello'})
for line in service.stream_task_log(task_id):
    print(line.decode("utf-8"))
