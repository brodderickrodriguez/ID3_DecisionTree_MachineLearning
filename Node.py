#!/usr/local/bin/python3
# Brodderick Rodriguez
# Auburn University - CSSE
# 28 Feb. 2019

import collections


class Node:
	# class variable for keeping track of the global 
	# node id. Used to generate unique ids.
	NODE_ID = 0

	def __init__(self, attribute=''):

		# name of the attribute this node represents
		self.attribute_name = attribute

		# this dictionary should work as follows:
		# key is the feature value: 1 (yes), 0 (no)
		# value is the child node
		# example: {1: <Node Instance>, 0: <Node Instance>}
		self.children = {}

		# get a unique node id
		self.node_id = Node.NODE_ID
		Node.NODE_ID += 1

	def is_leaf(self): 
		return 0

	# to string method
	def __str__(self):
		return str(self.node_id) + ' ' + str(self.pack())

	def add_child_n(self, node, attribute_value):
		if self.children.get(attribute_value) is not None:
			raise RuntimeError('a node with this value already exists')

		self.children[attribute_value] = node
		return node

	# adds a child node to this node
	def add_child(self, attribute, attribute_value):
		return self.add_child_n(Node(attribute), attribute_value)

	# checks if we are a leaf node
	def has_children(self):
		return len(self.children) == 0

	# pack this node into a dictionary 
	# creates a dictionary as follows:
	# {attribute: <attrribute>, children: {attribute_value: child_id}}
	def pack(self):
		children = {attribute_value: child.node_id for attribute_value, child in self.children.items()}
		return {'attribute': self.attribute_name, 'children': children, 'leaf': self.is_leaf()}


# a subclass of Node which functions as a leaf node
class LeafNode(Node):
	def __init__(self, data=[]):
		super().__init__()

		# two dimensions
		self.data_bucket = []
		self.add_data(data)
		self.predicted_label = None

	# adds from the feature matrix subset dataset
	def add_data(self, data):
		for sequence in data:
			for amino_acid in sequence:
				self.add_amino_acid(amino_acid)

	# adds a single amino acid
	def add_amino_acid(self, amino_acid):
		self.data_bucket.append(amino_acid)

	# returns a flag, true, to notify that we are a leaf node
	def is_leaf(self):
		return 1

	# computes the label for this leaf node 
	# and adds the predicted label to each amino acid
	def get_label(self):
		labels = []

		if len(self.data_bucket) == 0:
			return 

		for amino in self.data_bucket:
			labels.append(amino[2])


		count_labels = collections.Counter(labels)

		if count_labels['E'] > count_labels['B']:
			predicted_label = 'E'
		else:
			predicted_label = 'B'

		self.predicted_label = predicted_label
		for amino_acid in self.data_bucket:
			amino_acid.append(predicted_label)
