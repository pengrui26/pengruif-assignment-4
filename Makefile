# Makefile

install:
	# Install backend and frontend dependencies
	pip install -r requirements.txt
	cd frontend && npm install

run:
	# Run backend in the background
	(cd backend && python app.py &)
	# Wait for 40 seconds before starting frontend
	sleep 40
	# Start frontend
	(cd frontend && npm start &)
