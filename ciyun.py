# -*- coding=utf8 -*-
import matplotlib.pyplot as plt
import jieba.analyse
import numpy as np
from PIL import Image
from matplotlib import colors
from wordcloud import WordCloud, ImageColorGenerator
from random import *


def main():
    engine = CiYun()
    basename = 'col_23'
    txt_file = f"input_txt/{basename}.txt"
    source_img = "backgrounds/mask-cloud.png"
    font_path = "fonts/Alibaba-PuHuiTi-Medium.TTF"
    content = engine.readTxt(txt_file)
    keywords = engine.textDict(content)
    kwargs = {
        ## 轮廓颜色
        # "contour_color": "rgba({}, {}, {},{})".format(255,0,0,1),\
        ## 修改词云字体颜色
        # "color_list":["#FF0000","#a41a1a", "#FF9999",\
        #     "#FF6666", "#FF0033", "#CC0033", "#990033",\
        #     "#FFFFCC", "#CCCCFF","#996699", "#cd5c5c"],\
        ## 输出图片放在哪里
        "outfile": f"results/{basename}.png"}
    engine.renderWordCloud(keywords, source_img, font_path, **kwargs)

class CiYun():
    def random_color_func(self, word=None, font_size=None, position=None,\
            orientation=None, font_path=None, random_state=None):
        """ 指定了颜色, random返回个每个单词 """
        # l1 = [(120,100,90), (240,100,90), (0,100,90), (60,100,90),(20,100,70)]
        # 紫色，红色，黄色，橙色，绿色,
        # #CCCCFF, #FFCCCC,#FFFFCC,#FF9966,#CCFFCC
        l1 = [(275,100,74), (275,100,44), (275,100,42)]
        # #FF9999, FF6666, FF0033,CC0033, 990033 ,FFFFCC,
        # CCCCFF,996699,996699,FF9966
        hsl = sample(l1, 1)[0]
        h = hsl[0]
        s = hsl[1]
        l = hsl[2]
        return "hsl({}, {}%, {}%)".format(h, s, l)

    # def random_color_func_v2(self, word=None, font_size=None,\
    #         position=None,  orientation=None, font_path=None, random_state=None):
    #     """ 随机产生一些颜色的另一种生成方法
    #     """
    #     h  = randint(120, 250)
    #     s = int(100.0 * 255.0 / 255.0)
    #     l = int(100.0 * float(randint(60, 120)) / 255.0)
    #     return "hsl({}, {}%, {}%)".format(h, s, l)

    def grey_color_func(self, word, font_size, position,\
            orientation, random_state=None, **kwargs):
        """change the value in return to set the single color need, in hsl format.
            主要是紫色系
        """
        h = np.random.randint(240, 310)
        s = 100
        l = np.random.randint(40, 100)
        return "hsl({}, {}%, {}%)".format(h, s, l)

    def readTxt(self, file, encoding="utf8"):
        with open(file, "r", encoding="utf8") as f:
            txt = f.read()
        return txt

    def textDict(self, content):
        """
        jieba 提取500个关键词及其比重
        :return: {'时间': 1.0, '我会': 0.8452287990383122, '项目': 0.6111491255938793}
        """
        # jieba里不想分开的词，可以用add_word来特殊说明
        jieba.add_word('头脑风暴')
        result = jieba.analyse.textrank(
            content, topK=500, withWeight=True, allowPOS=("n"))
        # print(result)
        # 转化为比重字典
        keywords = dict()
        for i in result:
            keywords[i[0]] = i[1]
        return keywords

    def renderWordCloud(self, keywords, sourceImg, fontPath, **kwargs):
        # 获取图片资源
        image = Image.open(sourceImg)
        # 转为像素矩阵
        graph = np.array(image)
        newk = {}
        if "color_list" in kwargs.keys():
            newk["colormap"] = colors.ListedColormap(kwargs["color_list"])
        if "contour_color" in kwargs.keys():
            newk["contour_color"] = kwargs["contour_color"]
        
        wc = WordCloud(
            font_path=fontPath,
            # background_color="rgba({}, {}, {},{})".format(123, 104, 238,1),
            background_color="white",
            max_words=500,
            # max_font_size = 100,
            margin=1,
            scale=10,
            # 使用的词云模板背景
            mask=graph,
            color_func=self.grey_color_func,
            contour_width=0, **newk)# contour_width=1 contour_color="black"边框颜色
        # 基于关键词信息生成词云
        wc.generate_from_frequencies(keywords)
        wc.to_file(kwargs["outfile"])
        # 读取模板图片的颜色
        # image_color = ImageColorGenerator(graph)
        # 生成词云图
        plt.imshow(wc)
        # # 用模板图片的颜色覆盖
        # plt.imshow(wc.recolor(color_func=image_color))
        # 关闭图像坐标系
        plt.axis("off")
        # 显示图片--在窗口显示
        # plt.show()

if __name__ == "__main__":
    main()