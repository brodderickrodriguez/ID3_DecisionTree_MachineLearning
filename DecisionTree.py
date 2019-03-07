#!/usr/local/bin/python3
# Brodderick Rodriguez
# Auburn University - CSSE
# 28 Feb. 2019

import Node
import json
import os.path
import collections
import math
import AttributeLookUpTable as alt
import eval_accuracy as evalacc


# 
# sample of how to we are creating decision tree nodes
#
# 	r = Node.Node(attribute='root')
# 	self.set_root_node(r)
# 	c0 = r.add_child(attribute='c0', attribute_value=0)
# 	c1 = r.add_child(attribute='c1', attribute_value=1)
# 	c00 = c0.add_child(attribute='c00', attribute_value=0)
# 	c11 = c1.add_child(attribute='c11', attribute_value=1)
#
class DecisionTree:
	def __init__(self, feature_matrix):
		self.root_node = None
		self.feature_matrix = feature_matrix

	# sets the root node
	def set_root_node(self, node):
		if self.has_root_node():
			raise RuntimeError('root node is already set')

		self.root_node = node

	# checks if there is a root node
	def has_root_node(self):
		return self.root_node is not None

	# walks the tree for each amino acid
	def test(self):
		# check if there is a feature matrix
		if self.feature_matrix == None:
			raise RuntimeError('no feature matrix supplied')

		# create a local variable to test on
		testing = self.feature_matrix.testing

		# check if there is testing data
		if len(testing) == 0:
			raise RuntimeError('no testing data supplied')

		# check if there is a root node
		if self.root_node == None:
			raise RuntimeError('no root node. Did you train?')

		# walk the tree for each amino acid
		for sequence in testing:
			for amino_acid in sequence:
				self.walk_tree(self.root_node, amino_acid)

		print('finished testing')

	# used to test. Walks the tree for an amino acid 
	# and places the amino acid in the first leaf node it encounters
	def walk_tree(self, node, amino_acid):
		# if we have reached a leaf node, add this amino acid to it
		if node.is_leaf() == 1:
			node.add_amino_acid(amino_acid)
			return

		# get node variables
		node_attribute = node.attribute_name
		node_children = node.children

		# get the amino acid attribute value for this node
		amino_acid_attribute_value = amino_acid[1][node_attribute]

		# find the next node to walk to
		next_node = node_children[str(amino_acid_attribute_value)]

		# recuse on that node
		self.walk_tree(next_node, amino_acid)

	# trains (or builds) a decision tree based on the data
	def train(self):
		# local variable for our feature matrix traning data set
		training = self.feature_matrix.training

		# initiate a list of reamining attributes
		remaining_attributes = alt.get_attributes()
		
		# get the attribute for the initial split
		attribute = self.get_next_attribute(remaining_attributes, training)
		
		# remove it from the list of remaining attributes
		remaining_attributes.remove(attribute)

		# add our root node to this tree
		root = Node.Node(attribute=attribute)
		self.set_root_node(root)

		# subset the data given the attribute is 0 or 1
		d0 = self.feature_matrix.subset(training, attribute, 0)
		d1 = self.feature_matrix.subset(training, attribute, 1)

		# recurse and add nodes to the tree
		c0 = self.add_nodes(parent_node=root, data=d0, remaining_attributes=remaining_attributes)
		c1 = self.add_nodes(parent_node=root, data=d1, remaining_attributes=remaining_attributes)

		# add the root nodes children
		root.add_child_n(c0, attribute_value=0)
		root.add_child_n(c1, attribute_value=1)

		print('built tree')

	# recursivley adds nodes to our tree intil we have no
	# more attributes or our entropy is zero
	def add_nodes(self, parent_node, data, remaining_attributes):
		# if we have no more attributes to split on
		if len(remaining_attributes) == 0:
			return Node.LeafNode(data)

		# calculate the remaining entropy of our label
		label_prob = self.probability_of_labels(data)
		label_entropy = self.entropy(label_prob)

		# if our entropy is zero, return a leaf node
		if label_entropy == 0:
			return Node.LeafNode(data)

		# choose the next attribute
		next_attribute = self.get_next_attribute(remaining_attributes, data)
		# remaining_attributes.remove(next_attribute)
		remaining_attributes = [a for a in remaining_attributes if a != next_attribute]

		# the node we are adding to the tree
		node = Node.Node(attribute=next_attribute)

		# the subsets of data given our next attribute is 0 or 1
		d0 = self.feature_matrix.subset(data, next_attribute, 0)
		d1 = self.feature_matrix.subset(data, next_attribute, 1)

		# recursivley add the child nodes to the tree
		c0 = self.add_nodes(parent_node=node, data=d0, remaining_attributes=remaining_attributes)
		c1 = self.add_nodes(parent_node=node, data=d1, remaining_attributes=remaining_attributes)

		# add this node to the parent
		node.add_child_n(c0, attribute_value=0)
		node.add_child_n(c1, attribute_value=1)
		return node

	# determines the next attribute to split the tree on
	def get_next_attribute(self, remaining_attributes, data):
		# builds a dictionary: {<attribute>: <info_gain(attribute)>}
		info_gains = {a: self.information_gain(a, data) for a in remaining_attributes}

		# get the max information gain attribute
		return max(info_gains)

	# computes information gain given a parameter attribute and data
	def information_gain(self, attribute, data):
		# the probability proportions of the labels. i.e. 'B'=0.5, 'E'=0.5
		label_probs = self.probability_of_labels(data)

		# the computed entropy of the label probs in range [0, 1]
		label_entropy = self.entropy(label_probs)

		# the conditional entropy of this attrubite on this data
		ce = self.conditional_entropy(attribute, data)

		# compute information gain per ID3 algorithm 
		ig = label_entropy - ce
		return ig

	# computes the conditional entropy of an attribute given a subset dataset
	def conditional_entropy(self, attribute, data):
		# get the dictionary of the probabilities: {'B': Double, 'E': Double}
		probs = self.get_probability_of_attribute(attribute, data)

		# initialize entropy
		entropy = 0

		# for each probability, compute the partial entropy
		for val in probs:
			# generate a subset given attrbute = val. i.e. hydrophobic=1
			d = self.feature_matrix.subset(data, attribute, val)

			# get the probability of this amino acids label given oru subset dataset
			p = self.probability_of_labels(d)

			# compute the entropy of that probability 
			e = self.entropy(p)

			# compute entropy via the ID3 entropy equation
			entropy += (e * probs[val])

		return entropy

	# computes entropy of a dictionary {'1': Double, '0': Double}
	# where each double prepresents the probability of an attrribute having that value
	def entropy(self, probabilities):
		result = 0

		# for each probability
		for _, prob in probabilities.items():
			# if the probability is zero, add nothing to result
			if prob == 0:
				continue

			# otherwise, compute entropy via the ID3 entropy equation
			result += (-prob) * (math.log(prob) / math.log(2))

		return result

	# computes the probability of an attribute within a subset dataset
	# returns a dictionary: {'1': Double, '0': Double}
	def get_probability_of_attribute(self, attribute, data):
		# initialize a list to contain all the attribute values
		attribute_values = []

		# for each amino acid
		for sequence in data:
			for amino_acid in sequence:
				# append this attributes value to the attribute_value list
				attribute_values.append(amino_acid[1][attribute])

		# get the number of values
		num_items = len(attribute_values)

		# count the occurances of each attribute value
		value_occurances = collections.Counter(attribute_values)

		# build a dictionary: {'1': Double, '0': Double}
		probabilities = {v: value_occurances[v] / num_items for v in value_occurances}
		return probabilities

	# computes the probability of the amino acids labels given a subset dataset
	def probability_of_labels(self, data):
		# grab the values for the entire feature matrix
		labels = self.feature_matrix.labels

		# get the labels that appear in this subset dataset
		all_labels = self.feature_matrix.get_all_labels(data)

		# compute the number of items in all_labels
		num_items = len(all_labels) if len(all_labels) > 0 else 1

		# count the occurances of the labels
		labels_occurances = collections.Counter(all_labels)

		# build a probability dictionary: {<label>: <probability}
		probabilities = {l: labels_occurances[l] / num_items for l in labels}
		return probabilities

	# creates a saved model file for this Decision Tree
	def pack(self, file_path='./models/model.json'):
		if self.root_node is None:
			return ''

		result, queue = {}, [self.root_node]

		# while we have an element in the queue
		while queue:
			node = queue.pop(0)

			# add this node to the result
			result[node.node_id] = node.pack()

			# for each child, add it to the queue
			queue += [child for child in node.children.values()]

		file = open(file_path, 'w')
		file.write(json.dumps(result))
		file.close()
		return result

	# creates a Decision tree from a saved file
	def unpack(self, file_path):
		# check if the model exists
		if not os.path.isfile(file_path):
			raise RuntimeError('file does not exist')

		# check if this decison tree is empty
		if self.has_root_node():
			raise RuntimeError('decision tree not empty')

		# recursivley add children to each node is a DFS mannor
		def recurive_add_childen(parent_node, whole_dict, child_dict):
			# for each child node
			for child_attribute_value, child_id in child_dict.items():
				
				# get next child's attribute and children
				child_attribute = whole_dict[str(child_id)]['attribute']
				child_children = whole_dict[str(child_id)]['children']
				is_leaf = whole_dict[str(child_id)]['leaf']

				# create a node and add child to it 
				if is_leaf == 1:
					child_node = Node.LeafNode()
				else:
					child_node = Node.Node(child_attribute)

				parent_node.add_child_n(child_node, child_attribute_value)

				# recursively add its children 
				if is_leaf == 0:
					recurive_add_childen(parent_node=child_node, whole_dict=whole_dict, child_dict=child_children)

		# get the model file contens
		file = open(file_path, 'r')
		data = json.load(file)
		file.close()

		# get root entry in dict
		root_entry = data[str(0)]

		# build root node
		root = Node.Node(root_entry['attribute'])
		root_children = root_entry['children']

		# add each childens childen...
		recurive_add_childen(parent_node=root, whole_dict=data, child_dict=root_children)

		# set the root node
		self.set_root_node(root)
		return self.set_root_node


	def test_performance(self):
		 def find_leafs(node):
		 	c0 = node.children['0']
		 	c1 = node.children['1']

		 	if c0.is_leaf():
		 		c0.get_label()
		 	else:
		 		find_leafs(c0)

		 	if c1.is_leaf():
		 		c1.get_label()
		 	else:
		 		find_leafs(c1)


		 find_leafs(self.root_node)
		 acc = evalacc.eval_accuracy()
		 acc.test_accuracy(self.feature_matrix.testing)
