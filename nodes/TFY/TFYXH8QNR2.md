---
tag: TFYXH8QNR2
kind: definition
name: Banach algebra
msc: [46H05, 46J05]
defines: 9KYWN94QDN
uses: [7VS7JZ3Y5B, 0BDTTM24DP]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_algebra
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$.
A *Banach algebra* over $\mathbb{K}$ is a [[normed algebra|7VS7JZ3Y5B]] $(A, \norm{\cdot})$ over $\mathbb{K}$ such that the normed space $(A, \norm{\cdot})$ is complete, that is, a [[Banach space|0BDTTM24DP]].
So $A$ is an associative $\mathbb{K}$-algebra with a complete norm such that $\norm{xy} \le \norm{x}\norm{y}$ for all $x, y \in A$.
A Banach algebra is *unital* if it has a unit $1$, and then one usually also asks $\norm{1} = 1$.

## Remarks

Example: for a compact Hausdorff space $X$, the algebra $C(X)$ of continuous functions $X \to \C$ with $\norm{f} = \sup_{x \in X} \abs{f(x)}$.
Submultiplicativity holds since $\abs{f(x) g(x)} \le \norm{f}\norm{g}$ for every $x$, and completeness holds because a uniform limit of continuous functions is continuous.
Example: the bounded linear operators on a Banach space with the operator norm.
Non-example: the polynomial functions on $[0, 1]$ with the same sup norm form a normed algebra but not a Banach algebra.
They are dense in $C([0, 1])$ by the Weierstrass approximation theorem, and $e^x$ is a uniform limit of polynomials that is not a polynomial, so completeness fails.
In a unital Banach algebra, $1 - x$ is invertible with inverse $\sum_{n \ge 0} x^n$ when $\norm{x} < 1$.
