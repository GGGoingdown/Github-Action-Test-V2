# CHANGELOG



## v1.0.0-rc.1 (2024-06-06)

### Breaking

* feat: Refactor item and user query endpoints

BREAKING CHANGE: `extends` key in config file is now used for extending other config files

- Remove deprecated item and user query endpoints from `src/api.py` to improve API performance and maintainability. ([`b9d82d9`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/b9d82d964fde7341e88167cb317a19a55f054c98))

* feat!: remove some apis ([`be83516`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/be835167759d1ae778e1f4b9e342f48c3bdcc24a))

### Build

* build: Enhance CI/CD with Docker and notifications

- Introduce a new GitHub Actions workflow for Docker image automation, improving the build and deployment process.
- Extend automation to include Docker authentication and image tagging to streamline releases.
- Implement notification integration by configuring status updates to a Telegram chat group, enhancing communication and tracking of build statuses. ([`ccacefd`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/ccacefd33ec7f374dd3ca82d7232b3f8b692fdeb))

### Ci

* ci: Implement semantic release workflow

- Introduce a new GitHub Actions workflow to automate semantic releases.
- Automatically trigger releases when changes are merged into the master branch. ([`e9dc050`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/e9dc050e9c6b771c088a7afb30b540353a92a4dd))

### Feature

* feat: Standardize project version to 3.0.0

- Revert project version to `3.0.0` across all configuration and initiation files.
- Ensure version consistency after reverting across `src/__init__.py`, `.version`, and `pyproject.toml`. ([`36ce814`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/36ce814310fba2202bc6d04bce1e2bb57b68bca1))

* feat: Configure semantic release for 6.x.x branch

- Introduce new semantic release configuration for automated version management on the 6.x.x branch.
- Ensure compatibility and future maintainability with updates to project dependencies and configurations. ([`a7132fe`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/a7132fe915305457c26e539585beb78c08679fb0))

* feat: Update README for project version bump to 5

- Update README.md to reflect changes for version 5 upgrade
- Review files with extensive changes for detailed evaluation ([`f3d1057`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/f3d1057d90dee06c6e2c37aefa1f947444fde02d))

* feat: Bump project version to 4.0.0

- Upgrade the system-wide version to `4.0.0` across multiple files.
- Align software versioning consistently to `4.0.0` in preparation for the new major release. ([`abb7384`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/abb738444f2508d8267a33d7407dce5cd0a95992))

* feat: Standardize GitHub Action security tokens

- Update GitHub Actions release job to use the `GITHUB_TOKEN` for improved security and compliance.
- Ensure alignment with GitHub&#39;s best practices by modifying the token variable name in the workflow configuration. ([`c62abcb`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/c62abcb35efad3aabbdcbc056036d3c95a66d76b))

* feat: version 3.0.0 release updates

- Increment the project version to `3.0.0` to reflect major changes.
- Introduce a new `.version` file to maintain the version separately. ([`22c7b78`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/22c7b78e708fd122066b756b1fe843bc9098293e))

* feat: update github workflows to outputs ([`8a7aed1`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/8a7aed1a6312a0fff0abda49a4e03b677b93bc79))

* feat: update github workflows ([`5d45566`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/5d45566960351700fa796db95db246784be610b7))

* feat(api): create output ([`beab09f`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/beab09f72bcbcc7ee20e4ff831e6489dd13452b2))

* feat(api): create output ([`0d0aa20`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/0d0aa20ed53763a0c8375f33dccc7d629ec54fa6))

* feat(api): update github actions ([`7fdac3c`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/7fdac3c9b0a75b18d330beddcc30f17c0a68142f))

* feat(api): update github actions ([`3340f4b`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/3340f4bf82e51870173ca7cf75a0cc8c8c309d1f))

* feat(api): update api ([`354a1a5`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/354a1a52672a689b2b39a2e43b7e6920f0c793df))

* feat(api): update api ([`4b41eb8`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/4b41eb871cbbf799a006f666c686d53de552e099))

* feat: use workflow_dispatch ([`0afe65b`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/0afe65b4ba56b3a0e17ab4401dcf025c671e92de))

* feat: push.tags.* ([`279772a`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/279772a7bc0b80c7dc407940921513115de7cbf6))

* feat: trigger on master branch ([`42b315c`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/42b315c07a017b55310956d43d9c6348252d09d9))

* feat: create tag ([`9efb7ec`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/9efb7eccfdce8c6508951d7e41faafb0be000c5f))

* feat: update version ([`73a44a3`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/73a44a39746e3f2fc3f89da5b1a67e93c2a48327))

* feat: updatge trigger condition from tag to release ([`6567418`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/656741877a639f7422e4ecb0281f90c035ce8717))

* feat: Enhance API and refine CI trigger conditions

- Introduce a new API endpoint to manage an expanded item hierarchy level in `src/api.py`.
- Modify GitHub Actions in `.github/workflows/build.yaml` to trigger builds exclusively on tagged commits prefixed with &#39;v&#39;. ([`790bc2f`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/790bc2f20c0244d13accde72dad18d719bbc6936))

* feat: Add cross-user item read API endpoint

- Introduce new API endpoint in `src/api.py` for reading user items with cross-user context capabilities.
- Ensure changes are scalable and maintain current security protocols.
- Optimize API performance to handle increased query loads efficiently. ([`3e4dbf9`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/3e4dbf963b6f4b0ac8f302f9c9cbd9b8874d5e33))

* feat(API): Introduce user-context item fetch API endpoint

- Add a new API endpoint to handle fetching an item in relation to both a user and another item.
- Ensure the new endpoint integrates seamlessly with existing system architecture and user permissions. ([`9360ee0`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/9360ee07864f2ba0f742c9597bb813ec21df59ab))

* feat(api): Refactor API routing using FastAPI in src

- Introduce a new `src/api.py` file to centralize API endpoint implementations using FastAPI.
- Replace multiple route handlers in `src/main.py` with a single router inclusion from `src/api.py` to streamline the application structure. ([`9504d7c`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/9504d7c03311c15b76b449beef05b0d318b4afe9))

* feat(api): add get users by id endpoint ([`dc6902c`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/dc6902ccbcd9bcb92df39faf534e68bb8c90626c))

* feat(api): app users me endpoint ([`50fb030`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/50fb030e94110bf0deec8b8d2703c3b7de2c1db0))

### Fix

* fix(api): get output release ([`ad03bd8`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/ad03bd80580cdae156a650df124d95044dae5bb0))

* fix(api): update github token to PAT ([`46bc495`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/46bc49545a9c593fce4dbe540202a60e736a986c))

* fix(api): update trigger condition ([`6995e68`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/6995e684fb4d0319d9651e788f5c1e5dd54096a4))

* fix(api): update api ([`d14406f`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/d14406f63bf0330c3820c5d1ad295295900a8ccc))

* fix: Enhance debugging in read_item function

- Review added debug statement for clarity in the `read_item` function of `src/main.py` to track `item_id` processing.
- Ensure newly introduced debug code does not affect existing functionalities and complies with performance standards. ([`e44bdc1`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/e44bdc1abf6417a2ffeed2f7170c69bd2c0984be))

### Refactor

* refactor: Refine versioning strategy for refactor commits

- Update semantic release configuration in `pyproject.toml` to classify &#39;refactor&#39; commits as minor version bumps.
- Ensure some file changes are too extensive, resulting in their omission from the diff summary. ([`9dfdc8d`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/9dfdc8d3aeefd34bf126e5133463affea6f1b375))

### Unknown

* Expand semantic release support for 6.* branches

- Update release workflow to support `6.*` branches ([`d3dafc4`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/d3dafc468925e6931dcd27c46395fb17e3f5e48f))

* Update .version ([`4afaab1`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/4afaab12794c65f41601b115f17f6813fee601b1))

* Refine GitHub Actions release workflow

- Simplify syntax in GitHub Actions release workflow.
- Ensure consistency and efficiency in CI/CD processes. ([`e54b532`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/e54b532ab5298c7c4eb156b5c4dd2b5a7ea68163))

* Refine GitHub action triggers for releases

- Update GitHub Actions workflow to trigger tasks only for new releases.
- Ensure resource optimization by avoiding unnecessary workflow runs.
- Improve the efficiency of deployment processes. ([`e2272c5`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/e2272c56d7b1944fe34085ade50e94fa6c2ef77f))

* Refine post-release workflow conditions

- Update GitHub Actions workflow to only perform post-release tasks when `no_release` is specified.
- Ensure modifications align with the current release strategy to avoid unintended deployments. ([`b5296f0`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/b5296f066454ef89d187845a394fb60882bfa30f))

* Enhance README with updated sections

- Update README.md to include new sections detailing recent changes and updates.
- Ensure documentation reflects the latest project status and functionalities. ([`0f7b61f`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/0f7b61f5462b004de2fd192f29ae65937acb753b))

* Standardize module naming conventions

- Update module naming in changelog from &#39;api&#39; to &#39;apis&#39; for consistency and clarity. ([`242f4ee`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/242f4ee2b15a531dceb5f116d541b5bbdef42163))

* feat :Refine project configuration settings

- Update the file path for version variables in semantic_release configuration to ensure correct versioning.
- Review extensive changes in several large files for which detailed diffs were not provided. ([`1ea049b`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/1ea049bffbbe322c5cacfabee2bfef0c3f27feeb))

* Refine project configuration settings

- Update the version formatting in `pyproject.toml` to adhere to standards.
- Improve code readability and maintainability across various modules.
- Enhance performance by optimizing key functions and algorithms.
- Address and fix reported bugs to improve software stability. ([`651640a`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/651640a97c694ca8aefd590fe2689bd1e593163c))

* Optimize workflow triggers and cleanup steps

- Update the build workflow trigger in `.github/workflows/build.yaml` to activate on any tag push instead of waiting for `Semantic Release` completion.
- Simplify the workflow by removing conditions that check for a successful previous `workflow_run`.
- Eliminate redundant steps in the workflow related to acquiring the current git tag. ([`c87f33b`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/c87f33b06fd7cd275b509a9b8fd82c158571354d))

* Merge pull request #2 from GGGoingdown/develop

feat(api): Refactor API routing using FastAPI in src ([`e75f4ce`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/e75f4ce42efcd5c351526581efc9432a7331c880))

* Merge pull request #1 from GGGoingdown/develop

Develop ([`2b103fd`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/2b103fd0c9d43f8e699fbf446d6df9dfd02a981b))

* Introduce new utility functions in src/utils.py

- Add `src/utils.py` implementing a function for UTC datetime creation.
- Improve code modularity by separating common utilities. ([`d643ecb`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/d643ecb1bbb4804134a413b7caeba3225f75fa8a))

* Enhance endpoint flexibility in main.py

- Introduce a new API endpoint in `main.py` for item retrieval, supporting optional query parameters.
- Enhance functionality to improve user querying capabilities. ([`5a3be1d`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/5a3be1db3ff2897a0da9585f44e43929c469fe88))

* Add item details API endpoint in main.py

- Introduce a new API endpoint to provide detailed information on items.
- Enhance functionality in `main.py` to support the new feature. ([`293bb0c`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/293bb0c3c46fa387af048bf4ea8867d3907d824f))

* Initialize Github-Actions-Demo project setup

- Initialize the `Github-Actions-Demo` project structure with essential configuration and source files.
- Set up Python project dependencies, project metadata, and semantic release configurations in `pyproject.toml`.
- Create a basic FastAPI application in `src/main.py` with a greeting endpoint.
- Include a comprehensive `.gitignore` file suitable for Python projects integration. ([`4507c80`](https://github.com/GGGoingdown/Github-Action-Test-V2/commit/4507c806efd026257f680d2840ca4f18170c6a7f))
