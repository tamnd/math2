---
tag: NE2K5HAEFN
kind: statement
role: theorem
name: Whitehead's lemmas
msc: [17B56, 17B20]
uses: [69NARSMQCM, EY9DN7QAX1, TZAZ163QGK]
about: [69NARSMQCM, EY9DN7QAX1]
sources:
  - url: https://en.wikipedia.org/wiki/Whitehead%27s_lemma_(Lie_algebra)
same_as:
  wikidata: Q16934830
  wikipedia: Whitehead's lemma (Lie algebra)
---

## Statement

Let $\mathfrak{g}$ be a finite-dimensional [[semisimple Lie algebra|EY9DN7QAX1]] over a field $k$ of characteristic $0$.
Let $V$ be a finite-dimensional [[representation|TZAZ163QGK]] of $\mathfrak{g}$, that is, a finite-dimensional $\mathfrak{g}$-module.
Write $H^n(\mathfrak{g}, V)$ for the $n$-th [[Lie algebra cohomology|69NARSMQCM]] group of $\mathfrak{g}$ with coefficients in $V$.

1. (First Whitehead lemma) $H^1(\mathfrak{g}, V) = 0$.
2. (Second Whitehead lemma) $H^2(\mathfrak{g}, V) = 0$.

## Remarks

For an irreducible module $V$ on which $\mathfrak{g}$ acts nontrivially, the Casimir element of $V$ acts on $V$ by a nonzero scalar.
It also acts by zero on the cohomology, so all cohomology groups $H^n(\mathfrak{g}, V)$ vanish.
For the trivial module $k$, one has $H^1(\mathfrak{g}, k) \cong (\mathfrak{g}/[\mathfrak{g}, \mathfrak{g}])^*$, which is zero because $\mathfrak{g} = [\mathfrak{g}, \mathfrak{g}]$.
The vanishing of $H^2(\mathfrak{g}, k)$ uses the nondegeneracy of the Killing form.
A long exact sequence argument then passes from irreducible modules to all finite-dimensional modules.

The hypothesis of semisimplicity is necessary.
For the one-dimensional abelian Lie algebra $\mathfrak{g} = k$ and the trivial module $k$, every linear form on $\mathfrak{g}$ is a $1$-cocycle and the only coboundary is $0$, so $H^1(\mathfrak{g}, k) \cong k \neq 0$.
The lemmas do not extend to $H^3$: for a simple Lie algebra $\mathfrak{g}$, the $3$-form $(x, y, z) \mapsto \kappa([x, y], z)$ built from the Killing form $\kappa$ gives a nonzero class in $H^3(\mathfrak{g}, k)$.

## Explanations

### L1 human

Lie algebra cohomology measures how far certain linear equations involving the bracket are from being solvable.
The first and second cohomology groups control derivations and extensions.
Whitehead's lemmas say that for a semisimple Lie algebra in characteristic zero, these two groups are always zero.
So every problem of this kind has a solution: every derivation into a module is inner, and every extension by a module splits.

### L2 human

The first lemma gives a quick proof of Weyl's theorem on complete reducibility.
A submodule $W \subseteq V$ gives an extension of $\mathfrak{g}$-modules, and the obstruction to a complement lies in $H^1(\mathfrak{g}, \Hom(V/W, W))$, which is zero.
The second lemma is the key step in the proof of the Levi decomposition.
An abelian extension of a semisimple Lie algebra is classified by $H^2$, so it splits, and induction on the radical gives a semisimple complement.
