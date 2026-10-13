
"""
Main problem: 

When sequencing data, sometimes during the PCR step there is duplications of the same sequence, 
which can make it seem like there is more expression/ frequency of that sequence than there 
actually is.

We want to remove all duplicates, using the UMI's, leftmost mapping position, chromosome, bitwise 
flag, and CIGAR string. We also want to keep in mind that some sequences might have been soft
clipped during the quality trimming process or due to splicing. This means we cannot trust the 
left most mapping position entirely. 

the duplicates will have the same chrom, UMI, strand, and start position. 


"""

# all imports 
import os
import argparse 


# argparse stuff 
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', help='SAM file of uniquely mapped reads', type=str, required=True)
    parser.add_argument('-u', help='txt file with UMIs', type=str, required=True)
    return parser.parse_args()

args = get_args()
sam, umis = args.s, args.u

# umi reading function
def umi_read(umis: IOstr) -> list: 
	umi_list = []
	for line in umis: 
		read in umi and add it to the umi_list
	return umi_list 

# getting the true start position from leftmost start and softclipping
def true_start(pos: int, rev: bool, softclip_l: int, cigar: str) -> int:
	# length includes softclipping on both sides 
	start5 = pos - softclip_l + (length of read from cigar - 1 if rev else 0) 
	return start5
# test example: pos = 4, rev = 1, softclip_l = 2, cigar = 2S3M should return 6

# checking if read is mapped 
def mapped(flag: int) -> bool: 
	# if flag is 4 then it is unmapped
	return not ((flag & 4) == 4)
# test example: flag of 100 should return False 

# deduper function 
def dedupe (sam: str, umis: str) -> NULL:
	# a dict to store all the seen sam lines so far 
	# will be in format of a dict of lists 
	# key: value -> chrom: [1324, 6321, 6153 ...]
	seen = dict()

	with open sam and umis as read files: 
		# go through the umis and put them in a list 
		umi_list = umi_read(umis)

		# go through sam lines one at a time 
		for line in sam: 
			"""
			UMI == 1, FLAG == 2, RNAME (chrom) == 3, CIGAR == 6
			"""
			grab the flag, chrom, pos, umi, and cigar 
			# softclipping on both ends if there is any, if not it is 0
			grab softclip_l from cigar 
			start5 = 0 # true start position 
			length is sum of cigar string numbers
			rev_comp = 0 or 1 

			# check if it was mapped through the bitwise flag
			if not mapped(flag): continue 

			# check if reverse complimented 
			if ((flag & 16) == 16):
				rev_comp = True

			# find the true start position
			start5 = true_start(pos, rev_comp, softclip_l, cigar)

			# check if the chrom(x,y, [1-22]), UMI (1-96), strand(1,0), and start position 
			# are already encountered 
			if dict key for current chrom does not exist: # add to dict 
				seen[chrom] = (code for combination of umi, start5, strand)
			else: # chrom has been seen
				check list at chrom in seen dict
				if there is already a read with same umi, start5, and strand:
					continue
				else: 
					add current read to dict[chrom]


# which one do we keep?
# does soft clipping get rid of some of the biological sequence in the sam file
# would we want to keep the one that is not soft clipped 
# or just the first one

# is this human data? How many chroms 

# are N's in the CIGAR string ok (splicing in original template)? can we ignore?





