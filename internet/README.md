# Internet homework

In this mini-project we should create API for GENSCAN Web server 

## The task
 Serves http://hollywood.mit.edu/GENSCAN.html can find and cut out introns from given sequence

### The task is to make:
1) Function `run_genscan (sequence=None, sequence_file=None, organism="Vertebrate", exon_cutoff=1.00, sequence_name="")`  
 This function get request likewise filling the form.  
It takes same parameters as you should give from site (except Print options):  
- `sequence` - sequence in format of string or any other that will be convenient,
- `sequence_file` - path to file with sequence that will be uploaded instead of sequence.  
Function should return object of `GenscanOutput class`.
2) class `GenscanOutput` with next attributes:
- `status` - request status
- `cds_list` - the list with predicted protein sequences
- `intron_list` - the list if found introns. It could be any data type but it should contain information about its number, start and stop positions
- `exon_list` - same , but with exons.

## Folder structure

`test_file` - file to test the code
`API_homework.ipynb` - jupiter notebook with code, tests and comments  
`API_homework.py` - file only with code  
`reqirements.txt` - file with required packages to run the code  

  
Before running the code run the next command
```
pip3 install -r requirements.txt
```
