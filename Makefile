SHELL := /bin/bash

env:
	cp -n .env.example .env || true

up: env
	docker compose up -d --build
	@echo "✔ Up at http://localhost:8000/docs"