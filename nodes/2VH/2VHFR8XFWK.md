---
tag: 2VHFR8XFWK
kind: statement
role: theorem
name: Bott periodicity for C*-algebras
msc: [46L80, 19K99]
uses: [BP86XQRZD2, 7NTVTHC7CG, KK9S67F8CA, M2WFY1D3SZ, 6XCFW7YGX8]
about: [BP86XQRZD2, 7NTVTHC7CG]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_K-theory
---

## Statement

Let $A$ be a [[C*-algebra|M2WFY1D3SZ]] with unitization $\widetilde{A}$.
Let $SA$ be its suspension, viewed as the C*-algebra of continuous functions $f \colon \mathbb{T} \to A$ with $f(1) = 0$, where $\mathbb{T}$ is the unit circle.
Every element of $K_0(A)$ has the form $[p] - [s(p)]$, where $p$ is a projection in some $M_n(\widetilde{A})$.
Here $s(p)$ is the scalar projection obtained by applying the quotient map $\widetilde{A} \to \C$ entrywise.
For a projection $p \in M_n(\widetilde{A})$, let $f_p$ be the loop of [[unitaries|KK9S67F8CA]] $f_p(z) = z p + (1_n - p)$, $z \in \mathbb{T}$.
Then the formula
$$\beta_A\big([p] - [s(p)]\big) = \big[f_p f_{s(p)}^*\big]$$
defines an isomorphism of abelian groups $\beta_A \colon K_0(A) \to K_1(SA)$, natural in $A$, called the Bott map.
Together with the natural isomorphism $K_1(A) \cong K_0(SA)$, it gives natural isomorphisms
$$K_0(S^2 A) \cong K_0(A), \qquad K_1(S^2 A) \cong K_1(A).$$

## Remarks

The loop $f_p f_{s(p)}^*$ equals $1_n$ at $z = 1$, so it is a unitary in matrices over the unitization of $SA$ whose class lies in $K_1(SA)$.
One proof, due to Cuntz, uses the Toeplitz extension $0 \to \mathcal{K} \to \mathcal{T} \to C(\mathbb{T}) \to 0$ tensored with $A$.
Defining $K_n(A) = K_0(S^n A)$ for $n \ge 0$, the theorem says $K_{n+2}(A) \cong K_n(A)$, so operator K-theory has only two distinct groups.
For $A = C(X)$ with $X$ compact Hausdorff, it recovers Bott periodicity in [[topological K-theory|6XCFW7YGX8]].
Example: for $A = \C$ it gives $K_1(C_0(\R)) \cong K_0(\C) \cong \Z$, and then $K_0(C_0(\R^2)) \cong \Z$.

## Explanations

### L1 human

Suspending an algebra twice does not change its K-theory.
So instead of an infinite list of groups $K_0, K_1, K_2, \ldots$ there are only two, $K_0$ and $K_1$.
The isomorphism turns a projection into a loop of unitaries that turns the range of the projection once around the circle.

### L2 human

Bott periodicity is what lets the long exact sequence of an extension of C*-algebras close up into the six-term exact sequence.
The connecting map $K_0(B) \to K_1(I)$ of that sequence, the exponential map, is built from the Bott map and the index map.
For commutative algebras it contains the classical periodicity $\widetilde{K}^0(S^2 X) \cong \widetilde{K}^0(X)$ for compact spaces $X$.
