---
tag: 8P5NG5B4RA
kind: proof
name: Proof that disjoint cycles commute
msc: [20B30]
proves: 07E6D8R4D6
uses: [0RJMNEN3BJ, 0ZKPH2BD1T, 0PVG1CRAJN, 0W4RPA8QH3]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_permutation
    locator: Basic properties
---

## Proof

We compare $\sigma\tau(x)$ and $\tau\sigma(x)$ point by point. The argument works for any two permutations with disjoint sets of moved points.

1. Let $\sigma, \tau \in \operatorname{Sym}(X)$ be [[cycles|0ZKPH2BD1T]], elements of the [[symmetric group|0RJMNEN3BJ]]. The product $\sigma\tau$ is the composition, so $\sigma\tau(x) = \sigma(\tau(x))$.
2. Let $A = \{x \in X : \sigma(x) \ne x\}$ and $B = \{x \in X : \tau(x) \ne x\}$ be the sets of moved points. By hypothesis, $A$ and $B$ are [[disjoint|0W4RPA8QH3]].
3. Let $x \in A$, and put $y = \sigma(x)$. If $\sigma(y) = y$, then $\sigma(y) = \sigma(x)$, and $y = x$ since $\sigma$ is [[injective|0PVG1CRAJN]]. This contradicts $x \in A$.
4. So $\sigma(x) \in A$ for each $x \in A$.
5. Let $x \in A$. Then $x \notin B$, so $\tau(x) = x$ and $\sigma(\tau(x)) = \sigma(x)$.
6. By step 4, $\sigma(x) \in A$, so $\sigma(x) \notin B$ and $\tau(\sigma(x)) = \sigma(x)$. With step 5, $\sigma\tau(x) = \tau\sigma(x)$.
7. Let $x \in B$. Exchanging the roles of $\sigma$ and $\tau$ in steps 3 to 6 gives $\tau\sigma(x) = \tau(x) = \sigma\tau(x)$.
8. Let $x \notin A \cup B$. Then $\sigma(x) = x$ and $\tau(x) = x$, so $\sigma\tau(x) = x = \tau\sigma(x)$.
9. By steps 6 to 8, $\sigma\tau(x) = \tau\sigma(x)$ for every $x \in X$. Hence $\sigma\tau = \tau\sigma$.

## Idea

A permutation sends its moved points to moved points, so it never sends a point into the other cycle's territory. On the points of $\sigma$ only $\sigma$ acts, on the points of $\tau$ only $\tau$ acts, and all other points stay put. So the order of the two factors does not matter.
