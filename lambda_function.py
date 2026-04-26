import json
import boto3
import uuid
from datetime import datetime

# Initialize AWS clients
ses = boto3.client('ses', region_name='us-east-1')
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('CollegeEnquiries')

# ⚠️ CHANGE THESE TO YOUR VERIFIED EMAILS
SENDER_EMAIL = "xxxxx1@gmail.com"
RECEIVER_EMAIL = "xxxxxxx2@gmail.com"

def lambda_handler(event, context):
    
    # Handle CORS preflight request (browser sends this first)
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST,OPTIONS'
            },
            'body': ''
        }
    
    try:
        # Parse the form data sent from the HTML form
        body = json.loads(event['body'])
        
        student_name   = body.get('studentName', '')
        email          = body.get('email', '')
        phone          = body.get('phone', '')
        course         = body.get('course', '')
        marks_10th     = body.get('marks10th', '')
        marks_12th     = body.get('marks12th', '')
        message        = body.get('message', '')
        
        # Generate a unique ID for this submission
        submission_id = str(uuid.uuid4())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # --- SAVE TO DYNAMODB ---
        table.put_item(Item={
            'submissionId': submission_id,
            'studentName':  student_name,
            'email':        email,
            'phone':        phone,
            'course':       course,
            'marks10th':    marks_10th,
            'marks12th':    marks_12th,
            'message':      message,
            'timestamp':    timestamp
        })
        
        # --- SEND CONFIRMATION EMAIL TO STUDENT ---
        student_email_body = f"""
Dear {student_name},

Thank you for your enquiry at our college!

We have received your application details:
- Course Interested In: {course}
- 10th Marks: {marks_10th}%
- 12th Marks: {marks_12th}%

Our admissions team will contact you at {phone} or {email} within 2-3 working days.

Reference ID: {submission_id}

Best Regards,
Admissions Team
College Name
        """
        
        ses.send_email(
            Source=SENDER_EMAIL,
            Destination={'ToAddresses': [email]},
            Message={
                'Subject': {'Data': 'College Admission Enquiry - Confirmation'},
                'Body':    {'Text': {'Data': student_email_body}}
            }
        )
        
        # --- SEND NOTIFICATION EMAIL TO COLLEGE ADMIN ---
        admin_email_body = f"""
New Admission Enquiry Received!

Student Name : {student_name}
Email        : {email}
Phone        : {phone}
Course       : {course}
10th Marks   : {marks_10th}%
12th Marks   : {marks_12th}%
Message      : {message}
Submitted At : {timestamp}
Reference ID : {submission_id}
        """
        
        ses.send_email(
            Source=SENDER_EMAIL,
            Destination={'ToAddresses': [RECEIVER_EMAIL]},
            Message={
                'Subject': {'Data': f'New Enquiry from {student_name}'},
                'Body':    {'Text': {'Data': admin_email_body}}
            }
        )
        
        # Return success response
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Enquiry submitted successfully!',
                'referenceId': submission_id
            })
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Something went wrong. Please try again.'})
        }
        
