# ChaoXingGrep

![txtJcF.jpg](https://s1.ax1x.com/2020/06/14/txtJcF.jpg)


## Introduction -  超星爬取题库的小脚本

### Summary - 利用抓包工具(http Catcher),  捕获  <学生自测 - 查看试卷> 操作的数据包, 然后在pc端复现get请求, 拿到题库, 配合相关投屏软件(scrspy), 使用QQ的 OCR,  将识别的内容复制至剪贴板, 配合 轮询剪贴板脚本(拿到数据并在题库中进行模糊匹配), 从而实现答题速度 **9s/题** , 适用于一些不适合当代大学生做的思政考试

### <kdb>注意</kdb> : **当且仅当考试题库在学生自测的章节里才有有效**

### Features - 可移植性强, 目前支持windows 和mac 两种系统, 可扩展性强, 只要是能复现的请求, 都能扒到题库

### Requirements - 详见 requirements.txt 

### Installation - 无需安装, 双击exe即可食用

### Usage - windows系统: 双击dist/main.exe , Mac系统: 双击Unix可执行文件

### Development - mac端 : http catcher抓包 + scrcpy投屏 , windows端 : 开发者助手 + 华为多屏协同

### FAQ - 联系开发小哥哥 QQ:1810311204

### Support - 走过路过给个星傲~

### Contact - jasonleft@qq.com , 793183305@qq.com

# Authors and acknowledgment - HBUT 18级 左佳逊, 周世星

## License - HBUT.License