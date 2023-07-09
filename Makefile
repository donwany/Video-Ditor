release:
	rm -rf build dist
	python setup.py sdist bdist_wheel
	twine upload dist/*

lint:
	pylint --recursive=y cut background concat download watermark

install:
	pip install -e .

format:
	black *.py

sort:
	isort **/*.py -c -v

pre-release:
	python setup.py install

git-upload:
	git add . && git commit -m "first commit" && git push -u origin main