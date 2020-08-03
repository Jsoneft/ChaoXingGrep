# ChaoXingGrep

![txtJcF.jpg](https://s1.ax1x.com/2020/06/14/txtJcF.jpg)

## Introduction -  超星爬取题库的小脚本

> `Summary` - 利用抓包工具(http Catcher), 捕获  <学生自测 - 查看试卷> 操作的`数据包`, 然后在pc端复现`get请求`, 拿到题库, 配合相关投屏软件(scrspy), 使用QQ的`OCR`,  将识别的内容复制至剪贴板, 配合`轮询剪贴板`脚本(拿到数据并在题库中进行模糊匹配), 从而实现答题速度 **9s/题** , 适用于一些不适合当代大学生做的思政考试

<kbd>注意</kbd> : 当且仅当考试题库在学生自测的章节里才有有效

## Features

* 可移植性强
* 目前支持`windows` 和`mac` 两种系统
* 可扩展性强, 只要是能复现的请求, 都能扒到题库

## Requirements

详见 `requirements.txt`

### Installation

~~安装?~~</br>无需安装, <u>双击exe即可食用</u>

## Usage

* windows系统: 双击dist/main.exe
* Mac系统: 双击Unix可执行文件

## Development

* mac端 : `http catcher抓包` + `scrcpy投屏`
* windows端 : `开发者助手` + `华为多屏协同`(`scrcpy`在windows上可用)

## FAQ

*联系开发小哥哥 QQ:1018437256 1529420440*

## Support

走过路过给个星傲~

## Contact

1018437256@qq.com , 793183305@qq.com

## Authors and acknowledgment

HBUT 18级 左佳逊, 周世星

## License

<kbd>HBUT.License</kbd>
