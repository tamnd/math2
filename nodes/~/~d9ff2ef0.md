---
tag: ~d9ff2ef0
kind: statement
role: theorem
name: First Sylow theorem
msc: [20D20]
uses: [~496347af, ~f2158ffa, ~28340638]
sources:
  - url: https://en.wikipedia.org/wiki/Sylow_theorems
    locator: Statement
---

## Statement

Let $G$ be a finite [[group|G5S1M9]], let $p$ be a prime number, and let $k \geq 0$ with $p^k \mid |G|$.
Then $G$ has a [[subgroup|~b600248b]] of order $p^k$.
In particular, $G$ has a [[Sylow p-subgroup|~e7f618d0]].

## Remarks

For $k = 1$, this is [[Cauchy's theorem|~f2158ffa]].
Let $p^n$ be the largest power of $p$ that divides $|G|$. A proof by Wielandt lets $G$ act by left multiplication on the subsets of $G$ of size $p^n$.
For example, a group of order $12$ has a subgroup of order $4$ and a subgroup of order $3$.

## History

Ludwig Sylow proved the Sylow theorems in 1872, and he published them in Mathematische Annalen.

## Explanations

### L1 human

The converse of Lagrange's theorem is false in general.
But it is true for prime powers: each prime power that divides the order of the group is the order of a subgroup.
The largest such subgroups are the Sylow subgroups.
