import requests
from bs4 import BeautifulSoup
import re


class GenscanOutput:
    def __init__(self, status, cds_list, intron_list, exon_list):
        self.status = status
        self.cds_list = cds_list
        self.intron_list = intron_list
        self.exon_list = exon_list


def run_genscan(sequence=None, sequence_file=None, organism="Vertebrate", exon_cutoff=1.00, sequence_name=""):
    # request
    url = 'http://hollywood.mit.edu/cgi-bin/genscanw_py.cgi'
    payload = {
        "-o": organism,
        "-e": exon_cutoff,
        "-n": sequence_name,
        "-p": "Predicted peptides only"
    }
    if sequence is not None:
        payload['-s'] = sequence
        resp = requests.post(url, data=payload)
    if sequence_file is not None:
        seq_file = open(sequence_file, 'rb')
        file_list = {'-u': seq_file}
        resp = requests.post(url, data=payload, files=file_list)
        seq_file.close()
    resp_status = resp.status_code
    # save_content(resp, "page.html")
    soup = BeautifulSoup(resp.content)
    out = soup.find("pre").text
    out = str(out)

    # cds
    cds_list = []
    cds_pattern = re.compile(r'^>.+\n+([A-Z\n]+)', re.M)
    cds_drop_title = re.compile(r'^[A-Z\n]*', re.M)
    cds_find = cds_pattern.finditer(out)
    for i in cds_find:
        seq = cds_drop_title.findall(i.group())
        cds_list.append(seq[1].replace('\n', ''))

    # introns
    intron_list = []
    intron_pattern = re.compile(r'\d+ [A-z]{4}.*', re.M)
    intron_find = intron_pattern.finditer(out)
    for i in intron_find:
        start_pos = int(i.group()[12:16])
        end_pos = int(i.group()[19:23])
        intron_list += [[start_pos, end_pos]]

    # exons
    exon_list = []
    seq_length_pattern = re.compile(r'(\d+) bp', re.M)
    seq_length = seq_length_pattern.findall(out)
    length = int(seq_length[0])
    if len(intron_list) >= 1:
        exon_list += [[1, intron_list[0][1]]]
        if len(intron_list) >= 2:
            exon_list += [[intron_list[-1][2], length]]
            if len(intron_list) >= 3:
                for i in range(1, len(intron_list)):
                    exon_list += [[intron_list[i - 1][2], intron_list[i][1]]]

    return GenscanOutput(status=resp_status, cds_list=cds_list, intron_list=intron_list, exon_list=exon_list)


if __name__ == "__main__":
    example = run_genscan(sequence_file='./test_file.fasta')
    print('CDSs:', '\n', example.cds_list)
    print('exons:', '\n', example.exon_list)
    print('introns:', '\n', example.exon_list)
