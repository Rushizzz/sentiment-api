from sqlalchemy import create_engine, text

# 1. PASTE YOUR EXTERNAL URL INSIDE THE QUOTES BELOW
# (Make sure it starts with postgres://)
DATABASE_URL = "postgresql://sentiment_db_wrx2_user:M4lSHlUCpyBcacDJNBIARklOTDzoDl71@dpg-d5ie2i24d50c739l0av0-a.singapore-postgres.render.com/sentiment_db_wrx2"

# Fix for some systems requiring 'postgresql' instead of 'postgres'
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

try:
    # 2. Connect to the database
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()

    # 3. Run a simple SQL query
    print("Connecting to database...")
    result = connection.execute(text("SELECT * FROM predictions"))

    # 4. Print the results
    print("\n--- Prediction Logs ---")
    for row in result:
        # row[1] is text, row[2] is label, row[3] is score
        print(f"Input: {row[1]}")
        print(f"Result: {row[2]} ({row[3]:.4f})")
        print("-" * 20)

    connection.close()

except Exception as e:
    print(f"Error: {e}")
