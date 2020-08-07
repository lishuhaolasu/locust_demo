from locust import HttpUser, TaskSet, task, User, between, tag, events
from secret_config import host
from tasks_demo import TaskSetDemo, task_demo02

# 测试用户类，需要继承自 User (原Locust,已改名)
# 最基本的类，需要首先创建
class UserDemo(User):
    # 基本属性

    # 等待时间，需要返回一个时间，可以使用between，参数单位为秒
    wait_time = between(0.01,0.05)
    # 需要注意的是，wait_time是一个callable属性，调用之后返回一个数字即可，如：
    # last_wait_time = 0
    # def wai_time(self):
    #     self.last_wait_time += 0.1
    #     return self.last_wait_time

    # 权重值，表示该用户的权重。默认为1，值越大、权重越高。如：这个用户的权重值为10，是默认用户被调用的概率的10倍
    weight = 10

    # 测试地址的主机。这个是默认值，如果在调用时没有指定--host参数，则使用这个值
    host = host

    # environment属性，对当前环境进行操作。如果是主节点，则影响所有节点，如果是子节点，则影响自身。

    # task属性
    # 方式1：直接在这个类中声明一个函数，并使用task进行装饰
    # 也可以指定任务权重值。这个权重值的含义与本类的权重值含义一致，都是用来指定执行概率的
    @task(1)
    def task_demo01(self):
        ...
    # 方式2：添加外部任务
    # task_demo02 是一个类外定义的函数，可以将这个函数添加到一个列表中
    tasks = [task_demo02]
    # 或：这种方法可以指定权重值。实现上是将dict转成list，然后配权重随机
    tasks = {task_demo02:10}

    # TaskSet类。是的，task还可以是一个类
    # 这个类除了在调用上有区别外，还提供了client便于使用
    # 方式1：在本类外定义一个类，继承自TaskSet类
    tasks = [TaskSetDemo]
    # 方式2：直接把这个类定义在本类中，并使用task进行修饰。不建议这么搞
    @task
    class TaskSetDemo02(TaskSet):
        ...

    # task标签
    # 通过tag来修饰task，可以在运行时指定运行对应标签
    @tag('hehe')
    @task
    def task_demo03(self):
        ...

# 负载测试开始时执行
@events.test_start.add_listener
def on_test_start(**kwargs):
    ...
# 负载测试结束时执行
@events.test_stop.add_listener
def on_test_stop(**kwargs):
    ...
# on_start类似作用范围是class，on_test_start是整个test。
# 如果是分布式，on_test_start仅会在master节点触发

# 网页测试类用户，这个用户可以通过client进行http请求
class HttpUserDemo(HttpUser):
    wait_time = between(0.01,0.03)
    @task(20)
    def get_ifr(self):
        # client属性可以发起请求
        # 这个属性继承自requests的session类，可以使用session的所有方法
        self.client.get('/')

    @task(10)
    def get_fbc(self):
        self.client.get('/get_version')
    
    # 可以对请求的结果进行标记
    @task(0)
    def get_nothing(self):
        with self.client.get('/',catch_response=True) as response:
            if response.status_code != 200:
                response.failure('get failed!')
            else:
                response.success()
    # 代理：由于安全原因，一般关闭了环境代理，如果有需要，可以开启
    # self.client.trust_env = True

# 执行
# locust -f ${python_script}.py 
# -host=${host}         指定请求的地址，如果不指定则读取配置类中的host
# --master 指定主进程   单台机器如果不能模拟更多用户时，则可以用这个参数指定主服务器
