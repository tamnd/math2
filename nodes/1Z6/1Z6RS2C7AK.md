---
tag: 1Z6RS2C7AK
kind: definition
name: Dedekind number
msc: ["06A07", "05A15", "06E30"]
defines: 481ZPQ0GC3
uses: [0X05GS525E, 0A7KV2WB7A, 03HF498P1J]
sources:
  - url: https://en.wikipedia.org/wiki/Dedekind_number
---

## Definition

Let $n \ge 0$ be an integer, and order $\set{0, 1}^n$ coordinatewise: $x \le y$ when $x_i \le y_i$ for every $i$.
A [[Boolean function|0X05GS525E]] $f \colon \set{0, 1}^n \to \set{0, 1}$ is *monotone* if $x \le y$ implies $f(x) \le f(y)$.
The *Dedekind number* $M(n)$ is the number of monotone Boolean functions $f \colon \set{0, 1}^n \to \set{0, 1}$.

## Remarks

Identify $\set{0, 1}^n$ with the subsets of $\set{1, \ldots, n}$.
A monotone $f$ is determined by the minimal sets $S$ with $f(S) = 1$, and these form an [[antichain|03HF498P1J]].
So $M(n)$ is also the number of antichains of subsets of $\set{1, \ldots, n}$, including the empty antichain.

Example: $M(2) = 6$.
The monotone functions of $x, y$ are $0$, $1$, $x$, $y$, $x \wedge y$ and $x \vee y$.
The matching antichains are $\emptyset$, $\set{\emptyset}$, $\set{\set{1}}$, $\set{\set{2}}$, $\set{\set{1, 2}}$ and $\set{\set{1}, \set{2}}$.

Non-example: the function $x \oplus y$, equal to $1$ exactly when $x \ne y$, is not monotone.
Indeed $(1, 0) \le (1, 1)$ but $f(1, 0) = 1 > 0 = f(1, 1)$.
