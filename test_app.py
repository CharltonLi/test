import streamlit as st
from st_supabase_connection import SupabaseConnection

# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# Perform query.
rows = conn.table("Product").select("*").execute()

# Print results.
for row in rows.data:
    st.write(f"Product type: {row['product_name']}")
