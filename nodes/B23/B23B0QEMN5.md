---
tag: B23B0QEMN5
kind: statement
role: theorem
name: Szemerédi's theorem
msc: [11B25, 05D10, 11B30]
uses: [0T3RZQXDYD]
about: [G5TWXV565S]
sources:
  - url: https://en.wikipedia.org/wiki/Szemer%C3%A9di%27s_theorem
same_as:
  wikidata: Q1046232
  wikipedia: Szemerédi's theorem
---

## Statement

Let $A$ be a set of positive integers with positive upper density, that is,
$$\limsup_{N \to \infty} \frac{\abs{A \cap \set{1, \dots, N}}}{N} > 0,$$
where $\limsup$ is the [[limit superior|0T3RZQXDYD]].
Then for every integer $k \ge 1$, the set $A$ contains an arithmetic progression $a, a + d, \dots, a + (k-1)d$ of length $k$ with $d \ge 1$.

## Remarks

An equivalent finite form reads as follows.
For every $k \ge 1$ and $\delta > 0$ there is $N_0$ such that the following holds for all $N \ge N_0$.
Each subset of $\set{1, \dots, N}$ with at least $\delta N$ elements contains an arithmetic progression of length $k$.
Szemerédi's original proof is combinatorial and introduced the [[Szemerédi regularity lemma|ETMAPNQY7T]].
Other proofs use ergodic theory (Furstenberg's multiple recurrence theorem), higher-order Fourier analysis with [[Gowers norms|ZBFZGA1J5G]], and hypergraph regularity.
The case $k = 3$ is [[Roth's theorem on arithmetic progressions|E7H8NWXESF]].
The density hypothesis cannot simply be dropped: the infinite set of powers of $2$ has density zero and contains no three-term arithmetic progression.
The primes also have density zero, so the theorem does not apply to them directly; the [[Green–Tao theorem|H8BAHWSEMC]] handles them separately.

## Explanations

### L1 human

If a set of whole numbers takes up a fixed positive fraction of the numbers, then it contains evenly spaced patterns of every length.
For example, it must contain three numbers like $10, 17, 24$, four numbers like $3, 8, 13, 18$, and so on.
This holds even if the set looks very irregular.

### L2 human

Szemerédi's theorem is the density version of [[van der Waerden's theorem|V96FRZ2ME1]]: in a finite colouring one colour class has positive upper density, so it contains long progressions.
It is a central theorem of [[additive combinatorics|3NM362A2JG]], and the search for good quantitative bounds led to Gowers norms and much of the modern theory.
The ergodic proof opened the field of ergodic Ramsey theory, with polynomial and multidimensional extensions.
