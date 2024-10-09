# Makefile

install:
	# Install backend and frontend dependencies
	pip install -r backend/requirements.txt
	cd frontend && npm install

run:
	# Run backend in the background
	(cd backend && python app.py &)
	# Wait for 60 seconds before starting frontend
	sleep 60
	# Start frontend
	(cd frontend && npm start &)
