# 💬 AI-Powered Sentiment Analyzer (Serverless on AWS)

This project is a fully serverless web application that performs real-time sentiment analysis using **Amazon Comprehend**, logs user input and results in **DynamoDB**, and delivers everything through a clean, interactive frontend hosted on **GitHub Pages**.

---

## 🔗 Live Demo  
👉 [https://nyanlinhtutrain.github.io/sentiment-analyzer/](https://nyanlinhtutrain.github.io/sentiment-analyzer/)

---

## 🧠 What It Does

- Takes user text input from the browser
- Sends it through a secure POST request to an AWS Lambda backend
- Performs sentiment analysis using Amazon Comprehend (POSITIVE, NEGATIVE, NEUTRAL, MIXED)
- Logs the text, result, and confidence score into DynamoDB
- Returns sentiment + confidence live to the user

---

## 🧱 Built With

| Component     | Technology             |
|---------------|-------------------------|
| UI / Frontend | HTML, JavaScript        |
| Hosting       | GitHub Pages            |
| API Gateway   | AWS API Gateway         |
| Backend       | AWS Lambda (Python)     |
| AI Engine     | Amazon Comprehend       |
| Database      | AWS DynamoDB            |
| Auth Control  | IAM Role-based Policies |

---

## ⚙️ Architecture Overview

[ GitHub Pages (Static Site) ] ↓ [ API Gateway (POST /sentiment) ] ↓ [ Lambda Function (Python) ] ↓ [ Amazon Comprehend + DynamoDB ]




---

## 📂 Project Structure

sentiment-analyzer/ ├── index.html # Main frontend interface ├── README.md # This file



---

## 🧪 How It Was Built (in 2 hours)

1. Created Lambda function (Python) to call Amazon Comprehend and write to DynamoDB
2. Deployed REST API via AWS API Gateway (with full CORS + IAM)
3. Created a simple HTML frontend using fetch API to POST text
4. Enabled S3 + GitHub Pages for static site hosting
5. Linked it all together into a serverless full-stack app

---

## 🙌 Author

Built by **Rain ☁️**  
Deployed 100% with AWS Free Tier + GitHub.  
Feel free to fork, clone, and extend!

---
