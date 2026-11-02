---
tag: 4SBZ4EMPBZ
kind: statement
role: theorem
name: Maschke's theorem
msc: [20C05, 16S34, 16D60]
uses: [G5S1M9, MNP2HBWB5Q, WYGRXCG2RN, 0F6ES3BRYP, NY25HXA478]
about: [MNP2HBWB5Q, WYGRXCG2RN]
sources:
  - url: https://en.wikipedia.org/wiki/Maschke%27s_theorem
same_as:
  wikidata: Q656198
  wikipedia: Maschke's theorem
---

## Statement

Let $G$ be a finite [[group|G5S1M9]] and let $F$ be a field whose [[characteristic|0F6ES3BRYP]] does not divide the order $\abs{G}$.
Let $V$ be a [[representation|WYGRXCG2RN]] of $G$ over $F$, that is, a module over the [[group algebra|MNP2HBWB5Q]] $F[G]$.
Then every $G$-invariant subspace $W$ of $V$ has a $G$-invariant complement $W'$ with $V = W \oplus W'$.
Equivalently, the group algebra $F[G]$ is a [[semisimple ring|NY25HXA478]].

## Remarks

Take any linear projection $p \colon V \to W$ onto $W$ and average it over the group:
$$\tilde{p}(v) = \frac{1}{\abs{G}} \sum_{g \in G} g \, p(g^{-1} v).$$
The division by $\abs{G}$ is allowed by the hypothesis on the characteristic, $\tilde{p}$ is $G$-equivariant and is still a projection onto $W$, and $W' = \ker \tilde{p}$ is the required complement.
For example, every finite-dimensional complex representation of a finite group is a direct sum of irreducible representations.
The hypothesis is necessary: let $G = \set{1, g}$ have order $2$ and $F = \F_2$, acting on $F^2$ by swapping coordinates.
The line spanned by $(1, 1)$ is invariant, but it is the only invariant line, so it has no invariant complement.

## Explanations

### L1 human

Let a finite group act linearly on a space, and suppose one can divide by the size of the group.
Then an invariant piece can always be split off cleanly from the rest.
So each representation breaks into irreducible building blocks.
This is the reason why representations of finite groups over the complex numbers are so well behaved.

### L2 human

By the Artin–Wedderburn theorem, Maschke's theorem gives $\C[G] \cong M_{n_1}(\C) \times \cdots \times M_{n_k}(\C)$, which leads to $\abs{G} = \sum n_i^2$ and to character theory.
The converse also holds: if the characteristic of $F$ divides $\abs{G}$, then $F[G]$ is not semisimple.
Indeed, $N = \sum_{g \in G} g$ spans a nonzero two-sided ideal with $N^2 = \abs{G} N = 0$.
A semisimple ring has no such nilpotent ideal.
That case is the subject of modular representation theory.
The averaging argument also works for compact groups with the Haar integral in place of the sum.
