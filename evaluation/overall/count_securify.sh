set -e

echo -n "TOD Transfer: "
cut eval/tod_properties.csv -d ',' -f 5 | grep True | wc -l

echo -n "TOD Amount: "
cut eval/tod_properties.csv -d ',' -f 6 | grep True | wc -l

echo -n "TOD Receiver: "
cut eval/tod_properties.csv -d ',' -f 7 | grep True | wc -l