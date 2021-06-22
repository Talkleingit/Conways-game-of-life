
<!-- Title -->
## Conways game of life



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#The-design-architectural-pattern">The design architectural pattern</a></li>
    <li><a href="#UML">UML</a></li>
    <li><a href="#Picture-of-the-application">Picture of the application</a></li>
  
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This is an android application project written entirely in dart with the use of flutter. The project provides a friendly to use android application in which the user
can connect to the Flight gear application and control the plane's joystick and speed.





### Built With
1. Python
2. Pygame





<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

* python3
* pygame
* uuid

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Talkleingit/Remote-Joystick.git
   ```
2. in the command line prompt:
```sh
   python3 GameOfLife.py
   ```
   

<!-- The-design-architectural-pattern -->
## The design architectural pattern
 The architectural design pattern used in this project is the MVC design.
 ### 1. Model:
  The model is responsible for executing the business logic. In this project the model executes the needed functionality in order to verify that the rulesthat Conway stated 
  actually occur, meaning each cell in the matrix will stay alive only if it has 2 or 3 living neighbours. A cell is revived only if it has 3 living cells around it.
 ### 2. View:
  This directory contains all the view files. In the directory each main widget that is used in the application is defined in a separate file (there are 2 sub directories in
  this directory for the sliders (throttle slider, rudder slider) and for the text fields. Moreover, there is a Joystick.dart file for the joystick used in the application. 
  The joystick is not dependent on the ViewModel or any other file in the project for that matter. Instead it is a stand alone component that can be easily integrated into 
  another project. The joystick contains a callable property named onChangeLogic, in runtime this property is initialized with any callable object that accepts 2 double 
  parameters. In this project the callable object given at runtime commands the ViewModel to update the rudder and elevation parameters.
  ### 3. Controller:
  This directory contains the ViewModel.dart file. The ViewModel is in charge of sending commands to the Model whenever the view is changed. Meaning, for example, if the user 
  moved the joystick, the onChangedLogic function in the joystick (injected at runtime) will command the ViewModel to set the new rudder and elevator values, and thus the 
  ViewModel will command the Model to send the new values to the Flight gear. With this sort of methodology we have maintained a clear separation between the View and Model. The 
  chain events start at the view, continue to the ViewModel and end at the Model.
  

<!-- UML -->
## UML
![ProjectUmlDiagram](https://user-images.githubusercontent.com/72923818/122425191-fa394280-cf97-11eb-84a5-14aa466c8ca7.jpg)



<!-- Picture-of-the-application -->
## Picture of the application
![image](https://user-images.githubusercontent.com/72923818/122303620-7dad5200-cf0c-11eb-9e0a-1949e801a92b.png)









<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
