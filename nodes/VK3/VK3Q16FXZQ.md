---
tag: VK3Q16FXZQ
kind: definition
name: Real K-theory KO
msc: [55N15, 55R50]
defines: P7MN6MQV7P
uses: [P4DZM975BV, 5FDMY7PDYY, RASZAXBHX0, 9E4JE4902G, Q7RFNJH76Q, 0TVJZYB6SH, 0S1FJ8VEX9]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_K-theory
    locator: Definitions
---

## Definition

Let $X$ be a [[compact|0TVJZYB6SH]] [[Hausdorff space|0S1FJ8VEX9]].
Consider the commutative monoid of isomorphism classes of real [[vector bundles|P4DZM975BV]] over $X$ under direct sum.
The group $KO^0(X)$ is its [[Grothendieck group|5FDMY7PDYY]].
For a pointed compact Hausdorff space $(Y, y_0)$, the reduced group $\widetilde{KO}^0(Y)$ is the kernel of the restriction map $KO^0(Y) \to KO^0(\set{y_0}) = \Z$, as for [[reduced complex K-theory|RASZAXBHX0]].
For $n \ge 1$, set
$$KO^{-n}(X) = \widetilde{KO}^0(\Sigma^n (X_+)),$$
where $X_+$ is $X$ with a disjoint base point added and $\Sigma$ is the reduced [[suspension|Q7RFNJH76Q]].
*Real K-theory* $KO$ is the family of functors $X \mapsto KO^{-n}(X)$, $n \ge 0$.

## Remarks

Example: $KO^{-1}(\text{point}) = \widetilde{KO}^0(S^1) \cong \Z/2$.
A real line bundle over $S^1$ is either trivial or the Möbius bundle $M$, and $M \oplus M$ is trivial.
So $[M] - 1$ generates $\widetilde{KO}^0(S^1)$ and has order $2$.

Non-example: complexification $KO^0(X) \to K^0(X)$, $[E] \mapsto [E \otimes_{\R} \C]$, is not injective in general.
For $X = S^1$ it sends $[M] - 1 \ne 0$ to $0$, because $\tilde{K}^0(S^1) = 0$ in [[complex K-theory|9E4JE4902G]].

The groups $KO^{-n}(\text{point})$ for $n = 0, 1, \ldots, 7$ are $\Z, \Z/2, \Z/2, 0, \Z, 0, 0, 0$, and they repeat with period $8$.
For compact $X$, $KO^0(X)$ is the set of homotopy classes of maps $X \to \Z \times BO$.
