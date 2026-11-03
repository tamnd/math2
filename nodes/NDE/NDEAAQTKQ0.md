---
tag: NDEAAQTKQ0
kind: definition
name: Ross–Macdonald model of malaria
msc: [92D30, 34C60]
defines: 7H4V75462S
uses: [BX5ZA16MM6, 0P97V20RW7]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_modelling_of_infectious_diseases
---

## Definition

Let the following constants be positive.

1. $m$ is the number of female mosquitoes per human, and $a$ is the rate at which one mosquito bites humans.
2. $b$ is the probability that a bite by an infectious mosquito infects a human.
   $c$ is the probability that a bite on an infectious human infects the mosquito.
3. $r$ is the recovery rate of humans, and $g$ the death rate of mosquitoes.

Let $x(t), y(t) \in [0, 1]$ be the fractions of infected humans and of infected mosquitoes at time $t$.
The *Ross–Macdonald model* is the [[compartmental model|BX5ZA16MM6]] given by the [[ordinary differential equations|0P97V20RW7]]
$$x' = m a b \, y (1 - x) - r x, \qquad y' = a c \, x (1 - y) - g y.$$

## Remarks

The point $(0, 0)$ is the disease-free equilibrium.
Its Jacobian matrix is $\begin{pmatrix} -r & m a b \\ a c & -g \end{pmatrix}$, with trace $-(r + g) < 0$ and determinant $r g - m a^2 b c$.
So $(0, 0)$ is locally asymptotically stable if $m a^2 b c / (r g) < 1$ and unstable if this number exceeds $1$.
In the second case there is a unique equilibrium with $x, y \in (0, 1)$.
Some authors call $m a^2 b c / (r g)$ the basic reproduction number, and others its square root, since one cycle of transmission takes two steps.

Example: with $m = 10$, $a = 0.3$, $b = c = 0.5$, $r = 0.01$ and $g = 0.1$ per day, one gets $m a^2 b c / (r g) = 10 \cdot 0.09 \cdot 0.25 / 0.001 = 225$.
So transmission persists.

Non-example: the same equations with $g = 0$ do not form a Ross–Macdonald model, since clause 3 asks for $g > 0$.
In that system infected mosquitoes never die, and $y$ increases to $1$ whenever $x$ stays positive.

Macdonald's version adds the extrinsic incubation period $n$ of the parasite in the mosquito, which multiplies the threshold quantity by $e^{-g n}$.
