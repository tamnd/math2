---
tag: RDZGJ21WRX
kind: statement
role: theorem
name: Jordan–Zassenhaus theorem
msc: [16H20, 16G30, 11R54]
uses: [MWBDFS2KJ5, 1ZBX4TKVZ9, NY25HXA478, 05QY1VEBYD, KTKK9B1X41]
about: [1ZBX4TKVZ9]
sources:
  - url: https://en.wikipedia.org/wiki/Order_(ring_theory)
---

## Statement

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] with ring of integers $R$.
Let $A$ be a finite-dimensional [[semisimple|NY25HXA478]] algebra over $K$, and let $\Lambda$ be an $R$-[[order|1ZBX4TKVZ9]] in $A$.
A *$\Lambda$-lattice* is a [[finitely generated|05QY1VEBYD]] left $\Lambda$-module that is torsion-free as an $R$-module.
Then for every finitely generated left $A$-module $V$ there are only finitely many isomorphism classes of $\Lambda$-lattices $M$ with $K \otimes_R M \cong V$.

## Remarks

The proof combines a reduction theory for lattices with the finiteness of the class number.
In outline, one fixes a lattice $M_0$ with $K \otimes_R M_0 \cong V$ and finds a nonzero $c \in R$ such that every lattice $M$ with $K \otimes_R M \cong V$ is isomorphic to a lattice $N$ with $c M_0 \subseteq N \subseteq M_0$.
There are only finitely many such $N$, because $M_0 / c M_0$ is finite.
Example: take $A = K$, $\Lambda = R$ and $V = K$.
The $\Lambda$-lattices with $K M \cong K$ are the nonzero fractional ideals of $R$, up to isomorphism, so in this case the theorem is the finiteness of the [[class number|KTKK9B1X41]] of $K$.
Example: take $K = \Q$ and $\Lambda = \Z G$ for a finite group $G$; there are finitely many $\Z G$-lattices of each $\Z$-rank $n$ up to isomorphism.
Together with Minkowski's bound on the orders of finite subgroups of $GL_n(\Z)$, it follows that $GL_n(\Z)$ has only finitely many conjugacy classes of finite subgroups.

## Explanations

### L1 human

An order is a ring of integers inside an algebra, and a lattice over it is a module shaped like a grid.
Over a field, a module is determined by little more than its dimension, but grids can differ in subtle arithmetic ways.
The theorem says that only finitely many different grids, counted up to isomorphism, fill out a given module.
For the integers of a number field this is the classical fact that there are only finitely many ideal classes.

### L2 human

The theorem is the basic finiteness result of integral representation theory.
It lets one define the class number of an order, the number of isomorphism classes of lattices in a given genus.
This number can then be studied with adelic methods.
It extends to any Dedekind domain whose field of fractions is a global field, with $A$ a separable algebra.
Applied to integral group rings, it controls the integral representations of finite groups, and in crystallography it gives the finiteness of arithmetic classes of finite subgroups of $GL_n(\Z)$.
