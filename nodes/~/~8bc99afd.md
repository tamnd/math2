---
tag: ~8bc99afd
kind: proof
name: Proof that the image of a linear map is a subspace spanned by the images of a spanning set
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
proves: ~b1674adb
methods: [0NTF6DMVAP, MKHVRNW68H]
uses: [0JB228DCWB, 0EPTJA5QV4, 0BJKVF90Z6, 0HR573CHNM, 0F0RPPJ2TT, ~c10ad39e, 0CCQV3884B]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Kernel, image and the rank–nullity theorem
  - book: isbn:9780134860244
    locator: Section 2.1
---

## Proof

Part 1: we check the three conditions in the [[definition of a subspace|0EPTJA5QV4]].

1. By the [[lemma on zero|~c10ad39e]], $0 = T(0)$. So $0 \in \im T$.
2. Let $w_1, w_2 \in \im T$. Then $w_1 = T(v_1)$ and $w_2 = T(v_2)$ for some $v_1, v_2 \in V$.
3. Additivity gives $w_1 + w_2 = T(v_1 + v_2)$. So $w_1 + w_2 \in \im T$.
4. Let $a \in F$. Homogeneity gives $a w_1 = T(a v_1)$. So $a w_1 \in \im T$.
5. Steps 1, 3 and 4 show that $\im T$ is a subspace of $W$.

Part 2: we show both inclusions.

6. Each $T(s)$ with $s \in S$ is in $\im T$. By part 1, $\im T$ is a subspace, so it contains the [[span|0HR573CHNM]] of $T(S)$.
7. Let $w \in \im T$, so $w = T(v)$ for some $v \in V$.
8. $S$ spans $V$, so $v = a_1 s_1 + \dots + a_k s_k$ for some $s_i \in S$ and $a_i \in F$.
9. Part 3 of the [[lemma on linear combinations|~c10ad39e]] gives $w = a_1 T(s_1) + \dots + a_k T(s_k)$. So $w \in \operatorname{span} T(S)$.
10. Steps 6 and 9 give $\im T = \operatorname{span} T(S)$.

Part 3.

11. Let $T(x) = Ax$. The standard basis $e_1, \dots, e_n$ spans $F^n$, and $A e_j$ is the $j$-th column of $A$, by the [[matrix–vector product|0CCQV3884B]].
12. By part 2, $\im T$ is the span of the columns of $A$, which is the [[column space|0F0RPPJ2TT]].

## Idea

Sums and multiples of outputs are outputs of sums and multiples, so the outputs form a subspace.
Every input is a combination of the spanning set, so every output is the same combination of the images.

## Variants

- Part 1 in one step: $a T(v_1) + T(v_2) = T(a v_1 + v_2)$, so the image is closed under the single operation $(w_1, w_2) \mapsto a w_1 + w_2$.
- Part 3 also follows from the formula $Ax = x_1 c_1 + \dots + x_n c_n$, where $c_j$ are the columns of $A$.
