year=2025
dir=$year/$1

if [ -d $dir ]; then
    echo "directory already exists"
    exit 1
fi

mkdir $dir
touch $dir/puzzle.py
touch $dir/input.txt
touch $dir/input_min.txt

echo "\"\"\"" >> $dir/puzzle.py
echo "$dir" >> $dir/puzzle.py
echo "\"\"\"" >> $dir/puzzle.py
