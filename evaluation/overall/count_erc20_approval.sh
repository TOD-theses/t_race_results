set -e

echo -n "ERC20-Approval: "
cut eval/tod_properties.csv -d ',' -f 8 | grep True | wc -l