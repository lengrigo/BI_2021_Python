input_fastq = input("Path to file: ")  # path to fastq file with raw Illumina sequensing data


# function for opening the file
# it returns dictionary where key is a number of read and key is a list of four strings
def opening_fastq(input_fastq):
    with open(input_fastq, mode="r") as input_file:
        all_strings = input_file.read().splitlines()
        number_of_reads = len(all_strings) // 4
        reads = {key: [] for key in range(number_of_reads)}  # словарь где ключ - это номер рида,
        # а значения - спикок из 4х строк принадлежащих этому риду
        first_strings = []
        second_strings = []
        third_strings = []
        fourth_strings = []
        for i in range(0, len(all_strings), 4):
            first_strings += [all_strings[i]]
            second_strings += [all_strings[i + 1]]
            third_strings += [[all_strings[i + 2]]]
            fourth_strings += [all_strings[i + 3]]
        for i in reads.keys():
            reads[i] += [first_strings[i - 1]]
            reads[i] += [second_strings[i - 1]]
            reads[i] += third_strings[i - 1]
            reads[i] += [fourth_strings[i - 1]]
        return reads


# function for filtering by GC content. It returns list with reads that passed filtration
# gc_bounds is a list of one or two elements - interval for filtering.
# If  there is one element in list - it is an upper border
# function returns list of two dictionaries with passed and failed reads
def gc_filtering(reads, gc_bounds):
    upper_border = gc_bounds[1]
    lower_border = 0
    if len(gc_bounds) == 2:
        lower_border = gc_bounds[0]
    gc_content = {key: 0 for key in reads}
    reads_gc_passed = {}
    reads_gc_failed = {}
    for key, value in reads.items():
        gc_count = 0
        for nucleotide in value[1].upper():
            if nucleotide == "C" or nucleotide == "G":
                gc_count += 1
        gc_content[key] += (gc_count / len(value[1])) * 100

    for key, value in gc_content.items():
        if lower_border <= value <= upper_border:
            reads_gc_passed[key] = reads[key]
        else:

            reads_gc_failed[key] = reads[key]
    return [reads_gc_passed, reads_gc_failed]


# function for filtering reads by length
# length_bounds is a list of one or two elements - interval for filtering.
# If  there is one element in list - it is an upper border
# function returns list of two dictionaries with passed and failed reads
def length_filtering(reads, length_bounds):
    upper_border = length_bounds[1]
    lower_border = 0
    if len(length_bounds) == 2:
        lower_border = length_bounds[0]
    length = {key: 0 for key in reads}
    reads_length_passed = {}
    reads_length_failed = {}
    for key, value in reads.items():
        length[key] = value[1]
    for key, value in length.items():
        if lower_border <= len(value[1]) <= upper_border:
            reads_length_passed[key] = reads[key]
        else:
            reads_length_failed[key] = reads[key]
    return [reads_length_passed, reads_length_failed]


# function for filtering reads by quality
# quality_threshold is a quality value in ASCII scale
# passed reads have average quality over all nucleotides mor then quality_threshold
# function returns list of two dictionaries with passed and failed reads
def quality(reads, quaquality_threshold):
    qualities_of_reads = {key: 0 for key in reads}
    reads_quality_passed = {}
    reads_quality_failed = {}
    for key, value in reads.items():
        quality_in_number = 0
        for i in value[-1]:
            quality_in_number += ord(i)
        qualities_of_reads[key] = quality_in_number / len(value[-1])
    for key, value in qualities_of_reads.items():
        if value >= ord(quaquality_threshold):
            reads_quality_passed[key] = reads[key]
        elif value < ord(quaquality_threshold):
            reads_quality_failed[key] = reads[key]
    return [reads_quality_passed, reads_quality_failed]


# function for writing to file
# reads_passed and reads_failed is two dictionaries with reads after filtering
# output prefix is prefix that will be added to the name of the files
# save_filtered could be T or F and says if we should save reads that did not passed filtering
def writing_in_file(input_fastq, reads_passed, reads_failed, output_prefix, save_filtered):
    output_path = input_fastq[:-6]
    with open(output_path + output_prefix[0], mode="w") as output_1:
        for i in reads_passed.values():
            output_1.write('\n'.join(i))
            output_1.write('\n')
    if save_filtered == "True":
        with open(output_path + output_prefix[1], mode="w") as output_2:
            for i in reads_failed.values():
                output_2.write('\n'.join(i))
                output_2.write('\n')


def main(input_fastq, output_prefix=["_passed.fastq", "_failed.fastq"], gc_bounds=[0, 100], length_bounds=[0, 2 ** 32],
         quality_threshold=0, save_filtered="False"):
    reads = opening_fastq(input_fastq)
    reads_passed = gc_filtering(length_filtering(quality(reads, quality_threshold)[0], length_bounds)[0], gc_bounds)[0]
    reads_failed = quality(reads, quality_threshold)[1]
    for key, value in gc_filtering(reads, gc_bounds)[1]:
        if key not in reads_failed:
            reads_failed[key] = value
    for key, value in length_filtering(reads, length_bounds)[1]:
        if key not in reads_failed:
            reads_failed[key] = value
    writing_in_file(input_fastq, reads_passed, reads_failed, output_prefix, save_filtered)


main(input_fastq)
