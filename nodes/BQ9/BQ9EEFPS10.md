---
tag: BQ9EEFPS10
kind: example
name: The full relation algebra on a set
msc: ["03G15"]
topics: [QYA4H5Y7VR]
audience: research
instance_of: [GQK4DSA11K, KCG48CWY69]
uses: [RDSY11X6N2, 05AVARPXA2, 0PYSR20HGF, 054K3HNN5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Relation_algebra
---

## Example

Let $U$ be a set and let $\mathrm{Re}(U)$ be the set of all [[binary relations|05AVARPXA2]] on $U$, that is, $\mathcal{P}(U \times U)$.
Take union, intersection and complement in $U \times U$, the [[composition|0PYSR20HGF]] $R ; S$, the [[converse|054K3HNN5Z]] $\breve{R}$ and the identity relation $1' = \set{(u, u) : u \in U}$.
Remark 1 of [[the definition|RDSY11X6N2]] checks clause 6, and clauses 1 to 5 are the usual laws of relations.
So $\mathrm{Re}(U)$ is a [[relation algebra|GQK4DSA11K]].

Take $U = \set{a, b}$.
The algebra has $16$ elements, and its atoms are the four pairs $\set{(a, a)}$, $\set{(a, b)}$, $\set{(b, a)}$ and $\set{(b, b)}$.
The diversity element is $0' = \set{(a, b), (b, a)}$, and $0' ; 0' = 1'$, $1' ; 0' = 0'$.
The cycle law for $x = \set{(a, b)}$, $y = \set{(b, a)}$ and $z = \set{(a, a)}$ reads:

1. $(x ; y) \wedge z = \set{(a, a)} \ne 0$;
2. $(\breve{x} ; z) \wedge y = \set{(b, a)} \ne 0$;
3. $(z ; \breve{y}) \wedge x = \set{(a, b)} \ne 0$.

All three are nonzero together, as the law requires.

## Remarks

1. The four elements $0, 1', 0', 1$ form a subalgebra, since $0' ; 0' = 1'$ on two points; it is isomorphic to the algebra of subsets of the group $\mathbb{Z}/2$.
2. $\mathrm{Re}(U)$ is simple for $U \ne \emptyset$: for $x \ne 0$ one has $1 ; x ; 1 = 1$.
3. $\mathrm{Re}(U)$ is complete and atomic, with $|U|^2$ atoms.
4. On three points, $0' ; 0' = 1$, which is the main difference from two points.
5. Every representable relation algebra embeds in a product of algebras $\mathrm{Re}(U)$.

## Explanations

### L1 human

All relations on a fixed set form a relation algebra.
Its elements are sets of pairs, and the operations are the usual operations on relations.

### L2 human

1. On $U = \set{a, b}$, let $R = \set{(a, b), (b, b)}$.
2. $R ; R = \set{(a, b), (b, b)} = R$, so $R$ is transitive.
3. $\breve{R} ; R = \set{(b, b)}$, which is below $1'$, so $R$ is a function: each point has at most one image.
4. $R ; \breve{R} = 1$, which is above $1'$, so $R$ is total; it is not below $1'$, so $R$ is not injective.

The typical use: the full relation algebra is the model in which every abstract law is tested first.
The trap: $R ; \breve{R} \ge 1'$ says that $R$ is total, while $\breve{R} ; R \le 1'$ says that $R$ is a partial function; the two are easy to swap.
