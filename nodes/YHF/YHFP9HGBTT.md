---
tag: YHFP9HGBTT
kind: statement
role: theorem
name: Langlands classification
msc: ["22E46", "22E47", "22E50"]
uses: [SZV8Y806Y7, 2MKHH636C3, Z2FEBW5MQM, BM3TWJ0D4P, CWDF4KGHS3, 6Q7AHAZ6Q4, 42ZCE14AD2]
about: [SZV8Y806Y7]
sources:
  - url: https://en.wikipedia.org/wiki/Langlands_classification
same_as:
  wikidata: Q6486186
  wikipedia: Langlands classification
---

## Statement

Let $G$ be a linear connected [[real reductive Lie group|42ZCE14AD2]], and fix a minimal parabolic subgroup $P_0$ of $G$.
Consider the triples $(P, \sigma, \nu)$ such that:

1. $P \supseteq P_0$ is a [[parabolic subgroup|Z2FEBW5MQM]] with [[Langlands decomposition|BM3TWJ0D4P]] $P = MAN$;
2. $\sigma$ is an equivalence class of irreducible tempered representations of $M$;
3. $\nu \in \mathfrak a^*_\C$, where $\mathfrak a$ is the Lie algebra of $A$, and $\operatorname{Re} \nu$ is strictly positive on every root of $\mathfrak a$ in the Lie algebra of $N$.

For such a triple, the normalised [[induced representation|6Q7AHAZ6Q4]] $\mathrm{Ind}_P^G(\sigma \otimes e^\nu \otimes 1)$ has a unique irreducible quotient $J(P, \sigma, \nu)$, the Langlands quotient.
Every irreducible [[admissible representation|SZV8Y806Y7]] of $G$ is infinitesimally equivalent to exactly one $J(P, \sigma, \nu)$.

## Remarks

Infinitesimal equivalence means that the [[Harish-Chandra modules|2MKHH636C3]] are isomorphic.
The proof compares the leading exponents of the matrix coefficients of a representation with the parameter $\nu$.
The quotient $J(P, \sigma, \nu)$ is the image of a standard intertwining operator, which converges because $\operatorname{Re} \nu$ lies in the positive chamber.
If $G$ is semisimple and $P = G$, then $A$ is trivial, so $\nu = 0$, and $J(G, \sigma, 0) = \sigma$ runs over the tempered representations themselves.
Example: let $G = \mathrm{SL}_2(\R)$ and let $P$ be the upper triangular matrices.
The constant functions form a subrepresentation of the [[principal series|CWDF4KGHS3]] $I(\mathrm{triv}, -\rho)$, and dually the trivial representation is a quotient of $I(\mathrm{triv}, \rho)$.
So $J(P, \mathrm{triv}, \rho)$ is the trivial representation.
The positivity of $\operatorname{Re} \nu$ is needed: on the unitary axis $\operatorname{Re} \nu = 0$ the induced representation can be reducible with several irreducible quotients, so uniqueness fails.

## Explanations

### L1 human

The theorem reduces the classification of all irreducible representations to that of the tempered ones, which are the representations that appear in $L^2(G)$.
Each irreducible representation is built from a tempered representation of a smaller group and a parameter that measures its growth.

### L2 human

Langlands proved the classification for real groups; the analogous result for $p$-adic groups is due to Borel–Wallach and Silberger.
Tempered representations are in turn built from discrete series of Levi subgroups, so the whole picture rests on Harish-Chandra's discrete series.
The classification is the starting point of the local Langlands correspondence for real groups, which attaches $L$-parameters to the triples $(P, \sigma, \nu)$.
