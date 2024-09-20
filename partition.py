import os
import sys

arg = sys.argv[1]
buckets = []
max_size = 10485760

pdfs = sorted([f for f in os.listdir(arg) if f.endswith('pdf')])

total = 0
bucket = []
for pdf in pdfs:
    fpath = arg + '/' + pdf
    stat = os.stat(fpath)

    if (total + stat.st_size > max_size):
        buckets.append(bucket)
        total = stat.st_size
        bucket = [fpath]
    else:
        total += stat.st_size
        bucket.append(fpath)
buckets.append(bucket)

for bucket in buckets:
    print(" ".join(f for f in bucket))
