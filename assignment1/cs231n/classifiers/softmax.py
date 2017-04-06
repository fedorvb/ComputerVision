import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]
  num_classes = W.shape[1]
  loss = 0.0

  for i in xrange(num_train):
    # compute vector of scores
    f_i = X[i].dot(W)
    
    # normalization trick to avoid numerical instability
    f_i -= np.max(f_i)
    
    # compute normalization sum
    sum_j = np.sum(np.exp(f_i))
    prob_func = lambda k : np.exp(f_i[k]) / sum_j
    loss += -np.log(prob_func(y[i]))
    
    # computing gradient here
    for k in range(num_classes):       
       p_k = prob_func(k)
       # derivative of softmax in this case in the particular sample point X[i]
       dW[:, k] += (p_k - (k == y[i])) * X[i]

  loss /= num_train # average across all training examples
  dW /= num_train
  loss += 0.5 * reg * np.sum(W * W)
  dW += reg * W
  
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################
  
  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]
  f = X.dot(W)
  
  # doing a numerical stability trick here
  # remove max of f (raw value for every class) within every sample (row of matrix) 
  # sum values for rows
  f -= np.max(f) # np.max(f, axis=1, keepdims = True) # np.max(f) #
  
  # prepares vector of sums, every row is sum for the sample
  # sum values for rows
  sum_f = np.sum(np.exp(f), axis=1, keepdims = True) 

  # normalize the values so everything now is probability
  p = np.exp(f) / sum_f  # dimensionality N*C
  #print "p dimensions", p.shape 
  #print "p dimensions value", p[np.arange(num_train), y].shape
  #print "y.shape dimensions value", y.shape
    
  # Loss: L_i = - f(x_i)_{y_i} + log \sum_j e^{f(x_i)_j}
  # sum all the respective "correct" probabilities f(x_i)_{y_i}
  # that is why "[np.arange(num_train), y]" is necessary
  loss = np.sum(-np.log(p[np.arange(num_train), y]))
 
  loss /= num_train
  loss += 0.5 * reg * np.sum(W*W)

  ind = np.zeros_like(p) # replicates same structure as "p", but filled with zeros
  # setup indicator variables (k == y[i]), then is will be "1" value
  # similarly to line dW[:, k] += (p_k - (k == y[i])) * X[i]
  ind[np.arange(num_train), y] = 1
  dW = X.T.dot(p - ind) # dimensionality D*C
  dW /= num_train  
  dW += reg*W
  
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW
