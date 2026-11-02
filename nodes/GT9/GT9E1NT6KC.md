---
tag: GT9E1NT6KC
kind: definition
name: Polar set
msc: [31B15, 31A15, 31C15]
defines: C95QJ7YH5T
uses: [Z1MHMGFNFW]
sources:
  - url: https://en.wikipedia.org/wiki/Polar_set_(potential_theory)
---

## Definition

Let $n \ge 2$ and let $Z \subseteq \R^n$.
The set $Z$ is *polar* if there is a [[subharmonic function|Z1MHMGFNFW]] $u$ on $\R^n$, not identically $-\infty$, such that
$$Z \subseteq \set{ x \in \R^n : u(x) = -\infty }.$$

## Remarks

Example: in $\R^2$, the function $u(x) = \log \abs{x - a}$ is subharmonic, not identically $-\infty$, and equals $-\infty$ exactly at $a$, so $\set{a}$ is polar.
In $\R^n$ with $n \ge 3$ the function $u(x) = -\abs{x - a}^{2-n}$ plays the same role.
A countable union of polar sets is polar, so every countable subset of $\R^n$ is polar.

Non-example: the segment $[0, 1] \times \set{0}$ in $\R^2$ is not polar, because it has positive logarithmic capacity $1/4$.

Polarity is a local property.
A set $Z$ is polar if and only if each point of $Z$ has a neighbourhood $U$ with the following property.
Some subharmonic function on $U$, not identically $-\infty$ on any component, equals $-\infty$ on $Z \cap U$.
For Borel sets, being polar is equivalent to having capacity zero.
A polar set has Lebesgue measure zero.
