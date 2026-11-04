---
tag: 3MH8WKGV83
kind: proof
name: Proof that open sets are the sets that are neighbourhoods of all their points
msc: [54A05]
proves: 09CJ00H3NW
uses: [0CNQXVBHCX, 01ZQQDCERP, 05GK32H72H]
sources:
  - url: https://en.wikipedia.org/wiki/Neighbourhood_(mathematics)
    locator: Neighbourhood of a point
---

## Proof

We prove the two directions separately.

1. Let $A$ be [[open|01ZQQDCERP]] and let $x \in A$. Take $U = A$. Then $U$ is open and $x \in U \subseteq A$. So $A$ is a neighbourhood of $x$.
2. Conversely, let $A$ be a neighbourhood of each of its points. For each $x \in A$, choose an open set $U_x$ with $x \in U_x \subseteq A$.
3. Let $W = \bigcup_{x \in A} U_x$, the [[union|05GK32H72H]] of this family. Each $U_x \subseteq A$, so $W \subseteq A$.
4. Each $x \in A$ lies in $U_x$, so $A \subseteq W$. Hence $A = W$.
5. By the axioms of a [[topology|0CNQXVBHCX]], a union of members of $\tau$ is in $\tau$. This includes the empty family, whose union is $\varnothing$. So $A = W$ is open.

## Idea

An open set is its own open neighbourhood at each point. Conversely, if each point has an open set around it inside $A$, then $A$ is the union of these open sets, and unions of open sets are open.
