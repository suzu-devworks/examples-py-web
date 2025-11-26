# examples-flask-quickstart

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
#examples-py-web
pdm init --no-git -n
pdm add -d flake8 mypy black isort pytest-cov pyclean

# examples-flask-quickstart
mkdir -p packages/examples-flask-quickstart
cd packages/examples-flask-quickstart
pdm init --no-git --dist -n
pdm add flask

rm pdm.lock
cd ../../

pdm add -d -e packages/examples-flask-quickstart
```

## References

- [クイックスタート &#8212; Flask Documentation (2.2.x)](https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/quickstart.html)
