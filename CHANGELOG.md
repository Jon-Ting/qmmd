# CHANGELOG


## v1.1.3 (2026-05-25)


## v1.1.2 (2026-05-25)

### Bug Fixes

- Add requirements for Sphinx
  ([`d62c07f`](https://github.com/Jon-Ting/qmmd/commit/d62c07ff64456312e62cd23d13f445c370b7f1ee))

- Correct import path for genExampleXYZs in example notebook
  ([`9e3b20b`](https://github.com/Jon-Ting/qmmd/commit/9e3b20bef749d21ea021225f9c4f9c08347e21d1))

- Ensure clean build directory before distribution
  ([`4dba26f`](https://github.com/Jon-Ting/qmmd/commit/4dba26f7f15590c8d68c48ee5139ea030947f619))


## v1.1.1 (2026-05-26)

### Chores

- Manual version bump to 1.1.1 for testing
  ([`49a43ab`](https://github.com/Jon-Ting/qmmd/commit/49a43ab6f1ada6ce2b216aa4309dd91171e310e1))


## v1.1.0 (2026-05-25)

### Build System

- Add environment variable for Node.js actions and install uv in CI workflow
  ([`237a5c5`](https://github.com/Jon-Ting/qmmd/commit/237a5c5fcde5b35b6043ba9f6eb3d63bde151a68))

- Add semantic release configuration for Sphinx and commit parser options
  ([`3a6de56`](https://github.com/Jon-Ting/qmmd/commit/3a6de56e1fb6b05cc87fc6bc404b35f279cab1df))

- Add step to test installation from TestPyPI before publishing to PyPI
  ([`5ac5cbf`](https://github.com/Jon-Ting/qmmd/commit/5ac5cbff58ab536b9c8e5d0d1c43f51f65660222))

- Replace Poetry by uv
  ([`32b5a87`](https://github.com/Jon-Ting/qmmd/commit/32b5a870aba7b721628c56f83de5f9d8074abdc7))

- Update CI/CD workflow to streamline package publishing process
  ([`4193654`](https://github.com/Jon-Ting/qmmd/commit/4193654e9ff182a492adfe8ebff9d1f079ea2772))

- Update CI/CD workflow to use latest actions and improve dependency management
  ([`a303b9f`](https://github.com/Jon-Ting/qmmd/commit/a303b9f1112c3c99a7f08ad615874ae51c7cf63b))

- Update dependencies and remove setup.py in favor of pyproject.toml
  ([`33700ae`](https://github.com/Jon-Ting/qmmd/commit/33700ae0df81904784d2790b88c7cba5660b330b))

- Update project metadata and CI configuration for improved package management
  ([`05f0fa5`](https://github.com/Jon-Ting/qmmd/commit/05f0fa546c7fa8d747f0774d7cf029edc237dbef))

- Update Read the Docs configuration for Python and OS versions
  ([`7f0a41d`](https://github.com/Jon-Ting/qmmd/commit/7f0a41d3a4d9ce1cd0cee96d0554cdf7908bc08c))

- **deps-dev**: Bump gitpython from 3.1.41 to 3.1.50
  ([`a9ac96b`](https://github.com/Jon-Ting/qmmd/commit/a9ac96b5cfec3fae9819e76b93aff17006592ad9))

Bumps [gitpython](https://github.com/gitpython-developers/GitPython) from 3.1.41 to 3.1.50. -
  [Release notes](https://github.com/gitpython-developers/GitPython/releases) -
  [Changelog](https://github.com/gitpython-developers/GitPython/blob/main/CHANGES) -
  [Commits](https://github.com/gitpython-developers/GitPython/compare/3.1.41...3.1.50)

--- updated-dependencies: - dependency-name: gitpython dependency-version: 3.1.50

dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump idna from 3.7 to 3.15
  ([`42d1e44`](https://github.com/Jon-Ting/qmmd/commit/42d1e44e548b376707c3d73617aee63a38a2004f))

Bumps [idna](https://github.com/kjd/idna) from 3.7 to 3.15. - [Release
  notes](https://github.com/kjd/idna/releases) -
  [Changelog](https://github.com/kjd/idna/blob/master/HISTORY.md) -
  [Commits](https://github.com/kjd/idna/compare/v3.7...v3.15)

--- updated-dependencies: - dependency-name: idna dependency-version: '3.15'

dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump jupyter-server from 2.11.2 to 2.18.0
  ([`41d6145`](https://github.com/Jon-Ting/qmmd/commit/41d6145746799fac6d9aca577e9719a73197ae2d))

Bumps [jupyter-server](https://github.com/jupyter-server/jupyter_server) from 2.11.2 to 2.18.0. -
  [Release notes](https://github.com/jupyter-server/jupyter_server/releases) -
  [Changelog](https://github.com/jupyter-server/jupyter_server/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/jupyter-server/jupyter_server/compare/v2.11.2...v2.18.0)

--- updated-dependencies: - dependency-name: jupyter-server dependency-version: 2.18.0

dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump mistune from 3.0.1 to 3.2.1
  ([`ea8a9b7`](https://github.com/Jon-Ting/qmmd/commit/ea8a9b769b4dd000f65e9a1306888d01b668911c))

Bumps [mistune](https://github.com/lepture/mistune) from 3.0.1 to 3.2.1. - [Release
  notes](https://github.com/lepture/mistune/releases) -
  [Changelog](https://github.com/lepture/mistune/blob/main/docs/changes.rst) -
  [Commits](https://github.com/lepture/mistune/compare/v3.0.1...v3.2.1)

--- updated-dependencies: - dependency-name: mistune dependency-version: 3.2.1

dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump nbconvert from 7.17.0 to 7.17.1
  ([`c7c7443`](https://github.com/Jon-Ting/qmmd/commit/c7c74438d4dd75ede1c86d9575c85e6924943f30))

Bumps [nbconvert](https://github.com/jupyter/nbconvert) from 7.17.0 to 7.17.1. - [Release
  notes](https://github.com/jupyter/nbconvert/releases) -
  [Changelog](https://github.com/jupyter/nbconvert/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/jupyter/nbconvert/compare/v7.17.0...v7.17.1)

--- updated-dependencies: - dependency-name: nbconvert dependency-version: 7.17.1

dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump nbconvert from 7.6.0 to 7.17.0
  ([`d89da38`](https://github.com/Jon-Ting/qmmd/commit/d89da388ab78c221e26ed4944691da13906a994c))

Bumps [nbconvert](https://github.com/jupyter/nbconvert) from 7.6.0 to 7.17.0. - [Release
  notes](https://github.com/jupyter/nbconvert/releases) -
  [Changelog](https://github.com/jupyter/nbconvert/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/jupyter/nbconvert/compare/v7.6.0...v7.17.0)

--- updated-dependencies: - dependency-name: nbconvert dependency-version: 7.17.0

dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump pygments from 2.15.1 to 2.20.0
  ([`dad1e88`](https://github.com/Jon-Ting/qmmd/commit/dad1e885d19d6877841b0d0fe31060bb9582e34f))

Bumps [pygments](https://github.com/pygments/pygments) from 2.15.1 to 2.20.0. - [Release
  notes](https://github.com/pygments/pygments/releases) -
  [Changelog](https://github.com/pygments/pygments/blob/master/CHANGES) -
  [Commits](https://github.com/pygments/pygments/compare/2.15.1...2.20.0)

--- updated-dependencies: - dependency-name: pygments dependency-version: 2.20.0

dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump tornado from 6.5.1 to 6.5.5
  ([`58dece7`](https://github.com/Jon-Ting/qmmd/commit/58dece797f0c2f9ba7e059b973e2774f7e582158))

Bumps [tornado](https://github.com/tornadoweb/tornado) from 6.5.1 to 6.5.5. -
  [Changelog](https://github.com/tornadoweb/tornado/blob/master/docs/releases.rst) -
  [Commits](https://github.com/tornadoweb/tornado/compare/v6.5.1...v6.5.5)

--- updated-dependencies: - dependency-name: tornado dependency-version: 6.5.5

dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump urllib3 from 2.5.0 to 2.6.3
  ([`645a28a`](https://github.com/Jon-Ting/qmmd/commit/645a28a1598a2865746002d63305e352f4cf25b9))

Bumps [urllib3](https://github.com/urllib3/urllib3) from 2.5.0 to 2.6.3. - [Release
  notes](https://github.com/urllib3/urllib3/releases) -
  [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst) -
  [Commits](https://github.com/urllib3/urllib3/compare/2.5.0...2.6.3)

--- updated-dependencies: - dependency-name: urllib3 dependency-version: 2.6.3

dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump wheel from 0.40.0 to 0.46.2
  ([`09884f7`](https://github.com/Jon-Ting/qmmd/commit/09884f7601e82177e17473b9764f337e7bcc5adc))

Bumps [wheel](https://github.com/pypa/wheel) from 0.40.0 to 0.46.2. - [Release
  notes](https://github.com/pypa/wheel/releases) -
  [Changelog](https://github.com/pypa/wheel/blob/main/docs/news.rst) -
  [Commits](https://github.com/pypa/wheel/compare/0.40.0...0.46.2)

--- updated-dependencies: - dependency-name: wheel dependency-version: 0.46.2

dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>

### Documentation

- Add instructions to facilitate AI assistance
  ([`d72b4b1`](https://github.com/Jon-Ting/qmmd/commit/d72b4b115f3724db7165c886ecf28c220d5cbcf9))

- Update credits and contact information in README
  ([`f2276e1`](https://github.com/Jon-Ting/qmmd/commit/f2276e1a4c91c2a9d5db835addf7f82e2f8b8905))

- Update Read the Docs configuration
  ([`20112f7`](https://github.com/Jon-Ting/qmmd/commit/20112f748974dd51d0ab8ca707a70470cfa7e058))

### Features

- Refactored monolithic scripts into reusable functions and classes
  ([`fe6f353`](https://github.com/Jon-Ting/qmmd/commit/fe6f353a4953ee05c295fa4d81ec23cb61f0fe31))

### Refactoring

- Rename package to QMMD
  ([`1b80a69`](https://github.com/Jon-Ting/qmmd/commit/1b80a69fa80445369dc40418fd36afcc64426b48))

### Testing

- Update tests
  ([`8ab72ad`](https://github.com/Jon-Ting/qmmd/commit/8ab72ad5dfd0581d92632985804c716bee8f4a62))


## v1.0.22 (2025-07-29)

### Build System

- **deps-dev**: Bump urllib3 from 2.2.2 to 2.5.0
  ([`d641a8c`](https://github.com/Jon-Ting/qmmd/commit/d641a8c928f657afd598abafc6ea6c20e3541d84))

Bumps [urllib3](https://github.com/urllib3/urllib3) from 2.2.2 to 2.5.0. - [Release
  notes](https://github.com/urllib3/urllib3/releases) -
  [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst) -
  [Commits](https://github.com/urllib3/urllib3/compare/2.2.2...2.5.0)

--- updated-dependencies: - dependency-name: urllib3 dependency-version: 2.5.0

dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.21 (2025-06-10)

### Build System

- **deps-dev**: Bump requests from 2.32.0 to 2.32.4
  ([`bafe411`](https://github.com/Jon-Ting/qmmd/commit/bafe4112bfa553c038efe67f61429d5a324da8f5))

Bumps [requests](https://github.com/psf/requests) from 2.32.0 to 2.32.4. - [Release
  notes](https://github.com/psf/requests/releases) -
  [Changelog](https://github.com/psf/requests/blob/main/HISTORY.md) -
  [Commits](https://github.com/psf/requests/compare/v2.32.0...v2.32.4)

--- updated-dependencies: - dependency-name: requests dependency-version: 2.32.4

dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.20 (2025-06-10)

### Build System

- **deps-dev**: Bump tornado from 6.4.2 to 6.5.1
  ([`2ac55d3`](https://github.com/Jon-Ting/qmmd/commit/2ac55d3c2e573f2edb7855e4035ca0ef67315b3b))

Bumps [tornado](https://github.com/tornadoweb/tornado) from 6.4.2 to 6.5.1. -
  [Changelog](https://github.com/tornadoweb/tornado/blob/master/docs/releases.rst) -
  [Commits](https://github.com/tornadoweb/tornado/compare/v6.4.2...v6.5.1)

--- updated-dependencies: - dependency-name: tornado dependency-version: 6.5.1

dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.19 (2025-05-20)

### Build System

- **deps-dev**: Bump setuptools from 70.0.0 to 78.1.1
  ([`4b45a10`](https://github.com/Jon-Ting/qmmd/commit/4b45a10eba72598c0a4ef34f8e3d6e74de0c83d5))

Bumps [setuptools](https://github.com/pypa/setuptools) from 70.0.0 to 78.1.1. - [Release
  notes](https://github.com/pypa/setuptools/releases) -
  [Changelog](https://github.com/pypa/setuptools/blob/main/NEWS.rst) -
  [Commits](https://github.com/pypa/setuptools/compare/v70.0.0...v78.1.1)

--- updated-dependencies: - dependency-name: setuptools dependency-version: 78.1.1

dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.18 (2025-04-01)

### Build System

- **deps-dev**: Bump jinja2 from 3.1.5 to 3.1.6
  ([`dad4370`](https://github.com/Jon-Ting/qmmd/commit/dad43706e7310cd5d1cb30277593f4ecff960313))

Bumps [jinja2](https://github.com/pallets/jinja) from 3.1.5 to 3.1.6. - [Release
  notes](https://github.com/pallets/jinja/releases) -
  [Changelog](https://github.com/pallets/jinja/blob/main/CHANGES.rst) -
  [Commits](https://github.com/pallets/jinja/compare/3.1.5...3.1.6)

--- updated-dependencies: - dependency-name: jinja2 dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.17 (2025-01-06)

### Build System

- **deps-dev**: Bump jinja2 from 3.1.4 to 3.1.5
  ([`9487ae7`](https://github.com/Jon-Ting/qmmd/commit/9487ae7a42d2df47bcc2f4cba400a8ed31980dcf))

Bumps [jinja2](https://github.com/pallets/jinja) from 3.1.4 to 3.1.5. - [Release
  notes](https://github.com/pallets/jinja/releases) -
  [Changelog](https://github.com/pallets/jinja/blob/main/CHANGES.rst) -
  [Commits](https://github.com/pallets/jinja/compare/3.1.4...3.1.5)

--- updated-dependencies: - dependency-name: jinja2 dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.16 (2024-11-22)

### Build System

- **deps-dev**: Bump tornado from 6.4.1 to 6.4.2
  ([`c89f08d`](https://github.com/Jon-Ting/qmmd/commit/c89f08de6de5f939e295010e5b7455dfc2f8cf47))

Bumps [tornado](https://github.com/tornadoweb/tornado) from 6.4.1 to 6.4.2. -
  [Changelog](https://github.com/tornadoweb/tornado/blob/v6.4.2/docs/releases.rst) -
  [Commits](https://github.com/tornadoweb/tornado/compare/v6.4.1...v6.4.2)

--- updated-dependencies: - dependency-name: tornado dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.15 (2024-10-07)

### Build System

- **deps-dev**: Bump cryptography from 42.0.4 to 43.0.1
  ([`b153ca5`](https://github.com/Jon-Ting/qmmd/commit/b153ca5bfdece7248275f85483aa09f30497b6c6))

Bumps [cryptography](https://github.com/pyca/cryptography) from 42.0.4 to 43.0.1. -
  [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pyca/cryptography/compare/42.0.4...43.0.1)

--- updated-dependencies: - dependency-name: cryptography dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.14 (2024-07-16)

### Build System

- **deps-dev**: Bump setuptools from 68.0.0 to 70.0.0
  ([`68814e7`](https://github.com/Jon-Ting/qmmd/commit/68814e7df3dab1ef7f24df0785df2159988eaa70))

Bumps [setuptools](https://github.com/pypa/setuptools) from 68.0.0 to 70.0.0. - [Release
  notes](https://github.com/pypa/setuptools/releases) -
  [Changelog](https://github.com/pypa/setuptools/blob/main/NEWS.rst) -
  [Commits](https://github.com/pypa/setuptools/compare/v68.0.0...v70.0.0)

--- updated-dependencies: - dependency-name: setuptools dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.13 (2024-07-10)

### Build System

- **deps-dev**: Bump zipp from 3.15.0 to 3.19.1
  ([`5f85adf`](https://github.com/Jon-Ting/qmmd/commit/5f85adf29afde9e2dfda6accd637642d2a85e374))

Bumps [zipp](https://github.com/jaraco/zipp) from 3.15.0 to 3.19.1. - [Release
  notes](https://github.com/jaraco/zipp/releases) -
  [Changelog](https://github.com/jaraco/zipp/blob/main/NEWS.rst) -
  [Commits](https://github.com/jaraco/zipp/compare/v3.15.0...v3.19.1)

--- updated-dependencies: - dependency-name: zipp dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.12 (2024-07-06)

### Build System

- **deps-dev**: Bump certifi from 2023.7.22 to 2024.7.4
  ([`9a3857c`](https://github.com/Jon-Ting/qmmd/commit/9a3857c8e3369ec632773ff78ad1617c06636a7d))

Bumps [certifi](https://github.com/certifi/python-certifi) from 2023.7.22 to 2024.7.4. -
  [Commits](https://github.com/certifi/python-certifi/compare/2023.07.22...2024.07.04)

--- updated-dependencies: - dependency-name: certifi dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.11 (2024-06-17)

### Build System

- **deps-dev**: Bump urllib3 from 2.0.7 to 2.2.2
  ([`cc5f9b2`](https://github.com/Jon-Ting/qmmd/commit/cc5f9b2a1d7001eede8b628d53a95ad8d5493533))

Bumps [urllib3](https://github.com/urllib3/urllib3) from 2.0.7 to 2.2.2. - [Release
  notes](https://github.com/urllib3/urllib3/releases) -
  [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst) -
  [Commits](https://github.com/urllib3/urllib3/compare/2.0.7...2.2.2)

--- updated-dependencies: - dependency-name: urllib3 dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.10 (2024-06-07)

### Build System

- **deps-dev**: Bump tornado from 6.3.3 to 6.4.1
  ([`d67b8b9`](https://github.com/Jon-Ting/qmmd/commit/d67b8b9491453c825ba76a7c8b9e08682156cf2d))

Bumps [tornado](https://github.com/tornadoweb/tornado) from 6.3.3 to 6.4.1. -
  [Changelog](https://github.com/tornadoweb/tornado/blob/master/docs/releases.rst) -
  [Commits](https://github.com/tornadoweb/tornado/compare/v6.3.3...v6.4.1)

--- updated-dependencies: - dependency-name: tornado dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.9 (2024-05-21)


## v1.0.8 (2024-05-07)

### Build System

- **deps-dev**: Bump jinja2 from 3.1.3 to 3.1.4
  ([`4bc8e1c`](https://github.com/Jon-Ting/qmmd/commit/4bc8e1c4827ed071eb2a17381a424bb7d9d297da))

Bumps [jinja2](https://github.com/pallets/jinja) from 3.1.3 to 3.1.4. - [Release
  notes](https://github.com/pallets/jinja/releases) -
  [Changelog](https://github.com/pallets/jinja/blob/main/CHANGES.rst) -
  [Commits](https://github.com/pallets/jinja/compare/3.1.3...3.1.4)

--- updated-dependencies: - dependency-name: jinja2 dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.7 (2024-05-03)

### Build System

- **deps-dev**: Bump tqdm from 4.65.0 to 4.66.3
  ([`a128575`](https://github.com/Jon-Ting/qmmd/commit/a128575dfe5f0a50988c0890b987fd2ee04edb20))

Bumps [tqdm](https://github.com/tqdm/tqdm) from 4.65.0 to 4.66.3. - [Release
  notes](https://github.com/tqdm/tqdm/releases) -
  [Commits](https://github.com/tqdm/tqdm/compare/v4.65.0...v4.66.3)

--- updated-dependencies: - dependency-name: tqdm dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.6 (2024-04-12)

### Build System

- **deps-dev**: Bump idna from 3.4 to 3.7
  ([`1c2ca89`](https://github.com/Jon-Ting/qmmd/commit/1c2ca896e43f62b2a8607c7099600b326b2cefdf))

Bumps [idna](https://github.com/kjd/idna) from 3.4 to 3.7. - [Release
  notes](https://github.com/kjd/idna/releases) -
  [Changelog](https://github.com/kjd/idna/blob/master/HISTORY.rst) -
  [Commits](https://github.com/kjd/idna/compare/v3.4...v3.7)

--- updated-dependencies: - dependency-name: idna dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.5 (2024-04-08)

### Build System

- **deps**: Bump pillow from 10.2.0 to 10.3.0
  ([`6df120a`](https://github.com/Jon-Ting/qmmd/commit/6df120a687a42abd0f66259742661a90660e493d))

Bumps [pillow](https://github.com/python-pillow/Pillow) from 10.2.0 to 10.3.0. - [Release
  notes](https://github.com/python-pillow/Pillow/releases) -
  [Changelog](https://github.com/python-pillow/Pillow/blob/main/CHANGES.rst) -
  [Commits](https://github.com/python-pillow/Pillow/compare/10.2.0...10.3.0)

--- updated-dependencies: - dependency-name: pillow dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.4 (2024-02-21)

### Build System

- **deps-dev**: Bump cryptography from 42.0.2 to 42.0.4
  ([`3ed2030`](https://github.com/Jon-Ting/qmmd/commit/3ed2030c52d2e459157dc79f7725a6eb51950444))

Bumps [cryptography](https://github.com/pyca/cryptography) from 42.0.2 to 42.0.4. -
  [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pyca/cryptography/compare/42.0.2...42.0.4)

--- updated-dependencies: - dependency-name: cryptography dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.3 (2024-02-17)

### Build System

- **deps-dev**: Bump cryptography from 42.0.0 to 42.0.2
  ([`5059f06`](https://github.com/Jon-Ting/qmmd/commit/5059f06ab21a0ba7d1304dfceb1d13530cc541be))

Bumps [cryptography](https://github.com/pyca/cryptography) from 42.0.0 to 42.0.2. -
  [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pyca/cryptography/compare/42.0.0...42.0.2)

--- updated-dependencies: - dependency-name: cryptography dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v1.0.2 (2024-02-06)

### Documentation

- **readme**: Updated readme
  ([`d9d6218`](https://github.com/Jon-Ting/qmmd/commit/d9d6218b9dd003b86886d678a948545a0ad192f0))


## v1.0.1 (2024-02-06)

### Bug Fixes

- **BTK**: Explained abbreviation
  ([`8f119f6`](https://github.com/Jon-Ting/qmmd/commit/8f119f6c20085da23b418900657a5a614582e853))

BREAKING CHANGE: testing python-semantic-release.

### BREAKING CHANGES

- **BTK**: Testing python-semantic-release.


## v0.4.15 (2024-02-06)

### Build System

- **deps-dev**: Bump cryptography from 41.0.6 to 42.0.0
  ([`7433f42`](https://github.com/Jon-Ting/qmmd/commit/7433f42c21279a56866b39e234e86b7b0202c27c))

Bumps [cryptography](https://github.com/pyca/cryptography) from 41.0.6 to 42.0.0. -
  [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pyca/cryptography/compare/41.0.6...42.0.0)

--- updated-dependencies: - dependency-name: cryptography dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.4.14 (2024-02-05)


## v0.4.13 (2024-01-23)

### Build System

- **deps**: Bump pillow from 10.0.1 to 10.2.0
  ([`ff093b9`](https://github.com/Jon-Ting/qmmd/commit/ff093b9e60314e2a7689be66b79dd9ee8304f26d))

Bumps [pillow](https://github.com/python-pillow/Pillow) from 10.0.1 to 10.2.0. - [Release
  notes](https://github.com/python-pillow/Pillow/releases) -
  [Changelog](https://github.com/python-pillow/Pillow/blob/main/CHANGES.rst) -
  [Commits](https://github.com/python-pillow/Pillow/compare/10.0.1...10.2.0)

--- updated-dependencies: - dependency-name: pillow dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.4.12 (2024-01-11)

### Build System

- **deps-dev**: Bump gitpython from 3.1.37 to 3.1.41
  ([`a272c38`](https://github.com/Jon-Ting/qmmd/commit/a272c38205958dfa69e1676d5d7973ff942d3b34))

Bumps [gitpython](https://github.com/gitpython-developers/GitPython) from 3.1.37 to 3.1.41. -
  [Release notes](https://github.com/gitpython-developers/GitPython/releases) -
  [Changelog](https://github.com/gitpython-developers/GitPython/blob/main/CHANGES) -
  [Commits](https://github.com/gitpython-developers/GitPython/compare/3.1.37...3.1.41)

--- updated-dependencies: - dependency-name: gitpython dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump jinja2 from 3.1.2 to 3.1.3
  ([`0a8290e`](https://github.com/Jon-Ting/qmmd/commit/0a8290ebbd1091ee237c6ff056b732fda885ec21))

Bumps [jinja2](https://github.com/pallets/jinja) from 3.1.2 to 3.1.3. - [Release
  notes](https://github.com/pallets/jinja/releases) -
  [Changelog](https://github.com/pallets/jinja/blob/main/CHANGES.rst) -
  [Commits](https://github.com/pallets/jinja/compare/3.1.2...3.1.3)

--- updated-dependencies: - dependency-name: jinja2 dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.4.11 (2024-01-10)

### Build System

- **deps**: Bump fonttools from 4.40.0 to 4.43.0
  ([`5fa6689`](https://github.com/Jon-Ting/qmmd/commit/5fa6689924b95a52cb4d7b8e01ffc10b6f88c519))

Bumps [fonttools](https://github.com/fonttools/fonttools) from 4.40.0 to 4.43.0. - [Release
  notes](https://github.com/fonttools/fonttools/releases) -
  [Changelog](https://github.com/fonttools/fonttools/blob/main/NEWS.rst) -
  [Commits](https://github.com/fonttools/fonttools/compare/4.40.0...4.43.0)

--- updated-dependencies: - dependency-name: fonttools dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.4.10 (2023-12-13)

### Build System

- **deps-dev**: Bump cryptography from 41.0.4 to 41.0.6
  ([`c8f9260`](https://github.com/Jon-Ting/qmmd/commit/c8f926049cac68cb5704df5dd994bb3614bd27d8))

Bumps [cryptography](https://github.com/pyca/cryptography) from 41.0.4 to 41.0.6. -
  [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pyca/cryptography/compare/41.0.4...41.0.6)

--- updated-dependencies: - dependency-name: cryptography dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump jupyter-server from 2.7.2 to 2.11.2
  ([`75758a7`](https://github.com/Jon-Ting/qmmd/commit/75758a7396023226bb53de6d6a03b694233aa26e))

Bumps [jupyter-server](https://github.com/jupyter-server/jupyter_server) from 2.7.2 to 2.11.2. -
  [Release notes](https://github.com/jupyter-server/jupyter_server/releases) -
  [Changelog](https://github.com/jupyter-server/jupyter_server/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/jupyter-server/jupyter_server/compare/v2.7.2...v2.11.2)

--- updated-dependencies: - dependency-name: jupyter-server dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.4.9 (2023-11-01)

### Build System

- **deps-dev**: Bump gitpython from 3.1.35 to 3.1.37
  ([`fd24159`](https://github.com/Jon-Ting/qmmd/commit/fd24159806f74ae229417a008e4e54d095f4f54f))

Bumps [gitpython](https://github.com/gitpython-developers/GitPython) from 3.1.35 to 3.1.37. -
  [Release notes](https://github.com/gitpython-developers/GitPython/releases) -
  [Changelog](https://github.com/gitpython-developers/GitPython/blob/main/CHANGES) -
  [Commits](https://github.com/gitpython-developers/GitPython/compare/3.1.35...3.1.37)

--- updated-dependencies: - dependency-name: gitpython dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump urllib3 from 2.0.6 to 2.0.7
  ([`99eb713`](https://github.com/Jon-Ting/qmmd/commit/99eb713dd7cad95905e5b4ee11ec0f6e10be2364))

Bumps [urllib3](https://github.com/urllib3/urllib3) from 2.0.6 to 2.0.7. - [Release
  notes](https://github.com/urllib3/urllib3/releases) -
  [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst) -
  [Commits](https://github.com/urllib3/urllib3/compare/2.0.6...2.0.7)

--- updated-dependencies: - dependency-name: urllib3 dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.4.8 (2023-10-05)

### Build System

- **deps**: Bump pillow from 9.5.0 to 10.0.1
  ([`63be31b`](https://github.com/Jon-Ting/qmmd/commit/63be31b340fa385d7c8b8eed8372b169d1715091))

Bumps [pillow](https://github.com/python-pillow/Pillow) from 9.5.0 to 10.0.1. - [Release
  notes](https://github.com/python-pillow/Pillow/releases) -
  [Changelog](https://github.com/python-pillow/Pillow/blob/main/CHANGES.rst) -
  [Commits](https://github.com/python-pillow/Pillow/compare/9.5.0...10.0.1)

--- updated-dependencies: - dependency-name: pillow dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump urllib3 from 2.0.3 to 2.0.6
  ([`251863e`](https://github.com/Jon-Ting/qmmd/commit/251863eedb6f91ac0974c8842314544611f0578a))

Bumps [urllib3](https://github.com/urllib3/urllib3) from 2.0.3 to 2.0.6. - [Release
  notes](https://github.com/urllib3/urllib3/releases) -
  [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst) -
  [Commits](https://github.com/urllib3/urllib3/compare/2.0.3...2.0.6)

--- updated-dependencies: - dependency-name: urllib3 dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.4.7 (2023-09-22)

### Build System

- **deps-dev**: Bump gitpython from 3.1.32 to 3.1.35
  ([`4b49098`](https://github.com/Jon-Ting/qmmd/commit/4b4909861edc04b8377fddcdb7647af2f1531326))

Bumps [gitpython](https://github.com/gitpython-developers/GitPython) from 3.1.32 to 3.1.35. -
  [Release notes](https://github.com/gitpython-developers/GitPython/releases) -
  [Changelog](https://github.com/gitpython-developers/GitPython/blob/main/CHANGES) -
  [Commits](https://github.com/gitpython-developers/GitPython/compare/3.1.32...3.1.35)

--- updated-dependencies: - dependency-name: gitpython dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.4.6 (2023-09-22)

### Build System

- **deps-dev**: Bump cryptography from 41.0.3 to 41.0.4
  ([`fa1c3ac`](https://github.com/Jon-Ting/qmmd/commit/fa1c3ac82aa87c442b97513eb88c0a9d203dfa97))

Bumps [cryptography](https://github.com/pyca/cryptography) from 41.0.3 to 41.0.4. -
  [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pyca/cryptography/compare/41.0.3...41.0.4)

--- updated-dependencies: - dependency-name: cryptography dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump gitpython from 3.1.32 to 3.1.34
  ([`1ccb0ec`](https://github.com/Jon-Ting/qmmd/commit/1ccb0ec1a70ef1c86fcf41eb00e37ea45aa509f8))

Bumps [gitpython](https://github.com/gitpython-developers/GitPython) from 3.1.32 to 3.1.34. -
  [Release notes](https://github.com/gitpython-developers/GitPython/releases) -
  [Changelog](https://github.com/gitpython-developers/GitPython/blob/main/CHANGES) -
  [Commits](https://github.com/gitpython-developers/GitPython/compare/3.1.32...3.1.34)

--- updated-dependencies: - dependency-name: gitpython dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.4.5 (2023-09-05)

### Build System

- **deps-dev**: Bump jupyter-server from 2.6.0 to 2.7.2
  ([`923172d`](https://github.com/Jon-Ting/qmmd/commit/923172d4ed36932986e277991a76b61b92671ead))

Bumps [jupyter-server](https://github.com/jupyter-server/jupyter_server) from 2.6.0 to 2.7.2. -
  [Release notes](https://github.com/jupyter-server/jupyter_server/releases) -
  [Changelog](https://github.com/jupyter-server/jupyter_server/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/jupyter-server/jupyter_server/compare/v2.6.0...v2.7.2)

--- updated-dependencies: - dependency-name: jupyter-server dependency-type: indirect

...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.4.4 (2023-08-24)

### Build System

- **gitpython**: Resolved dependabot alert
  ([`39b5008`](https://github.com/Jon-Ting/qmmd/commit/39b5008e11145384d42619e0bbe7dd666228674d))

- **tornado**: Resolved dependabot alert
  ([`53cc294`](https://github.com/Jon-Ting/qmmd/commit/53cc294a73014084a0c56a1bbf669671917a8dc5))


## v0.4.3 (2023-08-17)

### Build System

- **readthedocs**: Resolved build.image deprecation issue
  ([`bfe1775`](https://github.com/Jon-Ting/qmmd/commit/bfe177529ac5d490276f0ceb062c2ef53680e81e))

### Documentation

- **__init__.py**: Fixed implicit name issue on readthedocs
  ([`544b5bf`](https://github.com/Jon-Ting/qmmd/commit/544b5bf59f539f49a7d24fbdd5b31a1d108cfc61))

- **example**: Updated example files
  ([`f0305a4`](https://github.com/Jon-Ting/qmmd/commit/f0305a4a41d28af6cfe8bc5dfd60a8e2dfe3d50c))


## v0.4.2 (2023-08-04)

### Build System

- **poetry.lock**: Resolved dependencies vulnerabilities
  ([`6ed7085`](https://github.com/Jon-Ting/qmmd/commit/6ed70851352c37a5077d4c734a5213c1356f7fb6))


## v0.4.1 (2023-07-08)


## v0.4.0 (2023-07-08)

### Documentation

- **example**: Updated examples
  ([`17c9eef`](https://github.com/Jon-Ting/qmmd/commit/17c9eefa9255a5569dd356e0daeb160381fa078f))

- **readme**: Updated example usage in readme
  ([`5edf801`](https://github.com/Jon-Ting/qmmd/commit/5edf8015371e30041ecdec021398898320a80842))

### Refactoring

- **constants**: Adjusted default values for GOVF in constants.py
  ([`deb5ce7`](https://github.com/Jon-Ting/qmmd/commit/deb5ce71408efe5c8ef9441d471be14620d6fad9))


## v0.3.1 (2023-07-08)

### Documentation

- **qmcalc**: Made qmcalc functions more verbose and adjusted default values
  ([`ac79de3`](https://github.com/Jon-Ting/qmmd/commit/ac79de331189bed1da7dfa9dc651a7fca745a14d))

### Features

- Updated example xyz files and added their Gaussian outputs
  ([`33671b8`](https://github.com/Jon-Ting/qmmd/commit/33671b8fb687af9d9efe1e2711c556ed9d4cced8))

### Refactoring

- **tabulate**: Renamed variables and functions in tabulate.py
  ([`8b61893`](https://github.com/Jon-Ting/qmmd/commit/8b61893690e1dc57b807594199d7a2ad2c0f0bbe))

### Testing

- Updated unit tests based on new qmcalc functions
  ([`fe65764`](https://github.com/Jon-Ting/qmmd/commit/fe657644648a9d8653f3d2addc6f3ca5b838c03f))


## v0.3.0 (2023-07-07)

### Build System

- Removed old staged-recipes/
  ([`a4011ae`](https://github.com/Jon-Ting/qmmd/commit/a4011aeca2fdc350caaf56e5ab5553d013e8da8b))

- **conda-forge**: Added new covdrugsim recipes
  ([`4f64c92`](https://github.com/Jon-Ting/qmmd/commit/4f64c928aadf28e1d9f8a4ea366e11e37e58309c))

### Documentation

- **prepGaussian**: Added docstrings to functions in prepGaussian.py
  ([`0661eb6`](https://github.com/Jon-Ting/qmmd/commit/0661eb63b9b1d22007003ec711d0be99482580b1))

### Features

- **import**: Allowed essential functions to be imported directly from package namespace
  ([`3ba99be`](https://github.com/Jon-Ting/qmmd/commit/3ba99be4dd55f8356060ef291733e0d333e4ec9d))

- **qmcalc**: Tidied up qmcalc functionalities
  ([`07d9e75`](https://github.com/Jon-Ting/qmmd/commit/07d9e756ac20ba42f8ba5b90ab05d20970d8684c))

### Refactoring

- Renamed variable names with underscores
  ([`8db8780`](https://github.com/Jon-Ting/qmmd/commit/8db8780b755e031675f16ff01f8cc77399b7bbae))

### Testing

- Added tests for qmcalc functionalities
  ([`1da9944`](https://github.com/Jon-Ting/qmmd/commit/1da9944b4a8d190e12bdcfac117c2db3837ad546))


## v0.2.0 (2023-07-05)

### Features

- **tabulate**: Renamed a function in tabulate.py
  ([`5e0c885`](https://github.com/Jon-Ting/qmmd/commit/5e0c8859e10071c38c6d3bb22b864ede56686739))

- **tabulate**: Renamed a function in tabulate.py
  ([`f608ca2`](https://github.com/Jon-Ting/qmmd/commit/f608ca2151e73a226e4a9634f8cc606ec166d3af))


## v0.1.0 (2023-07-05)

### Bug Fixes

- Initialised cleaning of source code
  ([`1cab90f`](https://github.com/Jon-Ting/qmmd/commit/1cab90f86eea9b3373f27e23adec2176637b68a6))

- Renamed imports
  ([`6622212`](https://github.com/Jon-Ting/qmmd/commit/66222124fdd2e24584f493bf32d7a40f358d8637))

### Build System

- Added dev dependencies
  ([`c7d19fe`](https://github.com/Jon-Ting/qmmd/commit/c7d19feeaddb0586e5b68ac84edae90c30f37fd7))

- Updated all build-related files
  ([`a151af1`](https://github.com/Jon-Ting/qmmd/commit/a151af1bed44cfc7ff966d181ffb9f19d1004b44))

- **ci-cd**: Updated ci-cd.yml
  ([`5ccf1ec`](https://github.com/Jon-Ting/qmmd/commit/5ccf1ec8b2ef6c6f020961ea75a1f80e2ea91d19))

### Documentation

- Created docstrings for unitConv()
  ([`3037c64`](https://github.com/Jon-Ting/qmmd/commit/3037c64e0ef69aa2d960fad1a5587f2eb14eda59))

- Updated readme and example
  ([`a1f88bf`](https://github.com/Jon-Ting/qmmd/commit/a1f88bf505c5fe0f3755ce5cf55c97ca11bfb0e9))

- **readme**: Updated readme
  ([`5869e60`](https://github.com/Jon-Ting/qmmd/commit/5869e60731a3429516398c9e8252652022b0f90c))

- **readme**: Updated readme
  ([`720b38c`](https://github.com/Jon-Ting/qmmd/commit/720b38c260b8e3753edf5a05f514acd5d7f7cff4))

### Features

- Attempt to fix PSR version problem
  ([`3607799`](https://github.com/Jon-Ting/qmmd/commit/36077992c1869d0e49eaa2a0ce5a30619921b896))

- **conda-forge**: Initialised publication to conda-forge
  ([`3c09d95`](https://github.com/Jon-Ting/qmmd/commit/3c09d95fc0c0158756e6d68a198180384188a84f))

### Refactoring

- Deleted redundant example files
  ([`e698fb3`](https://github.com/Jon-Ting/qmmd/commit/e698fb38a0ca92e38cfd607a8b66f90bafec348a))

### Testing

- Added unit test for E_unit_conv()
  ([`6e380be`](https://github.com/Jon-Ting/qmmd/commit/6e380be2d10b08788dd5651380f9229579697491))

- Updated tests/ directory
  ([`9e09974`](https://github.com/Jon-Ting/qmmd/commit/9e0997444d6d9bf0bb59c06e1f7947b07fe42b9f))
