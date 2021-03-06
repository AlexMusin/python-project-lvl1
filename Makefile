install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-gcd:
	poetry run brain-gcd

brain-calc:
	poetry run brain-calc

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games


