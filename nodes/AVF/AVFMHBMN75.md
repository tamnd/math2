---
tag: AVFMHBMN75
kind: definition
name: Global game
msc: [91A27, 91A10]
defines: MNEY8VGP30
uses: [5MZTZRC3CZ, 2XQ7VWT8KJ, 9BF72YM075, 0ZY9DX8FBF, 0DKRR22AEQ]
sources:
  - url: https://en.wikipedia.org/wiki/Global_game
---

## Definition

Let $N = \set{1, \dots, n}$ be a finite set of players with finite action sets $A_i$, and let $A = A_1 \times \cdots \times A_n$.
For each $\theta \in \R$ let $G(\theta)$ be a [[normal-form game|5MZTZRC3CZ]] with action sets $A_i$ and payoff functions $u_i(\cdot, \theta) \colon A \to \R$.
Let $\theta$ be a [[random variable|0DKRR22AEQ]] with a continuous [[density|0ZY9DX8FBF]] $g$.
Let $\varepsilon_1, \dots, \varepsilon_n$ be random variables, independent of each other and of $\theta$, each with a continuous density $f$.
Let $\sigma > 0$.
The *global game* $G^\sigma$ is the [[Bayesian game|2XQ7VWT8KJ]] in which:

1. nature draws $\theta$ and the noise terms $\varepsilon_i$;
2. each player $i$ observes only the private signal $x_i = \theta + \sigma \varepsilon_i$;
3. the players choose actions $a_i \in A_i$ simultaneously;
4. player $i$ receives $u_i(a, \theta)$.

Usually one also assumes *dominance regions*.
For each player, one action is [[strictly dominant|9BF72YM075]] in $G(\theta)$ for all low enough $\theta$, and another one for all high enough $\theta$.

## Remarks

The parameter $\theta$ is not common knowledge, even when $\sigma$ is small: each player is uncertain about the others' signals.
Carlsson and van Damme showed for two-player games with two actions each that, as $\sigma \to 0$, iterated deletion of strictly dominated strategies leaves a unique strategy profile for almost every signal.
At a parameter $\theta$ where $G(\theta)$ has two strict equilibria, this selects the risk-dominant one.

Example: two investors each choose Attack or Wait.
Wait pays $0$; Attack pays $1 - \theta$ if both attack and $-\theta$ otherwise, where $\theta$ is the strength of the currency.
For $\theta < 0$ Attack is strictly dominant, and for $\theta > 1$ Wait is strictly dominant, so the dominance regions exist.
With signals $x_i = \theta + \sigma \varepsilon_i$, all four clauses hold.

Non-example: if every player observed $\theta$ itself, clause 2 would fail.
Then for $0 < \theta < 1$ the game $G(\theta)$ has two strict equilibria, both attack and both wait, and no selection takes place.
