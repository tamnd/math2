---
tag: 9FGF9E8PJ4
kind: proof
name: Proof of transfinite induction from well-foundedness
msc: ["03E10"]
proves: 0ZHQMQ2C1N
uses: [0230ECX1Q5, 0T3DPBG981, 0RYYK8PG4S]
methods: [0J0XBKG64S]
sources:
  - url: https://proofwiki.org/wiki/Well-Founded_Induction
---

## Proof

We argue by contradiction, using a minimal counterexample.

1. Let $R$ be a [[well-founded relation|0230ECX1Q5]] on a set $A$ and let $P(x)$ be a [[predicate|0T3DPBG981]] on $A$.
2. Assume the hypothesis: for each $x \in A$, if $P(y)$ holds for each $y \in A$ with $y \mathrel{R} x$, then $P(x)$ holds.
3. Let $S = \set{x \in A \mid P(x) \text{ is false}}$. Suppose, for a contradiction, that $S$ is nonempty.
4. Since $R$ is well-founded and $S$ is a nonempty subset of $A$, there is $m \in S$ such that no $s \in S$ satisfies $s \mathrel{R} m$.
5. Let $y \in A$ with $y \mathrel{R} m$. By step 4, $y \notin S$. By the definition of $S$, $P(y)$ is not false. By the [[law of excluded middle|0RYYK8PG4S]], $P(y)$ holds.
6. By step 5, $P(y)$ holds for each $y \in A$ with $y \mathrel{R} m$. By step 2 with $x = m$, $P(m)$ holds.
7. But $m \in S$ by step 4, so $P(m)$ is false. This contradicts step 6.
8. Hence $S$ is empty. So for each $x \in A$, $P(x)$ is not false. By the law of excluded middle again, $P(x)$ holds.

## Idea

If $P$ failed somewhere, well-foundedness would give a minimal place where it fails. Below that place $P$ holds everywhere, so the hypothesis forces $P$ to hold there too. This contradiction shows that $P$ never fails.
