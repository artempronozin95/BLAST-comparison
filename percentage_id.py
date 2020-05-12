from Bio import AlignIO
align = AlignIO.parse("prot.aln", "clustal")
ali = list(align)
for alignments in ali:
    lenali = alignments.get_alignment_length()
    seq1=[]
    seq2=[]
    for record in alignments[0]:
        seq1.append(record)
    for record in alignments[1]:
        seq2.append(record)
    n=0
    num=0
    while n<lenali:
        seqq1=seq1[n]
        seqq2=seq2[n]
        for w in seqq1:
            if w in seqq2:
               num=num+1
        n=n+1
    percent=num/lenali
    print(percent)
