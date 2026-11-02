---
tag: NXCM67XY9E
kind: statement
role: theorem
name: Caristi fixed-point theorem
msc: [47H10, 54H25, 47H09]
uses: [0BY52JW6NK]
about: [0BY52JW6NK]
sources:
  - url: https://en.wikipedia.org/wiki/Caristi_fixed-point_theorem
same_as:
  wikidata: Q2287393
  wikipedia: Caristi fixed-point theorem
---

## Statement

Let $(X, d)$ be a nonempty [[complete metric space|0BY52JW6NK]].
Let $\varphi \colon X \to [0, \infty)$ be a lower semicontinuous function.
Let $T \colon X \to X$ be any map, not necessarily continuous, such that
$$d(x, T(x)) \le \varphi(x) - \varphi(T(x)) \quad \text{for all } x \in X.$$
Then $T$ has a fixed point: there is $x \in X$ with $T(x) = x$.

## Remarks

The theorem follows from [[Ekeland's variational principle|MJGPW5EVB3]].
With $\varepsilon = 1$, it gives a point $x_0$ with $\varphi(x_0) < \varphi(x) + d(x, x_0)$ for every $x \ne x_0$.
If $T(x_0) \ne x_0$, then taking $x = T(x_0)$ gives $\varphi(x_0) < \varphi(T(x_0)) + d(T(x_0), x_0) \le \varphi(x_0)$, a contradiction.

Example: the [[Banach fixed point theorem|0VK6VEH345]] is a special case.
If $d(T(x), T(y)) \le k\, d(x, y)$ with $0 \le k < 1$, put $\varphi(x) = d(x, T(x))/(1 - k)$, which is continuous.
The Caristi condition becomes $d(T(x), T(T(x))) \le k\, d(x, T(x))$, which holds.

Completeness is needed: on $X = (0, 1]$ with the usual metric, $T(x) = x/2$ and $\varphi(x) = x$ satisfy $d(x, T(x)) = x/2 = \varphi(x) - \varphi(T(x))$, but $T$ has no fixed point in $X$.

## Explanations

### L1 human

Think of $\varphi$ as a supply of fuel and of $T$ as a move.
Each move costs at least as much fuel as the distance travelled.
Since fuel cannot go below zero, the total distance of a run of moves is finite.
In a complete space the run settles down to a point that $T$ does not move.

### L2 human

The theorem does not ask $T$ to be continuous, which makes it more flexible than the Banach fixed point theorem.
It is equivalent in strength to Ekeland's variational principle, and each can be derived from the other.
It is used in nonlinear analysis for maps that are only known to decrease a lower semicontinuous potential, such as some descent schemes in optimisation.
