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

We prove the cycle of implications $1 \Rightarrow 2 \Rightarrow 3 \Rightarrow 1$, and then the last sentence of the statement.

1. Assume condition 1.
   The zero vector lies in $U + W$ as $0 = 0 + 0$, since $0 \in U$ and $0 \in W$ for [[subspaces|0EPTJA5QV4]].
2. Let $u + w = 0$ with $u \in U$ and $w \in W$.
   Then $u + w$ and $0 + 0$ are two expressions of $0$, so uniqueness gives $u = 0$ and $w = 0$, which is condition 2.
3. Assume condition 2, and let $x$ lie in the [[intersection|0V33SPH7RR]] $U \cap W$.
   Then $x \in U$, and $-x \in W$ because $W$ is closed under multiplication by the scalar $-1$.
4. We have $x + (-x) = 0$, so condition 2 gives $x = 0$.
   Hence $U \cap W = \{0\}$, which is condition 3.
5. Assume condition 3, and let $v$ lie in the [[sum|0RMKABS2S5]] $U + W$ with two expressions $v = u + w = u' + w'$, where $u, u' \in U$ and $w, w' \in W$.
   Rearranging gives
$$u - u' = w' - w.$$
6. The left side lies in $U$ and the right side lies in $W$, because subspaces are closed under subtraction.
   So both sides lie in $U \cap W = \{0\}$.
7. Hence $u = u'$ and $w = w'$.
   So the expression of $v$ is unique, and the sum is [[direct|041JTZCK9Q]], which is condition 1.
8. By definition, $V = U \oplus W$ means that $U + W$ is direct and equal to $V$.
   By steps 1 to 7, the sum is direct exactly when $U \cap W = \{0\}$, which gives the last sentence.

## Idea

Two expressions of one vector differ by an expression of $0$.
An expression $0 = u + w$ with $u \ne 0$ is the same thing as the vector $u = -w$ that lies in both subspaces.
So uniqueness of all expressions, uniqueness of the expression of zero and a zero intersection are three views of one condition.

## Variants

The step from 3 to 1 can be phrased with the addition map $U \times W \to V$, $(u, w) \mapsto u + w$.
This map is linear, and its kernel is $\{(x, -x) : x \in U \cap W\}$.
A linear map is injective exactly when its kernel is zero, so the expressions are unique exactly when $U \cap W = \{0\}$.
The same steps prove the criteria for submodules of a module over any ring.
