
test:
	py.test -s --cov

cov:
	py.test -s --cov-report html --cov modelindex
