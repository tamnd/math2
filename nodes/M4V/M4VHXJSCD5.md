---
tag: M4VHXJSCD5
kind: proof
name: Proof of the kernel test for injectivity
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
proves: 0BJBYCGMWE
methods: [TFQ1845T84, DD2P85Y8E9, 0NTF6DMVAP]
uses: [0NRYHJPQG2, 0S23E6YE83, 02YFME3RGW, 0PVG1CRAJN, 0EVHJFTG9Z, ~c10ad39e, ~46f99cf4, 0VTQTPQGAV]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: Properties
  - book: isbn:9780134860244
    locator: Section 2.1
---

## Proof

Part 1.

1. By the [[lemma on zero|~c10ad39e]], $T(0) = 0$. So $0 \in \ker T$, and $\{0\} \subseteq \ker T$ always holds.
2. By the [[lemma on the kernel|~46f99cf4]], $T(u) = T(v)$ if and only if $u - v \in \ker T$.
3. Suppose $T$ is injective, and let $v \in \ker T$. Then $T(v) = 0 = T(0)$, so $v = 0$ by [[injectivity|0PVG1CRAJN]]. Hence $\ker T = \{0\}$.
4. Suppose $\ker T = \{0\}$, and let $T(u) = T(v)$. By step 2, $u - v \in \ker T$, so $u - v = 0$ and $u = v$.
5. Steps 3 and 4 give part 1.

Part 2.

6. Let $T$ be injective, and let $a_1 T(v_1) + \dots + a_k T(v_k) = 0$ with $a_i \in F$.
7. By the [[lemma on linear combinations|~c10ad39e]], the left side is $T(a_1 v_1 + \dots + a_k v_k)$.
8. So $a_1 v_1 + \dots + a_k v_k \in \ker T$. By part 1, $a_1 v_1 + \dots + a_k v_k = 0$.
9. The $v_i$ are [[linearly independent|0EVHJFTG9Z]], so $a_1 = \dots = a_k = 0$. Hence the $T(v_i)$ are independent.

Part 3.

10. Let $(b_i)_{i \in I}$ be a [[basis|0VTQTPQGAV]] of $V$ with $(T(b_i))_{i \in I}$ linearly independent. Let $v \in \ker T$.
11. Write $v = a_1 b_{i_1} + \dots + a_k b_{i_k}$ with distinct indices. Then $0 = T(v) = a_1 T(b_{i_1}) + \dots + a_k T(b_{i_k})$.
12. The $T(b_i)$ are independent, so all $a_j = 0$ and $v = 0$. So $\ker T = \{0\}$, and $T$ is injective by part 1.

## Idea

Two vectors have the same image exactly when their difference lies in the kernel.
So the map can merge vectors only if the kernel holds a nonzero vector.
A dependence among the images pulls back, through linearity, to a kernel vector.

## Variants

- Part 1 can be stated as: the fibre $T^{-1}(w)$ over each $w \in \im T$ is a coset $v + \ker T$, so all fibres have the size of the kernel.
- Part 2 also follows from the contrapositive: a nontrivial dependence among the $T(v_i)$ gives a nonzero kernel vector $\sum a_i v_i$.
