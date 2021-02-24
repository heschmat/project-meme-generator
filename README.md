# Project Meme Generator

This projects covers apsects of developing a multimedia application to dynamically generate memes, including an image with an overlaid quote. It is designed to cover many areas of Python development. Especifically the roles of __data engineer__ and __full stack web developer__.

## Project challenges:
- Interact with a variety of complex filetypes.
- Load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
- Load, manipulate, and save image files.
- Accept dynamic user input through a command-line tool and a web service.

## Libraries
- requests
- flask
- pandas
- pillow
- python-docx

`python-docx` is used to convert microsoft word documents to simple txt format. 

## Software
- xpdf 

The app uses the `subprocess` module to execute this CLI tool to convert data from PDF format to TXT format. 
To install `pdftotext` on Mac or Windows refer to [here](https://www.xpdfreader.com/pdftotext-man.html).
On Linux you need to run `sudo apt-get install -y xpdf`. Note: sometimes you also have to run `sudo apt-get update` if the previous command throws an error.


## Project Interface
The project can be run in two modes:
1. To run the project in the command line, run `python meme.py`. At the command line, you could run `python meme.py --help` for an explanation of how to invoke the script.

```
(project_meme) C> python meme.py --help                                                                                 
usage: meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]                                                                                                                                                                               
Generate Meme.                                                                                                                                                                                                                                  
optional arguments:                                                                                                       
-h, --help       show this help message and exit                                                                        
--path PATH      The path to the image file.                                                                            
--body BODY      The text/quote to put on image.                                                                        
--author AUTHOR  The author of the quote. 

```

A sample command would be:
```
(project_meme) C> python meme.py --body "Carpe diem, seize the day people." --author "John Keating"                     
[Info] Image Saved to ./tmp\tmp-1614131312.6785374.png.                                                                 
./tmp\tmp-1614131312.6785374.png                                                                                                                                                                                                                
(project_meme) C>  
```
This way, the meme will be generated in `tmp` directory, with the requested parameters. 
The parameters are optional; if no parameters is passed, then a random meme will be created. 
The script returns a path to a generated image.

2. To run the project in the app, run `python app.py` and go to `http://127.0.0.1:5000/`.

```
(project_meme) C> python app.py                                                                                          
* Serving Flask app "app" (lazy loading)                                                                                
* Environment: production                                                                                                
WARNING: This is a development server. Do not use it in a production deployment.                                       
Use a production WSGI server instead.                                                                                 
* Debug mode: off                                                                                                       
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) 
```

The app uses the `Quote Engine` Module and `Meme Generator` module to generate a random captioned image.
It uses the `requests` package to fetch an image from a user submitted URL.


## Project Scaffolding

The structure of the project is as follows: 

The `QuoteEngine` module is responsible for ingesting many types of files that contain quotes.
This module is composed of many classes and show cases understanding of complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles.

The `MemeEngine` Module is responsible for manipulating and drawing text onto images.
