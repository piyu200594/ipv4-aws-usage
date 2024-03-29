# How to Run the Script?

# ipv4-local.py

This Script will generate the CSV file locally in your cloudshell
Ensure you have boto3 installed via pip: 

```pip install boto3```

You need to have set AWS credentials.
This script fetches public IPv4 addresses (Elastic IPs) across all regions. If there are no IPs for a region, that region simply won't appear in the CSV.
Always be cautious with the output, as it can contain sensitive information.
You can directly run this python file in your AWS Cloud Shell.



# ipv4-s3bucket.py

This script will produce two CSV files and move it to a S3 bucket:

ipv4_addresses.csv: Lists all the public IPv4 addresses of instances across all regions.

elastic_ips.csv: Lists all the EIPs, whether they're associated with an instance (Used) or not (Unused).

Please do not forget to change this line 44 of code to your S3 bucket name:

```bucket_name = "YOUR_S3_BUCKET_NAME"  # Change this to your S3 bucket name```

# Notes:

Make sure you've set up AWS credentials to access the necessary resources.
Ensure you have boto3 installed via pip: pip install boto3.
The script fetches both public IPv4 addresses and the status of Elastic IPs.
Depending on the number of regions, instances, and EIPs, this script might take some time to run. 
Always be cautious about where and how you store the output, as it can contain sensitive data.
