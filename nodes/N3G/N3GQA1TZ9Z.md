---
tag: N3GQA1TZ9Z
kind: statement
role: theorem
name: Brown–Gersten descent
msc: ["19E08", "18F20", "55P42"]
uses: [5GVFZWMWC8, 2VQX2E8EAH, MVGBS3J1P7, 1GHF4EKBXS, AND2WHZC8P, 1NDRD8BHFG, PQ6Q143ARJ, GG8AYV847V]
about: [5GVFZWMWC8, 1GHF4EKBXS]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Statement

Let $X$ be a [[Noetherian topological space|2VQX2E8EAH]] of finite [[Krull dimension|MVGBS3J1P7]] $d$.
Let $E$ be a [[presheaf|AND2WHZC8P]] of [[spectra|1GHF4EKBXS]] on the open subsets of $X$ such that:

1. $E(\emptyset)$ is contractible.
2. For all open sets $U, V \subseteq X$ the square formed by $E(U \cup V) \to E(U)$, $E(U \cup V) \to E(V)$, $E(U) \to E(U \cap V)$ and $E(V) \to E(U \cap V)$ is homotopy cartesian.

Let $\mathbb{H}(X; E)$ be the hypercohomology spectrum, the [[homotopy limit|1NDRD8BHFG]] over the Zariski site of a fibrant replacement of $E$.
Then $E$ satisfies Zariski descent: the map $E(X) \to \mathbb{H}(X; E)$ is a weak equivalence.
There is a strongly convergent [[spectral sequence|GG8AYV847V]]
$$E_2^{p,q} = H^p(X; \pi_{-q} E) \Rightarrow \pi_{-p-q} E(X).$$
Here $\pi_{-q} E$ is the sheaf associated with $U \mapsto \pi_{-q} E(U)$, and $H^p$ is [[sheaf cohomology|PQ6Q143ARJ]].
The $E_2$ terms vanish for $p > d$.

## Remarks

The idea: Brown and Gersten compare $E$ with a fibrant replacement in a model structure on presheaves on $X$.
On a Noetherian space every open set is quasi-compact, so condition 2 propagates by induction to all finite open covers, and finite dimension gives the convergence of the spectral sequence.

Example: for a regular separated Noetherian scheme $X$ of finite Krull dimension, Quillen's K-theory $U \mapsto K(U)$ satisfies condition 2 by Quillen's localization theorem.
So there is a spectral sequence $H^p(X; \mathcal{K}_{q}) \Rightarrow K_{q-p}(X)$, with $\mathcal{K}_q$ the Zariski sheaf of K-groups.
Combined with the Gersten resolution, it links K-groups with Chow groups as in Bloch's formula.

Condition 2 is not automatic: connective K-theory of singular schemes can fail it.
Thomason and Trobaugh showed that Bass's nonconnective K-theory satisfies it on every quasi-compact quasi-separated scheme, which gives Zariski descent there.

## Explanations

### L1 human

A presheaf of spectra assigns a homotopy-theoretic object to each open set.
The theorem says that if this assignment glues correctly for every pair of open sets, then it glues correctly for every open cover.
Then the value on the whole space is computed from local values by a spectral sequence, as for sheaf cohomology.

### L2 human

Brown and Gersten proved this to treat algebraic K-theory as a generalized sheaf cohomology.
For K-theory of regular schemes it gives the descent spectral sequence from Zariski cohomology of K-sheaves to K-groups.
It is the Zariski analogue of later results on Nisnevich descent, where condition 2 is replaced by a condition on elementary distinguished squares.
