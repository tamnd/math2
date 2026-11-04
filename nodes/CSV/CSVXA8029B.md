---
tag: CSVXA8029B
kind: proof
name: Proof of the Hausdorff maximal principle from Zorn's lemma
msc: ["03E25"]
proves: 0KM4KVR9MV
uses: [04RXTQA5ZA, 011C29Q1S1, 0GP9ASVQ1X, 0H5J02P8S9, 0TZEEFTNCC, WZKPDWBW2Z, 05GK32H72H]
sources:
  - url: https://en.wikipedia.org/wiki/Hausdorff_maximal_principle
    locator: Statement
---

## Proof

We apply Zorn's lemma to a set of chains ordered by inclusion.

1. Let $(P, \le)$ be a [[partially ordered set|011C29Q1S1]] and let $C_0$ be a [[chain|0GP9ASVQ1X]] of $P$.
2. Let $Q$ be the set of chains $C$ of $P$ with $C_0 \subseteq C$. Order $Q$ by inclusion $\subseteq$, which is a partial order. The set $Q$ is nonempty, since $C_0 \in Q$.
3. Let $K$ be a chain of $(Q, \subseteq)$. If $K$ is empty, then $C_0$ is an [[upper bound|0H5J02P8S9]] of $K$ in $Q$.
4. Let $K$ be nonempty, and let $W = \bigcup_{C \in K} C$ be the [[union|05GK32H72H]] of its members. Then $C_0 \subseteq W$.
5. The set $W$ is a chain of $P$. Let $x, y \in W$, with $x \in C$ and $y \in D$ for some $C, D \in K$. Since $K$ is a chain, $C \subseteq D$ or $D \subseteq C$.
6. So $x$ and $y$ lie in the larger of $C$ and $D$, which is a chain of $P$. Hence $x \le y$ or $y \le x$.
7. So $W \in Q$, and $C \subseteq W$ for each $C \in K$. Thus $W$ is an upper bound of $K$ in $Q$.
8. By steps 2 to 7, [[Zorn's lemma|04RXTQA5ZA]] applies to $(Q, \subseteq)$. It gives a [[maximal element|0TZEEFTNCC]] $M$ of $Q$.
9. Then $M$ is a chain with $C_0 \subseteq M$. Suppose that $D$ is a chain of $P$ with $M \subsetneq D$.
10. Then $C_0 \subseteq D$, so $D \in Q$, and $M \subsetneq D$ contradicts the maximality of $M$ in $Q$.
11. So $M$ is a [[maximal chain|WZKPDWBW2Z]] of $P$ that contains $C_0$.

## Idea

Chains that contain $C_0$, ordered by inclusion, satisfy the hypothesis of Zorn's lemma: a nested family of chains has a union that is again a chain. A maximal element of this family is a chain that cannot be enlarged, which is exactly a maximal chain.
