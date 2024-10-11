ENGLISH | [PORTUGUÊS](https://github.com/fazedordecodigo/PyFlunt/blob/main/docs/CONTRIBUTING.md)

# Contributing

Thank you for dedicating your time to contribute! 🙇‍♀️🙇‍♂️ All help is welcome!

- [First Contribution](#first-contribution)
- [Releasing a New Version](#releasing-a-new-version)

# First Contribution

How to make your first contribution:

- [1. Create a GitHub Account](#1-create-a-github-account)
- [2. Find an Issue to Work On](#2-find-an-issue-to-work-on)
- [3. Install Git](#3-install-git)
- [4. Fork the Project](#4-fork-the-project)
- [5. Clone Your Fork](#5-clone-your-fork)
- [6. Create a New Branch](#6-create-a-new-branch)
- [7. Run PyFlunt Locally](#7-run-pyflunt-locally)
- [8. Make Your Changes](#8-make-your-changes)
- [9. Test Your Changes](#9-test-your-changes)
- [10. Commit and Push Your Changes](#10-commit-and-push-your-changes)
- [11. Add Entries to CHANGELOG.md](#11-add-entries-to-changelogmd)
- [12. Create a PR on GitHub](#12-create-a-pr-on-github)
- [13. Update Your Branch if Necessary](#13-update-your-branch-if-necessary)

### 1. Create a GitHub Account

Make sure to have a [GitHub account][github-join] and be logged in.

### 2. Find an Issue to Work On

Visit the [PyFlunt issues page][pyflunt-issues] and find an issue you would like to work on that hasn't been assigned to anyone yet.

Leave a comment on the issue asking if you can work on it. Something like: "Hello, can I work on this issue?".

Wait until someone assigns the issue to you. Once assigned, you can proceed to the next step.

Feel free to ask any questions on the issue page before or during the development process.

When starting to contribute to the project, it's recommended to take one issue at a time. This helps ensure that other people also have the opportunity to collaborate and prevents resources from remaining inactive for too long.

### 3. Install Git

Make sure to have [Git installed][install-git].

### 4. Fork the Project

[Fork the brutils repository][github-forking].

### 5. Clone Your Fork

[Clone][github-cloning] your fork locally.

### 6. Create a New Branch

Navigate to the PyFlunt folder:

```bash
$ cd pyflunt
```

And create a new branch:

```bash
$ git checkout -b <issue_number>
```

### 7. Run PyFlunt Locally
## Installation
### Requirements

- [Python 3.9+][python]
- [Poetry][poetry]

Create a [virtualenv][virtualenv] for PyFlunt and activate it:

```shell
$ poetry shell
```

Install dependencies:

```shell
$ poetry install
$ poetry pre-commit-install
```

## Using Locally

Now you can use it [in the same way described in the README.md file](https://github.com/fazedordecodigo/PyFlunt/blob/main/README.md#utilization).

## Testing

```shell
$ poetry test
```

### 8. Make Your Changes

Now is the stage where you can implement your changes in the code.

It's important to note that we document our code using [docstrings][docstring-definition].
Modules, classes, functions, and methods should be documented. Your changes should also be well
documented and reflect updated docstrings, in case any parameters have been changed for a class/attribute or even functions.

All docstrings should be in English. Feel free to use Google Translate if
necessary. We will suggest changes in the translation if needed, so don't worry about possible
English errors.

We follow the pattern below to maintain consistency in docstrings:

```python
class Example:
    """Explain the purpose of the class

    Attributes:
    -----------
        x[dict]: Short explanation here
        y[type, optional]: Short explanation here

    Methods:
	-------
    - foobar(w): Short explanation here

    """

    def __init__(self, x, y=None):
        self.x = x
        self.y = y

    def foobar(self, w):
        """Purpose if the function

        Parameters
		----------
        `w`: str
            Short explanation here

        Returns:
        --------
        `value`: str
            Short explanation here

        Notes:
        ------
        - Describe conditions here

        Examples:
        ---------
        ```python
        obj = Example(1)
        obj.foobar(2)  >> Returns
        ```
        """
        ...
        return value

```

One thing to keep in mind when documenting code with docstrings is that you can ignore docstrings in
property decorators and magic methods.

### 9. Test Your Changes

#### Write New Tests

Make sure you have created the necessary tests for each new change you made.

#### Ensure All Tests Passed

Run all tests with `poetry test` and make sure they all pass.

**PRs will not be merged if there are any missing or failing tests.**

### 10. Commit and Push Your Changes

Commit your changes:

```bash
$ git commit -a -m "<commit_message>"
```

Push your commit to GitHub:

```bash
$ git push --set-upstream origin <issue_number>
```

Create as many changes/commits as you need and push them.

### 11. Add Entries to CHANGELOG.md

[Add an entry to CHANGELOG.md][keep-a-changelog].

### 12. Create a PR on GitHub

[Create a PR on GitHub][github-creating-a-pr].

### 13. Update Your Branch if Necessary

[Ensure your branch is updated with the main][github-sync-pr]

# Releasing a New Version

Here you will find how to release a new production version of brutils:

- [1. Create a Release Issue](#1-create-a-release-issue)
- [2. Create a Release PR](#2-create-a-release-pr)
- [3. Deploy via GitHub](#3-deploy-via-github)

### 1. Create a Release Issue

### Create the Issue

For the creation of the issue, you can use the feature template, with the name of the issue being `Release v<version>`. [Example](https://github.com/fazedordecodigo/pyflunt/issues/49)

### Create a Branch

The name of the branch created for the release is related to the number of the Issue, as shown in [this example](https://github.com/fazedordecodigo/pyflunt/pull/50)

### 2. Create a Release PR

#### Update the Library Version

Increment the version number, following the [Semantic Versioning][semantic-versioning],
in the `pyproject.toml` file:

- https://github.com/fazedordecodigo/pyflunt/blob/main/pyproject.toml#L3

#### Update the CHANGELOG.md

Add a title for the new version with the new number and the current date, as
[in this example](https://github.com/fazedordecodigo/pyflunt/blob

/main/CHANGELOG.md?plain=1#L9).

And add the version links, as [in this example](https://github.com/fazedordecodigo/pyflunt/blob/eac770e8b213532d2bb5948d117f6f4684f65be2/CHANGELOG.md?plain=1#L76)

#### Update Workflow

Edit the `release.yml` file at `line 46` with the new version (ex: `v2.0.0`),
`line 47` with the release name (ex: `Release v2.0.0`) and from `line 49` onwards add the changed changelog section.
[release.yml](https://github.com/fazedordecodigo/PyFlunt/blob/main/.github/workflows/release.yml)

#### Create the PR

Create a PR with the name `Release v<version>` containing the two changes above. In the description of the Pull Request, add the changed changelog section.

[Release PR Example](https://github.com/fazedordecodigo/pyflunt/pull/50)

#### Merge the PR

Once the PR is accepted and passes all checks, merge it.

### 3. Deploy via GitHub

After the PR approval and merge into main, the release of the new version in production will be done automatically via Github Actions.

When Deploy via GitHub is completed, the new version will also be automatically released on
[PyPI][pyflunt-on-pypi]. Download the new version of PyFlunt from PyPI and test if everything is
working as expected.

[pyflunt-issues]: https://github.com/fazedordecodigo/pyflunt/issues
[pyflunt-on-pypi]: https://pypi.org/project/flunt/
[creating-releases]: https://docs.github.com/pt/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release
[docstring-definition]: https://www.python.org/dev/peps/pep-0257/#what-is-a-docstring
[github-cloning]: https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository
[github-creating-a-pr]: https://docs.github.com/pt/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request
[github-forking]: https://docs.github.com/pt/get-started/quickstart/contributing-to-projects
[github-join]: https://github.com/join
[github-sync-pr]: https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/keeping-your-pull-request-in-sync-with-the-base-branch
[install-git]: https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git
[keep-a-changelog]: https://keepachangelog.com/pt-BR/1.0.0/
[poetry]: https://python-poetry.org/docs/#installation
[python]: https://www.python.org/downloads/
[semantic-versioning]: https://semver.org/lang/pt-BR/
[virtualenv]: https://virtualenv.pypa.io/en/latest/
