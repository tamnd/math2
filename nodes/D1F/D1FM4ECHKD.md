---
tag: D1FM4ECHKD
kind: definition
name: Interval arithmetic
msc: [65G30, 65G40]
defines: QPKKTE1ZY0
uses: [0Q1D85B8G6]
sources:
  - url: https://en.wikipedia.org/wiki/Interval_arithmetic
---

## Definition

Let $\mathbb{IR}$ be the set of closed bounded [[intervals|0Q1D85B8G6]] $[a, b] = \set{x \in \R : a \le x \le b}$ with real $a \le b$.
For $X, Y \in \mathbb{IR}$ and an operation $\circ \in \set{+, -, \times, \div}$, set
$$X \circ Y = \set{x \circ y : x \in X, \ y \in Y},$$
where for $\div$ one requires $0 \notin Y$.
*Interval arithmetic* is $\mathbb{IR}$ with these four operations.
For $X = [a, b]$ and $Y = [c, d]$ they are given by:

1. $X + Y = [a + c, \ b + d]$;
2. $X - Y = [a - d, \ b - c]$;
3. $X \times Y = [\min(ac, ad, bc, bd), \ \max(ac, ad, bc, bd)]$;
4. $X \div Y = X \times [1/d, \ 1/c]$ when $0 \notin Y$.

## Remarks

Each set $X \circ Y$ is again a closed bounded interval, because it is the image of the compact connected set $X \times Y$ under a continuous map.
Example: $[1, 2] \times [-1, 3]$ has the products $-1, 3, -2, 6$ of the end points, so it is $[-2, 6]$; indeed $x y$ takes every value between $-2$ and $6$ for $x \in [1, 2]$ and $y \in [-1, 3]$.
Non-example: $[1, 2] \div [-1, 1]$ is not defined, because $0 \in [-1, 1]$ and the set $\set{x / y : y \ne 0}$ is unbounded.
Addition and multiplication are associative and commutative, but $X - X \ne [0, 0]$ unless $X$ has one point, and only the subdistributive law $X \times (Y + Z) \subseteq X \times Y + X \times Z$ holds in general.
For example, $[-1, 1] \times ([1, 1] + [-1, -1]) = [0, 0]$, while $[-1, 1] \times [1, 1] + [-1, 1] \times [-1, -1] = [-2, 2]$.
