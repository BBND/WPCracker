# WPCracker
WPCracker is a python script used to detect Wordpress vulnerabilities to fix them."

⛔If the tool is used for malicious purposes, we will not be liable.⛔

## About the tool

- **Worspress user enumeration**
- **Wordpress version detector**
- **Wordpress plugins detector**

## Install

```sh
$ git clone https://github.com/BBND/WPCracker
$ cd WPCracker
```

## How it works ?

| Argument | Description |
| ------ | ------ |
| -e [URL] ,--enum [URL] | Set url for wordpress user enumeration. |
| -v [URL] ,--version [URL] | Set url to get WP version. |
| -p [URL] ,--plugins [URL]  | Set url to get all plugins. |
| -h , --help	  | Show documentation |

## Usage Examples

```sh
$ python wpCracker.py --enum www.example.com
```

```sh
$ python wpCracker.py -v www.example.com
```

## Author
[BBND](https://www.bbnd.eu)

## More informations :
[WPCracker](http://www.inspecting.site/wpCracker)
