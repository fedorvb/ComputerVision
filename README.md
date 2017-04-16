<div id="header">[![](img/visionlablogo.png) ](http://vision.stanford.edu/) [ ![](img/stanfordlogo.jpg) ](http://stanford.edu/) [

# CS231n: Convolutional Neural Networks for Visual Recognition

](index.html)</div>

<div class="sechighlight">

<div class="container sec">

## Schedule and Syllabus

(The syllabus for the (previous) Winter 2015 class offering has been moved [here](syllabus_winter2015.html).)
Unless otherwise specified the course lectures and meeting times are Monday, Wednesday 3:00-4:20, Bishop Auditorium in Lathrop Building ([map](http://campus-map.stanford.edu/?id=&lat=37.4292007889&lng=-122.167299117&zoom=16&srch=Bishop%20Auditorium))

**Update**: The class has ended! There are many people to thank for making this class run smoothly: [Andrej Karpathy](https://twitter.com/karpathy) for the class notes and lectures, [Justin Johnson](http://cs.stanford.edu/people/jcjohns/) the assignments and lectures, [Fei-Fei Li](https://twitter.com/drfeifei) for maintaining order, the entire [TA team](https://twitter.com/cs231n/status/707760595030781952) for their hard work on grading, office hours, and class logistics, and our wonderful students for their valuable feedback! The final course projects were posted [here](http://cs231n.stanford.edu/reports2016.html). You can find the raw lecture slides (Google Presentations) [here](https://drive.google.com/open?id=0B62MBK9B2knSY3ZmeHktSEhJNXM) and feel free to use material from any of the slides. Stay in touch on [Twitter](https://twitter.com/cs231n) or [Reddit r/cs231n](https://www.reddit.com/r/cs231n), and we'll see you again next year!
**Update2**: We had to take down the links to YouTube videos. Sorry about that. We're working on bringing them back, stay tuned.</div>

</div>

<div class="container sec">

| Event Type | Date | Description | Course Materials |
| Lecture | Jan 4 | Intro to Computer Vision, historical context. | [[slides]](http://cs231n.stanford.edu/slides/2016/winter1516_lecture1.pdf) |
| Lecture | Jan 6 | Image classification and the data-driven approach
k-nearest neighbor
Linear classification I | [[slides]](http://cs231n.stanford.edu/slides/2016/winter1516_lecture2.pdf) [video]
[[python/numpy tutorial]](http://cs231n.github.io/python-numpy-tutorial)
[[image classification notes]](http://cs231n.github.io/classification)
[[linear classification notes]](http://cs231n.github.io/linear-classify)
 |
| Lecture | Jan 11 | Linear classification II
Higher-level representations, image features
Optimization, stochastic gradient descent | [[slides]](http://cs231n.stanford.edu/slides/2016/winter1516_lecture3.pdf) [video]
[[linear classification notes]](http://cs231n.github.io/linear-classify)
[[optimization notes]](http://cs231n.github.io/optimization-1) |
| Lecture | Jan 13 | Backpropagation
Introduction to neural networks | [[slides]](http://cs231n.stanford.edu/slides/2016/winter1516_lecture4.pdf) [video]
[[backprop notes]](http://cs231n.github.io/optimization-2)
[[Efficient BackProp]](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf) (optional)
related: [[1]](http://colah.github.io/posts/2015-08-Backprop/), [[2]](http://neuralnetworksanddeeplearning.com/chap2.html), [[3]](https://www.youtube.com/watch?v=q0pm3BrIUFo) (optional) |
| Lecture | Jan 18 | Holiday; No class. |
| A1 Due | Jan 20 | Assignment #1 (kNN/SVM/Softmax/2-Layer Net) Due date | [[Assignment #1]](http://cs231n.github.io/assignments2016/assignment1/) |
| Lecture | Jan 20 | Training Neural Networks Part 1
activation functions, weight initialization, gradient flow, batch normalization
babysitting the learning process, hyperparameter optimization | [[slides]](http://cs231n.stanford.edu/slides/2016/winter1516_lecture5.pdf) [video]
[Neural Nets notes 1](http://cs231n.github.io/neural-networks-1/)
[Neural Nets notes 2](http://cs231n.github.io/neural-networks-2/)
[Neural Nets notes 3](http://cs231n.github.io/neural-networks-3/)
tips/tricks: [[1]](http://research.microsoft.com/pubs/192769/tricks-2012.pdf), [[2]](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf), [[3]](http://arxiv.org/pdf/1206.5533v2.pdf) (optional)
[Deep Learning [Nature]](http://www.nature.com/nature/journal/v521/n7553/full/nature14539.html) (optional) |
| Lecture | Jan 25 | Training Neural Networks Part 2: parameter updates, ensembles, dropout
Convolutional Neural Networks: intro | [[slides]](http://cs231n.stanford.edu/slides/2016/winter1516_lecture6.pdf) [video]
[Neural Nets notes 3](http://cs231n.github.io/neural-networks-3/)
 |
| Lecture | Jan 27 | Convolutional Neural Networks: architectures, convolution / pooling layers
Case study of ImageNet challenge winning ConvNets | [[slides]](http://cs231n.stanford.edu/slides/2016/winter1516_lecture7.pdf) [video]
[ConvNet notes](http://cs231n.github.io/convolutional-networks/)
 |
| Proposal due | Jan 30 | Couse Project Proposal due | [[proposal description]](http://cs231n.stanford.edu/project.html) |
| Lecture | Feb 1 | ConvNets for spatial localization
Object detection | [[slides]](http://cs231n.stanford.edu/slides/2016/winter1516_lecture8.pdf) [video] |
| Lecture | Feb 3 | Understanding and visualizing Convolutional Neural Networks
Backprop into image: Visualizations, deep dream, artistic style transfer
Adversarial fooling examples
 | [[slides]](http://cs231n.stanford.edu/slides/2016/winter1516_lecture9.pdf) [video] |
| A2 Due | Feb 5 | Assignment #2 (Neural Nets) Due date | [[Assignment #2]](http://cs231n.github.io/assignments2016/assignment2/) |
| Lecture | Feb 8 | Recurrent Neural Networks (RNN), Long Short Term Memory (LSTM)
RNN language models
Image captioning | [[slides]](http://cs231n.stanford.edu/slides/2016/winter1516_lecture10.pdf) [video]
[DL book RNN chapter](http://www.deeplearningbook.org/contents/rnn.html) (optional)
[min-char-rnn](https://gist.github.com/karpathy/d4dee566867f8291f086), [char-rnn](https://github.com/karpathy/char-rnn), [neuraltalk2](https://github.com/karpathy/neuraltalk2) |
| Midterm | Feb 10 | In-class midterm |
| Lecture | Feb 15 | Holiday; No class. |
| Milestone | **Feb 17** | Course Project Milestone |
| Lecture | Feb 17 | Training ConvNets in practice
Data augmentation, transfer learning
Distributed training, CPU/GPU bottlenecks
Efficient convolutions
 | [[slides]](http://cs231n.stanford.edu/slides/2016/winter1516_lecture11.pdf) [video] |
| Lecture | Feb 22 | Overview of Caffe/Torch/Theano/TensorFlow | [[slides]](http://cs231n.stanford.edu/slides/2016/winter1516_lecture12.pdf) [video] |
| A3 Due | Feb 24 | Assignment #3 (ConvNets) Due date | [[Assignment #3]](http://cs231n.github.io/assignments2016/assignment3/) |
| Lecture | Feb 24 | Segmentation
Soft attention models
Spatial transformer networks
 | [[slides]](http://cs231n.stanford.edu/slides/2016/winter1516_lecture13.pdf) [video] |
| Lecture | Feb 29 | ConvNets for videos
Unsupervised learning
 | [[slides]](http://cs231n.stanford.edu/slides/2016/winter1516_lecture14.pdf) [video] |
| Lecture | Mar 2 | Invited Talk: [Jeff Dean](http://en.wikipedia.org/wiki/Jeff_Dean_(computer_scientist)) [video] |
| Lecture | Mar 7 | Student spotlight talks, conclusions | [[slides]](http://cs231n.stanford.edu/slides/2016/winter1516_lecture15.pdf) |
| Poster Presentation | Mar 9 |
| Final Project Due | **Mar 13** | Final course project due date | [[reports]](http://cs231n.stanford.edu/reports.html) |

</div>