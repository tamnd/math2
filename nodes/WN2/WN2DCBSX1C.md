---
tag: WN2DCBSX1C
kind: statement
role: theorem
name: Bott periodicity theorem
msc: [55R45, 55N15, 19L99]
uses: [0R9R0Y1HDK, 0TKYAEJ8N7, P976WYEFMB, Q7RFNJH76Q, RASZAXBHX0, 9E4JE4902G, P7MN6MQV7P, 3M42BWTNQH, FJZXB1N7TP]
about: [9E4JE4902G, P7MN6MQV7P]
sources:
  - url: https://en.wikipedia.org/wiki/Bott_periodicity_theorem
same_as:
  wikidata: Q4948983
  wikipedia: Bott periodicity theorem
---

## Statement

Let $U = \bigcup_n U(n)$ and $O = \bigcup_n O(n)$ be the infinite [[unitary group|0R9R0Y1HDK]] and the infinite [[orthogonal group|0TKYAEJ8N7]], with the direct limit topology.

1. For all $i \ge 0$ there are isomorphisms of [[homotopy groups|P976WYEFMB]] $\pi_i(U) \cong \pi_{i+2}(U)$ and $\pi_i(O) \cong \pi_{i+8}(O)$.
2. Explicitly, $\pi_i(U) \cong \Z$ for $i$ odd and $\pi_i(U) = 0$ for $i$ even, and $\pi_i(O)$ for $i \equiv 0, 1, \ldots, 7 \pmod 8$ is $\Z/2, \Z/2, 0, \Z, 0, 0, 0, \Z$.
3. Let $\Sigma$ be the reduced [[suspension|Q7RFNJH76Q]], $\tilde{K}$ [[reduced complex K-theory|RASZAXBHX0]] and $\widetilde{KO}$ reduced [[real K-theory|P7MN6MQV7P]].
For every pointed compact Hausdorff space $X$, there are natural isomorphisms $\tilde{K}(X) \cong \tilde{K}(\Sigma^2 X)$ and $\widetilde{KO}(X) \cong \widetilde{KO}(\Sigma^8 X)$.

## Remarks

In the complex case, the isomorphism of part 3 is the external product with the class $b = [H] - 1 \in \tilde{K}(S^2)$, where $H$ is the tautological line bundle over $\C P^1 = S^2$.
Bott's original proof used Morse theory on spaces of paths in Lie groups; see [[Bott's Morse-theoretic proof of periodicity|FJZXB1N7TP]].
Atiyah and Bott later gave an elementary proof of the complex case through the [[clutching construction|3M42BWTNQH]]: they show that $K(X \times S^2) \cong K(X) \otimes K(S^2)$ and $K(S^2) \cong \Z[H]/(H - 1)^2$.

Example: applied to $X = S^0$, part 3 gives $\tilde{K}(S^{2n}) \cong \tilde{K}(S^0) \cong \Z$ and $\tilde{K}(S^{2n+1}) \cong \tilde{K}(S^1) = 0$ for all $n \ge 0$.

The infinite groups matter: for finite $n$ the groups $\pi_i(U(n))$ are not periodic, but they agree with $\pi_i(U)$ for $i < 2n$.

## Explanations

### L1 human

The theorem says that the homotopy groups of the infinite unitary group repeat with period $2$, and those of the infinite orthogonal group with period $8$.
In the language of K-theory, suspending a space twice does not change its complex K-theory, and suspending eight times does not change its real K-theory.
This regularity is rare in homotopy theory, where most computations are hard and irregular.

### L2 human

Bott periodicity is what makes [[complex K-theory|9E4JE4902G]] a cohomology theory defined in all degrees: one sets $K^{n} = K^{n-2}$ for all integers $n$.
It gives the K-theory of spheres, and through it the Thom isomorphism in K-theory, the Atiyah–Singer index theorem and Adams' solution of the Hopf invariant one problem.
The period $8$ of real K-theory matches the period $8$ of real Clifford algebras, which is the content of the Atiyah–Bott–Shapiro construction.
