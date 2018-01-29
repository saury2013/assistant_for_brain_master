# assistant_for_brain_master
微信头脑王者辅助

#基本原理<br>
1.安装mitmproxy拦截特定的response<br>

2.获取到返回的json数据后解析，得到问题和选项，然后先取数据库查询有无这个问题，没有就自动去百度查询。

3.改写response里的json数据，在选项后面加上备注，数据库有的问题，在正确选项后加[right]，<br>
    数据库没有的把百度搜索的结果统计选项出现的次数并标注在选项后面

4.下一步研究自动运行


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

3.命令行运行脚本<br>

![step4](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/step4.png)<br>
4.安装证书，在手机浏览器输入mitm.it<br>

![step5](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/step5.PNG)<br>
![step6](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/step6.PNG)<br>
![step7](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/step7.PNG)<br>

5.信任证书，IOS系统下一定要注意这个步骤<br>

![step8](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/step8.PNG)<br>
***
演示效果<br>

![show](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/show.PNG)<br>
![show2](https://github.com/saury2013/assistant_for_brain_master/blob/master/imgs/show2.PNG)<br>
