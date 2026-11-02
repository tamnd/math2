---
tag: MG20HMMYKY
kind: statement
role: theorem
name: Borel fixed-point theorem
msc: [20G15, 14L30]
uses: [GA81VVQHEP, 0FXJ7YFMMX, RW85C34GQW, HV6YBS0YDH, 9537RKBZPP, 0RRWNMYRXC]
about: [GA81VVQHEP, RW85C34GQW]
sources:
  - url: https://en.wikipedia.org/wiki/Borel_fixed-point_theorem
same_as:
  wikidata: Q4944908
  wikipedia: Borel fixed-point theorem
---

## Statement

Let $k$ be an algebraically closed field.
Let $G$ be a connected [[solvable|0FXJ7YFMMX]] [[linear algebraic group|GA81VVQHEP]] over $k$.
Let $X$ be a nonempty complete [[variety|HV6YBS0YDH]] over $k$ with an [[action|RW85C34GQW]] of $G$.
Then $G$ has a [[fixed point|0RRWNMYRXC]] in $X$.

## Remarks

The proof goes by induction on $\dim G$.
The derived group $G'$ is connected, normal and of smaller dimension, so its fixed-point set $Y = X^{G'}$ is nonempty, and it is closed, hence complete.
The group $G$ acts on $Y$, and an orbit of minimal dimension $G \cdot y$ is closed, so it is complete.
The stabilizer $G_y$ contains $G'$, so it is normal and $G / G_y$ is an affine group.
The orbit map gives a bijective morphism from $G / G_y$ onto the complete orbit $G \cdot y$, and one checks that $G / G_y$ is then complete as well.
A connected variety that is both affine and complete is a point, so the orbit is a point and $y$ is fixed.

Example: a connected solvable closed subgroup $H$ of $\mathrm{GL}_n$ acts on the variety of full flags in $k^n$, which is complete.
The theorem gives a flag fixed by $H$, and this proves the Lie–Kolchin theorem: $H$ is conjugate to a subgroup of the group $B$ of invertible upper triangular matrices.

Completeness is needed: $\mathbb{G}_m$ acts on $\mathbb{A}^1 \setminus \set{0}$ by multiplication without a fixed point.
Solvability is needed: $\mathrm{SL}_2$ acts on $\mathbb{P}^1$ transitively, so without a fixed point.
Connectedness is needed: the group $\Z / 2$ swaps the two points of a two-point variety.

## Explanations

### L1 human

A connected solvable group acting on a complete variety always leaves some point where it is.
Complete varieties, like projective space, have no "escape to infinity", so the group cannot push every point away.
The theorem is the algebraic analogue of fixed-point theorems for compact spaces.

### L2 human

The theorem is the basic tool for Borel subgroups.
Applied to a Borel subgroup $B$ acting on $G / P$, it shows that $B$ is conjugate into every parabolic subgroup $P$.
It gives the conjugacy of all [[Borel subgroups|5JSYA1JNCC]], and with it the conjugacy of maximal tori.
It also gives the Lie–Kolchin theorem on triangularizing connected solvable matrix groups.
