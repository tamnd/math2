---
tag: M4VHXJSCD5
kind: proof
name: Proof of the kernel test for injectivity
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
proves: 0BJBYCGMWE
methods: [TFQ1845T84, DD2P85Y8E9, 0NTF6DMVAP]
uses: [0NRYHJPQG2, 0S23E6YE83, 02YFME3RGW, 0PVG1CRAJN, 0EVHJFTG9Z, STYEWH8R4E, REWYZ8N7EN, 0VTQTPQGAV]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: Properties
  - book: isbn:9780134860244
    locator: Section 2.1
---

## Proof

We prove part 1 from the fact that $T(u) = T(v)$ means $u - v \in \ker T$, and then we turn dependences among images into kernel vectors for parts 2 and 3.

Part 1.

1. By the [[lemma on zero|STYEWH8R4E]], $T(0) = 0$, so $\{0\} \subseteq \ker T$ always holds.
2. By the [[lemma on the kernel|REWYZ8N7EN]], $T(u) = T(v)$ if and only if $u - v \in \ker T$.
3. Suppose $T$ is injective, and let $v \in \ker T$; then $T(v) = 0 = T(0)$, so $v = 0$ by [[injectivity|0PVG1CRAJN]], and $\ker T = \{0\}$.
4. Suppose $\ker T = \{0\}$, and let $T(u) = T(v)$; by step 2, $u - v \in \ker T$, so $u - v = 0$ and $u = v$.
5. Steps 3 and 4 give part 1.

Part 2.

6. Let $T$ be injective, and suppose $a_1 T(v_1) + \dots + a_k T(v_k) = 0$ with $a_i \in F$.
7. By the [[lemma on linear combinations|STYEWH8R4E]], the left side is $T(a_1 v_1 + \dots + a_k v_k)$.
8. So $a_1 v_1 + \dots + a_k v_k \in \ker T$, and part 1 gives $a_1 v_1 + \dots + a_k v_k = 0$.
9. The $v_i$ are [[linearly independent|0EVHJFTG9Z]], so $a_1 = \dots = a_k = 0$, and the $T(v_i)$ are independent.

Part 3.

10. Let $(b_i)_{i \in I}$ be a [[basis|0VTQTPQGAV]] of $V$ such that $(T(b_i))_{i \in I}$ is linearly independent, and let $v \in \ker T$.
11. Write $v = a_1 b_{i_1} + \dots + a_k b_{i_k}$ with distinct indices; then $0 = T(v) = a_1 T(b_{i_1}) + \dots + a_k T(b_{i_k})$.
12. The $T(b_i)$ are independent, so every $a_j = 0$ and $v = 0$.
13. So $\ker T = \{0\}$, and $T$ is injective by part 1.

## Idea

Two vectors have the same image exactly when their difference lies in the kernel.
So a linear map can merge two vectors only if the kernel contains a nonzero vector.
A dependence among the images pulls back, through linearity, to a vector of the kernel.

## Variants

Part 1 can be stated with fibers: the preimage $T^{-1}(w)$ of each $w \in \im T$ is a coset $v + \ker T$, so every fiber is a translate of the kernel.
Part 2 can also be argued by contrapositive: a nontrivial dependence $\sum a_i T(v_i) = 0$ gives the kernel vector $\sum a_i v_i$, which is nonzero because the $v_i$ are independent.
