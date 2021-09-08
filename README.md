# CPSC 386 - Lab 00

# Instructions

This is an exercise to ensure that you have Git, GitHub, and Python setup on your Linux system. This exercise can only be completed with a Linux system and you are encouraged to use [Tuffix](https://github.com/kevinwortman/tuffix).

A coarse outline of the steps you must follow is:

1. From a command shell, use `git` to clone your repository
1. From a command shell, navigate the filesystem to where your repository has been cloned
1. Edit the file `pycheck.py` to include a header
1. Change `pycheck.py` to have executable permission
1. Run the `pycheck.py` command.
1. Copy and paste the secret code from the output of the `pycheck.py` command into a Canvas quiz


First, use `git` to clone your repository onto your Linux computer. If you are new to using `git` or need a quick refresher, please review the [recommended reading](https://docs.google.com/document/d/184U-IQ0DrmlVlPMySjKaYxq2M-ScNvgX8NRa1Kkuk9Q/edit). Specifically, the book [Pro Git by Scott Chacon](https://git-scm.com/book/en/v2) is a good starting point.

Once you have cloned your repository to your computer, execute the `pycheck.py` program. You can do this by navigating to your repository's directory using the command shell.

If you are not familiar with how to use a shell or are a little rusty, the [recommended reading](https://docs.google.com/document/d/184U-IQ0DrmlVlPMySjKaYxq2M-ScNvgX8NRa1Kkuk9Q/edit) has [The Linux Command Line by William Shotts](http://linuxcommand.org/tlcl.php) as a reference.

The next step is to edit the program `pycheck.py` and add a header using your favorite text editor. If you do not have a favorite, you are recommended to use [Microsoft Visual Studio Code](https://code.visualstudio.com/).

Open the file `pycheck.py` in your text editor and add a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) and a header identifying you, your contact information, and the course's information. In this course, you are required to follow [PEP-8](https://www.python.org/dev/peps/pep-0008/), the official Python coding style and add a header to each Python source file you submit. The header is not a requirement of PEP-8. It is a requirement for this course.

The [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) should only be added to files which you intend on running or executing from the command prompt. In our case, `pycheck.py` will be so please include it. In the future, you may write a project across multiple files and including a shebang is not recommended for library files.

The version of Python that we are using in this course is version 3. It is important that you write all your code using Python version 3 and not any earlier versions.

To illustrate, let us imagine we have a hello world program written in Python saved in a file named `hello.py`.

```python
""" This is the file hello.py and it is a hello world program. """
def main():
    """ The main function """
    print("Hello World!")


if __name__ == '__main__':
    main()

```

To add a shebang, we need to add `#!/usr/bin/env python3` to the very first line. A shebang is _always_ the first line of a file. The file `hello.py` will contain:
```python
#!/usr/bin/env python3
""" This is the file hello.py and it is a hello world program. """
def main():
    """ The main function """
    print("Hello World!")


if __name__ == '__main__':
    main()

```

Let us add our header to the file. In this example, we will imagine the author's name is Tuffy Titan who has an email address tuffy.titan@csu.fullerton.edu, and Tuffy's GitHub login is `tuffytitan`.

```python
#!/usr/bin/env python3
# Tuffy Titan
# CPSC 120-01
# 2050-01-01
# tuffy.titan@csu.fullerton.edu
# @tuffytitan
#
# Lab 00-00
#

""" This is the file hello.py and it is a hello world program. """
def main():
    """ The main function """
    print("Hello World!")


if __name__ == '__main__':
    main()

```

Once all the changes are saved, our next step is to change the `pycheck.py` to have executable permission.

From the command prompt, use the command `chmod` to add the execute bit. For example:

```bash
$ chmod u+x pycheck.py
```

Next, run the `pycheck.py` program from the command prompt. For example:

```bash
$ ./pycheck.py 
Yay Linux!
Your secret code is:
26d4f4735af9373d8a557834c68b372059fd7441467ddbcea8eb9cb5e1eb2d500a92fc757fd63db96d7017aef7a7864206379cab2af973f241fb34f71db1a46d%99906006376971
```

If you get a warning message, follow the directions in the warnings message. Once you have the secret code, you can submit it through the Canvas quiz and you are all done with the exercise.

In this example, the secret code is `26d4f4735af9373d8a557834c68b372059fd7441467ddbcea8eb9cb5e1eb2d500a92fc757fd63db96d7017aef7a7864206379cab2af973f241fb34f71db1a46d%99906006376971`. Carefully copy and paste the code into the Canvas quiz. Do not put any spaces or extra characters in the code.


# Rubric

This exercise is worth 10 points. Submissions that do not execute (syntax or semantic error; uncaught exception) shall be assigned a zero grade. Submissions that have made no change substantive change from the template repository shall be assied a zero grade.

* Formatting & Readability (5 points): Your submission shall be assessed by checking whether your code passess the style and format check, as well as how well it follows the proper naming conventions, and internal documentation guidelines. Git log messages are an integral part of how readable your project is. Failure to include a header forfeits all marks. 

* Secret Code (5 points): these points shall be assigned through a Canvas quiz once you have submitted your secret code. Points are only assigned if the correct code is provided.

