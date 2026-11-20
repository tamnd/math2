---
tag: NQ6EK4PT1G
kind: proof
name: Proof that linear maps preserve zero, negatives and linear combinations
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
proves: STYEWH8R4E
methods: [0NTF6DMVAP, 0ASJVEFA9J]
uses: [0RJF668P1T, 000AYPA9AJ, 0V8F3E48E6]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Definition and first consequences
  - book: isbn:9780134860244
    locator: Section 2.1
---

## Proof

Let $T \colon V \to W$ be a [[linear map|0RJF668P1T]].

1. In $V$ we have $0 + 0 = 0$. Additivity gives $T(0) = T(0 + 0) = T(0) + T(0)$.
2. We add $-T(0)$ to both sides in $W$. The axioms of a [[vector space|000AYPA9AJ]] give $0 = T(0)$. This proves part 1.
3. Let $v \in V$. Since $v + (-v) = 0$, additivity and step 2 give $T(v) + T(-v) = T(0) = 0$.
4. In $W$ the additive inverse of $T(v)$ is unique. By step 3, $T(-v)$ is this inverse, so $T(-v) = -T(v)$. This proves part 2.
5. We prove part 3 by induction on $k$. For $k = 1$, homogeneity gives $T(a_1 v_1) = a_1 T(v_1)$.
6. Suppose part 3 holds for some $k \ge 1$, and let $u = a_1 v_1 + \dots + a_k v_k$. Then $a_1 v_1 + \dots + a_{k+1} v_{k+1} = u + a_{k+1} v_{k+1}$.
7. Additivity gives $T(u + a_{k+1} v_{k+1}) = T(u) + T(a_{k+1} v_{k+1})$.
8. The induction hypothesis gives $T(u) = a_1 T(v_1) + \dots + a_k T(v_k)$, and homogeneity gives $T(a_{k+1} v_{k+1}) = a_{k+1} T(v_{k+1})$.
9. Steps 7 and 8 give part 3 for $k + 1$. By induction, part 3 holds for each $k \ge 1$.
10. Now the last claim. If $T$ is linear, then additivity and homogeneity give $T(au + v) = T(au) + T(v) = a T(u) + T(v)$.
11. Conversely, suppose $T(au + v) = a T(u) + T(v)$ for all $u, v \in V$ and $a \in F$. The case $a = 1$ is additivity.
12. Steps 1 and 2 used only additivity, so $T(0) = 0$. The case $v = 0$ then gives $T(au) = a T(u) + T(0) = a T(u)$, which is homogeneity.
13. So $T$ is linear if and only if $T(au + v) = a T(u) + T(v)$ for all $u, v$ and $a$.

## Idea

The zero vector is the only vector with $0 + 0 = 0$, and additivity copies this equation into $W$.
Negatives and longer [[linear combinations|0V8F3E48E6]] follow by adding one term at a time.
The single condition $T(au + v) = aT(u) + T(v)$ contains both conditions as special cases.

## Variants

- Part 1 also follows from homogeneity alone: $T(0) = T(0 \cdot 0) = 0 \cdot T(0) = 0$, because $0 \cdot w = 0$ for each $w \in W$.
- Part 2 also follows from homogeneity: $T(-v) = T((-1) v) = (-1)\, T(v) = -T(v)$.
