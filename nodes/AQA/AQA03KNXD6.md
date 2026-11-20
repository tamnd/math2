---
tag: AQA03KNXD6
kind: proof
name: Proof of the alternating sum formula for exact sequences
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: grad
proves: EFBRMNWDQM
methods: [0NTF6DMVAP]
uses: [0MTBGVZ4XJ, 0SXDQ6TN00, 0QW084460E, CBDM280TDF]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_sequence
    locator: Properties
---

## Proof

1. Let $f_n \colon V_n \to 0$ be the zero map at the right end. For $0 \le i \le n$, let $k_i = \dim \ker f_i$. These are finite by the [[dimension of a subspace|0QW084460E]].
2. Exactness at $V_0$ means that $f_0$ is injective, so $k_0 = 0$.
3. For $0 \le i < n$, exactness at $V_{i+1}$ in the [[exact sequence|CBDM280TDF]] gives $\operatorname{im} f_i = \ker f_{i+1}$, so $\dim \operatorname{im} f_i = k_{i+1}$.
4. For $i = n$, the map $f_n$ is zero, so $\dim \operatorname{im} f_n = 0$. Set $k_{n+1} = 0$, so that $\dim \operatorname{im} f_i = k_{i+1}$ for every $0 \le i \le n$.
5. By the [[first isomorphism theorem|0MTBGVZ4XJ]], $V_i / \ker f_i \cong \operatorname{im} f_i$.
6. By the [[dimension of a quotient|0SXDQ6TN00]], $\dim V_i - k_i = \dim(V_i / \ker f_i) = \dim \operatorname{im} f_i = k_{i+1}$. So $\dim V_i = k_i + k_{i+1}$.
7. Then
$$\sum_{i=0}^n (-1)^i \dim V_i = \sum_{i=0}^n (-1)^i (k_i + k_{i+1}) = k_0 + (-1)^n k_{n+1},$$
because the term $(-1)^i k_{i+1}$ cancels with the term $(-1)^{i+1} k_{i+1}$ for $0 \le i < n$.
8. By steps 2 and 4, $k_0 = 0$ and $k_{n+1} = 0$. So the sum is $0$.

## Idea

Exactness cuts each $V_i$ into two pieces, the kernel of $f_i$ and a copy of the next kernel.
With alternating signs, every kernel is counted once with $+$ and once with $-$.

## Variants

- One can split the long sequence into short exact sequences $0 \to \ker f_i \to V_i \to \ker f_{i+1} \to 0$ and add the relation $\dim V_i = \dim \ker f_i + \dim \ker f_{i+1}$ from each one.
- The same proof shows that any function on finite-dimensional spaces that is additive on short exact sequences has alternating sum $0$ on exact sequences.
