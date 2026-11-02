---
tag: 3FYQZ4R6T8
kind: definition
name: Continuous geometry
msc: [06C20, 51A05]
defines: 5CET1KWWWH
uses: [QX7WZ92QAK, D7A0ZGZT5S, ZT47BK9Y6K, 0S8FE7ZMFM]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_geometry
---

## Definition

Let $L$ be a lattice with join $\vee$ and meet $\wedge$.
The lattice $L$ is a *continuous geometry* if:

1. $L$ is a [[modular lattice|QX7WZ92QAK]];
2. $L$ is a [[complete lattice|D7A0ZGZT5S]], with least element $0$ and greatest element $1$;
3. $L$ is [[complemented|ZT47BK9Y6K]];
4. for every [[chain|0S8FE7ZMFM]] $C \subseteq L$ and every $b \in L$,
$$b \wedge \bigvee_{c \in C} c = \bigvee_{c \in C} (b \wedge c) \quad\text{and}\quad b \vee \bigwedge_{c \in C} c = \bigwedge_{c \in C} (b \vee c);$$
5. $L$ is irreducible: the only elements of $L$ that have exactly one complement are $0$ and $1$.

## Remarks

Some authors omit the irreducibility clause 5 and call the irreducible ones continuous geometries in the strict sense.

Example: the lattice of subspaces of $D^n$ for a division ring $D$ and $n \ge 2$.
It is modular and complemented; it is complete and clause 4 holds because every chain in it is finite.
It is irreducible: a subspace $U \ne 0, D^n$ has more than one complement.
Indeed, a complement $W$ can be changed by adding a nonzero vector of $U$ to one basis vector of $W$.

Non-example: the lattice of all subsets of a set $X$ with at least two elements.
It satisfies clauses 1 to 4, but every subset has exactly one complement, so clause 5 fails.

Von Neumann proved that a continuous geometry has a dimension function $d \colon L \to [0, 1]$ with $d(0) = 0$, $d(1) = 1$ and $d(a \vee b) + d(a \wedge b) = d(a) + d(b)$.
Moreover $d(a) = d(b)$ if and only if $a$ and $b$ have a common complement.
Its range is either $\set{0, 1/n, \dots, 1}$ for some $n \ge 1$ or the whole interval $[0, 1]$.
