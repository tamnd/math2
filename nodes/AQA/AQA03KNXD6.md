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

We write each $\dim V_i$ as the sum of the dimensions of two kernels, and then the alternating sum telescopes.

1. Let $f_n \colon V_n \to 0$ be the zero map at the right end.
   For $0 \le i \le n$, let $k_i = \dim \ker f_i$.
   Each $k_i$ is finite, because $\ker f_i$ is a subspace of the finite-dimensional space $V_i$, by the [[dimension of a subspace|0QW084460E]].
2. Exactness at $V_0$ says $\ker f_0 = \operatorname{im}(0 \to V_0) = 0$, so $k_0 = 0$.
3. For $0 \le i < n$, exactness at $V_{i+1}$ in the [[exact sequence|CBDM280TDF]] says $\operatorname{im} f_i = \ker f_{i+1}$.
   So $\dim \operatorname{im} f_i = k_{i+1}$.
4. For $i = n$, the map $f_n$ is zero, so $\dim \operatorname{im} f_n = 0$.
   We set $k_{n+1} = 0$, and then $\dim \operatorname{im} f_i = k_{i+1}$ holds for every $0 \le i \le n$.
5. By the [[first isomorphism theorem|0MTBGVZ4XJ]], $V_i / \ker f_i \cong \operatorname{im} f_i$ for each $i$.
6. By the [[dimension of a quotient space|0SXDQ6TN00]] and steps 3 to 5,
$$\dim V_i - k_i = \dim (V_i / \ker f_i) = \dim \operatorname{im} f_i = k_{i+1}.$$
   So $\dim V_i = k_i + k_{i+1}$ for $0 \le i \le n$.
7. We substitute this into the alternating sum:
$$\sum_{i=0}^{n} (-1)^i \dim V_i = \sum_{i=0}^{n} (-1)^i k_i + \sum_{i=0}^{n} (-1)^i k_{i+1} = \sum_{i=0}^{n} (-1)^i k_i - \sum_{j=1}^{n+1} (-1)^{j} k_{j}.$$
   Here we put $j = i + 1$ in the second sum, so that $(-1)^i = -(-1)^j$.
8. The terms with $1 \le j \le n$ cancel between the two sums, and what remains is
$$k_0 - (-1)^{n+1} k_{n+1}.$$
9. By steps 2 and 4, $k_0 = 0$ and $k_{n+1} = 0$, so the alternating sum is $0$.

## Idea

Exactness cuts each space $V_i$ into two pieces: the kernel of the map that leaves it, and a piece that the map sends onto the next kernel.
So $\dim V_i$ is the sum of two neighboring kernel dimensions.
With alternating signs, each kernel is counted once with a plus sign and once with a minus sign, and the two outer kernels are $0$.
For $0 \to \R \to \R^3 \to \R^2 \to 0$ the kernels have dimensions $0, 1, 2$, and $1 = 0 + 1$, $3 = 1 + 2$, $2 = 2 + 0$.

## Variants

A second proof splits the long sequence into short exact sequences
$$0 \to \ker f_i \to V_i \to \ker f_{i+1} \to 0,$$
where the second map is $f_i$, which lands in $\operatorname{im} f_i = \ker f_{i+1}$.
Each short sequence gives $\dim V_i = \dim \ker f_i + \dim \ker f_{i+1}$, and adding these relations with alternating signs gives the result.

The proof uses only one property of the dimension: it adds up along short exact sequences.
So the same formula holds for any such additive quantity, for example the length of modules of finite length over a ring.
