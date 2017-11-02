.PHONY: dev

dev:
		pipenv run flask run -h 0.0.0.0 -p 9000
