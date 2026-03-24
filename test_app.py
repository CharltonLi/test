import streamlit as st
from st_supabase_connection import SupabaseConnection

st.write("1. Script started...")

# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

st.write("3. Connection object created. Fetching data...")

# Perform query.
rows = conn.table("Product").select("*").execute()

st.write("4. Data received!")

# Print results.
for row in rows.data:
    st.write(f"Product type: {row['product_name']}")
