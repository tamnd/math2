---
tag: 8ETHA6K7BY
kind: proof
name: Proof that closed subsets of complete spaces are complete
msc: ["54E50"]
proves: 0FBXJZX3MK
uses: [08EWT7J0SC, 0G5AV9Q4RR, 0T2WYDTRP2, 0MCK8K2D7Z, 06JYPJ4WHH, 09GQ3ZTQJ9]
sources:
  - url: https://proofwiki.org/wiki/Subspace_of_Complete_Metric_Space_is_Closed_iff_Complete
    locator: Necessary Condition
---

## Proof

1. Let $(X, d)$ be a [[complete metric space|08EWT7J0SC]] and let $F$ be a [[closed subset|0G5AV9Q4RR]] of $X$. Let $d_F$ be the [[subspace metric|0T2WYDTRP2]] on $F$.
2. Let $(x_n)$ be a [[Cauchy sequence|0MCK8K2D7Z]] in $(F, d_F)$.
3. We have $d(x_m, x_n) = d_F(x_m, x_n)$ for all $m, n$. So $(x_n)$ is also a Cauchy sequence in $(X, d)$.
4. Since $X$ is complete, $(x_n)$ [[converges|06JYPJ4WHH]] in $X$ to some point $x \in X$.
5. All $x_n$ lie in $F$, and $F$ is closed. Since [[closed sets contain their limits|09GQ3ZTQJ9]], we get $x \in F$.
6. For each $n$, $d_F(x_n, x) = d(x_n, x)$. So $d_F(x_n, x) \to 0$, and $(x_n)$ converges to $x$ in $(F, d_F)$.
7. Thus each Cauchy sequence in $F$ converges to a point of $F$, and $(F, d_F)$ is complete.

## Idea

A Cauchy sequence in $F$ has a limit in the big space, because the big space is complete.
A closed set cannot lose a limit of its own points, so the limit lies in $F$.
