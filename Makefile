Default: build run

build:
	python -m pip install .

run:
	python -m universidad

rm:
	python -m pip uninstall -y universidad && rm -rf build universidad.egg-info universidad/__pycache__