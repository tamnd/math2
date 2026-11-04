---
tag: 33XSWFTWNZ
kind: proof
name: Proof that polynomial functions are continuous
msc: [26A15]
proves: 0C5TP6RYSV
uses: [0P27W9RW0G, 0EEE2CZB2A, 0VGMHCF4SC]
sources:
  - url: https://www.jirka.org/ra/
    locator: Proposition 3.2.4
---

## Proof

We argue by induction, from constants and the identity, using that [[sums and products of continuous functions are continuous|0VGMHCF4SC]].

1. Let $c \in \R$ and let $k_c \colon \R \to \R$ be the constant function $k_c(x) = c$. Let $a \in \R$ and let $V$ be an open interval containing $k_c(a) = c$.
2. Take $U = (a - 1, a + 1)$. For all $x \in U$, $k_c(x) = c \in V$. So $k_c$ is [[continuous at|0EEE2CZB2A]] $a$. Hence $k_c$ is [[continuous|0P27W9RW0G]].
3. Let $\id \colon \R \to \R$ be $\id(x) = x$. Let $a \in \R$ and let $V$ be an open interval containing $a$. Take $U = V$. Then $\id(x) = x \in V$ for all $x \in U$. So $\id$ is continuous.
4. For each natural number $i$, let $m_i(x) = x^i$. We show by induction on $i$ that $m_i$ is continuous.
5. Base case: $m_0 = k_1$, which is continuous by step 2.
6. Induction step: $m_{i+1}(x) = m_i(x) \cdot x$, so $m_{i+1}$ is the product of $m_i$ and $\id$. It is continuous by the induction hypothesis, step 3 and the product rule.
7. For each $i$, the function $x \mapsto a_i x^i$ is the product of $k_{a_i}$ and $m_i$. So it is continuous, by steps 2 and 6 and the product rule.
8. For $j \le n$, let $p_j(x) = \sum_{i=0}^{j} a_i x^i$. By step 7, $p_0$ is continuous.
9. If $p_j$ is continuous and $j < n$, then $p_{j+1} = p_j + a_{j+1} x^{j+1}$ is a sum of two continuous functions, by step 7. So it is continuous.
10. By induction on $j$, $p_n = p$ is continuous.

## Idea

A polynomial is built from constants and the identity $x \mapsto x$ by finitely many sums and products. Both building blocks are continuous, and sums and products keep continuity. Induction on the degree carries this through.
