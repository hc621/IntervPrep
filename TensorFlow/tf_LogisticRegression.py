#1. inference: produces a probability distribution over the output classes given a minibatch
#2. loss: computes the value of the error function (in this case, the cross-entropy loss)
#3. training: responsible for computing the gradients of the model’s parameters and updating the model
#4. evaluate: will determine the effectiveness of a model

import tensorflow as tf

def inference(x):
    tf.constant_initializer(value=0)
    W = tf.get_variable("W", [784, 10],initializer=init)
    b = tf.get_variable("b", [10], initializer=init)
    output = tf.nn.softmax(tf.matmul(x, W) + b)
    return output

def loss(output, y):
    dot_product = y * tf.log(output)
    # Reduction along axis 0 collapses each column into a
    # single value, whereas reduction along axis 1 collapses
    # each row into a single value. In general, reduction along
    # axis i collapses the ith dimension of a tensor to size 1.
    xentropy = -tf.reduce_sum(dot_product, reduction_indices=1)
    loss = tf.reduce_mean(xentropy)
    return loss

def training(cost, global_step,learning_rate):
    optimizer = tf.train.GradientDescentOptimizer(learning_rate)
    train_op = optimizer.minimize(cost,global_step=global_step)
    return train_op

def evaluate(output, y):
    correct_prediction = tf.equal(tf.argmax(output, 1),tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    return accuracy



