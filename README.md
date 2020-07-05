# FastAPI Template

*Basic REST API template showcasing user creation and user endpoint*

[![codecov](https://codecov.io/gh/nymann/fastapi-template/branch/master/graph/badge.svg)](https://codecov.io/gh/nymann/fastapi-template)

### Tech stack
- [FastAPI](https://fastapi.tiangolo.com)
- [PostgreSQL](https://www.postgresql.org)
- [Gino](https://python-gino.org)
- [Docker](https://www.docker.com)


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

### Enable hooks
```
make hooks
```

### Contributing
Read [CONTRIBUTING.md](CONTRIBUTING.md)
