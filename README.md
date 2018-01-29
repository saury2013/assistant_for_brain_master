# assistant_for_brain_master

微信头脑王者辅助

#基本原理
1.安装mitmproxy拦截特定的response

2.获取到返回的json数据后解析，得到问题和选项，然后先取数据库查询有无这个问题，没有就自动去百度查询。

3.改写response里的json数据，在选项后面加上备注，数据库有的问题，在正确选项后加[right]，
    数据库没有的把百度搜索的结果统计选项出现的次数并标注在选项后面
    
#操作步骤
1.安装mitmproxy
    pip install mitmproxy
![step0][https://github.com/saury2013/Brain_master_assistant.git/imgs/step0.png]
2.设置代理
![step1][https://github.com/saury2013/Brain_master_assistant.git/imgs/step1.png]
![step2][https://github.com/saury2013/Brain_master_assistant.git/imgs/step2.png]
![step3][https://github.com/saury2013/Brain_master_assistant.git/imgs/step3.png]
3.命令行运行脚本
![step4][https://github.com/saury2013/Brain_master_assistant.git/imgs/step4.png]
4.安装证书，在手机浏览器输入mitm.it
![step5][https://github.com/saury2013/Brain_master_assistant.git/imgs/step5.png]
![step6][https://github.com/saury2013/Brain_master_assistant.git/imgs/step6.png]
![step7][https://github.com/saury2013/Brain_master_assistant.git/imgs/step7.png]
5.信任证书，IOS系统下一定要注意这个步骤
![step8][https://github.com/saury2013/Brain_master_assistant.git/imgs/step8.png]
***
演示效果
![show][https://github.com/saury2013/Brain_master_assistant.git/imgs/show.png]
![show2][https://github.com/saury2013/Brain_master_assistant.git/imgs/show2.png]