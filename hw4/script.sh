ls -l t*.txt | awk '{print $9}' > /tmp/rename.tmp

while read inputline
do
    fn = "$inputline"
    echo fn
done