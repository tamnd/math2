---
tag: S49XMZKGQC
kind: example
name: Tsirelson space
msc: [46B03, 46B45]
instance_of: [06GZ956657]
uses: [06GZ956657, NN8RWPC8WG, 08P6T2WH6R]
sources:
  - url: https://en.wikipedia.org/wiki/Tsirelson_space
same_as:
  wikidata: Q7849771
  wikipedia: Tsirelson space
---

## Example

Let $c_{00}$ be the space of real sequences with finitely many nonzero terms.
For finite sets $E, F \subset \N$, write $E < F$ when $\max E < \min F$.
For $x \in c_{00}$ and a finite set $E$, let $E x$ be the sequence equal to $x$ on $E$ and to $0$ off $E$.
Call finite sets $E_1, \dots, E_n$ admissible when $n \le \min E_1$ and $E_1 < E_2 < \cdots < E_n$.
There is exactly one norm on $c_{00}$ that satisfies
$$\norm{x} = \max \Big( \norm{x}_\infty, \ \frac{1}{2} \sup \sum_{j=1}^n \norm{E_j x} \Big),$$
where the supremum runs over all $n$ and all admissible $E_1, \dots, E_n$.
The completion $T$ of $c_{00}$ for this norm is the Tsirelson space.
It is a [[Banach space|06GZ956657]].

Check of two values.
For a unit vector $e_k$, at most one set $E_j$ meets $k$, so the sum is at most $\norm{e_k}$, and the equation gives $\norm{e_k} = 1$.
For $x = e_{n+1} + \cdots + e_{2n}$, the sets $\set{n+1}, \dots, \set{2n}$ are admissible, so $n/2 \le \norm{x} \le n$.

## Remarks

The unit vectors form an unconditional basis of $T$, and $T$ is [[reflexive|NN8RWPC8WG]].
The space $T$ contains no subspace isomorphic to $c_0$ or to any [[sequence space|08P6T2WH6R]] $\ell^p$ with $1 \le p < \infty$.
Tsirelson built the first space with this property in 1974.
The space above, described by Figiel and Johnson, is the dual of Tsirelson's original space.
The second check shows how the norm forces blocks far out in the sequence to behave like $\ell^1$ of their length.

## Explanations

### L1 human

For a long time it was open whether every Banach space contains a copy of one of the classical sequence spaces.
Tsirelson space shows that the answer is no.
Its norm is defined by an equation that refers to itself.
This rule makes the space look like $\ell^1$ on short blocks and stops it from containing any classical space as a whole.
