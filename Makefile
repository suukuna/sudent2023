.PHONY: setup
setup:
	@echo 'start installing'
	pip install pytest flake8
	pip install -r requirements.txt

.PHONY: testall
testall: setup
	flake8 --extend-ignore E203 \
         --exclude .git,__pycache__,docs/source/conf.py,old,build,dist,venv \
         --max-complexity 10 \
         --ignore=E501


.PHONY: tast.app
test.app:
	pytest .\\tests\\$(app)


.PHONY: run
run: testall
	@echo 'start application'
	uvicorn main:app --reload