---
tag: XEEZ2MQ6XM
kind: definition
name: Best approximation
msc: [41A50, 41A65]
defines: 7N4988HN3P
uses: [03J5RAKB30, 04KFTA34C5]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_theory
---

## Definition

Let $X$ be a [[normed vector space|03J5RAKB30]], let $A \subseteq X$ be nonempty, and let $x \in X$.
A point $a^* \in A$ is a *best approximation* of $x$ from $A$ if
$$\norm{x - a^*} \le \norm{x - a} \quad \text{for all } a \in A.$$
Equivalently, $\norm{x - a^*} = \inf_{a \in A} \norm{x - a}$, an [[infimum|04KFTA34C5]] that is attained at $a^*$.

## Remarks

Example: in $\R^2$ with the Euclidean norm, let $A$ be the horizontal axis and $x = (1, 2)$.
For $a = (t, 0)$ one has $\norm{x - a}^2 = (1 - t)^2 + 4 \ge 4$, with equality only at $t = 1$, so $(1, 0)$ is the best approximation.

Non-example: in $\R$, let $A = (0, 1]$ and $x = 0$.
The infimum of $\abs{0 - a}$ over $A$ is $0$, but no $a \in A$ attains it, so $x$ has no best approximation from $A$.

Other names are nearest point and, in the uniform norm, minimax approximation.
The set of best approximations of $x$ from $A$ can be empty, a single point, or larger.
