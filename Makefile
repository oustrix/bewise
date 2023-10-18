deps:
	pip-compile requirements.in
	pip-compile dev-requirements.in
	pip-sync requirements.txt dev-requirements.txt

lint:
	flake8 src

migrate:
	alembic upgrade head

image:
	docker build -t bewise .
