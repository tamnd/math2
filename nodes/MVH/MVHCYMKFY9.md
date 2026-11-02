---
tag: MVHCYMKFY9
kind: statement
role: theorem
name: Bockstein spectral sequence
msc: [55T05, 55S05]
uses: [H7PCM776GR, VXDPP4EJPG, M0Q5CFJ7ZH, XT7VWNTKGB]
about: [H7PCM776GR]
sources:
  - url: https://en.wikipedia.org/wiki/Bockstein_spectral_sequence
same_as:
  wikidata: Q4936293
  wikipedia: Bockstein spectral sequence
---

## Statement

Let $p$ be a prime and let $X$ be a space whose integral [[singular homology|M0Q5CFJ7ZH]] groups $H_n(X; \Z)$ are finitely generated for every $n$.
Then there is a [[spectral sequence|GG8AYV847V]] $(E^r_n, d^r)_{r \ge 1}$ with $d^r \colon E^r_n \to E^r_{n-1}$ such that:

1. $E^1_n = H_n(X; \F_p)$, the [[homology with coefficients|XT7VWNTKGB]] in $\F_p$, and $d^1$ is the [[Bockstein homomorphism|H7PCM776GR]] of $0 \to \Z/p \to \Z/p^2 \to \Z/p \to 0$;
2. $E^\infty_n = E^r_n$ for $r$ large, and $E^\infty_n \cong \big(H_n(X; \Z) / \mathrm{torsion}\big) \otimes \F_p$;
3. each direct summand $\Z/p^r$ of $H_{n-1}(X; \Z)$ gives classes in $E^r_n$ and $E^r_{n-1}$ joined by a nonzero $d^r$.
All nonzero $d^r$ arise in this way.

## Remarks

The spectral sequence comes from an [[exact couple|VXDPP4EJPG]] with $D = H_*(X; \Z)$ and $E = H_*(X; \F_p)$.
The map $D \to D$ is multiplication by $p$, and the other two maps come from the long exact sequence of $0 \to \Z \xrightarrow{p} \Z \to \Z/p \to 0$.

Example: for $X = \R P^2$ and $p = 2$, one has $H_1(X; \Z) = \Z/2$ and $H_2(X; \Z) = 0$.
Here $E^1_1 = E^1_2 = \F_2$ and $d^1 \colon E^1_2 \to E^1_1$ is an isomorphism, so $E^2_n = 0$ for $n = 1, 2$, which matches $E^\infty$ since the free part of $H_n(X; \Z)$ vanishes for $n = 1, 2$.

The finite generation hypothesis ensures that the spectral sequence stops at a finite page in each degree.
For a summand such as $\Z[1/p]$ or $\Z/p^\infty$ the description in terms of $E^\infty$ changes.

## Explanations

### L1 human

Mod $p$ homology is easy to compute but forgets how large the torsion of integral homology is.
The Bockstein spectral sequence recovers this: a summand $\Z/p^r$ shows up as a pair of mod $p$ classes that survive exactly $r$ pages before cancelling.
What survives to the end is the free part of integral homology.

### L2 human

The spectral sequence is used to detect higher torsion, for instance in the homology of Lie groups, loop spaces and Eilenberg–MacLane spaces.
In cohomology it is multiplicative, and the higher Bocksteins interact with Steenrod operations, which gives restrictions on how torsion can appear.
It is one of the simplest examples of a spectral sequence built from an exact couple.
