#===== Part 1 =====
#Loops & if/else 

numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4]
# A Identify all numbers with an absolut value >= 10. Print the sum of those numbers

new_sum = []
for i in numbers:  
    if abs(i) >= 10:  
        new_sum.append(i)

print("Sum of number >= 10:", sum(new_sum)) #I used ChatGPT to double check if the 'print' works being outside of the function or not c:

# B Build and print a list of the cubes (n^3) of negative numbers

nums_cubed = [] #its the list to hold my negative numbers and be able to append them once cubed
import math 
for i in numbers:
    if i < 0:
        nums_cubed.append(math.pow(i, 3)) #I learnt this in the practice and was 99% sure i could still use math.pow(i, 2) but changing the 2 to 3; googled that and it answered with its AI engine
print(nums_cubed)

# C Scan left-to-right and print the first repeated absolute value 

newlist = [] # empty list to hold unique elements from the list
duplicate = None # 
for i in numbers:
    if i in newlist:
        duplicate = i
        break  # stop at the first duplicate
    newlist.append(i) #basically im telling it to append i (integers) in the newlist list, but if its already there, break the loop and if found, print there is a duplicate found

if duplicate:
    print("The following integer is the first duplicate:", duplicate)
else:
    print("No repeats")

#==== Part 2 ====
import csv
import pandas as pd
import matplotlib.pyplot as plt
import argparse

# Task 2.1
def main():
    # 1️ Set up the argument parser for a manual CSV read, could have been 'program', 'description' or 'usage'
    parser = argparse.ArgumentParser() #Ill leave that empty
    parser.add_argument( # Adding an argument to the parser object with help messages and setting parameters such as its required
        "-f", "--file", #You can use either one, they both store their value in the same variable (args.file).
        type=str, #for it to check if/when crushing
        required=True,
        help="Path to the CSV file created in the previous exercise"
    )
    args = parser.parse_args() #“Look at what the user typed when running the script and put those values into the variable args.”

    csv_path = args.file #renaming the input argument value the user provided.
    """
I can skip #2 and #3 and go via
df = pandas.read_csv('csv_path')
so either do manually as below or using the shortcut with pandas.read_csv() command
    """
    # 2️ Read the CSV using the csv module first 
    """this block of code is about reading your CSV file manually 
    using Python's built-in csv module, before you move on to converting it into a pandas DataFrame."""
    rows = [] #You create an empty list that will store each row from your CSV file.
    with open(csv_path, "r", newline="") as f: #automatically closes the file afterward. Opens the file (in read mode) ="" avoids issues with extra blank lines on some systems.
        reader = csv.reader(f) #This creates a CSV reader object that can read each line in the file and split it into a list of values
        for row in reader: #This loop goes through each row from the CSV file (as a list) 
            rows.append(row) #and appends it to the list rows.

    print("\nCSV content (via csv module):")
    for row in rows:
        print(row)

    # 3️ Convert to a pandas DataFrame
    df = pd.DataFrame(rows)      # convert list of lists into dataframe
    """end of the read_csv()"""
    print(df.head())             # quick look
    print(df.describe())   # statistical summary, OR df[["0","1","2"]].describe()
"""Im re using what ive donde in task from practical 5 that I coded together with Emma and ChatGPT, i read through it and i still resonate with it"""
# Task 2.2
#2.2.1 Create a function that A) Plots a histogram of the column fpkm_log2 from the data frame i created 
# from reading the file brca_head500_genes.csv.csv. This will show a distribution of the log transformed expression
# Save the figure as an image called fpkm_distribution.png

"""the file includes these columns separated by a comma ',' , good to have here to double check for own sanity
gene_id,gene_name,gene_type,unstranded,stranded_first,stranded_second,tpm_unstranded,fpkm_unstranded,fpkm_uq_unstranded,fpkm_log2
"""
# Now ill use the pd.read_csv command because its faster and cleaner and also i suppose we are expected to use it 
# since we import pandas in the beginning c: 
df_brca = pd.read_csv("brca_head500_genes.csv")
print("\nTask 2.2; Columns detected:", list(df_brca.columns)) # for sanity purposes

# to plot a histogram on plt

plt.hist(df_brca["fpkm_log2"])

#2.2.3
plt.title("Distribution of gene expression")
plt.xlabel("Expression")
plt.ylabel("Number of genes")
plt.tight_layout() # After i wrote .hist .title .xlabel and .ylabel i asked chat gpt what i can add
#it gave me a long list but i kept this one

# command to save histogram as png
plt.savefig("fpkm_distribution.png")
# plt.show()

if __name__ == "__main__":
    main()