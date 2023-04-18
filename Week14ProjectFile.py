import boto3

ec2 = boto3.resource('ec2')

    
dev = ec2.create_instances(
    ImageId='ami-09c5c62bac0d0634e', #Image ID is specidic to your account
    InstanceType='t2.micro',
    MaxCount= 3,
    MinCount= 3,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name','Value': 'Production'},#Change the ID as required
                {'Key': 'ENV','Value': 'Production'}
                
            ]
        }
    ]
)

print(dev)