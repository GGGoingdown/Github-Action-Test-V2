# CHANGELOG



## v0.2.0 (2024-05-01)

### Feature

* feat(api): Refactor API routing using FastAPI in src

- Introduce a new `src/api.py` file to centralize API endpoint implementations using FastAPI.
- Replace multiple route handlers in `src/main.py` with a single router inclusion from `src/api.py` to streamline the application structure. ([`9504d7c`](https://github.com/GGGoingdown/Github-Actions-Test/commit/9504d7c03311c15b76b449beef05b0d318b4afe9))

### Unknown

* Merge pull request #2 from GGGoingdown/develop

feat(api): Refactor API routing using FastAPI in src ([`e75f4ce`](https://github.com/GGGoingdown/Github-Actions-Test/commit/e75f4ce42efcd5c351526581efc9432a7331c880))


## v0.1.1 (2024-05-01)

### Fix

* fix: Enhance debugging in read_item function

- Review added debug statement for clarity in the `read_item` function of `src/main.py` to track `item_id` processing.
- Ensure newly introduced debug code does not affect existing functionalities and complies with performance standards. ([`e44bdc1`](https://github.com/GGGoingdown/Github-Actions-Test/commit/e44bdc1abf6417a2ffeed2f7170c69bd2c0984be))

### Unknown

* Merge pull request #1 from GGGoingdown/develop

Develop ([`2b103fd`](https://github.com/GGGoingdown/Github-Actions-Test/commit/2b103fd0c9d43f8e699fbf446d6df9dfd02a981b))

* Introduce new utility functions in src/utils.py

- Add `src/utils.py` implementing a function for UTC datetime creation.
- Improve code modularity by separating common utilities. ([`d643ecb`](https://github.com/GGGoingdown/Github-Actions-Test/commit/d643ecb1bbb4804134a413b7caeba3225f75fa8a))

* Enhance endpoint flexibility in main.py

- Introduce a new API endpoint in `main.py` for item retrieval, supporting optional query parameters.
- Enhance functionality to improve user querying capabilities. ([`5a3be1d`](https://github.com/GGGoingdown/Github-Actions-Test/commit/5a3be1db3ff2897a0da9585f44e43929c469fe88))


## v0.1.0 (2024-05-01)

### Ci

* ci: Implement semantic release workflow

- Introduce a new GitHub Actions workflow to automate semantic releases.
- Automatically trigger releases when changes are merged into the master branch. ([`e9dc050`](https://github.com/GGGoingdown/Github-Actions-Test/commit/e9dc050e9c6b771c088a7afb30b540353a92a4dd))

### Feature

* feat(api): add get users by id endpoint ([`dc6902c`](https://github.com/GGGoingdown/Github-Actions-Test/commit/dc6902ccbcd9bcb92df39faf534e68bb8c90626c))

* feat(api): app users me endpoint ([`50fb030`](https://github.com/GGGoingdown/Github-Actions-Test/commit/50fb030e94110bf0deec8b8d2703c3b7de2c1db0))

### Unknown

* Add item details API endpoint in main.py

- Introduce a new API endpoint to provide detailed information on items.
- Enhance functionality in `main.py` to support the new feature. ([`293bb0c`](https://github.com/GGGoingdown/Github-Actions-Test/commit/293bb0c3c46fa387af048bf4ea8867d3907d824f))

* Initialize Github-Actions-Demo project setup

- Initialize the `Github-Actions-Demo` project structure with essential configuration and source files.
- Set up Python project dependencies, project metadata, and semantic release configurations in `pyproject.toml`.
- Create a basic FastAPI application in `src/main.py` with a greeting endpoint.
- Include a comprehensive `.gitignore` file suitable for Python projects integration. ([`4507c80`](https://github.com/GGGoingdown/Github-Actions-Test/commit/4507c806efd026257f680d2840ca4f18170c6a7f))
