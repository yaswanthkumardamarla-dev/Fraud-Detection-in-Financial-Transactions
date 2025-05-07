# Fraud-Detection-in-Financial-Transactions

# 📊 Final Results — Credit Card Fraud Detection Using Big Data

## 👥 Team Members
- **Yaswanth Kumar Damarla** (NetID: yd3034)
- **Bhagya Rekha Deenadayal** (NetID: bd2585)
- **Sai Spoorthi Tammineni** (NetID: st5294)

## 📝 Course Information
- **Course**: CSGY-6513-D Big Data  
- **Semester**: Spring 2025  
- **Project Title**: Fraud Detection in Financial Transactions  
- **GitHub**: [Fraud Detection Repository](https://github.com/yaswanthkumardamarla-dev/Fraud-Detection-in-Financial-Transactions)

---

## ✅ Final Results & Insights

### 1. Transaction Type Distribution
- **Swipe Transactions**: 63.09%  
- **Chip Transactions**: 25.78%  
- **Online Transactions**: 11.13%  

Swipe is the most common transaction method, emphasizing the need to prioritize fraud detection for physical card usage.

---

### 2. Monetary Volume by Transaction Type
- **Swipe**: \$0.652 billion  
- **Chip**: \$0.258 billion  
- **Online**: \$0.154 billion  

Swipe transactions not only dominate in count but also in total money, reinforcing their importance in fraud analysis.

---

### 3. Fraud Impact Analysis

#### 📉 Fraud in Total Transactions
- Fraud: 7.73%
- Non-Fraud: 92.27%

#### 💸 Fraud in Total Monetary Value
- Fraud: 8.49%
- Non-Fraud: 91.51%

Although fewer, fraudulent transactions account for higher average transaction values—making them more financially damaging.

---

### 4. 🌲 Random Forest Classifier Performance
- **Accuracy**: 0.9987  
- **F1 Score**: 0.9981  

Random Forest offers robust detection of both fraudulent and non-fraudulent transactions, with high confidence and low misclassification.

---

### 5. 📈 Logistic Regression Performance
- **Accuracy**: 0.9987  
- **F1 Score**: 0.9981  
- **AUC-ROC**: 0.7924

While LR performs similarly on surface metrics, its lower AUC-ROC score highlights inferior performance in identifying fraud probabilities.

---

## 🏆 Conclusion
Random Forest is the **preferred model** for credit card fraud detection due to:
- Better handling of feature interactions
- Higher AUC-ROC score (better fraud ranking)
- Resilience in imbalanced data environments

This model provides both high precision and recall, ensuring maximum fraud capture with minimal false positives.

---
