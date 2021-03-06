import numpy as np

class KNearestNeighbor(object):
  """ a kNN classifier with L2 distance """

  def __init__(self):
    pass

  def train(self, X, y):
    """
    Train the classifier. For k-nearest neighbors this is just 
    memorizing the training data.

    Inputs:
    - X: A numpy array of shape (num_train, D) containing the training data
      consisting of num_train samples each of dimension D.
    - y: A numpy array of shape (N,) containing the training labels, where
         y[i] is the label for X[i].
    """
    self.X_train = X
    self.y_train = y
    
  def predict(self, X, k=1, num_loops=0):
    """
    Predict labels for test data using this classifier.

    Inputs:
    - X: A numpy array of shape (num_test, D) containing test data consisting
         of num_test samples each of dimension D.
    - k: The number of nearest neighbors that vote for the predicted labels.
    - num_loops: Determines which implementation to use to compute distances
      between training points and testing points.

    Returns:
    - y: A numpy array of shape (num_test,) containing predicted labels for the
      test data, where y[i] is the predicted label for the test point X[i].  
    """
    if num_loops == 0:
      dists = self.compute_distances_no_loops(X)
    elif num_loops == 1:
      dists = self.compute_distances_one_loop(X)
    elif num_loops == 2:
      dists = self.compute_distances_two_loops(X)
    else:
      raise ValueError('Invalid value %d for num_loops' % num_loops)

    return self.predict_labels(dists, k=k)

  def compute_distances_two_loops(self, X):
    """
    Compute the distance between each test point in X and each training point
    in self.X_train using a nested loop over both the training data and the 
    test data.

    Inputs:
    - X: A numpy array of shape (num_test, D) containing test data.

    Returns:
    - dists: A numpy array of shape (num_test, num_train) where dists[i, j]
      is the Euclidean distance between the ith test point and the jth training
      point.
    """
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train))
    for i in xrange(num_test):
      for j in xrange(num_train):
        #####################################################################
        # TODO:                                                             #
        # Compute the l2 distance between the ith test point and the jth    #
        # training point, and store the result in dists[i, j]. You should   #
        # not use a loop over dimension.                                    #
        #####################################################################
        dists[i, j] = np.sqrt(np.sum((X[i] - self.X_train[j])**2))        
        #####################################################################
        #                       END OF YOUR CODE                            #
        #####################################################################
    return dists

  def compute_distances_one_loop(self, X):
    """
    Compute the distance between each test point in X and each training point
    in self.X_train using a single loop over the test data.

    Input / Output: Same as compute_distances_two_loops
    """
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train))
    for i in xrange(num_test):
      #######################################################################
      # TODO:                                                               #
      # Compute the l2 distance between the ith test point and all training #
      # points, and store the result in dists[i, :].                        #
      #######################################################################
      # firstly vector X[i] is broadcasted across matrix X_train, 
      # and we calculated the squared difference element wise of every row of 
      # matrix X_train, then we square it and then do a row sum which results in the 
      # vector of sums, which we assign to the resulted distance matrix     
      dists[i,:] = np.sqrt(np.sum((X[i] - self.X_train)**2, axis=1))      
      #######################################################################
      #                         END OF YOUR CODE                            #
      #######################################################################
    return dists

  def compute_distances_no_loops(self, X):
    """
    Compute the distance between each test point in X and each training point
    in self.X_train using no explicit loops.

    Input / Output: Same as compute_distances_two_loops
    """
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train)) 
    #########################################################################
    # TODO:                                                                 #
    # Compute the l2 distance between all test points and all training      #
    # points without using any explicit loops, and store the result in      #
    # dists.                                                                #
    #                                                                       #
    # You should implement this function using only basic array operations; #
    # in particular you should not use functions from scipy.                #
    #                                                                       #
    # HINT: Try to formulate the l2 distance using matrix multiplication    #
    #       and two broadcast sums.                                         #
    #########################################################################
    # we will decompose the calculations into (X-Y) = X*X -2*X*Y + Y*Y
    Y = self.X_train
    # calculating sum of all coordinates (squared) of the test examples 
    # therefore the dimintionality of the vector will be number of test examples
    XX = np.square(X).sum(axis = 1)
    #print 'Test data squired shape: ', XX.shape
    # calculating sum of all coordinates (squared) of the train examples
    # therefore the dimintionality of the vector will be number of training examples
    YY = np.square(Y).sum(axis = 1)    
    #print 'Train data squired share: ', YY.shape    
    # here we are multiplying matrix of the test example on the matrix of the training examples
    # to get all the multiplications of the respective (same dimention) coordinates of the test adn train examples
    # the dimention of this matrix is (number of test example) * (number of training examples)
    XY = X.dot(Y.T)
    #print 'Train/text data multiplication shape: ', XY.shape    
    #print 'np.matrix(XX) data shape: ', np.matrix(XX).shape
    # we are doing np.matrix(XX) here to distrobute the vector YY to all rows of XX
    dists = (np.matrix(XX).T + YY) -2*XY 
    
    XY = np.dot(X, Y.T)
    XX = np.square(X).sum(axis = 1)
    YY = np.square(Y).sum(axis = 1)
    dists = np.sqrt(np.matrix(XX).T +YY -2*XY)
    #########################################################################
    #                         END OF YOUR CODE                              #
    #########################################################################
    return dists

  def predict_labels(self, dists, k=1):
    """
    Given a matrix of distances between test points and training points,
    predict a label for each test point.

    Inputs:
    - dists: A numpy array of shape (num_test, num_train) where dists[i, j]
      gives the distance betwen the ith test point and the jth training point.

    Returns:
    - y: A numpy array of shape (num_test,) containing predicted labels for the
      test data, where y[i] is the predicted label for the test point X[i].  
    """
    num_test = dists.shape[0]
    #print "Number of test examples:", num_test
    y_pred = np.zeros(num_test)
    for i in xrange(num_test):
      # A list of length k storing the labels of the k nearest neighbors to
      # the ith test point.
      closest_y = []
      #########################################################################
      # TODO:                                                                 #
      # Use the distance matrix to find the k nearest neighbors of the ith    #
      # testing point, and use self.y_train to find the labels of these       #
      # neighbors. Store these labels in closest_y.                           #
      # Hint: Look up the function numpy.argsort.                             #
      #########################################################################    
            
      # use indexes of sorted distance array to select the labels in the sorted order
      allDistances = self.y_train[np.argsort(dists[i])] 
      closest_y = allDistances[:k] # take labels for the items with first K smallest distances
    
      #########################################################################e
      # TODO:                                                                 #
      # Now that you have found the labels of the k nearest neighbors, you    #
      # need to find the most common label in the list closest_y of labels.   #
      # Store this label in y_pred[i]. Break ties by choosing the smaller     #
      # label.                                                                #
      #########################################################################
        
      # np.bincount - Counts number of occurrences of each value in array of non-negative ints.
      # we take the label with the highest count, so this is a voting classifier 
      y_pred[i] = np.argmax(np.bincount(closest_y[:, 0]))      
      #########################################################################
      #                           END OF YOUR CODE                            # 
      #########################################################################

    return y_pred

