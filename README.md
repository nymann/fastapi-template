# FastAPI Template

*Basic REST API template showcasing user creation and user endpoint*

[![codecov](https://codecov.io/gh/nymann/fastapi-template/branch/master/graph/badge.svg)](https://codecov.io/gh/nymann/fastapi-template)

### Tech stack
- [FastAPI](https://fastapi.tiangolo.com)
- [PostgreSQL](https://www.postgresql.org)
- [Gino](https://python-gino.org)
- [Docker](https://www.docker.com)

### Design
This template is structued with loose coupling in mind. It's split into the
following modules.
```sh
.
├── asgi.py
├── core
│   ├── config_loader.py      # Loads the config from .env or environment vars.
│   ├── db.py                 # Contains the base instance of our Gino DB.
│   ├── __init__.py
│   ├── security.py           # Logic for hashing passwords and access tokens.
│   ├── service_factory.py    # How routers obtain a service.
│   └── version.py            # Where we keep our version number.
├── domain
│   ├── base_schemas.py       # Common pydantic schemas used by multiple routes.
│   └── users
│       ├── __init__.py
│       ├── user_model.py     # Database object relational mapping.
│       ├── user_queries.py   # Queries for user_model.
│       ├── user_schemas.py   # Pydantic schemas used for /users/.
│       └── user_services.py  # Logic for each endpoint is stored here.
├── __init__.py
└── routers
    ├── __init__.py
    └── users.py              # All endpoints for /users/.
```
##### Typical flow (create user)
1. Client sends a POST request to `/users/` (stored in `routers/users.py`)
2. Router validates the `user` payload in the request using Pydantic, if something in the request doesn't adhere to what's required it sends an error message.
3. Router calls the corresponding service in this case `service.create(user)` (stored in domain/users/user_services.py)
4. The service calls the corresponding `self._queries.create(user)` (stored in domain/users/user_queries.py) note that the result of this function call is transformed to the relevant schema here.
5. The `Queries` class tells the `Model` class to create a new user.

###### Why?
By seperating our API into differnet layers our router knows nothing about our
`Model` or `Queries` class, the only thing it knows about is what services it
can call. (I added type hints for schemas too though this is not strictly
necessary).
And our `Model` class knows nothing about our services or routers.

###### Why's that a benefit?
We could easily switch out a layer in our application with out it affecting the
other parts of the code. Fx. we could make a drastic change and switch out
FastAPI with Flask without rewriting the entire code base.


### Making it your own
The following requires [GNU Parallel](https://www.gnu.org/software/parallel/) (`yay -S parallel`).
```sh
#!/usr/bin/env sh

rename_to=${1:?"Specify what the project should be renamed to."}
rename_from=${2:-fastapi_template}

grep -rl ${rename_from} . | parallel sed -i "s#${rename_from}#${rename_to}#g" {}
mv src/${rename_from} src/${rename_to}
sudo rm -r .git
git init
echo "Empty git project initialized, run:"
echo "git remote add origin git@github.com:/YOUR_GROUP/YOUR_PROJECT.git"
echo "To setup your project."
```

### Enable pre-commit hooks
```
make hooks
```

Take a look in `.pre-commit-config.yaml` to add or remove hooks.


### Contributing
Read [CONTRIBUTING.md](CONTRIBUTING.md)

### Inspirations
[Slimovich's fastapi template](https://github.com/slimovich/Realworld-fastapi-gino-template)
I really liked his overall structure of the program.
