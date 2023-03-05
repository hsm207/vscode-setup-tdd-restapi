test:
	pytest --cov=. --cov-report=term-missing tests/

format:
	black .