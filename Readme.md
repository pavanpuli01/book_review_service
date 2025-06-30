#Step into your project folder
cd Desktop/book_review_service

# 1. #Step into your project folder
cd Desktop/book_review_service

# 2. Start and enable Redis
sudo systemctl enable redis-server
sudo systemctl start redis-server

# 3. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 4. Install Python dependencies
pip install -r requirements.txt

# 5. Run database migration
alembic upgrade head

# 6. Run the FastAPI app
uvicorn app.main:app --reload
✅ Once running, visit: http://localhost:8000/docs
