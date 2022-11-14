model_default = fasttext.train_supervised(input="week3_train_1.txt")
model_default.save_model("week3_model_defaut_train_1.bin")
model_default.test("week3_test_1.txt")
(10000, 0.4832, 0.4832)

model_default.test("week3_test_1.txt", 2)
(10000, 0.29635, 0.5927)

model_default.test("week3_test_1.txt", 3)
(10000, 0.2153, 0.6459)

In [29]: model_tweaked_params_1 = fasttext.train_supervised(input="week3_train_1.txt", lr=0.6, epoch=25, wordNgr
    ...: ams=2)
Read 0M words
Number of words:  7586
Number of labels: 387
Progress: 100.0% words/sec/thread:   11725 lr:  0.000000 avg.loss:  2.623785 ETA:   0h 0m 0s

In [30]: model_tweaked_params_1.save_model("week3_model_tweaked_params_train_1.bin")

In [31]: model_tweaked_params_1.test("week3_test_1.txt", 1)
Out[31]: (10000, 0.5263, 0.5263)

In [32]: model_tweaked_params_1.test("week3_test_1.txt", 2)
Out[32]: (10000, 0.32785, 0.6557)

In [33]: model_tweaked_params_1.test("week3_test_1.txt", 3)
Out[33]: (10000, 0.23786666666666667, 0.7136)

In [39]: model_tweaked_params_1.test("week3_test_1.txt", 5)
Out[39]: (10000, 0.15514, 0.7757)

# 100000 traning queries
In [34]: model_tweaked_params_2 = fasttext.train_supervised(input="week3_train_2.txt", lr=0.6, epoch=25, wordNgr
    ...: ams=2)
Read 0M words
Number of words:  10983
Number of labels: 387
Progress: 100.0% words/sec/thread:    7258 lr:  0.000000 avg.loss:  2.844083 ETA:   0h 0m 0s

In [35]: model_tweaked_params_2.test("week3_test_1.txt")
Out[35]: (10000, 0.5437, 0.5437)

In [36]: model_tweaked_params_2.test("week3_test_1.txt", 2)
Out[36]: (10000, 0.33885, 0.6777)

In [37]: model_tweaked_params_2.test("week3_test_1.txt", 3)
Out[37]: (10000, 0.247, 0.741)

In [38]: model_tweaked_params_2.test("week3_test_1.txt", 5)
Out[38]: (10000, 0.16048, 0.8024)
