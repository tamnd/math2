---
tag: 8APGCB1CKH
kind: definition
name: Specialization preorder
msc: [54D10, 06A06]
defines: CMYVK9CEKZ
uses: [0CQHFPGJ45, 0QEAJB91GZ, 0VABYWJWH9]
sources:
  - url: https://en.wikipedia.org/wiki/Specialization_(pre)order
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
For $y \in X$, write $\overline{\set{y}}$ for the [[closure|0QEAJB91GZ]] of $\set{y}$.
The *specialization preorder* on $X$ is the relation $\le$ defined by
$$x \le y \iff x \in \overline{\set{y}}, \qquad x, y \in X.$$

## Remarks

The relation is a [[preorder|0VABYWJWH9]]: $x \in \overline{\set{x}}$, and if $x \in \overline{\set{y}}$ and $y \in \overline{\set{z}}$ then $\overline{\set{y}} \subseteq \overline{\set{z}}$, so $x \in \overline{\set{z}}$.
Equivalently, $x \le y$ if and only if every open set that contains $x$ also contains $y$.

The preorder is antisymmetric, hence a partial order, if and only if $X$ is a [[T0 space|07SG12TQH3]].
It is the equality relation if and only if every point of $X$ is closed, that is, $X$ is T1.
Every continuous map is monotone for the specialization preorders.

Example: in the spectrum of a commutative ring with the Zariski topology, the closure of a prime $\mathfrak q$ is the set of primes that contain $\mathfrak q$.
So $\mathfrak p \le \mathfrak q$ holds exactly when $\mathfrak q \subseteq \mathfrak p$.

Non-example: on $X = \set{a, b}$ with the indiscrete topology, $a \le b$ and $b \le a$ but $a \ne b$.
So the specialization preorder is not a partial order, and indeed $X$ is not T0.

Some authors use the opposite convention, with $x \le y$ when $y \in \overline{\set{x}}$.
