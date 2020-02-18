PYTHON=python3.7

dev-install:
	 ${PYTHON} -m pip install -e .

api-validation:
	./generate.sh validate

code-generation:
	./generate.sh client

installation:
	${PYTHON} -m pip install -r requirements.txt . --no-cache-dir

.PHONY: tests

tests:
	${PYTHON} -m pip install -r test-requirements.txt && pytest

make-distribution:
	${PYTHON} -m pip install wheel twine
	rm -rf dist/
	rm -rf build/
	${PYTHON} setup.py sdist bdist_wheel

test-release:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

release:
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
