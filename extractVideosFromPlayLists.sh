
# Check if input file is provided
if [ $# -eq 0 ]
then
    echo "No input file provided"
    exit 1
fi

# Check if input file exists
if [ ! -f $1 ]
then
    echo "Input file does not exist"
    exit 1
fi

INPUT=$1

while IFS= read -r line
do
  #Echo the current line
  echo "$line"
  #Extract the text starting with 'http' from the current line
  temp=$(echo "$line"|  grep -o "http[^ ]*")

  #Fetch the website specified in the temp variable and search for specific class
  curl -s $temp|grep 'class="yt-uix-sessionlink"'|grep watch|pup 'a[href]'|
  #Extract the href value
  sed -n 's/.*href="\([^"]*\).*/\1/p'|
  #Add youtube url before extracted link
  awk -F";" '{print "http://www.youtube.com"$1}'|
  #Remove the string '&amp'
  sed 's/&amp//g'
    
done < "$INPUT"
