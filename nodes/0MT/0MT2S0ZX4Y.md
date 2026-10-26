---
tag: 0MT2S0ZX4Y
kind: definition
name: Contraction mapping
msc: [47H09]
defines: 0QN69YA357
uses: [063W5JMY85, 0TMZ21WKCN]
sources:
  - url: https://en.wikipedia.org/wiki/Contraction_mapping
    locator: lead section
---

## Definition

Let $(X, d)$ be a [[metric space|063W5JMY85]].
A map $f \colon X \to X$ is a contraction when there is a real number $k$ with $0 \le k < 1$ such that
$$d\bigl(f(x), f(y)\bigr) \le k \, d(x, y) \quad \text{for all } x, y \in X.$$

## Remarks

A contraction is a [[Lipschitz map|0TMZ21WKCN]] with a constant less than $1$. Thus it is uniformly continuous.
The map $x \mapsto x/2$ on $\mathbb{R}$ is a contraction with $k = 1/2$.
The condition $d(f(x), f(y)) < d(x, y)$ for all $x \neq y$ is weaker. The map $x \mapsto x + 1/x$ on $[1, \infty)$ satisfies it, but it is not a contraction and has no fixed point.

## Explanations

### L1 human

A contraction pulls the points of the space closer together, each time by at least the same factor.
If you apply it again and again, all points are pulled toward one point.
