---
tag: 0BDTTM24DP
kind: definition
name: Banach space
aliases: [complete-normed-space]
msc: [46B99]
defines: 06GZ956657
uses: [0J3578562S, 08EWT7J0SC]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_space
    locator: Definition
---

## Definition

Let $V$ be a vector space over $\mathbb{R}$ or $\mathbb{C}$ with a [[norm|0J3578562S]] $\|\cdot\|$, and let $d(x, y) = \|x - y\|$.
The space $(V, \|\cdot\|)$ is a Banach space when the metric space $(V, d)$ is [[complete|08EWT7J0SC]].

## Remarks

Examples are $\mathbb{R}^n$ with any norm, the spaces [[ell p|08P6T2WH6R]] for $1 \le p \le \infty$, and $C_b(X)$ with the [[sup norm|0PARCKE8WP]].
The space of polynomial functions on $[0, 1]$ with the sup norm is not a Banach space. Its completion is $C([0, 1])$.
In a normed space $V$, completeness is the same as: [[each absolutely convergent series converges|082MGNWNA8]].
Each [[finite-dimensional normed space is complete|0ABP2F2ZP7]].

## Explanations

### L1 human

A Banach space is a vector space where you can measure lengths, and where Cauchy sequences always converge.
So you can take limits in it freely, as in $\mathbb{R}^n$.
