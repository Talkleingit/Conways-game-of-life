
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
        <li><a href="#Prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#The-architectural-design-pattern">The architectural design pattern</a></li>
    <li><a href="#Picture-of-the-application">Picture of the application</a></li>
  
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
A python application of Conway's game of life. The project includes a gui that generates living/dead blocks according to a set of defined rules. 




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
   

<!-- The-architectural-design-pattern -->
## The architectural design pattern
 The architectural design pattern used in this project is the MVC design.
 ### 1. Model:
  The model is responsible for executing the business logic. In this project the model executes the needed functionality in order to verify that the rules that Conway stated 
  actually occur, meaning each cell in the matrix will stay alive only if it has 2 or 3 living neighbours. A cell is revived only if it has 3 living cells around it.
 ### 2. View:
  The view is responsible to draw each cell using pygame. A living cell is drawn to in white and blue and a dead cell is drawn in black.
  ### 3. Controller:
  The controller runs the evolution, it is responsible for setting the rate at which the data is calculated and it commands both the model and view to execute their tasks 
  at the needed time.
  



<!-- Picture-of-the-application -->
## Picture of the application
![image](https://user-images.githubusercontent.com/72923818/122975722-5509da00-d39c-11eb-954f-63f01b465194.png)









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
