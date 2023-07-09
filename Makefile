release:
	rm -rf build dist
	python setup.py sdist bdist_wheel
	twine upload dist/*

lint:
	pylint --recursive=y editor

install:
	pip install -e .

format:
	black *.py

sort:
	isort *.py

pre-release:
	python setup.py install