import json
import locale


def main():
    locales = get_locales_from_file()

    for locale_str in locales:
        set_locale(locale_str)
        print_locale_info()


def get_locales_from_file():
    with open("locales.txt", "r") as file:
        return map(lambda x: x.strip(), file.readlines())


def set_locale(locale_str: str):
    locale.setlocale(locale.LC_ALL, (locale_str, "UTF-8"))


def print_locale_info():
    print()
    print(locale.getlocale()[0])
    print(json.dumps(locale.localeconv(), indent=2))


if __name__ == "__main__":
    main()
