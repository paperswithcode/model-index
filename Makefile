
test:
	py.test -s --cov modelindex

cov:
	py.test -s --cov-report html --cov modelindex

doc:
	cd docs && make html && open _build/html/index.html