import math


class eval_accuracy:
    def test_accuracy(self, dataset):
        print('Evaluating...')

        true_pos, true_neg = 0, 0
        false_pos, false_neg = 0, 0
        metrics = ['precision:', 'recall:  ','accuracy:', 'f1 score:', 'matthew c.:']
        truth_matrix = ['True positive', 'False positive', 'True negative', 'False negative']
        values = []
        truth_values = []
        for seq in dataset:
            for amino in seq:
                predicted = amino[2]
                actual = amino[3]
                if predicted == 'E' and actual == 'E':
                    true_pos += 1
                elif predicted == 'E' and actual == 'B':
                    false_pos += 1
                elif predicted == 'B' and actual == 'B':
                    true_neg += 1
                else:
                    false_neg += 1


        precision = calculate_precision(true_pos, false_pos)
        recall = calculate_recall(true_pos, false_neg)
        accuracy = calculate_accuracy(true_pos, true_neg, false_pos, false_neg)

        f1_score = 0.0

        if precision != None and recall != None:
            f1_score = 2 * ((precision * recall) / (precision + recall))
        
        matthew_correl = calculate_matthew_correl(true_pos, true_neg, false_pos, false_neg)
        values.extend((precision, recall, accuracy, f1_score, matthew_correl))
        truth_values.extend((true_pos, false_pos, true_neg, false_neg))

        print_truth_matrix(truth_matrix, truth_values)
        print_dictionary(metrics, values, {})



def print_truth_matrix(truth_matrix, truth_values):
    print('\ntruth matrix:')

    for i in range(len(truth_matrix)):
        s = '\t' + str(truth_matrix[i]) + ':\t' + str(truth_values[i])
        print(s)


def calculate_precision(true_pos, false_pos):
    if true_pos!=0 or false_pos!=0:
        return (true_pos) / (true_pos + false_pos)


def calculate_recall(true_pos, false_neg):
    if true_pos != 0 or false_neg != 0:
        return (true_pos) / (true_pos + false_neg)


def calculate_accuracy(true_pos, true_neg, false_pos, false_neg):
    return (true_pos + true_neg) / (false_pos + false_neg + true_pos + true_neg)


def calculate_matthew_correl(true_pos, true_neg, false_pos, false_neg):
    sqrt_val = (true_pos + true_neg) * (true_pos + false_neg) * (true_neg + false_pos) * (true_neg + false_neg)
    if sqrt_val!=0:
        return ((true_pos * true_neg) - (false_pos * false_neg)) / (math.sqrt(sqrt_val))
    else:
        return 0

def print_dictionary(metrics, values, print_dict):
    print('\n')
    i = 0
    for key in metrics:
        print_dict[key] = values[i]
        i+=1
    for k in print_dict.keys():
        print (str(k) + "\t" + str(print_dict[k]))




