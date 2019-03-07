------------------
Usage Instructions
------------------

Mac & Linux:
you can use the run.sh Bash Shell Script to run this project: `bash ./run.sh`

Python version support:
Our program has been verified on Python 3.6.6 and 3.7.2 BUT does not
run on 2.7.14. Please note the 'python3' call below in 'To run'


To run:

Option 1:
		Use the Bash Shell Script: `bash ./run.sh`
		This has preprogrammed python3 commands with
		filepaths predefined for easy running.

Option 2:
		Manually call python3: `python3 ./main.py`


Please insert the dataset according to the below file hierarchy.
Fasta:
├───data
│   ├───fasta
│   └───sa

 Go to project2_code/data/fasta--> drop a fasta file. Go to project2_code/data/sa--> drop the respective solvent accessibility labels file.
However, a sample file has been placed in both the directories. After inserting, call main.py file. The results will be printed out.
