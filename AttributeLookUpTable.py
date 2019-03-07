#!/usr/local/bin/python3
# Brodderick Rodriguez
# Auburn University - CSSE
# 25 Feb. 2019

def AttributeLookUpTable():
	lt = {
	'A': {'hydrophobic':  1, 'Polar': 0, 'Small': 1, 'Proline': 0, 'Tiny': 1, 'Aliphatic': 0, 'Aromatic': 0, 'Positive': 0, 'Negative': 0, 'Charged': 0},
	'C': {'hydrophobic':  1, 'Polar': 0, 'Small': 1, 'Proline': 0, 'Tiny': 0, 'Aliphatic': 0, 'Aromatic': 0, 'Positive': 0, 'Negative': 0, 'Charged': 0},
	'D': {'hydrophobic':  0, 'Polar': 1, 'Small': 1, 'Proline': 0, 'Tiny': 0, 'Aliphatic': 0, 'Aromatic': 0, 'Positive': 0, 'Negative': 1, 'Charged': 1},
	'E': {'hydrophobic':  0, 'Polar': 1, 'Small': 0, 'Proline': 0, 'Tiny': 0, 'Aliphatic': 0, 'Aromatic': 0, 'Positive': 0, 'Negative': 1, 'Charged': 1},
	'F': {'hydrophobic':  1, 'Polar': 0, 'Small': 0, 'Proline': 0, 'Tiny': 0, 'Aliphatic': 0, 'Aromatic': 1, 'Positive': 0, 'Negative': 0, 'Charged': 0},
	'G': {'hydrophobic':  1, 'Polar': 0, 'Small': 1, 'Proline': 0, 'Tiny': 1, 'Aliphatic': 0, 'Aromatic': 0, 'Positive': 0, 'Negative': 0, 'Charged': 0},
	'H': {'hydrophobic':  0, 'Polar': 1, 'Small': 0, 'Proline': 0, 'Tiny': 0, 'Aliphatic': 0, 'Aromatic': 1, 'Positive': 1, 'Negative': 0, 'Charged': 1},
	'I': {'hydrophobic':  1, 'Polar': 0, 'Small': 0, 'Proline': 0, 'Tiny': 0, 'Aliphatic': 1, 'Aromatic': 0, 'Positive': 0, 'Negative': 0, 'Charged': 0},
	'K': {'hydrophobic':  0, 'Polar': 1, 'Small': 0, 'Proline': 0, 'Tiny': 0, 'Aliphatic': 0, 'Aromatic': 0, 'Positive': 1, 'Negative': 0, 'Charged': 1},
	'L': {'hydrophobic':  1, 'Polar': 0, 'Small': 0, 'Proline': 0, 'Tiny': 0, 'Aliphatic': 1, 'Aromatic': 0, 'Positive': 0, 'Negative': 0, 'Charged': 0},
	'M': {'hydrophobic':  1, 'Polar': 0, 'Small': 0, 'Proline': 0, 'Tiny': 0, 'Aliphatic': 1, 'Aromatic': 1, 'Positive': 0, 'Negative': 0, 'Charged': 0},
	'N': {'hydrophobic':  0, 'Polar': 1, 'Small': 1, 'Proline': 0, 'Tiny': 0, 'Aliphatic': 0, 'Aromatic': 0, 'Positive': 0, 'Negative': 0, 'Charged': 0},
	'P': {'hydrophobic':  1, 'Polar': 0, 'Small': 1, 'Proline': 1, 'Tiny': 0, 'Aliphatic': 0, 'Aromatic': 0, 'Positive': 0, 'Negative': 0, 'Charged': 0},
	'Q': {'hydrophobic':  0, 'Polar': 1, 'Small': 0, 'Proline': 0, 'Tiny': 0, 'Aliphatic': 0, 'Aromatic': 0, 'Positive': 0, 'Negative': 0, 'Charged': 0},
	'R': {'hydrophobic':  0, 'Polar': 1, 'Small': 0, 'Proline': 0, 'Tiny': 0, 'Aliphatic': 0, 'Aromatic': 0, 'Positive': 1, 'Negative': 0, 'Charged': 1},
	'S': {'hydrophobic':  0, 'Polar': 1, 'Small': 1, 'Proline': 0, 'Tiny': 1, 'Aliphatic': 0, 'Aromatic': 0, 'Positive': 0, 'Negative': 0, 'Charged': 0},
	'T': {'hydrophobic':  1, 'Polar': 1, 'Small': 1, 'Proline': 0, 'Tiny': 0, 'Aliphatic': 0, 'Aromatic': 0, 'Positive': 0, 'Negative': 0, 'Charged': 0},
	'V': {'hydrophobic':  1, 'Polar': 0, 'Small': 1, 'Proline': 0, 'Tiny': 0, 'Aliphatic': 1, 'Aromatic': 0, 'Positive': 0, 'Negative': 0, 'Charged': 0},
	'W': {'hydrophobic':  1, 'Polar': 0, 'Small': 0, 'Proline': 0, 'Tiny': 0, 'Aliphatic': 0, 'Aromatic': 1, 'Positive': 0, 'Negative': 0, 'Charged': 0},
	'Y': {'hydrophobic':  1, 'Polar': 1, 'Small': 0, 'Proline': 0, 'Tiny': 0, 'Aliphatic': 0, 'Aromatic': 1, 'Positive': 0, 'Negative': 0, 'Charged': 0},
	}

	return lt

def get_attributes():
	return ['hydrophobic', 'Polar', 'Small', 'Proline', 'Tiny', 'Aliphatic', 'Aromatic', 'Positive', 'Negative', 'Charged']
