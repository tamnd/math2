---
tag: A71EWRZBZV
kind: definition
name: Shift space
msc: [37B10]
defines: A1XE59ZHNM
uses: [0GBG8B49AA, 0TVJZYB6SH, 0QT00PB5G2, CV013KHVJG]
sources:
  - url: https://en.wikipedia.org/wiki/Shift_space
---

## Definition

Let $\mathcal{A}$ be a finite set, the alphabet, with the discrete topology, and give $\mathcal{A}^{\Z}$ the [[product topology|0GBG8B49AA]].
The *shift map* $\sigma \colon \mathcal{A}^{\Z} \to \mathcal{A}^{\Z}$ is $\sigma(x)_i = x_{i+1}$ for $x = (x_i)_{i \in \Z}$.
A *shift space* (or *subshift*) over $\mathcal{A}$ is a subset $X \subseteq \mathcal{A}^{\Z}$ such that:

1. $X$ is closed in $\mathcal{A}^{\Z}$.
2. $\sigma(X) = X$.

## Remarks

The space $\mathcal{A}^{\Z}$ is [[compact|0TVJZYB6SH]], with the metric $d(x, y) = 2^{-\min\set{\abs{i} : x_i \neq y_i}}$ for $x \neq y$, and $\sigma$ is a [[homeomorphism|0QT00PB5G2]]; so $\sigma$ restricts to a homeomorphism of each shift space.
The whole space $\mathcal{A}^{\Z}$ is the *full shift*.
Equivalent form: $X$ is a shift space if and only if it is defined by a set $\mathcal{F}$ of forbidden words.
Here $\mathcal{F}$ is a set of finite words, elements of the [[free monoid|CV013KHVJG]] on $\mathcal{A}$.
Then $X$ is the set of sequences in which no word of $\mathcal{F}$ occurs as a block of consecutive symbols.
One-sided shift spaces are defined in the same way in $\mathcal{A}^{\N}$, with $\sigma(X) \subseteq X$.
Example: the golden mean shift $X \subseteq \set{0, 1}^{\Z}$, the sequences with no block $11$.
A limit of such sequences has no block $11$, since a block $11$ at positions $i, i+1$ would appear in the sequences close to it.
So $X$ is closed, and shifting does not create or remove blocks, so $\sigma(X) = X$.
Non-example: the set of sequences in $\set{0, 1}^{\Z}$ with exactly one symbol $1$ satisfies clause 2, but not clause 1.
Its elements with the $1$ at position $n$ tend to the all-$0$ sequence as $n \to \infty$, which is not in the set.

## Explanations

### L1 human

A shift space is a closed, shift-invariant set of two-sided infinite sequences over a finite alphabet.
