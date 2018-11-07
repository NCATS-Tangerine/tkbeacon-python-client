specification = api1.3.0.yaml

dev-install:
	pip install -e .

install:
	python setup.py install

generate:
	wget --no-clobber http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O swagger-codegen-cli.jar 2> /dev/null || echo "swagger-codegen-cli.jar already exists, did not download"
	java -jar swagger-codegen-cli.jar generate -i $(specification) -l python -o . -DpackageName=tkbeacon

release:
	pip install twine
	rm -rf dist/
	rm -rf build/
	python setup.py sdist bdist_wheel
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
