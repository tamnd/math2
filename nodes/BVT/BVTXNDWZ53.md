---
tag: BVTXNDWZ53
kind: proof
name: Proof of the criteria for a direct sum of two subspaces
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
proves: 20A0K3KBZD
methods: [TFQ1845T84, 0NTF6DMVAP]
uses: [041JTZCK9Q, 0EPTJA5QV4, 0RMKABS2S5, 0V33SPH7RR]
sources:
  - book: isbn:9783031410253
    locator: Section 1C
  - url: https://en.wikipedia.org/wiki/Direct_sum_of_modules
    locator: Internal direct sum
---

## Proof

We prove $1 \Rightarrow 2 \Rightarrow 3 \Rightarrow 1$.

1. Assume condition 1. The zero vector lies in $U + W$, and $0 = 0 + 0$ with $0 \in U$ and $0 \in W$, since both are [[subspaces|0EPTJA5QV4]].
2. If $u + w = 0$ with $u \in U$ and $w \in W$, then $u + w$ and $0 + 0$ are two expressions of $0$. By uniqueness, $u = 0$ and $w = 0$. This is condition 2.
3. Assume condition 2, and let $x \in U \cap W$, the [[intersection|0V33SPH7RR]].
4. Then $x \in U$ and $-x \in W$, since $W$ is closed under scalar multiplication by $-1$.
5. We have $x + (-x) = 0$. By condition 2, $x = 0$. So $U \cap W = \{0\}$, which is condition 3.
6. Assume condition 3. Let $v \in U + W$, the [[sum|0RMKABS2S5]], and suppose $v = u + w = u' + w'$ with $u, u' \in U$ and $w, w' \in W$.
7. Then $u - u' = w' - w$. The left side lies in $U$ and the right side lies in $W$, since both are subspaces.
8. So $u - u' \in U \cap W = \{0\}$. Hence $u = u'$, and then $w = w'$.
9. So the expression of $v$ is unique, and the sum is [[direct|041JTZCK9Q]]. This is condition 1.
10. For the last sentence: $V = U \oplus W$ means that $U + W$ is direct and equal to $V$. By steps 1 to 9, the sum is direct exactly when $U \cap W = \{0\}$.

## Idea

Two expressions of one vector differ by an expression of $0$.
An expression $0 = u + w$ is the same thing as a vector $u = -w$ in both subspaces.
So uniqueness, uniqueness at $0$, and zero intersection are three views of one condition.

## Variants

- The proof of $3 \Rightarrow 1$ can be phrased with the addition map $U \times W \to V$: its kernel is $\{(x, -x) : x \in U \cap W\}$, and a linear map is injective exactly when its kernel is zero.
- The same steps prove the criteria for submodules of a module over any ring.
