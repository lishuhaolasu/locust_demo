from locust import TaskSet, task, SequentialTaskSet,events, HttpUser

# 任务套件，需要继承自 TaskSet
class TaskSetDemo(TaskSet):
    # 用户启动时调用
    def on_start(self):
        print('this is start method')

    # 用户结束时调用,时机在interrupt之后
    def on_stop(self):
        print('this is stop method')

    # locust永远不会结束，除非使用interrupt显式结束
    def stop(self):
        self.interrupt()
    
@task
def task_demo02(l):
    ...

# 序列任务套组。
# 1：执行顺序：所有的任务按照声明顺序执行：这个任务的执行顺序是：last_task->task_demo02->first_task->InnerTaskSet
# 2：嵌套：序列任务套组和任务套组可以互相嵌套
# 3：执行特点：无视权重值，严格按顺序执行
class SequentialTaskSetDemo(SequentialTaskSet):
    
    @task
    def last_task(self):
        ...

    tasks = [task_demo02]

    @task
    def first_task(self):
        ...

    class InnerTaskSet(TaskSet):
        
        @task
        def task_01(self):
            ...
    
