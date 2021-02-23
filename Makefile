
test:
	py.test -s --cov modelindex

cov:
	py.test -s --cov-report html --cov modelindex

doc:
	cd docs && make html && open _build/html/index.html

clean:
	rm -rf build
	rm -rf dist

build: clean               ## Build the source and wheel distribution packages.
	@python3 setup.py sdist bdist_wheel

release: build       ## Build and upload the package to PyPI.
	@twine upload --repository-url  https://upload.pypi.org/legacy/ dist/*
	@rm -fr build dist "model_index.egg-info"