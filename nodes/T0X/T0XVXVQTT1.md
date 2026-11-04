---
tag: T0XVXVQTT1
kind: proof
name: Proof that the reals are Archimedean from the completeness axiom
msc: [26A03]
proves: 0A3GWZ86AY
uses: [0AXWET80YW, 0M8TGGP9JP, 0BTMQ04556, 0B5H2V4JW8, 0QSPNASE50, 0HQARMKEV5]
methods: [0J0XBKG64S]
sources:
  - url: https://proofwiki.org/wiki/Archimedean_Principle
---

## Proof

We argue by contradiction.

1. Let $x$ and $y$ be real numbers with $y > 0$. For a natural number $n$, write $n y = y + \dots + y$ with $n$ terms. Then $(n + 1) y = n y + y$.
2. Suppose that $n y \le x$ for every natural number $n$.
3. Let $S = \set{n y : n \in \N}$. It is nonempty, and by step 2 it is [[bounded above|0B5H2V4JW8]] by $x$.
4. By the [[completeness axiom|0AXWET80YW]], $S$ has a [[supremum|0BTMQ04556]] $b$.
5. Since $y > 0$, we have $b - y < b$, in the [[ordered field|0QSPNASE50]] $\R$.
6. By the [[approximation property of the supremum|0M8TGGP9JP]], there is an element $m y$ of $S$ with $b - y < m y$.
7. Add $y$ to both sides: $b < m y + y = (m + 1) y$.
8. But $(m + 1) y \in S$, so $(m + 1) y \le b$ since $b$ is an upper bound. This contradicts step 7.
9. So some natural number $n$ satisfies $n y > x$. Thus $\R$ is an [[Archimedean ordered field|0HQARMKEV5]].

## Idea

If the multiples of $y$ were bounded, they would have a least upper bound $b$. Some multiple is within $y$ of $b$, and the next multiple then passes $b$, which is impossible.
