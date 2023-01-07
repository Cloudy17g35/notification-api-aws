import boto3

sns = boto3.client('sns')


def lambda_handler(event, context):
    
    phone_number:str = event['phone_number']
    message:str = event['message']
    
    sns.publish(PhoneNumber=phone_number, Message=message)
    print(f'message sent succefully to number {phone_number}')
    return 'Success!'
