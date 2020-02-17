specification = api1.3.0.yaml

dev-install:
	pip install -e .

install:
	python setup.py install

api-validation:
	./generate.sh validate

code-generation:
	./generate.sh client

client-installation:
	cd tkbeacon && python -m pip install -r requirements.txt . --no-cache-dir

.PHONY: client-tests

client-tests:
	cd tkbeacon && python -m pip install -r test-requirements.txt && nosetests

release:
	pip install twine
	rm -rf dist/
	rm -rf build/
	python setup.py sdist bdist_wheel
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
