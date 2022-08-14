Default: build run

build:
	python -m pip install .

run:
	python .

clean:
	python -m pip uninstall -y universidad && rm -rf __pycache__ build universidad.egg-info universidad/__pycache__
