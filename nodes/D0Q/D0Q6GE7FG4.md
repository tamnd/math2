---
tag: D0Q6GE7FG4
kind: definition
name: Solvmanifold
msc: ["22E25", 22F30, 53C30]
defines: HBDEPTRF11
uses: [9CNSVFQ801, 85TWR6E75P, 7JBRGCVJRB]
sources:
  - url: https://en.wikipedia.org/wiki/Solvmanifold
---

## Definition

Let $G$ be a connected [[solvable Lie group|9CNSVFQ801]] and let $H$ be a closed subgroup of $G$.
The [[homogeneous space|85TWR6E75P]] $G/H$, with its manifold structure as a quotient of [[Lie groups|7JBRGCVJRB]], is a *solvmanifold*.
Equivalently, a solvmanifold is a manifold with a smooth transitive action of a connected solvable Lie group.

## Remarks

Example: $G$ the group of maps $x \mapsto ax + b$ of $\R$ with $a > 0$ and $b \in \R$.
It is solvable, since its commutator subgroup lies in the abelian group of translations.
It acts transitively on $\R$, and the stabilizer of $0$ is the closed subgroup $H = \set{x \mapsto ax}$.
So $\R \cong G/H$ is a solvmanifold.

Non-example: the presentation $S^2 = \mathrm{SO}(3)/\mathrm{SO}(2)$ does not show that $S^2$ is a solvmanifold, because $\mathrm{SO}(3)$ is not solvable: its Lie algebra $\mathfrak{so}(3)$ is simple.

Many authors call only the compact quotients $G/\Gamma$ by a discrete subgroup $\Gamma$ solvmanifolds.
Each nilmanifold is a solvmanifold, since nilpotent groups are solvable.
