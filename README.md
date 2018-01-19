<p align="center">
  <img src="https://user-images.githubusercontent.com/24781621/34276993-cc4267f2-e658-11e7-8783-8e60082179b7.png" alt="Improv.live logo"/>
</p>

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
$ pip install flask
$ pip install flask-cors
$ pip install flask_pymongo
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

- In your browser, go to “localhost:5000/index”. From there, you can access all the pages from links in the index page. 
![il_index_0](https://user-images.githubusercontent.com/24781621/34277360-3a2e228c-e65a-11e7-9d8e-4d6e310b99f8.png)
![il_inddex_1](https://user-images.githubusercontent.com/24781621/34277228-b3342178-e659-11e7-9b7c-6df1ea1ddddd.png)

- Wheel Page: "localhost:5000/wheel"
![il_wheel_0](https://user-images.githubusercontent.com/24781621/34277398-5e05ceee-e65a-11e7-81d6-301e6d53afa6.png)

Once you make a selection from the dropdown menu, the wheel is populated with choices. 
Click "Spin" to have the wheel make your random selection!
![il_wheel_3](https://user-images.githubusercontent.com/24781621/34277408-67b0d2f4-e65a-11e7-9964-9f9af24800c5.png)

- Game Page: "localhost:5000/game"
Click on the dropdown menu to make a selection.
![il_game_0](https://user-images.githubusercontent.com/24781621/34277518-f419ebfe-e65a-11e7-8ff5-f31f4b84a583.png)
Check the boxes for the number of players for the games. 
![il_game_2](https://user-images.githubusercontent.com/24781621/34277507-e59d133a-e65a-11e7-96df-132dfe15bc3f.png)
Once you click "Search" the page will be populated and you can scroll through the choices available.
![il_game_3](https://user-images.githubusercontent.com/24781621/34277508-e6afc696-e65a-11e7-89a5-795a624223e0.png)



## To-Do

- [ ] Tests: update console tests to work with MongoDB
- [ ] Tests: add tests for MongoDB
- [ ] Create console to work with MongoDB
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
* Logo: Carrie Ybay   [GutHub](https://github.com/hicarrie)  |  [LinkedIn](https://www.linkedin.com/in/carrie-ybay/)
