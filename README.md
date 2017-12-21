# Improv.live

Improv.live is a web application to provide information about improvisational games as well as a wheel to help choose prompts or games per a user's specifications.

This project utilizes a stack consisting of: Linux, Nginx, MongoDB, and Python.


## Key Features

- Simple Design
- Dynamic Content
- Accessibility of Colors Tested with [AreMyColorsAccessible.com](http://www.aremycolorsaccessible.com)
- Open Source, Dyslexic Friendly Font: [OpenDyslexic](https://opendyslexic.org)


### Environment
These files have been tested on Ubuntu 14.05.5 LTS in VirtualBox on [Ubuntu](https://atlas.hashicorp.com/ubuntu/boxes/trusty64) via [Vagrant](https://www.vagrantup.com/)(1.9.1).

## Getting Started

Future Versions of this site will be hosted live, but until then, you can have a personal copy of the project!

Below, the steps needed to use and improve the application have been outlined.

### Prerequisites

- Python3

```
$ sudo apt-get update
$ sudo apt-get install python3.4
```

- MongoDB

```
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
$ echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
```

- Flask and related extentions
```
$ pip install Flask
$ pip install flask-cors
$ pip install Flask-PyMongo
```

### Installing

Follow the below instructions to install improv.live locally.

- Clone the repository
```
$ git clone https://github.com/KRLoyd/improv_live.git
```

- Go into the folder
```
$ cd improv_live
```

- Use the dump file to create the `improv_live` database in MongoDB with it's collections

```
$ mongorestore dump/
```

## Running the application

- Run the application on port 5000
```
python3 -m app
```

- In your browser, go to “localhost:5000/index”
From there, you can access all the pages from links in the index page. 

To see the other pages individually, you can go to “localhost:5000/wheel” and “localhost:5000/game”

## To-Do

- [ ] Console: update to work with MongoDB instead of SQLALchemy
- [ ] Tests: update console tests to work with MongoDB
- [ ] Tests: add tests for MongoDB
- [ ] UX (Wheel Page): split drop-down menu into 2 (prompts, games)
- [ ] UX: redo drop-down menus on all pages, style is wonky
- [ ] UX (Game Page): redo style of resizing game information with the window
- [ ] Content: add more games to the database
- [ ] Content: add more info for each game (type, skill level)


## Authors

Kristen Loyd   [GitHub](https://github.com/KRLoyd)  |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Spinning Wheel: [Andre Cortellini](https://codepen.io/AndreCortellini/) via [CodePen](https://codepen.io/AndreCortellini/pen/vERwmL?page=1&)
* Mentorship: Rona Chong   [GitHub](https://github.com/ronachong)  |  [LinkedIn](https://www.linkedin.com/in/rona-chong-15b167b6/)
