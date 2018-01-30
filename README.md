# assistant_for_brain_master
微信头脑王者辅助

#基本原理<br>
1.安装mitmproxy拦截特定的response<br>

2.获取到返回的json数据后解析，得到问题和选项，然后先取数据库查询有无这个问题，没有就自动去百度查询。

3.改写response里的json数据，在选项后面加上备注，数据库有的问题，在正确选项后加[right]，<br>
    数据库没有的把百度搜索的结果统计选项出现的次数并标注在选项后面

4.下一步研究自动运行，找了半天只能在android系统才能使用ADB操作

5.另外写了一个web端用于接收请求，然后发送adb指令给手机，因为脚本是在mitmproxy运行，<br>
暂时不知道如何在respone里处理这个事件


#操作步骤<br>
1.安装mitmproxy<br>
~~~
    pip install mitmproxy
~~~
![step0](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/step0.png)<br>

2.进入手机设置里的wifi,设置代理<br>

![step1](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/step1.PNG)<br>
![step2](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/step2.PNG)<br>
![step3](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/step3.PNG)<br>

3.命令行运行脚本(手动版本是mitmproxy_script.py,自动版是mitmproxy_script_auto_run.py)<br>

![step4](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/step4.png)<br>
4.安装证书，在手机浏览器输入mitm.it.(安卓手机有些无法直接安装，在第三方浏览器打开这个网址下载安装才行)<br>

![step5](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/step5.PNG)<br>
![step6](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/step6.PNG)<br>
![step7](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/step7.PNG)<br>

5.信任证书，IOS系统下一定要注意这个步骤(安卓系统不用这步)<br>

![step8](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/step8.PNG)<br>

6.要运行自动答题脚本的话需要在安装adb，并把adb.exe的路径设置到环境变量中，USB线连接手机并打开开发者模式<br>
要设置点击坐标，可以打开安卓系统的设置-更多设置-开发者选项-指针位置，这样你点击屏幕最上方会显示dX,dY坐标<br>
获得每个选项的坐标，替换start.py中的setting<br>

7.自动答题脚本还需要先安装Flask，再运行web端start.py
~~~
    pip install flask
~~~

***
演示效果<br>

![show](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/show.PNG)<br>
![show2](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/show2.PNG)<br>
