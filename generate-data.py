import random
import pandas as pd
from faker import Faker

fake = Faker()

# Define some constants
NUM_DRIVERS = 100
NUM_RECORDS = 1000

# Define the possible locations and order statuses
locations = ['Algiers', 'Oran', 'Constantine', 'Batna', 'Biskra', 'Sétif', 'Annaba', 'Tlemcen', 'Béjaïa', 'Tizi Ouzou']
statuses = ['cancelled', 'pending', 'inactive', 'confirmed', 'paid']

# Create the dataframe
df = pd.DataFrame({
    'driver_id': [random.randint(1, NUM_DRIVERS) for _ in range(NUM_RECORDS)],
    'driver_location': [random.choice(locations) for _ in range(NUM_RECORDS)],
    'order_amount': [random.randint(200, 3000) for _ in range(NUM_RECORDS)],
    'order_status': [random.choice(statuses) for _ in range(NUM_RECORDS)]
})

# Save the dataframe as a CSV file
df.to_csv('sample_data.csv', index=False)
