init:
	python setup.py develop
	pip install -r requirements.txt

test: init
	coverage run `which testify` tests.unit

ci: test
	pep8 authoritarian > pep8.report
	pyflakes docs authoritarian tests setup.py > pyflakes.report
	coverage html

documentation:
	cd docs; make html
