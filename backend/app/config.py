from sqlalchemy.engine import URL

class Config:
    SECRET_KEY = 'your-secret-key-here'  # Change this for production

    SQLALCHEMY_DATABASE_URI = URL.create(
        "mysql+mysqlconnector",  # or use "mysql+pymysql" if you're using PyMySQL
        username="root",
        password="Aa@123456",
        host="localhost",  # or your MySQL server address
        port=3306,
        database="TaskManager",  # Your MySQL database name
        query={
            "charset": "utf8mb4"
        }
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
