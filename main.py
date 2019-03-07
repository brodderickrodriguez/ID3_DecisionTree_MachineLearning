#!/usr/local/bin/python3
# Brodderick Rodriguez
# Auburn University - CSSE
# 25 Feb. 2019

import FeatureMatrix
import AttributeLookUpTable as alt
import DecisionTree


def example_of_dataset_structure():
	fm = FeatureMatrix.FeatureMatrix()

	file0 = fm.training[1]
	amino_acid0 = file0[0]
	amino_acid0_name = amino_acid0[0]
	amino_acid0_label = amino_acid0[2]
	amino_acid0_attributes = amino_acid0[1]
	amino_acid0_attributes_hydrophobic = amino_acid0_attributes['hydrophobic']
	print(amino_acid0_attributes_hydrophobic)


def check_count_of_B_or_E():
	fm = FeatureMatrix.FeatureMatrix(training_set_percentage=1.0)
	amino_acids = {str(e):{'B':0, 'E':0} for e in alt.AttributeLookUpTable()}

	for sequence in fm.training:
		for amino_acid in sequence:
			print(amino_acid[0], amino_acid[2])
			amino_acids[amino_acid[0]][amino_acid[2]] += 1
		break

	[print(a) for a in amino_acids.items()]



def make_toy_dt():
	d = DecisionTree.DecisionTree()
	d.sample()
	packed_json = d.pack()
	print(packed_json)

	d1 = DecisionTree.DecisionTree()

	d1.unpack('./models/model.json')
	print('\n\n\n\n')
	print(d1.pack())
	pass



if __name__ == '__main__':
	print('ID3 algo')
	# example_of_dataset_structure()
	# check_count_of_B_or_E()
	# make_toy_dt()

	fm = FeatureMatrix.FeatureMatrix(training_set_percentage=0.75)


	#decision_tree = DecisionTree.DecisionTree(fm)
	#decision_tree.train()
	#x = decision_tree.pack()
	#print(x)

	decision_tree = DecisionTree.DecisionTree(fm)
	decision_tree.unpack('./models/model.json')
	print(decision_tree.pack())

	decision_tree.test()
	decision_tree.test_performance()









