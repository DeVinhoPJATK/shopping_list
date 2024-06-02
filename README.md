# Dawid Łacheta s24177
# Aplikacja Listy Zakupów

Aplikacja Listy Zakupów to narzędzie wiersza poleceń zaprojektowane, aby pomóc użytkownikom zarządzać ich listami zakupów. Aplikacja pozwala na tworzenie i usuwanie list zakupów, wyświetlanie wszystkich list, wyświetlanie produktów z konkretnej listy oraz dodawanie i usuwanie produktów z listy. Dane dotyczące list oraz produktów są serializowane do formatu JSON oraz zapisywane w plikach .json w katologu **data/**. 

## Struktura Projektu

Projekt składa się z następujących głównych komponentów:

- **application.py**: Główny punkt wejścia do aplikacji.
- **data/**: Katalog do przechowywania plików z listami zakupów.
- **handlers/**: Katalog zawierający moduły obsługi do zarządzania listami i plikami.
- **models/**: Katalog zawierający modele danych dla aplikacji.
- **util/**: Moduły pomocnicze dla różnych funkcji pomocniczych.
- **README.md**: Plik dokumentacji projektu.
- **.gitignore**: Plik konfiguracyjny Git do wykluczania niektórych plików z kontroli wersji.

### Uruchamianie Aplikacji

Aby uruchomić aplikację, wykonaj następujące polecenie z katalogu projektu:

```sh
python application.py
