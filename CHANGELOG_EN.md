ENGLISH | [PORTUGUÊS](https://github.com/fazedordecodigo/PyFlunt/blob/main/docs/CHANGELOG.md)

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/lang/pt-BR/spec/v2.0.0.html).

## [Unreleased]
- Add Result Pattern [#61](https://github.com/fazedordecodigo/PyFlunt/issues/61)

## [3.0.1] - 2025-06-22
### Added
- Added detailed documentation with introduction, getting started guide, API reference, and usage examples ([#docs])
- Added benchmarking and logging examples in samples for usage and performance comparison of dictionaries

### Changed
- N/A

### Fixed
- N/A

## [3.0.0] - 2025-04-04
### Added
- Implementation of `uv` to replace Poetry for dependency management
- Improved support for Brazilian Portuguese messages and internationalization
- Addition of generic types `StringType` and `Self` return for better typing
- New constant `IS_NOT_SIZED` to improve error messages in validations
- Memory optimization in the `Notifiable` class with the use of `__slots__`
- Improvements in collection and string validations
- More comprehensive tests for all validation functions
- Workflow update for multiple Python versions support (3.11, 3.12, 3.13)
- Refactor FluntRegexPatterns [#129](https://github.com/fazedordecodigo/PyFlux/issues/129)
- Add standardized messages in PT-BR and EN [#18](https://github.com/fazedordecodigo/PyFlunt/issues/18)

### Changed
- Requires Python 3.11 or higher (previously supported 3.9+)
- Refactoring of the `CollectionsValidationContract` class for better object verification
- Parameter type change for `contains` and `not_contains` functions to `StringType`
- Renamed fields in the `Pessoa` example from `first_name`/`last_name` to `primeiro_nome`/`ultimo_nome`

### Fixed
- Fixed handling of `None` values in collection validations
- Proper handling for objects that do not implement the `Sized` protocol
- Fixed string formatting in notification tests

## [2.3.1] - 2024-12-16
### Added
- Refactor to use `get_pattern` in `CreditCardValidationContract` and `EmailValidationContract`.

### Fixed
- Ensure regex patterns return valid data for validations.
- Refactor `FluntRegexPatterns` [#129](https://github.com/fazedordecodigo/PyFlunt/issues/129)

## [2.3.0] - 2024-03-17
### Added
- Collections validation [#30](https://github.com/fazedordecodigo/PyFlunt/issues/30)

### Fixed
- Lack of return typing in Requires overloads [#59](https://github.com/fazedordecodigo/PyFlunt/issues/59)
- Pipeline Linters with broken path for requirements.txt [#60](https://github.com/fazedordecodigo/PyFlunt/issues/60)

## [2.2.0] - 2024-03-13
### Added
- Applied Duck Typing for UUID validation [#11](https://github.com/fazedordecodigo/PyFlunt/issues/11)
- New unit test scenarios

### Fixed
- Fixed broken links in the README [#53](https://github.com/fazedordecodigo/PyFlunt/issues/53)
- Fixed bug in `requires` that returned a false positive when receiving the boolean value `False`.
- Rewritten existing unit tests.

## [2.1.1] - 2024-02-27
### Fixed
- Broken README links [#53](https://github.com/fazedordecodigo/PyFlunt/issues/53)
- Commands for pre-commit execution script [#53](https://github.com/fazedordecodigo/PyFlunt/issues/53)
- Communication method for reporting a vulnerability [#53](https://github.com/fazedordecodigo/PyFlunt/issues/53)

## [2.1.0] - 2024-02-24
### Added
- CONTRIBUTING in PT-BR and EN [#39](https://github.com/fazedordecodigo/PyFlunt/issues/39)
- CODE_OF_CONDUCT in PT-BR and EN [#40](https://github.com/fazedordecodigo/PyFlunt/issues/40)
- README in PT-BR [#41](https://github.com/fazedordecodigo/PyFlunt/issues/41)
- CHANGELOG in PT-BR and EN [#42](https://github.com/fazedordecodigo/PyFlunt/issues/42)
- SECURITY in PT-BR and EN [#43](https://github.com/fazedordecodigo/PyFlunt/issues/43)
- FUNDING [#44](https://github.com/fazedordecodigo/PyFlunt/issues/44)
- Pull Request Template in PT-BR [#45](https://github.com/fazedordecodigo/PyFlunt/issues/45)
- Issue Template Bug Report in PT-BR [#46](https://github.com/fazedordecodigo/PyFlunt/issues/46)
- Issue Template Feature Report in PT-BR [#47](https://github.com/fazedordecodigo/PyFlunt/issues/47)
- Issue Template Vulnerability Report in PT-BR [#48](https://github.com/fazedordecodigo/PyFlunt/issues/48)

### Fixed
- Bug that prevented running on Python v3.9 [#36](https://github.com/fazedordecodigo/PyFlunt/issues/36)

## [2.0.0] - 2024-02-13
### Added

- Add Python setup and dependencies installation by @fazedordecodigo in #25

### Changed

- Updated CD by @fazedordecodigo in #16
- Updated issue templates by @fazedordecodigo in #20
- Updated actions by @fazedordecodigo in #24

## [1.0.0] - 2023-05-22
### Added

- Implemented CD. Version 0.2.0 by @fazedordecodigo in #9

## [0.2.0] - 2021-11-22
### Added

- Created LICENSE by @fazedordecodigo in #4
- Implemented new methods is_false, is_true, is_not_none, is_none by @fazedordecodigo in #8

### Changed

- Edited Readme by @fazedordecodigo in #3 and #5
- CI adjustments by @fazedordecodigo in #6 and #7

## [0.1.1] - 2021-11-19
### Added

- Release by @fazedordecodigo in #1



<br>
<br>
<br>

[3.0.0](https://github.com/fazedordecodigo/PyFlunt/compare/v2.3.1...v3.0.0)

[2.3.1](https://github.com/fazedordecodigo/PyFlunt/compare/v2.3.0...v2.3.1)

[2.3.0](https://github.com/fazedordecodigo/PyFlunt/compare/v2.2.0...v2.3.0)

[2.2.0](https://github.com/fazedordecodigo/PyFlunt/compare/v2.1.1...v2.2.0)

[2.1.1](https://github.com/fazedordecodigo/PyFlunt/compare/v2.1.0...v2.1.1)

[2.1.0](https://github.com/fazedordecodigo/PyFlunt/compare/v2.0.0...v2.1.0)

[2.0.0](https://github.com/fazedordecodigo/PyFlunt/compare/v1.0.0...v2.0.0)

[1.0.0](https://github.com/fazedordecodigo/PyFlunt/compare/0.2.0...v1.0.0)

[0.2.0](https://github.com/fazedordecodigo/PyFlunt/compare/0.1.1...0.2.0)

[0.1.1](https://github.com/fazedordecodigo/PyFlunt/commits/0.1.1)
