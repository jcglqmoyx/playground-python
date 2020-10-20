import wordcloud
import matplotlib.pyplot as plt


def generate_wordcloud():
    file = open('/home/jcglqmoyx/Desktop/visualize_novel.py', 'r')
    txt = file.read()
    file.close()
    # import jieba
    # seg_list = jieba.cut(txt, use_paddle=True)
    # txt = ' '.join(list(seg_list))
    # print("Paddle Mode: " + '/'.join(list(seg_list)))

    w = wordcloud.WordCloud(
        background_color='black',
        # mask=backgroup_Image,  # 背景图
        mask=plt.imread('/home/jcglqmoyx/Desktop/222.jpg'),
        # font_path='/home/jcglqmoyx/Downloads/微软雅黑.ttf',
        height=2000,
        width=2400,
    )

    w.generate(txt)
    w.to_file("/home/jcglqmoyx/Desktop/222.png")


generate_wordcloud()
