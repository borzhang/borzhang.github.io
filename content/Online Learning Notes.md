Title: Notes on Online Learning
Date: 20161002 15:01
tags: Machine learning

Note: When I take notes on some technical topics, I'll skip basic stuff to save time. What I write down will be mostly problems/results that I've not been familiar with. 

I'm reading basically two quite serious materials about online learning, namely [the Wikipedia page](https://en.wikipedia.org/wiki/Online_machine_learning) and [a long article](http://www.nowpublishers.com/article/Details/MAL-018) published on "Foundations and Trends in Machine Learning". Here's some notes.

#### Concepts clarification
Model is about assumptions, forms, parameters and goals.
During solving a model's objective, one can get a form of some algorithm.
Algorithm is about process of computation, can be used for multiple models.
With different assumptions and conditions, same algorithms can have different results in convergence analysis.
SGD is an algorithm. So are its variants.

#### Statistical learning models

Statistical learning models are the case that the training sample $(x_i,y_i)$ are assumed to be drawn * i.i.d* from the true distribution $p(x,y)$. The objective is to minimize the expected risk
$$$ I[f] = \mathbb{E}[V(f(x),y)]=\int V(f(x),y)dp(x,y).$$$




** From recursive least squares to stochastic gradient descent.**

** Incremental SGD**

** Kernel method**
Basically it's another viewpoint of iteration.

#### Adversarial models: Sequential learning
The difference from statistical learning models is that there's no i.i.d. assumption in this case. The concept "regret" is based on this case. The objective is to minimize regret, instead of expected risk.

** Online convex optimization**
To handle non-convex cases, people use convexification. Two ways: by randomisation, and by surrogate loss functions.

** Follow the leader (FTL) and Follow the regularized leader (FTRL)**
are they related to mirror descent?
dual averaging is involved.
check out what is "linear loss function" which is written as a inner product in this doc.
In the case of linear loss, FTRL can be reduced to SGD.
Notice that SGD itself has nothing to do with the i.i.d. assumption. 
This assumption is for theoritical analysis.
Here lazy projection is also involved.


** Online subgradient descent (OSD)**
It's just a generalization of SGD. 

** Other algorithms**
- online mirror descent
- prediction with expert advice

#### Comparison of the models
The paradigm of online learning interestingly has three distinct interpretations depending on the choice of the learning model.
The standard SGD is used for this discussion. The form is 
$$
w_t=w_{t-1}-\gamma_t\nabla V(\langle w_{t-1},x_t\rangle,y_t)
$$


