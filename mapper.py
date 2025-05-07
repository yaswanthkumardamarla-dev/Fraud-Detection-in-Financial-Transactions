import sys
import csv



def map_transaction_data():
     
    for line in sys.stdin:
         
        fields = line.strip().split(',')

   
        try:
            user_id = fields[0]            # User ID
            card_id = fields[1]            # Card ID
            year = fields[2]               # Year of transaction
            month = fields[3]              # Month of transaction
            day = fields[4]                # Day of transaction
            time = fields[5]               # Time of transaction
            amount = fields[6].replace('$', '').replace(',', '')  # Transaction Amount (remove dollar signs and commas)
            use_chip = fields[7]           # Use of Chip (for example, "Swipe Transaction")
            merchant_name = fields[8]      # Merchant Name
            merchant_city = fields[9]      # Merchant City
            merchant_state = fields[10]    # Merchant State
            zip_code = fields[11]          # Zip code of merchant
            mcc = fields[12]               # Merchant Category Code
            is_fraud = fields[13]          # Fraud status (fraudulent or not)
            
            try:
                amount = float(amount)
            except ValueError:
                amount = 0.0  # If there is a parsing error, set the amount to 0.0

            print(f"{user_id}\t{card_id}\t{year}\t{month}\t{day}\t{time}\t{amount}\t{use_chip}\t{merchant_name}\t{merchant_city}\t{merchant_state}\t{zip_code}\t{mcc}\t{is_fraud}")
        
        except IndexError:
            # If the row has missing data, skip the row
            continue

if __name__ == "__main__":
    map_transaction_data()
