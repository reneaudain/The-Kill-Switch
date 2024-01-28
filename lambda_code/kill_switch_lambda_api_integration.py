# Importing required libraries: boto3 for AWS SDK and json for parsing JSON data.
import boto3
import json

# Setting the AWS region that this script will operate in.
region = 'us-east-1'

# Defining the main handler function for the Lambda service.
# The 'event' parameter is used to pass in event data to the handler.
# The 'context' parameter provides information about the invocation, function, and execution environment.
def lambda_handler(event, context):
    # Creating an EC2 client. This client provides a high-level interface to interact with EC2.
    ec2 = boto3.client('ec2', region_name=region)

    # Parsing the 'Environment' field from the JSON body of the event.
    # It's assumed that the event contains a JSON body with an 'Environment' field.
    ec2tag = json.loads(event['body'])['Environment']

    # Initializing an empty list to store instance IDs.
    instanceids = []

    # A redundant condition check, as it always evaluates to True.
    if ec2tag == ec2tag:
        # Calling the describe_instances method to retrieve information about all EC2 instances.
        response = ec2.describe_instances()

        # Iterating over the reservations in the response.
        for reservations in response['Reservations']:
            # Each reservation in the response contains information about EC2 instances.
            for instance in reservations["Instances"]:
                # Checking if the instance has any tags.
                if "Tags" in instance:
                    # Iterating over the tags of the instance.
                    for tag in instance["Tags"]:
                        # If a tag's value matches ec2tag, add the instance ID to the list.
                        if tag["Value"] == ec2tag:
                            # Appending the instance ID to the instanceids list and printing it.
                            print(instanceids.append(instance['InstanceId']))
        
        # Stopping the instances with IDs in the instanceids list.
        # This command sends a request to stop the instances, but there's no handling for the response or errors.
        response = ec2.stop_instances(InstanceIds=instanceids)
