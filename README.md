# 词云生成
## 首先讲个故事
有一天，在一个问卷里，我们收集到了一些学生对在XXX比赛中最想学习的三件事，这是一道开放填写文本题，当然结果会五花八门。

我们想快速可视化吸取问卷里的宝贵反馈，于是我们就想到了词云。

词云能通过显示比较重要的词，根据词频大小来勾勒词的大小的方式，来显示一段文本最重要的信息。
## 软件包准备说明
故事目前来说讲完了，我们来说说要安装的软件版。首先声明，本人安装的python 版本是3.7.5。接下来是一些安装包：
``` cmd
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt
```
当然了，你也可以直接 pip install -r requirements.txt，之所以上面这种写法，就是把下载都圈定在国内，不下载国外的下载包，防止网速蜗牛般奇慢。

## 输入说明
+ 文本输入是个 txt 文本，放在 input_txt 文件夹里。
+ source_img 是词云背景轮廓的样式，是一片云，还是一只鸟，还是其他。
+ font_path 告诉机器词的字体格式（防止因默认而用到一些付费商用字体，我通常会用免费开放的阿里普惠体）。

## 代码运行说明
``` python
python ciyun.py
```

## 输出说明
图片放在 results 文件夹里。![结果展示](results/col_23.png)
## 踩坑说明
+ 先用jieba分的词，也有其他分词方式，有兴趣的可以自己修改代码实现。
+ 细节都在代码里，有兴趣可以细品。
+ 出现generate_from_frequencies OSError: cannot open resource 错误！

很可能是 font_path 找不到。试试"fonts/Alibaba-PuHuiTi-Medium.TTF"，

或者从你自己的机子里先找个默认可以显示中文的字体，如"simfang"，整体都搞明白了，再来搞这个字体细节。