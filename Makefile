# Makefile

install:
    pip install -r backend/requirements.txt
    cd frontend && npm install

run:
    # Run backend
    (cd backend && python app.py &) \
    # Run frontend
    && (cd frontend && npm start &)
