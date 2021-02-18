
test:
	py.test -s --cov modelindex

cov:
	py.test -s --cov-report html --cov modelindex
