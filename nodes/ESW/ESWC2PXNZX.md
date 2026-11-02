---
tag: ESWC2PXNZX
kind: definition
name: Hypergeometric function
msc: ["33C05"]
defines: 463X5V31D9
uses: [428M453CR2, 0M3YQJ81NB, 0NAHXR1FRH]
sources:
  - url: https://en.wikipedia.org/wiki/Hypergeometric_function
---

## Definition

Let $a, b, c \in \C$ with $c \notin \set{0, -1, -2, \ldots}$.
The *hypergeometric function* ${}_2F_1(a, b; c; \cdot)$ is the unique [[holomorphic function|0NAHXR1FRH]] on $\C \setminus [1, \infty)$ that agrees on the disc $\abs{z} < 1$ with the sum of the [[hypergeometric series|428M453CR2]]
$$\sum_{n=0}^{\infty} \frac{(a)_n (b)_n}{(c)_n} \, \frac{z^n}{n!}.$$

## Remarks

Existence of this [[analytic continuation|0M3YQJ81NB]] follows from Euler's integral representation when $\operatorname{Re} c > \operatorname{Re} b > 0$.
In general it follows from the hypergeometric differential equation, whose only finite singular points are $0$ and $1$.
Uniqueness holds because $\C \setminus [1, \infty)$ is connected.
This is the principal branch; continuation across the cut gives other branches of a multivalued function.

Example: ${}_2F_1(a, b; b; z) = (1 - z)^{-a}$ on the whole cut plane, with the principal power, since both sides are holomorphic there and agree for $\abs{z} < 1$.

Non-example: ${}_2F_1(1, 1; 2; z) = -\log(1 - z)/z$ has no holomorphic extension to a neighbourhood of $z = 1$ or to any annulus around $1$: going once around $z = 1$ changes $\log(1 - z)$ by $2\pi i$.
So the cut, or a choice of branch, is needed.

Gauss's notation $F(a, b; c; z)$ is common, and the normalized function ${}_2F_1(a, b; c; z)/\Gamma(c)$ is entire in $c$.
