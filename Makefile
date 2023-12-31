install:
	npm i -g mintlify
	npm i @mintlify/scraping

start:
	mintlify dev

update-api:
	python3 convert.py
	npx @mintlify/scraping openapi-file openapi.json -o api-reference
