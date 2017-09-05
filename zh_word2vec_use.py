#coding: utf-8
#中文版处理的word2vec使用

from gensim import models
# 引入日志配置
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = models.Word2Vec.load("./zh_word2vec")

print '\n女人 + 丈夫 - 男人:'
result = model.most_similar(positive=['女人', '丈夫'], negative=['男人'], topn=1)
print result[0][0], result[0][1]

print '\n抢夺和抢劫相近程度:'
print model.similarity('抢夺', '抢劫')

print "\n抢劫的近义词"
result = model.most_similar(['抢劫'])
for value in result:
    print value[0], value[1]

print '\n公司法的近义词:'
result = model.most_similar(['公司法'])
for value in result:
    print value[0], value[1]

print '\n公司法和协议组成的近义词:'
result = model.most_similar(['公司法', '协议'])
for value in result:
    print value[0], value[1]

print '\n委托书的近义词:'
result = model.most_similar(['委托书'])
for value in result:
    print value[0], value[1]

print '\n投资的近义词:'
result = model.most_similar(['投资'])
for value in result:
    print value[0], value[1]


print "\n找出投资、抢劫、强奸、盗窃中,哪个词不是一组的:"
result = model.doesnt_match(['投资', '抢劫', '强奸', '盗窃'])
print result
