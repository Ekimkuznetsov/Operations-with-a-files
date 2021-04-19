# Use the file name mbox-short.txt as the file name
# Write a program that prompts for a file name, then opens that file and reads through the file

fname = input("Enter file name: ")
fh = open(fname)
count = 0
conf = 0
for line in fh:
    line = line.rstrip() #remove spaces between lines
    if not line.startswith("X-DSPAM-Confidence:") : continue
    sline = line.split()
    conf = conf + float(sline[1])
    count = count + 1
avconf = conf / count
print("Average spam confidence:s", avconf)
