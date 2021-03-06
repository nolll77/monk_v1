import os
import sys
import time

from monk.pip_unit_tests.pytorch.test_optimizer_sgd import test_optimizer_sgd
from monk.pip_unit_tests.pytorch.test_optimizer_nesterov_sgd import test_optimizer_nesterov_sgd
from monk.pip_unit_tests.pytorch.test_optimizer_rmsprop import test_optimizer_rmsprop
from monk.pip_unit_tests.pytorch.test_optimizer_momentum_rmsprop import test_optimizer_momentum_rmsprop
from monk.pip_unit_tests.pytorch.test_optimizer_adam import test_optimizer_adam
from monk.pip_unit_tests.pytorch.test_optimizer_adamax import test_optimizer_adamax
from monk.pip_unit_tests.pytorch.test_optimizer_adamw import test_optimizer_adamw
from monk.pip_unit_tests.pytorch.test_optimizer_adadelta import test_optimizer_adadelta
from monk.pip_unit_tests.pytorch.test_optimizer_adagrad import test_optimizer_adagrad

from monk.pip_unit_tests.pytorch.test_loss_l1 import test_loss_l1
from monk.pip_unit_tests.pytorch.test_loss_l2 import test_loss_l2
from monk.pip_unit_tests.pytorch.test_loss_l2 import test_loss_l2
from monk.pip_unit_tests.pytorch.test_loss_softmax_crossentropy import test_loss_softmax_crossentropy
from monk.pip_unit_tests.pytorch.test_loss_crossentropy import test_loss_crossentropy
from monk.pip_unit_tests.pytorch.test_loss_sigmoid_binary_crossentropy import test_loss_sigmoid_binary_crossentropy
from monk.pip_unit_tests.pytorch.test_loss_binary_crossentropy import test_loss_binary_crossentropy
from monk.pip_unit_tests.pytorch.test_loss_kldiv import test_loss_kldiv
from monk.pip_unit_tests.pytorch.test_loss_poisson_nll import test_loss_poisson_nll
from monk.pip_unit_tests.pytorch.test_loss_huber import test_loss_huber
from monk.pip_unit_tests.pytorch.test_loss_hinge import test_loss_hinge
from monk.pip_unit_tests.pytorch.test_loss_squared_hinge import test_loss_squared_hinge
from monk.pip_unit_tests.pytorch.test_loss_multimargin import test_loss_multimargin
from monk.pip_unit_tests.pytorch.test_loss_squared_multimargin import test_loss_squared_multimargin
from monk.pip_unit_tests.pytorch.test_loss_multilabelmargin import test_loss_multilabelmargin
from monk.pip_unit_tests.pytorch.test_loss_multilabelsoftmargin import test_loss_multilabelsoftmargin

from monk.pip_unit_tests.pytorch.test_layer_convolution1d import test_layer_convolution1d
from monk.pip_unit_tests.pytorch.test_layer_convolution2d import test_layer_convolution2d
from monk.pip_unit_tests.pytorch.test_layer_convolution3d import test_layer_convolution3d
from monk.pip_unit_tests.pytorch.test_layer_transposed_convolution1d import test_layer_transposed_convolution1d
from monk.pip_unit_tests.pytorch.test_layer_transposed_convolution2d import test_layer_transposed_convolution2d
from monk.pip_unit_tests.pytorch.test_layer_transposed_convolution3d import test_layer_transposed_convolution3d
from monk.pip_unit_tests.pytorch.test_layer_max_pooling1d import test_layer_max_pooling1d
from monk.pip_unit_tests.pytorch.test_layer_max_pooling2d import test_layer_max_pooling2d
from monk.pip_unit_tests.pytorch.test_layer_max_pooling3d import test_layer_max_pooling3d
from monk.pip_unit_tests.pytorch.test_layer_average_pooling1d import test_layer_average_pooling1d
from monk.pip_unit_tests.pytorch.test_layer_average_pooling2d import test_layer_average_pooling2d
from monk.pip_unit_tests.pytorch.test_layer_average_pooling3d import test_layer_average_pooling3d
from monk.pip_unit_tests.pytorch.test_layer_global_max_pooling1d import test_layer_global_max_pooling1d
from monk.pip_unit_tests.pytorch.test_layer_global_max_pooling2d import test_layer_global_max_pooling2d
from monk.pip_unit_tests.pytorch.test_layer_global_max_pooling3d import test_layer_global_max_pooling3d
from monk.pip_unit_tests.pytorch.test_layer_global_average_pooling1d import test_layer_global_average_pooling1d
from monk.pip_unit_tests.pytorch.test_layer_global_average_pooling2d import test_layer_global_average_pooling2d
from monk.pip_unit_tests.pytorch.test_layer_global_average_pooling3d import test_layer_global_average_pooling3d
from monk.pip_unit_tests.pytorch.test_layer_batch_normalization import test_layer_batch_normalization
from monk.pip_unit_tests.pytorch.test_layer_instance_normalization import test_layer_instance_normalization
from monk.pip_unit_tests.pytorch.test_layer_layer_normalization import test_layer_layer_normalization
from monk.pip_unit_tests.pytorch.test_layer_identity import test_layer_identity
from monk.pip_unit_tests.pytorch.test_layer_fully_connected import test_layer_fully_connected
from monk.pip_unit_tests.pytorch.test_layer_dropout import test_layer_dropout
from monk.pip_unit_tests.pytorch.test_layer_flatten import test_layer_flatten

from monk.pip_unit_tests.pytorch.test_activation_relu import test_activation_relu
from monk.pip_unit_tests.pytorch.test_activation_sigmoid import test_activation_sigmoid 
from monk.pip_unit_tests.pytorch.test_activation_tanh import test_activation_tanh
from monk.pip_unit_tests.pytorch.test_activation_softplus import test_activation_softplus
from monk.pip_unit_tests.pytorch.test_activation_softsign import test_activation_softsign
from monk.pip_unit_tests.pytorch.test_activation_elu import test_activation_elu
from monk.pip_unit_tests.pytorch.test_activation_leaky_relu import test_activation_leaky_relu
from monk.pip_unit_tests.pytorch.test_activation_prelu import test_activation_prelu
from monk.pip_unit_tests.pytorch.test_activation_selu import test_activation_selu
from monk.pip_unit_tests.pytorch.test_activation_hardshrink import test_activation_hardshrink
from monk.pip_unit_tests.pytorch.test_activation_hardtanh import test_activation_hardtanh
from monk.pip_unit_tests.pytorch.test_activation_logsigmoid import test_activation_logsigmoid
from monk.pip_unit_tests.pytorch.test_activation_relu6 import test_activation_relu6
from monk.pip_unit_tests.pytorch.test_activation_rrelu import test_activation_rrelu
from monk.pip_unit_tests.pytorch.test_activation_celu import test_activation_celu
from monk.pip_unit_tests.pytorch.test_activation_softshrink import test_activation_softshrink
from monk.pip_unit_tests.pytorch.test_activation_tanhshrink import test_activation_tanhshrink
from monk.pip_unit_tests.pytorch.test_activation_threshold import test_activation_threshold
from monk.pip_unit_tests.pytorch.test_activation_softmin import test_activation_softmin
from monk.pip_unit_tests.pytorch.test_activation_softmax import test_activation_softmax
from monk.pip_unit_tests.pytorch.test_activation_logsoftmax import test_activation_logsoftmax

from monk.pip_unit_tests.pytorch.test_layer_concatenate import test_layer_concatenate
from monk.pip_unit_tests.pytorch.test_layer_add import test_layer_add


from monk.pip_unit_tests.pytorch.test_block_resnet_v1 import test_block_resnet_v1
from monk.pip_unit_tests.pytorch.test_block_resnet_v2 import test_block_resnet_v2
from monk.pip_unit_tests.pytorch.test_block_resnet_v1_bottleneck import test_block_resnet_v1_bottleneck
from monk.pip_unit_tests.pytorch.test_block_resnet_v2_bottleneck import test_block_resnet_v2_bottleneck
from monk.pip_unit_tests.pytorch.test_block_resnext import test_block_resnext
from monk.pip_unit_tests.pytorch.test_block_mobilenet_v2_linear_bottleneck import test_block_mobilenet_v2_linear_bottleneck
from monk.pip_unit_tests.pytorch.test_block_mobilenet_v2_inverted_linear_bottleneck import test_block_mobilenet_v2_inverted_linear_bottleneck
from monk.pip_unit_tests.pytorch.test_block_squeezenet_fire import test_block_squeezenet_fire
from monk.pip_unit_tests.pytorch.test_block_densenet import test_block_densenet
from monk.pip_unit_tests.pytorch.test_block_conv_bn_relu import test_block_conv_bn_relu
from monk.pip_unit_tests.pytorch.test_block_inception_a import test_block_inception_a
from monk.pip_unit_tests.pytorch.test_block_inception_b import test_block_inception_b
from monk.pip_unit_tests.pytorch.test_block_inception_c import test_block_inception_c
from monk.pip_unit_tests.pytorch.test_block_inception_d import test_block_inception_d
from monk.pip_unit_tests.pytorch.test_block_inception_e import test_block_inception_e


from monk.pip_functionality_tests.pytorch.test_default_train import test_default_train
from monk.pip_functionality_tests.pytorch.test_default_eval_infer import test_default_eval_infer
from monk.pip_functionality_tests.pytorch.test_update_copy_from import test_update_copy_from
from monk.pip_functionality_tests.pytorch.test_update_normal import test_update_normal
from monk.pip_functionality_tests.pytorch.test_update_eval_infer import test_update_eval_infer
from monk.pip_functionality_tests.pytorch.test_expert_train import test_expert_train
from monk.pip_functionality_tests.pytorch.test_expert_eval_infer import test_expert_eval_infer
from monk.pip_functionality_tests.pytorch.test_switch_default import test_switch_default
from monk.pip_functionality_tests.pytorch.test_switch_expert import test_switch_expert
from monk.pip_functionality_tests.pytorch.test_compare import test_compare
from monk.pip_functionality_tests.pytorch.test_analyse import test_analyse





def run_functionality_tests():
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

	print("Running 1/11");
	system_dict = test_default_train(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


	print("Running 2/11");
	sys.stdout = open("test_logs.txt", 'a');
	system_dict = test_default_eval_infer(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));
	print("")


	print("Running 3/11");
	sys.stdout = open("test_logs.txt", 'a');
	system_dict = test_update_copy_from(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));
	print("")


	print("Running 4/11");
	sys.stdout = open("test_logs.txt", 'a');
	system_dict = test_update_normal(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));
	print("")



	print("Running 5/11");
	sys.stdout = open("test_logs.txt", 'a');
	system_dict = test_update_eval_infer(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));
	print("")



	print("Running 6/11");
	sys.stdout = open("test_logs.txt", 'a');
	system_dict = test_expert_train(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));



	print("Running 7/11");
	sys.stdout = open("test_logs.txt", 'a');
	system_dict = test_expert_eval_infer(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));
	print("")




	print("Running 8/11");
	sys.stdout = open("test_logs.txt", 'a');
	system_dict = test_switch_default(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));
	print("")




	print("Running 9/11");
	sys.stdout = open("test_logs.txt", 'a');
	system_dict = test_switch_expert(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));
	print("")




	print("Running 10/11");
	sys.stdout = open("test_logs.txt", 'a');
	system_dict = test_compare(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));
	print("")



	print("Running 11/11");
	sys.stdout = open("test_logs.txt", 'a');
	system_dict = test_analyse(system_dict)
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





def run_unit_tests():

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
	system_dict = test_optimizer_adamax(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


	print("Running {}/<num>".format(exp_num));
	exp_num += 1;
	system_dict = test_optimizer_adamw(system_dict)
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
	system_dict = test_loss_softmax_crossentropy(system_dict)
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
	system_dict = test_loss_sigmoid_binary_crossentropy(system_dict)
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
	system_dict = test_loss_poisson_nll(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


	print("Running {}/<num>".format(exp_num));
	exp_num += 1;
	system_dict = test_loss_huber(system_dict)
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


	print("Running {}/<num>".format(exp_num));
	exp_num += 1;
	system_dict = test_loss_multimargin(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


	print("Running {}/<num>".format(exp_num));
	exp_num += 1;
	system_dict = test_loss_squared_multimargin(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


	print("Running {}/<num>".format(exp_num));
	exp_num += 1;
	system_dict = test_loss_multilabelmargin(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


	print("Running {}/<num>".format(exp_num));
	exp_num += 1;
	system_dict = test_loss_multilabelsoftmargin(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


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
	system_dict = test_layer_transposed_convolution1d(system_dict)
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
	system_dict = test_layer_instance_normalization(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


	print("Running {}/<num>".format(exp_num));
	exp_num += 1;
	system_dict = test_layer_layer_normalization(system_dict)
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
	system_dict = test_activation_sigmoid(system_dict)
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
	system_dict = test_activation_elu(system_dict)
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
	system_dict = test_activation_prelu(system_dict)
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
	system_dict = test_activation_hardshrink(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


	print("Running {}/<num>".format(exp_num));
	exp_num += 1;
	system_dict = test_activation_hardtanh(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


	print("Running {}/<num>".format(exp_num));
	exp_num += 1;
	system_dict = test_activation_logsigmoid(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


	print("Running {}/<num>".format(exp_num));
	exp_num += 1;
	system_dict = test_activation_relu6(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


	print("Running {}/<num>".format(exp_num));
	exp_num += 1;
	system_dict = test_activation_rrelu(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


	print("Running {}/<num>".format(exp_num));
	exp_num += 1;
	system_dict = test_activation_celu(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


	print("Running {}/<num>".format(exp_num));
	exp_num += 1;
	system_dict = test_activation_softshrink(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


	print("Running {}/<num>".format(exp_num));
	exp_num += 1;
	system_dict = test_activation_tanhshrink(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


	print("Running {}/<num>".format(exp_num));
	exp_num += 1;
	system_dict = test_activation_threshold(system_dict)
	sys.stdout = origstdout;
	print("Tests Completed           - {}".format(system_dict["total_tests"]));
	print("Tests Succesful           - {}".format(system_dict["successful_tests"]));    
	print("")


	print("Running {}/<num>".format(exp_num));
	exp_num += 1;
	system_dict = test_activation_softmin(system_dict)
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
	system_dict = test_activation_logsoftmax(system_dict)
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