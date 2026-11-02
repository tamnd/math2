---
tag: QGPAB6AS9F
kind: statement
role: theorem
name: Tannaka–Krein duality
msc: [22D35, 18M25]
uses: [G5S1M9, WYGRXCG2RN, KYCPCC57FT, PY430TXMG0, 5S7ER95XAC, A10WW8GEKR]
about: [WYGRXCG2RN]
sources:
  - url: https://en.wikipedia.org/wiki/Tannaka%E2%80%93Krein_duality
same_as:
  wikidata: Q7683608
  wikipedia: Tannaka–Krein duality
---

## Statement

Let $G$ be a compact Hausdorff topological [[group|G5S1M9]].
Let $\mathrm{Rep}(G)$ be the category of finite-dimensional continuous complex [[representations|WYGRXCG2RN]] of $G$, and let $\omega \colon \mathrm{Rep}(G) \to \mathbf{Vect}_\C$ be the forgetful functor.
Let $T(G)$ be the group of families $u = (u_V)_{V \in \mathrm{Rep}(G)}$ of linear automorphisms $u_V \colon \omega(V) \to \omega(V)$ such that:

1. $u$ is a [[natural transformation|KYCPCC57FT]] $\omega \to \omega$;
2. $u_{V \otimes W} = u_V \otimes u_W$ for all $V, W$, and $u$ is the identity on the trivial representation $\C$;
3. $u_{\overline{V}} = \overline{u_V}$ for every $V$, where $\overline{V}$ is the complex conjugate representation.

Then the map $G \to T(G)$ that sends $g$ to the family of operators $(\pi_V(g))_V$ is an isomorphism of groups.

## Remarks

This is Tannaka's theorem: a compact group is determined by its category of representations together with the forgetful functor.
Proof idea: by the Peter–Weyl theorem, the matrix coefficients of the representations span a dense subalgebra $\mathcal{R}(G)$ of the algebra $C(G)$ of continuous functions.
These functions also separate the points of $G$.
An element of $T(G)$ defines an algebra homomorphism $\mathcal{R}(G) \to \C$ that commutes with complex conjugation.
One shows that every such homomorphism is evaluation at a unique point of $G$.

Without clause 3 the group is larger.
For $G = U(1)$, the representations are the $\Z$-graded spaces, and families satisfying clauses 1 and 2 are given by $t \in \C^\times$ acting by $t^n$ in degree $n$; clause 3 forces $\abs{t} = 1$.
For a compact Lie group, clauses 1 and 2 alone give its complexification.
Krein's part of the duality describes which categories with such a functor arise from compact groups.
The algebraic version concerns a neutral Tannakian category over a field $k$.
It says that such a category is equivalent, as a rigid symmetric monoidal category, to the category of finite-dimensional representations of an affine group scheme over $k$.

## Explanations

### L1 human

A compact group can be rebuilt from the way it acts on vector spaces.
One records all its finite-dimensional representations, all the maps between them, and how tensor products of representations behave.
The group is then recovered as the set of consistent ways to act on all these spaces at once.
This generalizes Pontryagin duality, which rebuilds a compact abelian group from its characters.

### L2 human

For a compact abelian group, every irreducible representation is one-dimensional, and the theorem reduces to recovering $G$ from its character group, as in Pontryagin duality.
For non-abelian groups the representations do not form a group, but they do form a [[rigid|A10WW8GEKR]] [[symmetric monoidal category|5S7ER95XAC]], and the forgetful functor is a strong [[monoidal functor|PY430TXMG0]].
The group appears as the automorphisms of this functor that respect the tensor product.
This idea is central to the theory of Tannakian categories, motivic Galois groups, and the reconstruction of quantum groups from their representation categories.
