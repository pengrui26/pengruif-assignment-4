# Makefile

install:
	# Install backend and frontend dependencies
	pip install -r requirements.txt
	cd frontend && npm install

run:
	# Run backend
	(cd backend && python app.py &) \
	sleep 40 && \
	# Run frontend
	(cd frontend && npm start &)
