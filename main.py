from locust import HttpUser, TaskSet, task, User, between
from secret_config import host
# 任务套件，需要继承自 TaskSet
class UserBehavior(TaskSet):
    def on_start(self):
        # 每次启动时调用
        print('this is start method')

    def on_stop(self):
        # 每次结束时调用
        print('this is stop method')

    # 使用task修饰的函数表示这是一个任务
    # 括号内的数字代表权重，权重越大，执行的概率越高。默认为1
    @task(20)
    def get_ifr(self):
        # client属性可以发起请求
        # 这个属性继承自requests的session类，可以使用session的所有方法
        self.client.get('/')

    @task(10)
    def get_fbc(self):
        self.client.get('get_version')
    

# 测试用户类，需要继承自 User (原Locust,已改名)
class WebsiteUser(User):
    # 测试地址的域名
    host = host
    # 测试套件
    task_set = UserBehavior
    # (每次测试间)最小等待间隔
    min_wait = 20
    # (每次测试间)最大等待间隔
    max_wait = 50
    # 间隔也可以直接使用下面这个方式, 单位是秒
    # wait_time = between(1,2)
    weight = 10




# 执行
# locust -f ${python_script}.py 
# -host=${host}         指定请求的地址，如果不指定则读取配置类中的host
# --master 指定主进程   单台机器如果不能模拟更多用户时，则可以用这个参数指定主服务器
