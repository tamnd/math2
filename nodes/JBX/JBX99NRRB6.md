---
tag: JBX99NRRB6
kind: statement
role: theorem
name: Thom isomorphism in K-theory
msc: [55N15, 55R25, 19L99]
uses: [P4DZM975BV, 5MNYT3AFPH, 0MDMZ965VE, RASZAXBHX0, 9E4JE4902G, WN2DCBSX1C, N685RXHDZX]
about: [5MNYT3AFPH, 9E4JE4902G]
sources:
  - url: https://en.wikipedia.org/wiki/Thom_space
---

## Statement

Let $X$ be a compact Hausdorff space and let $p \colon E \to X$ be a complex [[vector bundle|P4DZM975BV]] of rank $n$.
Let $\operatorname{Th}(E)$ be its [[Thom space|5MNYT3AFPH]], which for compact $X$ is the one-point compactification of $E$.
Then there is a class $\lambda_E \in \tilde{K}(\operatorname{Th}(E))$, the *K-theory Thom class*, with these properties.

1. For each $x \in X$, the restriction of $\lambda_E$ to $\operatorname{Th}(E_x) \cong S^{2n}$ is a generator of $\tilde{K}(S^{2n}) \cong \Z$.
2. The map
$$K(X) \to \tilde{K}(\operatorname{Th}(E)), \quad a \mapsto p^*(a) \cdot \lambda_E,$$
is an isomorphism of groups.

Here $K$ is [[complex K-theory|9E4JE4902G]], $\tilde{K}$ is [[reduced K-theory|RASZAXBHX0]], and the product is the module structure of $\tilde{K}(\operatorname{Th}(E))$ over $K(E) \cong K(X)$.

## Remarks

The class $\lambda_E$ is represented by a Koszul complex of [[exterior powers|0MDMZ965VE]] over $E$:
$$0 \to \Lambda^0 p^*E \to \Lambda^1 p^*E \to \cdots \to \Lambda^n p^*E \to 0.$$
Its maps at a point $v \in E$ are $\omega \mapsto v \wedge \omega$.
It is exact away from the zero section, so it defines a class with compact support.
The proof starts with a trivial bundle over a point, where the statement is $\tilde{K}(S^{2n}) \cong \Z$ from [[Bott periodicity|WN2DCBSX1C]].
It then glues over a finite cover of $X$ by trivializing open sets with Mayer–Vietoris sequences.

Example: for $X$ a point and $E = \C^n$, the theorem says $\tilde{K}(S^{2n}) \cong K(\text{point}) = \Z$.

The complex structure matters: a real vector bundle need not have a Thom class in K-theory.
Real bundles with a K-theory Thom class are called K-oriented; they include all real bundles with a spin$^c$ structure.
The theorem is the K-theory analogue of the [[Thom isomorphism|N685RXHDZX]] in ordinary cohomology.

## Explanations

### L1 human

The Thom space of a vector bundle is obtained by compactifying the total space with one extra point.
The theorem says that, for complex bundles, the K-theory of this Thom space is a copy of the K-theory of the base.
The identification is given by multiplying with one special class, which on each fibre is the Bott generator of a sphere.

### L2 human

The K-theory Thom isomorphism is the key step in the construction of push-forward maps in K-theory, also called Gysin maps.
Take an embedding of manifolds with a complex normal bundle.
One goes from the submanifold to the Thom space of the normal bundle by the Thom isomorphism.
Then one goes to the big manifold by collapsing the complement of a tubular neighbourhood.
This is how the topological index in the Atiyah–Singer index theorem is defined.
Comparing the K-theory Thom class with the cohomology Thom class through the Chern character produces the Todd class, which explains the Todd class in the Riemann–Roch formulas.
