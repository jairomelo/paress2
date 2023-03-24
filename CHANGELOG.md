# Changelog

## [0.1.6] - 2023-03-23

### Added

- Incluido soporte para Firefox

### Changed

- Modificado el comportamiento de webdriver para que el cursor se desplace al botón de descarga antes de hacer clic en él. Este cambio lidia con la excepción `ElementClickInterceptedException` de Selenium.
- Añadida una excepción de Selenium `TimeoutException` para lidiar con conexiones lentas.
