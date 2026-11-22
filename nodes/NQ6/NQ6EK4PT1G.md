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

We get parts 1 and 2 from additivity and the group axioms of $W$, part 3 by induction on $k$, and the last claim by special choices of $a$ and $v$.
Let $T \colon V \to W$ be a [[linear map|0RJF668P1T]].

1. In $V$ we have $0 + 0 = 0$, so additivity gives $T(0) = T(0 + 0) = T(0) + T(0)$.
2. Adding $-T(0)$ to both sides in $W$ and using the axioms of a [[vector space|000AYPA9AJ]] gives $0 = T(0)$, which is part 1.
3. Let $v \in V$; since $v + (-v) = 0$, additivity and step 2 give $T(v) + T(-v) = T(0) = 0$.
4. The additive inverse of $T(v)$ in $W$ is unique, and step 3 shows that $T(-v)$ is an inverse, so $T(-v) = -T(v)$, which is part 2.
5. For part 3 we use induction on $k$; for $k = 1$, homogeneity gives $T(a_1 v_1) = a_1 T(v_1)$.
6. Suppose part 3 holds for some $k \ge 1$, and put $u = a_1 v_1 + \dots + a_k v_k$, so that the combination of $k + 1$ terms is $u + a_{k+1} v_{k+1}$.
7. Additivity gives $T(u + a_{k+1} v_{k+1}) = T(u) + T(a_{k+1} v_{k+1})$.
8. The induction hypothesis gives $T(u) = a_1 T(v_1) + \dots + a_k T(v_k)$, and homogeneity gives $T(a_{k+1} v_{k+1}) = a_{k+1} T(v_{k+1})$.
9. Steps 7 and 8 together give part 3 for $k + 1$, so by [[induction|0ASJVEFA9J]] part 3 holds for each $k \ge 1$.
10. For the last claim, if $T$ is linear, then additivity and then homogeneity give $T(au + v) = T(au) + T(v) = a\,T(u) + T(v)$.
11. Conversely, suppose $T(au + v) = a\,T(u) + T(v)$ for all $u, v \in V$ and $a \in F$; the case $a = 1$ is additivity.
12. Steps 1 and 2 used only additivity, so $T(0) = 0$, and the case $v = 0$ gives $T(au) = a\,T(u) + T(0) = a\,T(u)$, which is homogeneity.
13. So $T$ is linear if and only if $T(au + v) = a\,T(u) + T(v)$ for all $u, v \in V$ and $a \in F$.

## Idea

The zero vector is the one vector with $0 + 0 = 0$, and additivity copies this equation into $W$, where it forces $T(0) = 0$.
Negatives follow in the same way from $v + (-v) = 0$.
Longer [[linear combinations|0V8F3E48E6]] are built by adding one term at a time, so induction on the number of terms does the rest.
The single condition $T(au + v) = a\,T(u) + T(v)$ contains both conditions as special cases, with $a = 1$ and with $v = 0$.

## Variants

Part 1 also follows from homogeneity alone: $T(0) = T(0 \cdot 0) = 0 \cdot T(0) = 0$, because $0 \cdot w = 0$ for each $w \in W$.
Part 2 also follows from homogeneity, because $-v = (-1)v$ in every vector space, so $T(-v) = (-1)\,T(v) = -T(v)$.
