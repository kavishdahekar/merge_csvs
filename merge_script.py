import os

# First open the files for reading
input_files_list = []
input_files_list.append(open('file_1.csv','r'))
input_files_list.append(open('file_2.csv','r'))
input_files_list.append(open('file_3.csv','r'))
input_files_list.append(open('file_4.csv','r'))

# Now open the output file in write mode so you can write to it line by line
file_op = open('OUTPUT_file_merged.csv','w')

# Loop over all the input files
for input_file in input_files_list:
	# loop over each line from the file
	for input_line in input_file:
		# Remove all extra characters from the lines
		input_line = input_line.rstrip()
		# write the line to the output file with a new line character at the end
		file_op.write(input_line + "\n")

	# Before copying next file, add some new line characters
	file_op.write("\n\n")