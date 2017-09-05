## 说明
这是博客[word2vec初体验](http://www.liuchungui.com/2017/09/04/word2vec%E5%88%9D%E4%BD%93%E9%AA%8C/)的Demo

## 使用

#### clone代码到本地
```
git clone git@github.com:liuchungui/Word2VecDemo.git
```

#### 安装gensim依赖
```
pip install gensim
```

#### 训练
```
python zh_word2vec.py
```

#### 查看效果
```
python zh_word2vec_use.py
```

## 各文件作用
#### data文件夹中的8个txt文件
分好词的语料库

#### zh_word2vec.py
训练模型的代码

#### zh_word2vec_use.py
查看训练模型效果的代码