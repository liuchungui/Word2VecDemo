#coding: utf-8
#中文版处理的word2vec

from gensim import models
import os
# 引入日志配置
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

file_path = "case.txt"
train_dir = "./data"

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        # 遍历对应目录下所有文件
        for filename in os.listdir(self.dirname):
            file_path = self.dirname + "/" + filename
            for line in open(file_path):
                # 以空格进行分割词语
                words = line.split(" ")
                result_word = []
                for word in words:
                    if word and word != '\n':
                        result_word.append(word)
                yield result_word

sentences = MySentences(train_dir)
model = models.Word2Vec(sentences, workers=20, min_count=5, size=200)

# 保存模型
model.save("./zh_word2vec")

