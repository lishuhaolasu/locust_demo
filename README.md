# locust_demo

学习使用 locust

## 安装

```bash
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple locust
```

## 使用

常用方式如下：

```bash
locust # 自动寻找当前目录下的locustfile.py运行
```

常用参数：

```bash
-f 指定文件
-T , -tags 指定对应的标签，空格分割
-E , --exclude-tags 与tags相反
--config 指定config文件
-H , --host 指定加载测试的主机
--web-host 指定能访问的主机，默认为*
--web-port 指定绑定的端口
--tls-cert 指定正数
--tls-key 指定key
--web-auth 指定账号密码 username:password
```

无头参数:headless模式下的参数

```bash
--headless 无头模式
-u , --users 指定用户数量
-r , --hatch-rate 孵化速度
```

更多参数:[locust 全部参数](https://docs.locust.io/en/stable/configuration.html#all-available-configuration-options)

## 运行

加载:  

+ cmd args  
+ ./locustfile.py

编写:  
demo.py中有简单的编写说明

## 配置

加载顺序:

+ cmd args  
+ env vars  
+ (file specified using --conf)  
+ ./locust.conf  
+ ~/locust.conf  

编写:  
config.py中有简单的编写说明
