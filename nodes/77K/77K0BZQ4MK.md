---
tag: 77K0BZQ4MK
kind: statement
role: theorem
name: Künneth theorem
msc: [55U25, 18G15, 55N10]
uses: [0CMD0BCH8T, WQ82C0M3QB, 2J4JJJYP22, F0HQXQ0HCD, DDQRERAQCV, M0Q5CFJ7ZH, 0CQHFPGJ45]
about: [M0Q5CFJ7ZH, DDQRERAQCV]
sources:
  - url: https://en.wikipedia.org/wiki/K%C3%BCnneth_theorem
same_as:
  wikidata: Q1307676
  wikipedia: Künneth theorem
---

## Statement

Let $R$ be a [[principal ideal domain|0CMD0BCH8T]].

1. Let $C_\bullet$ and $D_\bullet$ be [[chain complexes|WQ82C0M3QB]] of $R$-modules such that every $C_n$ is a free $R$-module. Then for every $n$ there is a natural short exact sequence
$$0 \to \bigoplus_{i+j=n} H_i(C) \otimes_R H_j(D) \to H_n(C \otimes_R D) \to \bigoplus_{i+j=n-1} \operatorname{Tor}_1^R(H_i(C), H_j(D)) \to 0,$$
and it splits, though not naturally.
2. Let $X$ and $Y$ be [[topological spaces|0CQHFPGJ45]]. Then for every $n$ there is a natural short exact sequence, which splits but not naturally,
$$0 \to \bigoplus_{i+j=n} H_i(X; R) \otimes_R H_j(Y; R) \to H_n(X \times Y; R) \to \bigoplus_{i+j=n-1} \operatorname{Tor}_1^R(H_i(X; R), H_j(Y; R)) \to 0.$$

Here $H$ is the [[homology|2J4JJJYP22]] of a complex, and $H_n(-; R)$ is [[singular homology|M0Q5CFJ7ZH]] with coefficients in $R$.
The symbol $\otimes_R$ is the [[tensor product|F0HQXQ0HCD]] and $\operatorname{Tor}_1^R$ is the [[Tor functor|DDQRERAQCV]].

## Remarks

For the algebraic part, note that the cycles $Z_\bullet$ and boundaries $B_\bullet$ of $C$ are free, since $R$ is a principal ideal domain.
So $0 \to Z_\bullet \to C_\bullet \to B_{\bullet - 1} \to 0$ is a split sequence of free complexes.
The long exact sequence after tensoring with $D$ gives the result.
The topological part follows from the algebraic one and the Eilenberg–Zilber theorem.
That theorem gives a chain homotopy equivalence between the singular chains of $X \times Y$ and the tensor product of the singular chains of $X$ and of $Y$.
If $R$ is a field, all Tor terms vanish and $H_n(X \times Y; R) \cong \bigoplus_{i+j=n} H_i(X; R) \otimes_R H_j(Y; R)$.
Over $\Z$ the Tor term matters.
For the real projective plane $P$, one has $H_0(P) = \Z$, $H_1(P) = \Z/2\Z$ and $H_2(P) = 0$.
So the tensor part in degree $3$ is zero, and the formula gives $H_3(P \times P; \Z) \cong \operatorname{Tor}_1^\Z(\Z/2\Z, \Z/2\Z) \cong \Z/2\Z$.

## Explanations

### L1 human

The Künneth theorem computes the holes of a product space from the holes of its factors.
With coefficients in a field, the answer is the simplest one: the homology of the product is the tensor product of the homologies.
For the torus, the product of two circles, this gives one class in degree $0$, two in degree $1$ and one in degree $2$.
With integer coefficients there is a correction term built from torsion.

### L2 human

The theorem is a direct application of the derived functor Tor: the failure of $H(C \otimes D) \cong H(C) \otimes H(D)$ is measured by $\operatorname{Tor}_1$.
Taking $D$ to be a module $M$ in degree $0$ gives the homology form of the [[universal coefficient theorem|GTA8ZFGZ3N]].
There are also cohomology versions, with a cross product into $H^n(X \times Y; R)$, and spectral sequence versions over rings that are not principal ideal domains.
