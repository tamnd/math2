---
tag: J0B6MDK0PN
kind: proof
name: Proof of the dimension of the annihilator and of the duals of quotients and subspaces
msc: ["15A03", "15A04"]
topics: [9K7FFF26QR]
audience: ug2
proves: 06Q1EFVH0Q
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0R6M158SQ9, 0QW084460E, 0KCQ9Y3QKA, 0M4SXE5WW3, 03GSZ8RTZJ, 0W6M3PSD08, 0ZD2CF6ZS0, 0R8X9XA83A, 0ZERJX6PH6, 0SVR29SV1V, 0MTBGVZ4XJ]
sources:
  - url: https://math.iisc.ac.in/~vamsipingali/teaching/ma219linalgebra2019fall/12Sept2019.pdf
    locator: Theorem 2.1
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
    locator: Duals of quotient spaces
---

## Proof

*Part 1.*

1. For $g \in (V/U)^*$, the map $g \circ \pi$ is linear and vanishes on $U$, since $\pi(u) = 0$ for $u \in U$. So $g \circ \pi \in U^0$.
2. The map $g \mapsto g \circ \pi$ is linear, since $(ag + bh) \circ \pi = a(g \circ \pi) + b(h \circ \pi)$.
3. It is injective. If $g \circ \pi = 0$, then $g(\pi(v)) = 0$ for all $v$. Since $\pi$ is surjective, $g = 0$.
4. It is surjective. Let $f \in U^0$. Then $f$ vanishes on $U$, so by the [[universal property of the quotient space|0ZERJX6PH6]], $f = g \circ \pi$ for a linear $g \colon V/U \to F$.
5. By steps 1 to 4, $g \mapsto g \circ \pi$ is an isomorphism $(V/U)^* \to U^0$.

*Part 2.*

6. The restriction $r(f) = f|_U$ is linear, and $r(f) = 0$ exactly when $f$ vanishes on $U$. So $\ker r = U^0$.
7. Let $\psi \in U^*$. Choose a basis $C$ of $U$ and [[extend it to a basis|0M4SXE5WW3]] $D$ of $V$.
8. By the [[theorem on maps determined by a basis|0R8X9XA83A]], there is $f \in V^*$ with $f = \psi$ on $C$ and $f = 0$ on $D \setminus C$. Then $f|_U = \psi$, since both are linear and agree on $C$. So $r$ is surjective.
9. By the [[first isomorphism theorem|0MTBGVZ4XJ]], $V^*/\ker r \cong \im r$, that is, $V^*/U^0 \cong U^*$.

*Part 3.*

10. Let $n = \dim V$. By the result on the [[dimension of a subspace|0QW084460E]], $U$ is finite-dimensional. Let $k = \dim U$.
11. Let $b_1, \dots, b_k$ be a [[basis|0KCQ9Y3QKA]] of $U$. It is linearly independent in $V$, so it extends to a basis of $V$.
12. By the definition of [[dimension|03GSZ8RTZJ]], this basis of $V$ has $n$ elements. Write it as $b_1, \dots, b_n$.
13. Let $b_1^*, \dots, b_n^* \in V^*$ be the [[dual basis|0W6M3PSD08]], so $b_i^*(b_j) = \delta_{ij}$.
14. We claim that $b_{k+1}^*, \dots, b_n^*$ is a basis of the [[annihilator|0R6M158SQ9]] $U^0$.
15. Each $b_i^*$ with $i > k$ lies in $U^0$. Each $u \in U$ is $u = \sum_{j=1}^{k} c_j b_j$, so $b_i^*(u) = \sum_{j=1}^{k} c_j \delta_{ij} = 0$, since $j \le k < i$.
16. The forms $b_{k+1}^*, \dots, b_n^*$ are linearly independent. Suppose $\sum_{i=k+1}^{n} c_i b_i^* = 0$ with $c_i \in F$.
17. Evaluate this sum at $b_j$ for $j > k$. This gives $\sum_{i=k+1}^{n} c_i \delta_{ij} = c_j = 0$. So all $c_j$ are $0$.
18. The forms $b_{k+1}^*, \dots, b_n^*$ span $U^0$. Let $f \in U^0$ and put $g = \sum_{i=k+1}^{n} f(b_i) b_i^*$.
19. For $j \le k$, we have $g(b_j) = 0$ by step 15, and $f(b_j) = 0$ because $b_j \in U$.
20. For $j > k$, we have $g(b_j) = \sum_{i=k+1}^{n} f(b_i) \delta_{ij} = f(b_j)$.
21. So $f$ and $g$ agree on the basis $b_1, \dots, b_n$. A [[linear map is determined by its values on a basis|0R8X9XA83A]], so $f = g$.
22. By steps 15 to 21, $b_{k+1}^*, \dots, b_n^*$ is a basis of $U^0$. So $\dim U^0 = n - k$.
23. Hence $\dim U + \dim U^0 = k + (n - k) = n = \dim V$.

## Idea

Choose a basis of $V$ that starts with a basis of $U$.
The [[dual basis|0ZD2CF6ZS0]] forms that belong to the remaining basis vectors vanish on $U$, and they give exactly the forms that vanish on $U$.
So the annihilator has one dimension for each basis vector outside $U$.
Parts 1 and 2 say the same without coordinates: forms that kill $U$ are forms on $V/U$, and forms on $U$ are forms on $V$ up to forms that kill $U$.

## Variants

- Part 3 follows from part 1: $\dim U^0 = \dim (V/U)^* = \dim (V/U) = n - k$, by the [[dimension of the dual space|00889YD15K]] and the [[dimension of a quotient space|0SXDQ6TN00]].
- Part 3 also follows from part 2 and the [[rank-nullity theorem|0W4FSW1TVB]] for $r$: $n = \dim V^* = \dim U^0 + \dim U^* = \dim U^0 + k$.
