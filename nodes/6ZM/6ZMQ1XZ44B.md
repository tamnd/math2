---
tag: 6ZMQ1XZ44B
kind: definition
name: Riesz space
msc: ["46A40", "06F20"]
defines: 99709K2NJM
uses: [X32V6Y5PYW, WH4SFAACAS, 0P27W9RW0G, G4CA22W2XX]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_space
---

## Definition

Let $V$ be a real vector space with a partial order $\le$ such that $(V, \le)$ is an [[ordered vector space|X32V6Y5PYW]].
The space $V$ is a *Riesz space*, or *vector lattice*, if $(V, \le)$ is a [[lattice|WH4SFAACAS]].
That is, any two elements $x, y \in V$ have a least upper bound $x \vee y$ and a greatest lower bound $x \wedge y$.

## Remarks

Example: $\R^n$ with the componentwise order is a Riesz space, with $x \vee y$ the componentwise maximum.
Example: the space $C([0, 1])$ of [[continuous functions|0P27W9RW0G]] with the pointwise order is a Riesz space, since $\max(f, g)$ and $\min(f, g)$ are continuous.
Non-example: on $\R^2$, let $(a, b) \le (c, d)$ when $a \le c$ and $b = d$.
This makes $\R^2$ an ordered vector space, but $(0, 0)$ and $(0, 1)$ have no common upper bound, so it is not a lattice.
In a Riesz space one writes $x^+ = x \vee 0$, $x^- = (-x) \vee 0$ and $\abs{x} = x \vee (-x)$, and then $x = x^+ - x^-$ and $\abs{x} = x^+ + x^-$.
A Riesz space with a complete norm satisfying $\abs{x} \le \abs{y} \implies \norm{x} \le \norm{y}$ is a [[Banach lattice|G4CA22W2XX]].
