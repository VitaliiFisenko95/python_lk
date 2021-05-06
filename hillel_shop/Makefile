IMAGE ?= app:develop

.EXPORT_ALL_VARIABLES:

.default: run

run: COMPOSE ?= docker-compose -f compose-base.yaml -f compose-dev.yaml
run: docker-build
	$(COMPOSE) up -d


logs: COMPOSE ?= docker-compose -f compose-base.yaml -f compose-dev.yaml
logs:
	$(COMPOSE) logs -f api


docker-build:
	docker build -t $(IMAGE) .

mm:
mm:
	alembic revision --autogenerate


migrate:
migrate:
	alembic upgrade heads
