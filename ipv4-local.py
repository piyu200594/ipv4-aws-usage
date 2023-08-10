import boto3
import csv

def get_all_regions():
    ec2_client = boto3.client('ec2')
    return [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

def get_ipv4_and_eip_for_region(region):
    ec2_client = boto3.client('ec2', region_name=region)
    
    # Fetch all instances and their public IPs
    ipv4_data = []
    reservations = ec2_client.describe_instances()['Reservations']
    for reservation in reservations:
        for instance in reservation['Instances']:
            if 'PublicIpAddress' in instance:
                ipv4_data.append((region, instance['PublicIpAddress'], instance['InstanceId']))
                
    # Fetch all Elastic IPs and their association status
    eip_data = []
    addresses = ec2_client.describe_addresses()
    for address in addresses['Addresses']:
        ip = address['PublicIp']
        if 'InstanceId' in address:
            eip_data.append((region, ip, address['InstanceId'], 'Used'))
        else:
            eip_data.append((region, ip, 'N/A', 'Unused'))
    
    return ipv4_data, eip_data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

if __name__ == '__main__':
    all_ipv4_data = [('Region', 'IPV4', 'InstanceId')]
    all_eip_data = [('Region', 'EIP', 'InstanceId', 'Status')]
    
    for region in get_all_regions():
        ipv4_data, eip_data = get_ipv4_and_eip_for_region(region)
        all_ipv4_data.extend(ipv4_data)
        all_eip_data.extend(eip_data)
    
    save_to_csv(all_ipv4_data, 'ipv4_addresses.csv')
    save_to_csv(all_eip_data, 'elastic_ips.csv')
