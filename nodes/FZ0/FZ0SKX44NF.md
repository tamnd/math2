---
tag: FZ0SKX44NF
kind: statement
role: theorem
name: Wick's theorem
msc: [81T18, 60G15]
uses: [K9SR95P4NJ, 1TJ8TNH331, 0NHK9MFFW9]
about: [K9SR95P4NJ]
sources:
  - url: https://en.wikipedia.org/wiki/Wick%27s_theorem
same_as:
  wikidata: Q850495
  wikipedia: Wick's theorem
---

## Statement

Let $\phi$ be the free real scalar field of mass $m > 0$ on [[Fock space|1TJ8TNH331]], with vacuum $\lvert 0 \rangle$.
Write $\phi = \phi^+ + \phi^-$, where $\phi^+$ is the annihilation part and $\phi^-$ is the creation part.
The normal-ordered product ${:}\phi(x_1)\cdots\phi(x_n){:}$ is obtained by expanding and moving every $\phi^-$ to the left of every $\phi^+$.
Let $T$ denote time ordering and let $\Delta_F$ be the Feynman [[propagator|K9SR95P4NJ]].
Then
$$T\{\phi(x_1)\cdots\phi(x_n)\} = \sum_{P} \prod_{\{i,j\} \in P} \Delta_F(x_i - x_j) \; {:}\prod_{k \notin \cup P} \phi(x_k){:}.$$
Here $P$ runs over all sets of pairwise disjoint pairs $\{i, j\}$ of indices in $\set{1, \dots, n}$, including the empty set.

## Remarks

The proof is by induction on $n$.
One commutes annihilation parts to the right; each commutator $[\phi^+(x), \phi^-(y)]$ is a number, and with time ordering these numbers combine into $\Delta_F(x - y)$.

Taking the vacuum expectation value kills every normal-ordered product with at least one field.
So $\langle 0 \rvert T\{\phi(x_1)\cdots\phi(x_n)\} \lvert 0 \rangle$ is $0$ for odd $n$, and for even $n$ it is the sum over [[perfect matchings|0NHK9MFFW9]] of the indices of the products of propagators.
Example: for $n = 4$ there are three matchings, so the four-point function is $\Delta_{12}\Delta_{34} + \Delta_{13}\Delta_{24} + \Delta_{14}\Delta_{23}$, with $\Delta_{ij} = \Delta_F(x_i - x_j)$.

The probabilistic form is Isserlis' theorem.
For centred jointly Gaussian random variables $X_1, \dots, X_n$, $\mathbb{E}[X_1 \cdots X_n]$ is the sum over perfect matchings of the products of the covariances $\mathbb{E}[X_i X_j]$.

## Explanations

### L1 human

For a free field, all correlations are built from correlations of pairs.
Wick's theorem says how: to compute a product of many fields, pair them up in every possible way and multiply the pair correlations.
This is what makes free fields, and Gaussian random variables, so easy to compute with.

### L2 human

Wick's theorem is the engine of perturbation theory.
Expanding $e^{-iH_{\text{int}}t}$ in the interaction picture gives vacuum expectations of products of free fields, and Wick's theorem turns each one into a sum of products of propagators.
Each term is encoded by a [[Feynman diagram|BS6HVNMTWC]]: the fields are the vertices and the pairs are the edges.
For fermion fields the same theorem holds with a sign given by the parity of the permutation that brings each pair together.
