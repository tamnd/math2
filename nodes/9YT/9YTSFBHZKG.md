---
tag: 9YTSFBHZKG
kind: statement
role: theorem
name: Serre's theorem on semisimple Lie algebras
msc: ["17B20", "17B22"]
uses: [AVVV93CASN, CSBM217V1N, H59F1XBDZP, NNAXK7BM3H, EY9DN7QAX1, BB098JPWGA, AR0D7V1J8T]
about: [EY9DN7QAX1, H59F1XBDZP]
sources:
  - url: https://en.wikipedia.org/wiki/Serre%27s_theorem_on_a_semisimple_Lie_algebra
same_as:
  wikidata: Q97359412
  wikipedia: Serre's theorem on a semisimple Lie algebra
---

## Statement

Let $F$ be an algebraically closed field of characteristic $0$.
Let $\Phi$ be a [[root system|AVVV93CASN]] with a base $\set{\alpha_1, \dots, \alpha_l}$ of [[simple roots|CSBM217V1N]].
Let $a_{ij} = \langle \alpha_i, \alpha_j \rangle$ be the entries of its [[Cartan matrix|H59F1XBDZP]].
Let $\mathfrak{g}$ be the quotient of the [[free Lie algebra|NNAXK7BM3H]] on $3l$ generators $e_i, f_i, h_i$ by the following relations, for all $i, j$:

1. $[h_i, h_j] = 0$;
2. $[e_i, f_i] = h_i$, and $[e_i, f_j] = 0$ for $i \ne j$;
3. $[h_i, e_j] = a_{ji} e_j$ and $[h_i, f_j] = -a_{ji} f_j$;
4. $(\operatorname{ad} e_i)^{1 - a_{ji}} (e_j) = 0$ and $(\operatorname{ad} f_i)^{1 - a_{ji}} (f_j) = 0$ for $i \ne j$.

Then $\mathfrak{g}$ is a finite-dimensional [[semisimple Lie algebra|EY9DN7QAX1]].
The span $\mathfrak{h}$ of $h_1, \dots, h_l$ is a [[Cartan subalgebra|BB098JPWGA]] of $\mathfrak{g}$, and the root system of $\mathfrak{g}$ with respect to $\mathfrak{h}$ is isomorphic to $\Phi$.

## Remarks

The proof first studies the algebra with only relations 1 to 3, which splits as $\mathfrak{n}^- \oplus \mathfrak{h} \oplus \mathfrak{n}^+$ with $\mathfrak{n}^\pm$ free on the $e_i$ or the $f_i$.
Relations 4 generate ideals there, and in the quotient the operators $\operatorname{ad} e_i$ and $\operatorname{ad} f_i$ are locally nilpotent.
This makes the Weyl group act, which bounds the weights by $\Phi$ and gives finite dimension.
Example: for $\Phi = A_1$ there is one generator of each kind, and the relations give $[h, e] = 2e$, $[h, f] = -2f$, $[e, f] = h$, so $\mathfrak{g} = \mathfrak{sl}_2(F)$.
Relations 4 are needed: without them the algebra is infinite-dimensional as soon as $l \ge 2$, for example $(\operatorname{ad} e_1)^n (e_2) \ne 0$ for all $n$.
Since every semisimple Lie algebra satisfies these relations for suitable generators, it is isomorphic to the algebra built from its own root system.
Thus every root system arises from a semisimple Lie algebra, unique up to isomorphism, which gives the existence part of the [[root system of a semisimple Lie algebra|AR0D7V1J8T]] correspondence.

## Explanations

### L1 human

Serre's theorem gives a recipe that builds a semisimple Lie algebra from a finite table of integers, the Cartan matrix.
Three generators for each simple root and a short list of relations are enough.
So every Dynkin diagram really comes from a Lie algebra, including the exceptional ones.

### L2 human

The theorem gives a uniform construction of all simple Lie algebras, including $E_6, E_7, E_8, F_4, G_2$, without explicit matrices.
Removing the finiteness from the Cartan matrix and keeping the same relations defines the Kac–Moody algebras, of which the affine Lie algebras are the next simplest case.
