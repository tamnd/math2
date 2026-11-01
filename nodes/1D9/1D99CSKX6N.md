---
tag: 1D99CSKX6N
kind: statement
role: theorem
name: Dirichlet's unit theorem
msc: [11R27]
uses: [MWBDFS2KJ5, 07C6ECNJET, 0YV2CKP2AV, 0WJX8MGG37, WN9V7WSJKF, 0K387S2PKQ, RWK0HNF1NA]
about: [07C6ECNJET, MWBDFS2KJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet%27s_unit_theorem
same_as:
  wikidata: Q1227702
  wikipedia: Dirichlet's unit theorem
---

## Statement

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] with ring of integers $\mathcal{O}_K$.
Let $r_1$ be the number of field embeddings $K \to \R$ and $r_2$ the number of pairs of complex conjugate non-real embeddings $K \to \C$.
Let $\mu(K)$ be the set of [[roots of unity|0YV2CKP2AV]] in $K$.
Then $\mu(K)$ is a finite cyclic group, and the [[group of units|07C6ECNJET]] $\mathcal{O}_K^\times$ is finitely generated with
$$\mathcal{O}_K^\times \cong \mu(K) \times \Z^{r_1 + r_2 - 1}.$$

## Remarks

The proof uses the logarithmic embedding $u \mapsto \big(N_j \log \abs{\sigma_j(u)}\big)_j$ into $\R^{r_1 + r_2}$, where $\sigma_j$ runs over the real embeddings and one embedding from each complex pair, and $N_j$ is $1$ or $2$.
Its kernel on $\mathcal{O}_K^\times$ is the finite group $\mu(K)$, and its image lies in the hyperplane where the coordinates sum to $0$.
The hard part is that the image is a full [[lattice|WN9V7WSJKF]] in that hyperplane; this uses [[Minkowski's theorem|0K387S2PKQ]] to produce enough units.

A set of $r = r_1 + r_2 - 1$ units that generate $\mathcal{O}_K^\times$ modulo $\mu(K)$ is a system of *fundamental units*.

Example: for $K = \Q(\sqrt{2})$, $r_1 = 2$ and $r_2 = 0$, so the rank is $1$.
The units of $\Z[\sqrt{2}]$ are exactly $\pm (1 + \sqrt{2})^k$ with $k \in \Z$.
For an imaginary quadratic field, $r_1 = 0$ and $r_2 = 1$, so the rank is $0$ and every unit is a root of unity; for $\Q(i)$ the units are $\pm 1, \pm i$.

## Explanations

### L1 human

The units of a number field are the algebraic integers whose inverse is also an algebraic integer.
The theorem says that all of them are built from a finite list of basic units by multiplication, up to roots of unity.
The number of basic units is given by counting the real and complex embeddings of the field.

### L2 human

The theorem is one of the two finiteness results at the start of algebraic number theory, with the finiteness of the class number.
In terms of [[free abelian groups|0WJX8MGG37]], $\mathcal{O}_K^\times / \mu(K)$ is free of rank $r_1 + r_2 - 1$.
The covolume of the unit lattice is the [[regulator|RWK0HNF1NA]], which enters the [[class number formula|55XX5A7XZV]].
For real quadratic fields, the fundamental unit gives the solutions of Pell's equation.
