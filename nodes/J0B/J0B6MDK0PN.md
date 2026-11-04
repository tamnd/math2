---
tag: J0B6MDK0PN
kind: proof
name: Proof of the dimension of the annihilator by a dual basis
msc: [15A03, 15A04]
proves: 06Q1EFVH0Q
uses: [0R6M158SQ9, 0QW084460E, 0KCQ9Y3QKA, 0M4SXE5WW3, 03GSZ8RTZJ, 0W6M3PSD08, 0ZD2CF6ZS0, 0R8X9XA83A]
sources:
  - url: https://math.iisc.ac.in/~vamsipingali/teaching/ma219linalgebra2019fall/12Sept2019.pdf
    locator: Theorem 2.1
---

## Proof

1. Let $n = \dim V$. By the result on the [[dimension of a subspace|0QW084460E]], $W$ is finite-dimensional. Let $k = \dim W$.
2. Let $b_1, \dots, b_k$ be a [[basis|0KCQ9Y3QKA]] of $W$. It is linearly independent in $V$, so it [[extends to a basis|0M4SXE5WW3]] of $V$.
3. By the definition of [[dimension|03GSZ8RTZJ]], this basis of $V$ has $n$ elements. Write it as $b_1, \dots, b_n$.
4. Let $b_1^*, \dots, b_n^* \in V^*$ be the [[dual basis|0W6M3PSD08]], so $b_i^*(b_j) = \delta_{ij}$. Here $\delta_{ij} = 1$ if $i = j$ and $\delta_{ij} = 0$ otherwise.
5. We claim that $b_{k+1}^*, \dots, b_n^*$ is a basis of the [[annihilator|0R6M158SQ9]] $W^0 = \set{f \in V^* : f(w) = 0 \text{ for all } w \in W}$.
6. Each $b_i^*$ with $i > k$ lies in $W^0$. Indeed, each $w \in W$ is $w = \sum_{j=1}^{k} c_j b_j$ with $c_j \in F$. Then $b_i^*(w) = \sum_{j=1}^{k} c_j \delta_{ij} = 0$, since $j \le k < i$.
7. The forms $b_{k+1}^*, \dots, b_n^*$ are linearly independent. Suppose $\sum_{i=k+1}^{n} c_i b_i^* = 0$ with $c_i \in F$.
8. Evaluate the sum of step 7 at $b_j$ for $j > k$. This gives $\sum_{i=k+1}^{n} c_i \delta_{ij} = c_j = 0$. So all $c_j$ are $0$.
9. The forms $b_{k+1}^*, \dots, b_n^*$ span $W^0$. Let $f \in W^0$ and put $g = \sum_{i=k+1}^{n} f(b_i) b_i^*$.
10. For $j \le k$, we have $g(b_j) = 0$ by step 6, and $f(b_j) = 0$ because $b_j \in W$.
11. For $j > k$, we have $g(b_j) = \sum_{i=k+1}^{n} f(b_i) \delta_{ij} = f(b_j)$.
12. So $f$ and $g$ agree on the basis $b_1, \dots, b_n$. A [[linear map is determined by its values on a basis|0R8X9XA83A]], so $f = g$.
13. By steps 6 to 12, $b_{k+1}^*, \dots, b_n^*$ is a basis of $W^0$. So $\dim W^0 = n - k$.
14. Hence $\dim W + \dim W^0 = k + (n - k) = n = \dim V$.

## Idea

Choose a basis of $V$ that starts with a basis of $W$. The [[dual basis|0ZD2CF6ZS0]] forms that belong to the remaining basis vectors vanish on $W$, and they give exactly the forms that vanish on $W$. So the annihilator has one dimension for each basis vector outside $W$.
