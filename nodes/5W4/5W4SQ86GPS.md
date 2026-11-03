---
tag: 5W4SQ86GPS
kind: definition
name: Preference relation
msc: [91B08, 06A06]
defines: JGP0Q56FRY
uses: [05AVARPXA2, 0GJZW9JFZQ]
sources:
  - url: https://en.wikipedia.org/wiki/Preference_(economics)
---

## Definition

Let $X$ be a set, the set of alternatives.
A *preference relation* on $X$ is a [[binary relation|05AVARPXA2]] $\succsim$ on $X$ with these two properties.

1. Completeness: for all $x, y \in X$, $x \succsim y$ or $y \succsim x$.
2. Transitivity: for all $x, y, z \in X$, if $x \succsim y$ and $y \succsim z$, then $x \succsim z$.

The statement $x \succsim y$ is read "$x$ is at least as good as $y$".
The *strict preference* is $x \succ y$ when $x \succsim y$ and not $y \succsim x$.
The *indifference* is $x \sim y$ when $x \succsim y$ and $y \succsim x$.

## Remarks

On $X = \R^2_{\ge 0}$, bundles of two goods, set $x \succsim y$ when $x_1 + x_2 \ge y_1 + y_2$.
This is complete, since any two real numbers are comparable, and [[transitive|0GJZW9JFZQ]], since $\ge$ on $\R$ is transitive.
On the same set, set $x \succsim y$ when $x_1 \ge y_1$ and $x_2 \ge y_2$.
This is transitive but not complete: neither $(1, 0) \succsim (0, 1)$ nor $(0, 1) \succsim (1, 0)$ holds.
Completeness gives reflexivity, by taking $x = y$, so a preference relation is a total preorder.
The strict preference $\succ$ is then a strict weak ordering, see [[weak ordering|PW2NKAPXWA]], and $\sim$ is an equivalence relation whose classes are the indifference classes.
Some authors call such a relation a rational preference relation.
