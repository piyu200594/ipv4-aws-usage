# ipv4-local.py

Ensure you have boto3 installed via pip: pip install boto3.
You need to have set AWS credentials.
This script fetches public IPv4 addresses (Elastic IPs) across all regions. If there are no IPs for a region, that region simply won't appear in the CSV.
Always be cautious with the output, as it can contain sensitive information.
You can directly run this python file in your AWS Cloud Console.

# ipv4-s3bucket.py

This script will produce two CSV files:

ipv4_addresses.csv: Lists all the public IPv4 addresses of instances across all regions.
elastic_ips.csv: Lists all the EIPs, whether they're associated with an instance (Used) or not (Unused).

Notes:

Make sure you've set up AWS credentials to access the necessary resources.
Ensure you have boto3 installed via pip: pip install boto3.
The script fetches both public IPv4 addresses and the status of Elastic IPs.
Depending on the number of regions, instances, and EIPs, this script might take some time to run. 
Always be cautious about where and how you store the output, as it can contain sensitive data.
