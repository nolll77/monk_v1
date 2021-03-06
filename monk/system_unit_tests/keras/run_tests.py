import os
import sys
import time


from test_optimizer_sgd import test_optimizer_sgd
from test_optimizer_nesterov_sgd import test_optimizer_nesterov_sgd
from test_optimizer_rmsprop import test_optimizer_rmsprop
from test_optimizer_adam import test_optimizer_adam
from test_optimizer_nadam import test_optimizer_nadam
from test_optimizer_adamax import test_optimizer_adamax
from test_optimizer_adadelta import test_optimizer_adadelta
from test_optimizer_adagrad import test_optimizer_adagrad

from test_loss_l1 import test_loss_l1
from test_loss_l2 import test_loss_l2
from test_loss_crossentropy import test_loss_crossentropy
from test_loss_binary_crossentropy import test_loss_binary_crossentropy
from test_loss_kldiv import test_loss_kldiv
from test_loss_hinge import test_loss_hinge
from test_loss_squared_hinge import test_loss_squared_hinge



origstdout = sys.stdout


print("Running Tests...");
sys.stdout = open("test_logs.txt", 'w');



system_dict = {};
system_dict["total_tests"] = 0;
system_dict["successful_tests"] = 0;
system_dict["failed_tests_lists"] = [];
system_dict["failed_tests_exceptions"] = [];
system_dict["skipped_tests_lists"] = [];


start = time.time()

exp_num = 1;



print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_optimizer_sgd(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_optimizer_nesterov_sgd(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_optimizer_rmsprop(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_optimizer_adam(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_optimizer_nadam(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_optimizer_adamax(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_optimizer_adadelta(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")



print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_optimizer_adagrad(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")



print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_loss_l1(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_loss_l2(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")



print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_loss_crossentropy(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_loss_binary_crossentropy(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_loss_kldiv(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_loss_hinge(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_loss_squared_hinge(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")





from test_layer_convolution1d import test_layer_convolution1d
from test_layer_convolution2d import test_layer_convolution2d
from test_layer_convolution3d import test_layer_convolution3d
from test_layer_transposed_convolution2d import test_layer_transposed_convolution2d
from test_layer_transposed_convolution3d import test_layer_transposed_convolution3d
from test_layer_max_pooling1d import test_layer_max_pooling1d
from test_layer_max_pooling2d import test_layer_max_pooling2d
from test_layer_max_pooling3d import test_layer_max_pooling3d
from test_layer_average_pooling1d import test_layer_average_pooling1d
from test_layer_average_pooling2d import test_layer_average_pooling2d
from test_layer_average_pooling3d import test_layer_average_pooling3d
from test_layer_global_max_pooling1d import test_layer_global_max_pooling1d
from test_layer_global_max_pooling2d import test_layer_global_max_pooling2d
from test_layer_global_max_pooling3d import test_layer_global_max_pooling3d
from test_layer_global_average_pooling1d import test_layer_global_average_pooling1d
from test_layer_global_average_pooling2d import test_layer_global_average_pooling2d
from test_layer_global_average_pooling3d import test_layer_global_average_pooling3d
from test_layer_batch_normalization import test_layer_batch_normalization
from test_layer_identity import test_layer_identity
from test_layer_fully_connected import test_layer_fully_connected
from test_layer_dropout import test_layer_dropout
from test_layer_flatten import test_layer_flatten
from test_layer_concatenate import test_layer_concatenate
from test_layer_add import test_layer_add

from test_activation_relu import test_activation_relu
from test_activation_softmax import test_activation_softmax
from test_activation_thresholded_relu import test_activation_thresholded_relu
from test_activation_elu import test_activation_elu
from test_activation_prelu import test_activation_prelu
from test_activation_leaky_relu import test_activation_leaky_relu
from test_activation_selu import test_activation_selu
from test_activation_softplus import test_activation_softplus
from test_activation_softsign import test_activation_softsign
from test_activation_tanh import test_activation_tanh
from test_activation_sigmoid import test_activation_sigmoid
from test_activation_hard_sigmoid import test_activation_hard_sigmoid

from test_initializer_xavier_normal import test_initializer_xavier_normal
from test_initializer_xavier_uniform import test_initializer_xavier_uniform
from test_initializer_random_normal import test_initializer_random_normal
from test_initializer_random_uniform import test_initializer_random_uniform
from test_initializer_lecun_normal import test_initializer_lecun_normal
from test_initializer_lecun_uniform import test_initializer_lecun_uniform
from test_initializer_he_normal import test_initializer_he_normal
from test_initializer_he_uniform import test_initializer_he_uniform
from test_initializer_truncated_normal import test_initializer_truncated_normal
from test_initializer_orthogonal import test_initializer_orthogonal
from test_initializer_variance_scaling import test_initializer_variance_scaling


from test_block_resnet_v1 import test_block_resnet_v1
from test_block_resnet_v2 import test_block_resnet_v2
from test_block_resnet_v1_bottleneck import test_block_resnet_v1_bottleneck
from test_block_resnet_v2_bottleneck import test_block_resnet_v2_bottleneck
from test_block_resnext import test_block_resnext
from test_block_mobilenet_v2_linear_bottleneck import test_block_mobilenet_v2_linear_bottleneck
from test_block_mobilenet_v2_inverted_linear_bottleneck import test_block_mobilenet_v2_inverted_linear_bottleneck
from test_block_squeezenet_fire import test_block_squeezenet_fire
from test_block_densenet import test_block_densenet
from test_block_conv_bn_relu import test_block_conv_bn_relu
from test_block_inception_a import test_block_inception_a
from test_block_inception_b import test_block_inception_b
from test_block_inception_c import test_block_inception_c
from test_block_inception_d import test_block_inception_d
from test_block_inception_e import test_block_inception_e











print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_convolution1d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_convolution2d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_convolution3d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_transposed_convolution2d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_transposed_convolution3d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_max_pooling1d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_max_pooling2d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_max_pooling3d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")



print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_average_pooling1d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_average_pooling2d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_average_pooling3d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_global_max_pooling1d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_global_max_pooling2d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_global_max_pooling3d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")



print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_global_average_pooling1d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_global_average_pooling2d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_global_average_pooling3d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")

print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_batch_normalization(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_identity(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_fully_connected(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")



print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_dropout(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_flatten(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_activation_relu(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")

print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_activation_softmax(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")

print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_activation_thresholded_relu(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")

print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_activation_elu(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")

print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_activation_prelu(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")

print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_activation_leaky_relu(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_activation_selu(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")

print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_activation_softplus(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")

print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_activation_softsign(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")

print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_activation_tanh(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")

print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_activation_sigmoid(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")

print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_activation_hard_sigmoid(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")

print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_concatenate(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")

print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_layer_add(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")



print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_initializer_xavier_normal(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_initializer_xavier_uniform(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_initializer_random_normal(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_initializer_random_uniform(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_initializer_lecun_normal(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_initializer_lecun_uniform(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_initializer_he_normal(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_initializer_he_uniform(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_initializer_truncated_normal(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_initializer_orthogonal(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_initializer_variance_scaling(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")



print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_block_resnet_v1(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")



print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_block_resnet_v2(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_block_resnet_v1_bottleneck(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_block_resnet_v2_bottleneck(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_block_resnext(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_block_mobilenet_v2_linear_bottleneck(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")



print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_block_mobilenet_v2_inverted_linear_bottleneck(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_block_squeezenet_fire(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_block_densenet(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_block_conv_bn_relu(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_block_inception_a(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_block_inception_b(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_block_inception_c(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_block_inception_d(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")


print("Running {}/<num>".format(exp_num));
exp_num += 1;
system_dict = test_block_inception_e(system_dict)
sys.stdout = origstdout;
print("Tests Completed           - {}".format(system_dict["total_tests"]));
print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
print("")



sys.stdout = open("test_logs.txt", 'a');
end = time.time();

print("Total Tests           - {}".format(system_dict["total_tests"]));
print("Time Taken            - {} sec".format(end-start));
print("Num Successful Tests  - {}".format(system_dict["successful_tests"]));
print("Num Failed Tests      - {}".format(len(system_dict["failed_tests_lists"])));
print("Num Skipped Tests     - {}".format(len(system_dict["skipped_tests_lists"])));
print("");















for i in range(len(system_dict["failed_tests_lists"])):
    print("{}. Failed Test:".format(i+1));
    print("Name     - {}".format(system_dict["failed_tests_lists"][i]));
    print("Error    - {}".format(system_dict["failed_tests_exceptions"][i]));
    print("");


print("Skipped Tests List    - {}".format(system_dict["skipped_tests_lists"]));
print("");


sys.stdout = origstdout;


print("Total Tests           - {}".format(system_dict["total_tests"]));
print("Time Taken            - {} sec".format(end-start));
print("Num Successful Tests  - {}".format(system_dict["successful_tests"]));
print("Num Failed Tests      - {}".format(len(system_dict["failed_tests_lists"])));
print("Num Skipped Tests     - {}".format(len(system_dict["skipped_tests_lists"])));
print("See test_logs.txt for errors");
print("");


os.system("rm -r workspace");