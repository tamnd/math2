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

We prove parts 1 and 2 of the [[theorem|06Q1EFVH0Q]] from the universal property of the quotient and the extension of a basis, and part 3 with a dual basis adapted to $U$.

*Part 1: forms that kill $U$ are forms on $V/U$.*

1. Let $g \in (V/U)^*$. The map $g \circ \pi$ is linear, and it vanishes on $U$ because $\pi(u) = 0$ for $u \in U$. So $g \circ \pi \in U^0$.
2. The map $g \mapsto g \circ \pi$ is linear, since $(ag + bh) \circ \pi = a(g \circ \pi) + b(h \circ \pi)$ for $a, b \in F$.
3. It is injective. If $g \circ \pi = 0$, then $g(\pi(v)) = 0$ for every $v \in V$, and $\pi$ is onto $V/U$, so $g = 0$.
4. It is surjective. Let $f \in U^0$. Since $f$ vanishes on $U$, the [[universal property of the quotient space|0ZERJX6PH6]] gives a linear $g \colon V/U \to F$ with $f = g \circ \pi$.
5. By steps 1 to 4, $g \mapsto g \circ \pi$ is an isomorphism $(V/U)^* \to U^0$.

*Part 2: forms on $U$ are forms on $V$ up to $U^0$.*

6. The restriction $r(f) = f|_U$ is linear, and $r(f) = 0$ exactly when $f$ vanishes on $U$. So $\ker r = U^0$.
7. Let $\psi \in U^*$. Choose a basis $C$ of $U$ and [[extend it to a basis|0M4SXE5WW3]] $D$ of $V$.
8. By the [[theorem on maps determined by a basis|0R8X9XA83A]], there is $f \in V^*$ with $f = \psi$ on $C$ and $f = 0$ on $D \setminus C$.
9. The forms $f|_U$ and $\psi$ are linear and agree on the basis $C$ of $U$, so $f|_U = \psi$. Hence $r$ is surjective.
10. By the [[first isomorphism theorem|0MTBGVZ4XJ]], $V^*/\ker r \cong \im r$, that is, $V^*/U^0 \cong U^*$.

*Part 3: the count in finite dimension.*

11. Let $n = \dim V$. By the theorem on the [[dimension of a subspace|0QW084460E]], $U$ is finite-dimensional; let $k = \dim U$.
12. Let $b_1, \dots, b_k$ be a [[basis|0KCQ9Y3QKA]] of $U$. It is linearly independent in $V$, so it extends to a basis of $V$, which has $n$ elements by the definition of [[dimension|03GSZ8RTZJ]]. Write this basis as $b_1, \dots, b_n$.
13. Let $b_1^*, \dots, b_n^*$ be the [[dual basis|0W6M3PSD08]] of $V^*$, so that $b_i^*(b_j) = \delta_{ij}$. We claim that $b_{k+1}^*, \dots, b_n^*$ is a basis of $U^0$.
14. Each $b_i^*$ with $i > k$ lies in $U^0$. A vector $u \in U$ has the form $u = \sum_{j=1}^{k} c_j b_j$, so
$$b_i^*(u) = \sum_{j=1}^{k} c_j \delta_{ij} = 0,$$
because $j \le k < i$ in every term.
15. The forms $b_{k+1}^*, \dots, b_n^*$ are independent. Suppose $\sum_{i=k+1}^{n} c_i b_i^* = 0$. Evaluating at $b_j$ with $j > k$ gives $\sum_{i=k+1}^{n} c_i \delta_{ij} = c_j = 0$.
16. The forms $b_{k+1}^*, \dots, b_n^*$ span $U^0$. Let $f \in U^0$ and put $g = \sum_{i=k+1}^{n} f(b_i)\, b_i^*$.
17. For $j \le k$, we have $g(b_j) = 0$ by the computation of step 14, and $f(b_j) = 0$ because $b_j \in U$.
18. For $j > k$, we have $g(b_j) = \sum_{i=k+1}^{n} f(b_i) \delta_{ij} = f(b_j)$.
19. So $f$ and $g$ agree on the basis $b_1, \dots, b_n$, and a [[linear map is determined by its values on a basis|0R8X9XA83A]], so $f = g$.
20. By steps 14 to 19, $b_{k+1}^*, \dots, b_n^*$ is a basis of $U^0$. So $\dim U^0 = n - k$, and
$$\dim U + \dim U^0 = k + (n - k) = n = \dim V.$$

## Idea

Choose a basis of $V$ that starts with a basis of $U$.
The forms of the [[dual basis|0ZD2CF6ZS0]] that belong to the remaining basis vectors kill $U$, and every form that kills $U$ is a combination of them.
So the annihilator gets one dimension for each basis vector outside $U$, and that is $\dim V - \dim U$.
Parts 1 and 2 say the same thing without coordinates: a form that kills $U$ is a form on $V/U$, and a form on $U$ is the restriction of a form on $V$, unique up to a form that kills $U$.

## Variants

Part 3 also follows from part 1.
In finite dimension, $\dim U^0 = \dim (V/U)^* = \dim (V/U) = n - k$, by the theorem on the [[dimension of the dual space|00889YD15K]] and the formula for the [[dimension of a quotient space|0SXDQ6TN00]].

Part 3 also follows from part 2.
The [[rank-nullity theorem|0W4FSW1TVB]] for the surjective map $r \colon V^* \to U^*$ gives $n = \dim V^* = \dim U^0 + \dim U^* = \dim U^0 + k$.
Both variants use $\dim W^* = \dim W$ for a finite-dimensional space $W$, which the dual basis proves.
