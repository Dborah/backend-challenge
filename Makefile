.PHONY: test install pep8 clean

test: pep8


install:
	# Install dependencies

migrations:
	flask db init
	flask db migrate -m "Created Meeting Room"
	flask db upgrade

dropdb:
	dropdb scheduling

create_db:
	createdb scheduling

run:
	flask run

clean:
	rm -rf migrations