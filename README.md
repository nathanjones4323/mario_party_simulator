<p align="center">
  <a href="https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/software/switch/70010000014158/0ca41128bf40b7e0dc32a046a659ecdc69e4d7cc7a3257d6280be665d2f795b5" rel="noopener">
 <img width=200px height=200px src="https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/software/switch/70010000014158/0ca41128bf40b7e0dc32a046a659ecdc69e4d7cc7a3257d6280be665d2f795b5" alt="Project logo"></a>
</p>

<h3 align="center">Super Mario Party Simulator</h3>

---

<p align="center"> Optimize your character selection in Super Mario Party
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [🔬 Methodology](#🔬_methodology)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Limitations](#limtations)
- [Next Steps and Extending the Analysis](#next_steps_and_extending_the_analysis)

## 🧐 About <a name = "about"></a>

Everyone loves Mario Party. We all have a favorite character, but does that character really embody our desired play strategy?

Since each charater has a different die, there is a some strategy invloved in the choice of character.

One simple strategy is to move as many spaces as possible over the span of the game, so you can reach the star more frequently. Taking this strategy, you would want to pick the character with the highest [expected value](https://en.wikipedia.org/wiki/Expected_value) over all die rolls.

## 🧐 Methodology <a name = "🔬_methodology"></a>

We can figure out the **expected value** of spaces moved for each character over a number of turn schemes via 2 methods:

1. Statistics Knowledge
1. [Monte Carlo Simulation](https://en.wikipedia.org/wiki/Monte_Carlo_method)

### Statistics Knowledge

Each die is 6 sided, and the roll outcomes are uniformly distributed.

This means that the **expected value** of each die roll is $\frac{1}{6} * number_rolled$.

For a single die roll

$\mathbf{E}[X] = \sum \frac{1}{6} * n$, $\forall n \in \{n_1, n_2, n_3, n_4, n_5, n_6\}$ where n is the number rolled, and $\{n_1, n_2, n_3, n_4, n_5, n_6\}$ are the possible outcomes on a roll.

Because of the [Linearity of Expectation](https://en.wikipedia.org/wiki/Expected_value#Properties), we know that

$\mathbf{E}[nX] = n\mathbf{E}[X]$ where n is the number of rolls.

Combining these 2 facts, we can find the expected number of spaces moved over a set of n rolls (equivalent to a turn) is 

$\mathbf{E}[nX] = n\mathbf{E}[X]$ = $n\sum \frac{1}{6} * n$, $\forall n \in \{n_1, n_2, n_3, n_4, n_5, n_6\}$

### Monte Carlo Simulation

We can simulate rolls for each character for all turn schemes over a large number of games. As the number of games increases, the sample mean spaces moved converges to the true mean spaces moved.

To simulate a roll, we will set up a list of possible die values for each character and select an element at random from the list (uniform random) on each roll.

We can verify our simulation by checking the mean spaces moved per character for a large number of ganmes to the true mean calculated via our stats knowledge.

## 🏁 Getting Started <a name = "getting_started"></a>

#### Prerequisites

* Python Virtual Environment
* Jupyter Notebook

<!-- * Docker ([Docker Desktop comes with Docker](https://www.docker.com/products/docker-desktop/)) -->

You see the entire statistical analysis, simulation, and plots inisde of the [Jupyter Notebook file]() or just the simulation, and plots through a few commands in the terminal.


## Usage <a name = "usage"></a>

The simulations and basic analysis have already been done, so you don't need to run anything unless you want to extend the experiments or try it for yourself.

### Running the Simulation

**Terminal**

Run the following in your terminal to produce a `./simulation_results` folder which contains a `data` folder and `plots` folder showing the results of the simulation.

Run the following commands inside of the root directory to simulate from the terminal

> :warning: You should activate a virtual environment first and run `pip install -r requirements.txt` before this step

    ```
    python characters.py && python simulation.py && python analysis.py
    ```

This will take a long time to finish. I had to cap the number of turns at 10,000 to avoid any massive slowdowns (performance improvements here?).

**Jupyter Notebook**

Run the entire notebook to see inline plots of the simulation results.

### Analyzing the Simulation Results

We can use the plots to answer:
1. What character moves the mmost spaces on average?
1. What character earns the most coins on average?
1. What are the distributions for spaces moved per character?
  1. Do you notice anything about the variance in spaces moved for some characters?
  1. Is there a correlation between characters with the high expected value of spaces moved high variance?

**Jupyter Notebook**

View the plots at the end of the notebook.

## 🧐 Limitations <a name = "limitations"></a>

  ```
  TODO
  ```

## 🧐 Next Steps and Extending the Analysis <a name = "next_steps_and_extending_the_analysis"></a>

  ```
  TODO
  ```