#!/usr/local/bin/python3
# Brodderick Rodriguez
# Auburn University - CSSE
# 25 Feb. 2019

import os
import math
import random
import AttributeLookUpTable as alt

'''
The feature matrix is shaped as follows:
dimension 0: a sequence
dimension 1: an amino acid in the sequence
dimension 2: the attributes of that amino acid

An example of how to access sequences, amino acids, attributes, labels:
	
	fm = fm.FeatureMatrix()
	file0 = fm.training[0]
	amino_acid0 = file0[0]
	amino_acid0_name = amino_acid0[0]
	amino_acid0_label = amino_acid0[2]
	amino_acid0_attributes = amino_acid0[1]
	amino_acid0_attributes_hydrophobic = amino_acid0_attributes['hydrophobic']

'''
class FeatureMatrix:
	def __init__(self, training_set_percentage=0.75, 
		         fasta_files_directory='./data/fasta', 
		         sa_files_directory='./data/sa'):
		# get the raw dataset filenames
		raw_dataset = self.build_raw_dataset(fasta_files_directory, sa_files_directory)

		# build complete feature matrix
		feature_matrix = self.filenames_to_feature_matrix(raw_dataset)

		# randomly shuffle the feature matrix to generate 'random sampling'
		random.shuffle(feature_matrix)

		# split dataset into training and testing sets
		self.training, self.testing = self.feature_matrix_to_training_testing_set(feature_matrix, training_set_percentage)

		# get the different possible labels
		self.labels = self.get_label_values(feature_matrix)


	def get_label_values(self, feature_matrix):
		labels = list(set(self.get_all_labels(feature_matrix)))
		return labels

	def get_all_labels(self, data):
		labels = [amino_acid[2] for sequence in data for amino_acid in sequence]
		return labels


	def subset(self, data, attribute, value):
		result = []
		for sequence in data:
			r = []
			for amino_acid in sequence:
				if amino_acid[1][attribute] == value:
					r.append(amino_acid)
			if len(r) > 0:
				result.append(r)
		return result


	def build_raw_dataset(self, fasta_files_directory, sa_files_directory):
		# get all .fasta, .sa files from the specified directories
		fasta_files = os.listdir(fasta_files_directory)
		sa_files = os.listdir(sa_files_directory)

		# sort so the fasta, sa files match up
		fasta_files.sort()
		sa_files.sort()

		# add the prefix directory to each filename
		fasta_files = [fasta_files_directory + '/' + fname for fname in fasta_files]
		sa_files = [sa_files_directory + '/' + fname for fname in sa_files]

		# tuple (<.fasta>, <.sa>) of all the files
		raw_files = [(fasta_files[i], sa_files[i]) for i in range(len(fasta_files))]
		return raw_files

	def filenames_to_feature_matrix(self, raw_dataset):
		# get a copy of the lookup table
		lookup_table = alt.AttributeLookUpTable()
		
		# initialize feature matrix
		fm = []

		# for each file in our raw data set
		for (fasta, sa) in raw_dataset:

			# get the character list of each of the fasta, sa files
			fasta_contents = self.get_file_contents(fasta)
			sa_contents = self.get_file_contents(sa)

			# initialize a matrix for this current file
			file_feature_matrix = []

			# for a character in the fasta file
			for i in range(len(fasta_contents)):
				# get the amino acid by index
				amino_acid = fasta_contents[i]

				# get the attributes of this amino acid
				attributes = lookup_table[amino_acid]

				# ge the label from the sa file of this amino acid
				label = sa_contents[i]

				# append the row to the file_feature_matrix
				file_feature_matrix.append([amino_acid, attributes, label])

			# append this file feature matrix to the dataset feature matrix
			fm.append(file_feature_matrix)

		return fm

	def get_file_contents(self, filename):
		with open(filename) as file: raw = file.read()
		return list(raw.split('\n')[1])

	def feature_matrix_to_training_testing_set(self, feature_matrix, training_set_percentage):
		# index at which we will split the split the dataset 
		# into training and testing datasets
		piv_idx = math.floor(len(feature_matrix) * training_set_percentage)

		# build and return training and testing datasets
		training_set = feature_matrix[:piv_idx]
		testing_set = feature_matrix[piv_idx:]
		return training_set, testing_set
