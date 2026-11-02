---
tag: G5AN43WE9D
kind: definition
name: Lattice-ordered group
msc: ["06F15", "06F20"]
defines: J0DHYQ0MDE
uses: [A49BATWQEH, WH4SFAACAS, VQ4SSKS53D]
sources:
  - url: https://en.wikipedia.org/wiki/Partially_ordered_group
---

## Definition

Let $(G, \le)$ be an [[ordered group|A49BATWQEH]].
It is a *lattice-ordered group*, or *$\ell$-group*, if the partially ordered set $(G, \le)$ is a [[lattice|WH4SFAACAS]].
That is, any two elements $a, b \in G$ have a least upper bound $a \vee b$ and a greatest lower bound $a \wedge b$ in $G$.

## Remarks

Example: $\Z^2$ under addition with the componentwise order is an $\ell$-group.
Here $(a, b) \vee (c, d) = (\max(a, c), \max(b, d))$ and $(a, b) \wedge (c, d) = (\min(a, c), \min(b, d))$.
Non-example: on $\Z^2$, let $(a, b) \le (c, d)$ when $a \le c$ and $b = d$.
This makes $\Z^2$ an ordered group, but $(0, 0)$ and $(0, 1)$ have no common upper bound, so it is not a lattice.
In an $\ell$-group, multiplication distributes over joins and meets: $c(a \vee b) = ca \vee cb$ and $(a \vee b)c = ac \vee bc$.
The lattice of an $\ell$-group is distributive.
Every $\ell$-group is a [[torsion-free group|VQ4SSKS53D]].
For $a \in G$ one writes $a^+ = a \vee e$, $a^- = a^{-1} \vee e$ and $\abs{a} = a \vee a^{-1}$, and then $a = a^+ (a^-)^{-1}$.
