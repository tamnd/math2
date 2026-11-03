---
tag: 7BRCTFGE6B
kind: statement
role: theorem
name: Harsanyi's purification theorem
msc: [91A27, 91A10]
uses: [5MZTZRC3CZ, P01KKHB155, 745WYP9YJ0, 2XQ7VWT8KJ, 0ZY9DX8FBF, 2Z2QVWZ262]
about: [745WYP9YJ0, 2XQ7VWT8KJ]
sources:
  - url: https://en.wikipedia.org/wiki/Purification_theorem
same_as:
  wikidata: Q5313424
  wikipedia: Purification theorem
---

## Statement

Let $G$ be a finite [[normal-form game|5MZTZRC3CZ]] with players $i = 1, \dots, n$, finite action sets $A_i$, payoff functions $u_i$, and $A = A_1 \times \cdots \times A_n$.
For $\varepsilon > 0$, let $G_\varepsilon$ be the [[Bayesian game|2XQ7VWT8KJ]] in which player $i$ has the payoff $u_i(a) + \varepsilon \theta_i(a)$.
Here $\theta_i = (\theta_i(a))_{a \in A}$ is a random vector known only to player $i$.
Assume that $\theta_1, \dots, \theta_n$ are independent and that each has a continuously differentiable [[probability density|0ZY9DX8FBF]] on a bounded set.
Then for all games $G$ outside a set of payoff vectors of [[Lebesgue measure|2Z2QVWZ262]] zero, the following holds.
For every [[Nash equilibrium|745WYP9YJ0]] $\sigma$ of $G$ in [[mixed strategies|P01KKHB155]], there are Bayesian Nash equilibria $s^\varepsilon$ of $G_\varepsilon$ such that:

1. in $s^\varepsilon$, almost every type of each player plays a pure action, and
2. as $\varepsilon \to 0$, the distribution of the action of each player $i$ induced by $s^\varepsilon$ converges to $\sigma_i$.

## Remarks

For almost every game, all Nash equilibria are regular, which means that a certain Jacobian at the equilibrium is non-singular.
For a regular equilibrium, the implicit function theorem lets one follow the equilibrium into the perturbed games.
In the perturbed game a type is indifferent between two actions only for a set of $\theta_i$ of probability zero, so best responses are pure almost surely.
The proportion of types choosing each action then reproduces the mixing probabilities of $\sigma$.

Example: in matching pennies the unique Nash equilibrium has both players mix with probabilities $1/2$.
With small private payoff shocks, each player chooses heads exactly when her shock favours heads by more than a threshold.
For an outside observer, each player then plays heads with probability close to $1/2$, though no type randomizes.

The genericity hypothesis is needed: in degenerate games, some mixed equilibria cannot be approached by equilibria of perturbed games in this way.

## Explanations

### L1 human

Mixed strategies ask a player to randomize on purpose, which can seem odd for a real decision maker.
Harsanyi's theorem gives another reading.
Each player has small private reasons, unknown to the others, that tip her to one action or the other.
She acts deterministically, but to the other players she looks as if she were flipping a coin.
So a mixed equilibrium describes the others' uncertainty about her choice.

### L2 human

The theorem justifies the use of mixed equilibria in applications, by showing that they are limits of pure-strategy equilibria of nearby games with incomplete information.
It uses the [[Bayesian game|2XQ7VWT8KJ]] model and a genericity argument based on regular equilibria.
The conclusion concerns equilibria of the perturbed games, not equilibria of the original game, and it needs the perturbations to be independent across players.
Later work extended the result to more general classes of perturbations.
