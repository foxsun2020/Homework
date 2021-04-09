# 导论
## GAN简介
传统机器学习算法擅长识别已有数据中的模式：分类、回归……

generative-adversarial-network

### 何时停止循环
零和博弈--纳什均衡点：

1. 生成的和真实的一样了

2. 鉴别器智能随机猜测真实性了（真的概率为50%）

GAN从而就收敛了，现实中GAN几乎不能达到纳什均衡


### 生成手写数字
生成器：学习合成这些模式而不是识别这些模式

#### 与传统网络的不同：

1. GAN的loss function依赖于两个network的parameters
    
2. GAN中每个network只能调整自己的parameters
    
#### 对抗的目标：

1. 生成器：使得D(x*)尽可能接近1
    
2. 鉴别器：使得D(x*)尽可能接近0
    
#### 混淆矩阵

鉴别器的分类结果：

true positive--真实样本正确分类为真

false negative--真实样本错误分类为假

true negative--生成样本正确分类为假

false positive--生成样本错误分类为真

生成器不关心鉴别器对真实样本的分类效果，只关心对生成样本的分类效果。

#### GAN算法

mini-batch：取随机r小批量

训练鉴别器时，生成器parameters保持不变。训练生成器时，鉴别器parameters保持不变。

训练超参数：

迭代次数呵批大小

目前没有一种行之有效的办法确定正确的迭代次数或正确的批大小，只能观察训练精度，通过反复试验来确定。

### DCGAN
Deep Convolutional GAN

batch normalization: 数据的缩放，使其具有零均差和单位方差。

$$ \hat{x} = \frac{x - \mu }{\sigma } $$

covariate shift: 训练旗舰各层之间输入值分布的变化。使用batch normaliztion进行减少。

批归一化：

$$ \hat{x} = \frac{x - \mu_{B}}{\sqrt {\sigma^{2} + \varepsilon}} $$

增加$ \varepsilon $项是为了保持数值稳定，避免被0除。

#### 转置卷积
用于增加宽度和高度，同时减小深度。

# 前沿主题

### 评估

#### 评估框架

使用最大似然可能会生成现实世界中永远不会存在的样本。

#### IS

Inception Score

采用真实分布和生成分布之间的KL差异

对上一步的结果求指数

#### FID

Frechet Inception Distance

计算嵌入均值的距离、方差和两个分布的协方差
