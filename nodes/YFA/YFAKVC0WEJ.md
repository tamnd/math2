---
tag: YFAKVC0WEJ
kind: definition
name: Generalized cohomology theory
msc: [55N20]
defines: H28PSZR7XG
uses: [YHK51GHK2T, 082GHNPJ53, 6N7BC70CX0, F2F143KQ2M, JB7ZBFBA9C]
sources:
  - url: https://en.wikipedia.org/wiki/Cohomology
---

## Definition

Consider pairs of spaces $(X, A)$ and maps of pairs, as in the [[Eilenberg–Steenrod axioms|YHK51GHK2T]], and write $X$ for $(X, \emptyset)$.
A *generalized cohomology theory* consists of contravariant functors $h^n$, for $n \in \Z$, from pairs of spaces to [[abelian groups|082GHNPJ53]], and natural transformations $\delta \colon h^n(A) \to h^{n+1}(X, A)$, such that:

1. (Homotopy) [[Homotopic|F2F143KQ2M]] maps of pairs induce the same homomorphisms.
2. (Exactness) For each pair, the sequence $\cdots \to h^n(X, A) \to h^n(X) \to h^n(A) \xrightarrow{\delta} h^{n+1}(X, A) \to \cdots$, with the unnamed maps induced by inclusions, is [[exact|JB7ZBFBA9C]].
3. (Excision) If $Z \subseteq A$ and the closure of $Z$ lies in the interior of $A$, then the inclusion $(X \setminus Z, A \setminus Z) \to (X, A)$ induces isomorphisms $h^n(X, A) \to h^n(X \setminus Z, A \setminus Z)$.
4. (Additivity) If $X$ is the disjoint union of spaces $X_\alpha$, the inclusions induce an isomorphism $h^n(X) \to \prod_\alpha h^n(X_\alpha)$.

No condition is put on the groups $h^n(P)$ of a one-point space $P$.

## Remarks

Often the axioms are only asked for CW pairs, or for pairs of spaces with the homotopy type of CW pairs.
A *generalized homology theory* is defined in the same way with covariant functors.

Example: [[singular cohomology|6N7BC70CX0]] $H^n(-; G)$ with coefficients in an abelian group $G$ is a generalized cohomology theory, and it also satisfies the dimension axiom $H^n(P; G) = 0$ for $n \ne 0$.

Example: complex topological K-theory is a generalized cohomology theory with $K^n(P) \cong \Z$ for $n$ even and $K^n(P) = 0$ for $n$ odd, by Bott periodicity; it is not an ordinary theory.

Non-example: the homotopy groups $\pi_n(X, A, x_0)$ of pointed pairs satisfy a homotopy axiom and have long exact sequences, but they fail excision, so they do not form a generalized homology theory.
