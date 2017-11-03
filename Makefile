.PHONY: dev

# Execute the pipenv shell before executing dev
dev:
		 flask run -h 0.0.0.0 -p 8080
