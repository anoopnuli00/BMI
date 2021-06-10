
test_argument=0
main_argument=0

# read command line arguments
for i in "$@"
do
   case $i in
      -t|--test)
      test_argument=1
	  ;;
      -m|--main)
      main_argument=1
      ;;
      *)
      echo "USAGE : [ $0 --test --main]"
	  exit
      ;;
   esac
done

if [ "$test_argument" -eq 0 ] && [ "$main_argument" -eq 0 ]; then
	echo "USAGE : [ $0 --test --main]"
fi

if [ "$test_argument" -eq 1 ]; then 
	python test.py
fi

if [ "$main_argument" -eq 1 ]; then 
	python main.py
fi


