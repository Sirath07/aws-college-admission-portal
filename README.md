# 🎓 AWS Serverless College Admission Portal

> **Live Production Project** — Built entirely on AWS Cloud  
> Designed & Deployed by **Sayed Mohammed Sirath Raza**  
> BCA Student | AI & Cloud Computing | Yenepoya University, Mangalore

---

## 🌐 Live Demo
🔗 [Click here to view live project](https://college-enquiry-fx.s3.us-east-1.amazonaws.com/index.html)

---

## 📌 Project Overview
A fully serverless, production-grade College Admission 
Portal built on AWS — with zero server management.

This is not a demo. This is a **LIVE system** actively 
capturing real student enquiries stored in AWS DynamoDB.

---

## 🎨 Frontend Features
- ✅ Professional university-grade UI
- ✅ Multi-category course explorer  
  (Medical, Nursing, Engineering, BCA, MBA & more)
- ✅ Course-wise fee & duration display
- ✅ Smart Admission Enquiry Form
- ✅ Hostel & Y-ENTRANCE exam info section
- ✅ Real-time success/error feedback

---

## ⚙️ AWS Architecture

Student fills form (S3 Static Website)
↓
API Gateway (REST API + CORS)
↓
AWS Lambda (Python 3.12 + Boto3)
/         
DynamoDB        SES
(stores data)   (sends 2 emails)


## 🛠️ Services Used

| AWS Service | Purpose |
|---|---|
| Amazon S3 | Static website hosting |
| AWS Lambda | Serverless backend (Python 3.12) |
| Amazon API Gateway | REST API endpoint |
| Amazon DynamoDB | NoSQL database for submissions |
| Amazon SES | Automated dual-email notifications |
| AWS IAM | Least-privilege role permissions |

---

## 📊 Proof It Works
- 6+ real student enquiries captured live
- Each submission stored with unique UUID
- Timestamps, course, marks all recorded

## 📸 Screenshots

### 🌐 Live Portal — Homepage
![Portal Homepage](screenshots/portal.png.png)

### 📋 Admission Enquiry Form
![Enquiry Form](screenshots/portal2.png.png)

### 🗄️ DynamoDB — Live Data
![DynamoDB Live Data](screenshots/dynamodb.png.png)

---

## 🚀 Setup Guide
1. Verify 2 emails in Amazon SES
2. Create IAM role with SES + DynamoDB + Lambda policies
3. Create DynamoDB table: `CollegeEnquiries`
4. Deploy Lambda function with Python code
5. Create API Gateway REST API → link to Lambda
6. Upload `index.html` to S3 → enable static hosting
7. Replace API URL in HTML → done!

---

## 💼 Need This For Your College or Business?
I build custom AWS-powered websites and lead capture 
systems for colleges, schools & businesses.

📩 **Contact:** sayedsirath83@gmail.com  
💼 **LinkedIn:** www.linkedin.com/in/sayed-sirath-2baa5022a

---

## 👨‍💻 Author
**Sayed Mohammed Sirath Raza**  
BCA | AI & Cloud Computing + DevOps Specialization  
Yenepoya University, Mangalore  

#AWS #Serverless #CloudComputing #Lambda #DynamoDB
