import tensorflow as tf

# tf variables
# Variables must be explicitly initialized before a graph is used for the first time.
# We can use gradient methods to modify variables after each iteration as we search for a model’s optimal parameter settings.
# We can save the values stored in variables to disk and restore them for later use.
# the name of the varibale make them different
weights = tf.Variable(tf.random.normal([3,2],stddev=0.5),name='weight')
print(weights)

shape=[2,2]
x=tf.zeros(shape, dtype=tf.float32, name=None)
y=tf.ones(shape, dtype=tf.float32, name=None)
z=tf.random.normal(shape, mean=0.0, stddev=1.0,dtype=tf.float32, seed=None,name=None)
a=tf.random.truncated_normal(shape, mean=0.0, stddev=1.0,dtype=tf.float32, seed=None,name=None)
b=tf.random.uniform(shape, minval=0, maxval=None,dtype=tf.float32, seed=None,name=None)


# tf place holder
# A variable is insufficient because it is only meant to be initialized once. Instead,we need a component that we populate every single time the computation graph is run.
# the size of the placeholer can be partially initialized, None can be filled with any arbitrary number

x = tf.compat.v1.placeholder(tf.float32, name="x", shape=[None, 7])
W = tf.Variable(tf.random.uniform([7,10], -1, 1), name="W")
multiply = tf.matmul(x, W)

# Session
#The TensorFlow session is responsible for building the initial graph, and can be used to initialize all variables appropriately and to run the computational graph.
from read_data import get_minibatch()

# describe the cumputational graph
x = tf.placeholder(tf.float32, name="x", shape=[None, 784])
W = tf.Variable(tf.random_uniform([784, 10], -1, 1), name="W")
b = tf.Variable(tf.zeros([10]), name="biases")
output = tf.matmul(x, W) + b

init_op = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init_op)
feed_dict = {"x" : get_minibatch()}
sess.run(output, feed_dict=feed_dict)


# reuse variable
tf.get_variable(<name>, <shape>, <initializer>)
# Checks if a variable with this name exists, retrieves the variable if it does, or creates it using the shape and initializer if it doesn’t.

#
tf.variable_scope(<scope_name>)
# Manages the namespace and determines the scope in which tf.get_variable operates

def layer(input, weight_shape, bias_shape):
    weight_init = tf.random_uniform_initializer(minval=-1,maxval=1)
    bias_init = tf.constant_initializer(value=0)
    W = tf.get_variable("W", weight_shape,initializer=weight_init)
    b = tf.get_variable("b", bias_shape,initializer=bias_init)
    return tf.matmul(input, W) + b

def my_network(input):
    with tf.variable_scope("layer_1"):
        output_1 = layer(input, [784, 100], [100])
    with tf.variable_scope("layer_2"):
        output_2 = layer(output_1, [100, 50], [50])
    with tf.variable_scope("layer_3"):
        output_3 = layer(output_2, [50, 10], [10])
    return output_3

# Even with different initial input , the function cannot be called twice, since the variable with same name cannot be shared  or initiated twice.
# unless we say sharing within a variable scope explicitly
with tf.variable_scope("shared_variables") as scope:
    i_1 = tf.placeholder(tf.float32, [1000, 784], name="i_1")
    my_network(i_1)
    scope.reuse_variables()
    i_2 = tf.placeholder(tf.float32, [1000, 784], name="i_2")
    my_network(i_2)

# managing devices
#If we desire to use a specific device, we may do so by using with

with tf.device('/gpu:2'):
    a = tf.constant([1.0, 2.0, 3.0, 4.0], shape=[2, 2], name='a')
    b = tf.constant([1.0, 2.0], shape=[2, 1], name='b')
    c = tf.matmul(a, b)

sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True))
sess.run(c)