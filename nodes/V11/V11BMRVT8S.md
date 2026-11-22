---
tag: V11BMRVT8S
kind: proof
name: Proof that the image of a linear map is a subspace spanned by the images of a spanning set
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
proves: B6KFVB1H5F
methods: [0NTF6DMVAP, MKHVRNW68H]
uses: [0JB228DCWB, 0EPTJA5QV4, 0BJKVF90Z6, 0HR573CHNM, 0F0RPPJ2TT, STYEWH8R4E, 0CCQV3884B]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Kernel, image and the rank–nullity theorem
  - book: isbn:9780134860244
    locator: Section 2.1
---

## Proof

We check the subspace conditions for part 1, prove two inclusions for part 2, and apply part 2 to the standard basis for part 3.

Part 1 uses the three conditions in the [[definition of a subspace|0EPTJA5QV4]].

1. By the [[lemma on zero|STYEWH8R4E]], $0 = T(0)$, so $0 \in \im T$.
2. Let $w_1, w_2 \in \im T$, so that $w_1 = T(v_1)$ and $w_2 = T(v_2)$ for some $v_1, v_2 \in V$.
3. Additivity gives $w_1 + w_2 = T(v_1) + T(v_2) = T(v_1 + v_2)$, so $w_1 + w_2 \in \im T$.
4. Let $a \in F$; homogeneity gives $a w_1 = a\,T(v_1) = T(a v_1)$, so $a w_1 \in \im T$.
5. Steps 1, 3 and 4 show that $\im T$ is a subspace of $W$.

Part 2 shows that $\operatorname{span} T(S)$ and $\im T$ contain each other.

6. Each $T(s)$ with $s \in S$ lies in $\im T$, and $\im T$ is a subspace by part 1, so it contains the [[span|0HR573CHNM]] of $T(S)$.
7. Conversely, let $w \in \im T$, so that $w = T(v)$ for some $v \in V$.
8. Since $S$ [[spans|0BJKVF90Z6]] $V$, we can write $v = a_1 s_1 + \dots + a_k s_k$ with $s_i \in S$ and $a_i \in F$.
9. The [[lemma on linear combinations|STYEWH8R4E]] gives $w = a_1 T(s_1) + \dots + a_k T(s_k)$, so $w \in \operatorname{span} T(S)$.
10. Steps 6 and 9 give $\im T = \operatorname{span} T(S)$.

Part 3 is the case of a matrix map.

11. Let $T(x) = Ax$; the standard basis $e_1, \dots, e_n$ spans $F^n$, and $A e_j$ is the $j$-th column of $A$, by the [[matrix-vector product|0CCQV3884B]].
12. By part 2, $\im T$ is the span of the columns of $A$, which is the [[column space|0F0RPPJ2TT]] of $A$.

## Idea

A sum or multiple of outputs is the output of the corresponding sum or multiple of inputs, so the outputs form a subspace.
Every input is a combination of the spanning set, and linearity turns it into the same combination of the images.
For a matrix, the images of the standard basis vectors are the columns.

## Variants

Part 1 can be done in one step: $a\,T(v_1) + T(v_2) = T(a v_1 + v_2)$, so the image is closed under $(w_1, w_2) \mapsto a w_1 + w_2$, and it contains $0$.
Part 3 also follows from the formula $Ax = x_1 c_1 + \dots + x_n c_n$, where $c_1, \dots, c_n$ are the columns of $A$.
The same proof shows that $T(U)$ is a subspace for every subspace $U$ of $V$, by replacing $V$ with $U$.
