---
tag: G653QANYYD
kind: definition
name: Set of uniqueness
msc: [42A63]
defines: K7CNWXF9SN
uses: [FZK2M8KGXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Set_of_uniqueness
---

## Definition

Let $\mathbb{T} = \R / 2\pi\Z$ be the circle.
A subset $E \subset \mathbb{T}$ is a *set of uniqueness* if the following holds.
Whenever a [[trigonometric series|FZK2M8KGXQ]] $\sum_{n \in \Z} c_n e^{inx}$ with complex coefficients satisfies
$$\lim_{N \to \infty} \sum_{n=-N}^{N} c_n e^{inx} = 0 \quad \text{for every } x \in \mathbb{T} \setminus E,$$
then $c_n = 0$ for all $n \in \Z$.
A subset of $\mathbb{T}$ that is not a set of uniqueness is a *set of multiplicity*.

## Remarks

Sets of uniqueness are often called U-sets, and sets of multiplicity M-sets.
A subset of a set of uniqueness is again a set of uniqueness.

Example: the empty set is a set of uniqueness; this is [[Cantor's uniqueness theorem|NSS3XW4BYZ]].
Every [[countable set|01TQB88H4C]] is also a set of uniqueness, a result of W. H. Young.

Non-example: let $E$ contain an open arc $I$ of $\mathbb{T}$.
Choose a nonzero infinitely differentiable function $g$ on $\mathbb{T}$ that vanishes outside $I$.
Its Fourier series converges absolutely to $g$ at every point, so it converges to $0$ outside $E$.
Its coefficients are not all $0$, because $g \ne 0$, so $E$ is a set of multiplicity.

More generally every set of positive Lebesgue measure is a set of multiplicity, and a Borel set of uniqueness has measure zero.
The converse fails: [[Menshov's example|AW16MYJV5Q]] is a closed set of measure zero that is a set of multiplicity.
The middle-thirds [[Cantor set|0BXNDZFQME]] is a set of uniqueness.
