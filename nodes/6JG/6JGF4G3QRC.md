---
tag: 6JGF4G3QRC
kind: proof
name: Proof of the dimension formula for a quotient space
msc: [15A03]
proves: 0SXDQ6TN00
uses: [0QW084460E, 0M4SXE5WW3, 0WK0Y8RH1M, 0BR3FY5Q8M, 0KCQ9Y3QKA, 0CRMGPAH83, 088RYKAWK9, 03GSZ8RTZJ, 0ZHWKQMVX5]
sources:
  - url: https://pi.math.cornell.edu/~dcollins/math4310/IsomorphismTheorems.pdf
    locator: Proposition 1
---

## Proof

We extend a basis of $W$ to a basis of $V$ and show that the cosets of the new vectors form a basis of $V / W$.

1. Let $n = \dim V$. By the [[dimension of a subspace|0QW084460E]], $W$ is finite-dimensional. Let $m = \dim W$ and let $(w_1, \dots, w_m)$ be a [[basis|0KCQ9Y3QKA]] of $W$.
2. The family $(w_1, \dots, w_m)$ is [[linearly independent|0CRMGPAH83]] in $V$. By [[extension to a basis|0M4SXE5WW3]], it is part of a basis of $V$.
3. By the [[dimension theorem|0WK0Y8RH1M]], this basis has $n$ vectors. Write it as $(w_1, \dots, w_m, v_{m+1}, \dots, v_n)$.
4. In the [[quotient space|0BR3FY5Q8M]] $V / W$, the zero vector is $0 + W = W$, since $(0 + W) + (v + W) = v + W$ for all $v \in V$.
5. For $x \in V$, we have $x + W = W$ if and only if $x \in W$. If $x + W = W$, then $x = x + 0 \in W$. If $x \in W$, then $x + w \in W$ and $w = x + (w - x)$ for each $w \in W$, so $x + W = W$.
6. The cosets $v_{m+1} + W, \dots, v_n + W$ [[span|088RYKAWK9]] $V / W$. Let $v + W \in V / W$, and write $v = \sum_{i=1}^m a_i w_i + \sum_{k=m+1}^n a_k v_k$ in the basis of step 3.
7. By the operations of $V / W$, $v + W = \sum_{i=1}^m a_i (w_i + W) + \sum_{k=m+1}^n a_k (v_k + W)$.
8. Each $w_i$ lies in $W$, so $w_i + W$ is the zero vector by steps 4 and 5. Hence $v + W = \sum_{k=m+1}^n a_k (v_k + W)$.
9. The cosets $v_{m+1} + W, \dots, v_n + W$ are linearly independent. Suppose $\sum_{k=m+1}^n b_k (v_k + W) = W$ with $b_k \in F$.
10. The left side equals $x + W$ with $x = \sum_{k=m+1}^n b_k v_k$. By step 5, $x \in W$.
11. Since $(w_1, \dots, w_m)$ spans $W$, $x = \sum_{i=1}^m d_i w_i$ for some $d_1, \dots, d_m \in F$.
12. Then $\sum_{i=1}^m d_i w_i - \sum_{k=m+1}^n b_k v_k = 0$. The basis of step 3 is linearly independent, so all $b_k = 0$.
13. By steps 6 to 12, $(v_{m+1} + W, \dots, v_n + W)$ is a basis of $V / W$ with $n - m$ vectors.
14. So $V / W$ is [[finite-dimensional|0ZHWKQMVX5]] with [[dimension|03GSZ8RTZJ]] $n - m$. Hence $\dim(V / W) + \dim W = (n - m) + m = \dim V$.

## Idea

Choose a basis of $V$ that starts with a basis of $W$. Passing to the quotient kills the vectors of $W$. The remaining basis vectors survive as cosets and form a basis of $V / W$, so exactly $\dim W$ dimensions are lost.
