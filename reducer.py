import sys


def reduce_transaction_data():
    current_user = None
    fraud_count = 0
    total_amount = 0.0
    fraud_transactions = []
    
    # Read the key-value pairs from standard input (Hadoop or Spark streams)
    for line in sys.stdin:
        # Split the line into fields (each field is separated by tab)
        fields = line.strip().split('\t')
        
        if len(fields) != 13:  # Ensure the correct number of fields are present
            continue
        
        user_id, card_id, year, month, day, time, amount, use_chip, merchant_name, merchant_city, merchant_state, zip_code, mcc, is_fraud = fields
        
        # Convert amount to float
        try:
            amount = float(amount)
        except ValueError:
            amount = 0.0  # If the amount can't be parsed, set it to 0.0
        
  
        if current_user == user_id:
            total_amount += amount
            if is_fraud == 'Yes':
                fraud_count += 1
                fraud_transactions.append((user_id, card_id, amount, merchant_name, merchant_state))
        else:
        
            if current_user:
                print(f"{current_user}\tTotal Amount: {total_amount}\tFraud Count: {fraud_count}")
                print(f"Fraud Transactions for {current_user}: {fraud_transactions}")
            
        
            current_user = user_id
            total_amount = amount
            fraud_count = 1 if is_fraud == 'Yes' else 0
            fraud_transactions = [(user_id, card_id, amount, merchant_name, merchant_state)] if is_fraud == 'Yes' else []
    
  
    if current_user:
        print(f"{current_user}\tTotal Amount: {total_amount}\tFraud Count: {fraud_count}")
        print(f"Fraud Transactions for {current_user}: {fraud_transactions}")

if __name__ == "__main__":
    reduce_transaction_data()
