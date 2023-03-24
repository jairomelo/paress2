# Changelog

## [Unreleased]

## [0.1.6] - 2023-03-23

### Added

- Incluido soporte para Firefox
- Probado en Debian 10 (buster) y Windows 11

### Changed

- Añadida una excepción de Selenium `TimeoutException` para lidiar con conexiones lentas.

### Fixed

- Modificado el comportamiento de webdriver para que el cursor se desplace al botón de descarga antes de hacer clic en él. Este cambio lidia con la excepción `ElementClickInterceptedException` de Selenium.
- Añadida la condición de `invisibility_of_element_located` al elemento `<div class="loader">` que obstruye el clic al botón `saveImageLink`.
