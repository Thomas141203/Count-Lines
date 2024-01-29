# Count-Lines
This project is a Python program that counts all the lines of code in all the files of all the GitHub repositories of a given user.

## Usage

### Installation

```shell
git clone https://github.com/Thomas141203/Count-Lines
```

### Configuration 
Obtain your GitHub username and personal access token <br>
Then you nedd to replace "YOUR_USERNAME" and "YOUR_TOKEN" with your github username and personal access token at the end of the main.py file.

### Run

```python
python main.py
```

### Example Usage 

```bash
$ python main.py
Lines in username/repo1: 1000
Lines in username/repo2: 1500
Total lines: 2500
```

## Dependencies

This project uses the requests library to make HTTP requests to the GitHub API. You can install it using pip:

```shell
pip install requests
```

## Contribution 

Contributions are welcome! If you want to contribute to this project, please open an issue to discuss the changes you would like to make.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

