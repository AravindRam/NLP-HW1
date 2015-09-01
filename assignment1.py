import sys

#Main Function
if __name__ == "__main__":
	if(len(sys.argv) == 1):					#Check for various cases of the command line arguments
		print("Missing input and output files!!")
	elif(len(sys.argv) == 2):
		print("Please specify input or output filename properly!!")
	elif(len(sys.argv) > 3):
		print("Too many arguments!! Specify only 2 arguments")
	elif(len(sys.argv) == 3): 
		inputFile = sys.argv[1]				#Getting the file pathnames
		outputFile = sys.argv[2]
		fin = open(inputFile,"r")			#Opening the files
		fout = open(outputFile,"w")
		tokens = []
		for line in fin.readlines():			#Reading the input file
			tokens = line.split(" ")		#Tokenize each line in the input file
			fout.write(str(len(tokens)))		#Write the number of tokens in each line to the output file
			fout.write("\n")
		fin.close()					#Closing the files
		fout.close()

