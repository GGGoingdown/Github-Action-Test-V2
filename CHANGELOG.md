# CHANGELOG



## v0.12.1 (2024-05-01)

### Fix

* fix(apis): update trigger condition ([`6995e68`](https://github.com/GGGoingdown/Github-Actions-Test/commit/6995e684fb4d0319d9651e788f5c1e5dd54096a4))


## v0.12.0 (2024-05-01)

### Feature

* feat(api): update api ([`4b41eb8`](https://github.com/GGGoingdown/Github-Actions-Test/commit/4b41eb871cbbf799a006f666c686d53de552e099))

* feat: use workflow_dispatch ([`0afe65b`](https://github.com/GGGoingdown/Github-Actions-Test/commit/0afe65b4ba56b3a0e17ab4401dcf025c671e92de))

### Fix

* fix(api): update api ([`d14406f`](https://github.com/GGGoingdown/Github-Actions-Test/commit/d14406f63bf0330c3820c5d1ad295295900a8ccc))


## v0.11.0 (2024-05-01)

### Feature

* feat: push.tags.* ([`279772a`](https://github.com/GGGoingdown/Github-Actions-Test/commit/279772a7bc0b80c7dc407940921513115de7cbf6))


## v0.10.0 (2024-05-01)

### Feature

* feat: trigger on master branch ([`42b315c`](https://github.com/GGGoingdown/Github-Actions-Test/commit/42b315c07a017b55310956d43d9c6348252d09d9))


## v0.9.0 (2024-05-01)

### Feature

* feat: create tag ([`9efb7ec`](https://github.com/GGGoingdown/Github-Actions-Test/commit/9efb7eccfdce8c6508951d7e41faafb0be000c5f))


## v0.8.0 (2024-05-01)

### Feature

* feat: update version ([`73a44a3`](https://github.com/GGGoingdown/Github-Actions-Test/commit/73a44a39746e3f2fc3f89da5b1a67e93c2a48327))


## v0.7.0 (2024-05-01)

### Feature

* feat: updatge trigger condition from tag to release ([`6567418`](https://github.com/GGGoingdown/Github-Actions-Test/commit/656741877a639f7422e4ecb0281f90c035ce8717))


## v0.6.0 (2024-05-01)

### Feature

* feat: Enhance API and refine CI trigger conditions

- Introduce a new API endpoint to manage an expanded item hierarchy level in `src/api.py`.
- Modify GitHub Actions in `.github/workflows/build.yaml` to trigger builds exclusively on tagged commits prefixed with &#39;v&#39;. ([`790bc2f`](https://github.com/GGGoingdown/Github-Actions-Test/commit/790bc2f20c0244d13accde72dad18d719bbc6936))

### Unknown

* feat :Refine project configuration settings

- Update the file path for version variables in semantic_release configuration to ensure correct versioning.
- Review extensive changes in several large files for which detailed diffs were not provided. ([`1ea049b`](https://github.com/GGGoingdown/Github-Actions-Test/commit/1ea049bffbbe322c5cacfabee2bfef0c3f27feeb))

* Refine project configuration settings

- Update the version formatting in `pyproject.toml` to adhere to standards.
- Improve code readability and maintainability across various modules.
- Enhance performance by optimizing key functions and algorithms.
- Address and fix reported bugs to improve software stability. ([`651640a`](https://github.com/GGGoingdown/Github-Actions-Test/commit/651640a97c694ca8aefd590fe2689bd1e593163c))


## v0.5.0 (2024-05-01)

### Feature

* feat: Add cross-user item read API endpoint

- Introduce new API endpoint in `src/api.py` for reading user items with cross-user context capabilities.
- Ensure changes are scalable and maintain current security protocols.
- Optimize API performance to handle increased query loads efficiently. ([`3e4dbf9`](https://github.com/GGGoingdown/Github-Actions-Test/commit/3e4dbf963b6f4b0ac8f302f9c9cbd9b8874d5e33))


## v0.4.0 (2024-05-01)

### Build

* build: Enhance CI/CD with Docker and notifications

- Introduce a new GitHub Actions workflow for Docker image automation, improving the build and deployment process.
- Extend automation to include Docker authentication and image tagging to streamline releases.
- Implement notification integration by configuring status updates to a Telegram chat group, enhancing communication and tracking of build statuses. ([`ccacefd`](https://github.com/GGGoingdown/Github-Actions-Test/commit/ccacefd33ec7f374dd3ca82d7232b3f8b692fdeb))

### Feature

* feat(API): Introduce user-context item fetch API endpoint

- Add a new API endpoint to handle fetching an item in relation to both a user and another item.
- Ensure the new endpoint integrates seamlessly with existing system architecture and user permissions. ([`9360ee0`](https://github.com/GGGoingdown/Github-Actions-Test/commit/9360ee07864f2ba0f742c9597bb813ec21df59ab))

### Unknown

* Optimize workflow triggers and cleanup steps

- Update the build workflow trigger in `.github/workflows/build.yaml` to activate on any tag push instead of waiting for `Semantic Release` completion.
- Simplify the workflow by removing conditions that check for a successful previous `workflow_run`.
- Eliminate redundant steps in the workflow related to acquiring the current git tag. ([`c87f33b`](https://github.com/GGGoingdown/Github-Actions-Test/commit/c87f33b06fd7cd275b509a9b8fd82c158571354d))


## v0.3.0 (2024-05-01)

### Refactor

* refactor: Refine versioning strategy for refactor commits

- Update semantic release configuration in `pyproject.toml` to classify &#39;refactor&#39; commits as minor version bumps.
- Ensure some file changes are too extensive, resulting in their omission from the diff summary. ([`9dfdc8d`](https://github.com/GGGoingdown/Github-Actions-Test/commit/9dfdc8d3aeefd34bf126e5133463affea6f1b375))


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
