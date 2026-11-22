---
tag: PP93XQZ6WR
kind: proof
name: Proof of the diagonalization of a quadratic form by an orthogonal basis
msc: ["11E04", "15A63"]
topics: [6TSCEW8QMK]
audience: ug1
proves: 0Z3FEWZ8HA
methods: [0ASJVEFA9J, 0WCP0PVET6]
uses: [0HZNE5QZDJ, 0TX2YH2FQS, 0744CN4MDA, 0P799D6AMN, 05Q4JD6XEH, 0RJF668P1T, 02YFME3RGW, 0W4FSW1TVB, 05G2G0P224, 0VTQTPQGAV, 0EVHJFTG9Z, 096V7H13H9]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf
    locator: Theorem 4.7
---

## Proof

We reduce the statement to the existence of an orthogonal basis for the associated bilinear form, and we build that basis by induction on $n = \dim V$.

1. Let $B(u, v) = \tfrac{1}{2} \bigl( Q(u + v) - Q(u) - Q(v) \bigr)$ be the [[symmetric bilinear form associated with|0TX2YH2FQS]] $Q$, which is defined because $2 \ne 0$ in $F$.
   By the definition of a [[quadratic form|0HZNE5QZDJ]], $B$ is a [[bilinear form|0P799D6AMN]], and it is [[symmetric|0744CN4MDA]] because the formula does not change when $u$ and $v$ are exchanged.
2. The rule $Q(av) = a^2 Q(v)$ gives $Q(2v) = 4Q(v)$, so $B(v, v) = \tfrac{1}{2}\bigl(4Q(v) - 2Q(v)\bigr) = Q(v)$.
3. Suppose $(e_1, \dots, e_n)$ is a basis that is [[orthogonal|05Q4JD6XEH]] for $B$, and let $a_i = Q(e_i)$.
   By bilinearity and step 2,
   $$Q\Bigl(\sum_i x_i e_i\Bigr) = \sum_{i, j} x_i x_j B(e_i, e_j) = \sum_i a_i x_i^2.$$
   So it suffices to find a $B$-orthogonal basis.
4. We prove by induction on $n$ that every symmetric bilinear form on an $n$-dimensional space over $F$ has an orthogonal [[basis|0VTQTPQGAV]].
   For $n \le 1$ every basis is orthogonal, since there are no two distinct indices.
5. Let $n \ge 2$, assume the claim in dimension $n - 1$, and let $B$ be a symmetric bilinear form on $V$ with $\dim V = n$.
6. Suppose first that $B(v, v) = 0$ for all $v$.
   Bilinearity and symmetry give $B(u + v, u + v) = B(u, u) + 2B(u, v) + B(v, v)$, so $2B(u, v) = 0$ and, since $2 \ne 0$, $B(u, v) = 0$ for all $u, v$.
   Then every basis of $V$ is orthogonal.
7. Otherwise choose $e_1 \in V$ with $c = B(e_1, e_1) \ne 0$.
   The map $f(v) = B(e_1, v)$ is a [[linear map|0RJF668P1T]] from $V$ to $F$, and $f(e_1) = c \ne 0$, so $f$ is onto $F$.
8. Let $W$ be the [[kernel|02YFME3RGW]] of $f$.
   By the [[rank-nullity theorem|0W4FSW1TVB]], $\dim W = n - 1$.
9. The restriction of $B$ to $W \times W$ is a symmetric bilinear form on $W$.
   By the induction hypothesis, $W$ has a basis $e_2, \dots, e_n$ that is orthogonal for $B$.
10. The family $e_1, \dots, e_n$ is [[linearly independent|0EVHJFTG9Z]].
    Indeed, if $c_1 e_1 + \dots + c_n e_n = 0$, applying $f$ gives $c_1 c = 0$, because $f(e_i) = 0$ for $i \ge 2$.
    So $c_1 = 0$, and then $c_2 = \dots = c_n = 0$ because $e_2, \dots, e_n$ is a basis of $W$.
11. By the [[definition of dimension|05G2G0P224]] and [[the basis criterion|096V7H13H9]], the $n$ independent vectors $e_1, \dots, e_n$ form a basis of $V$.
12. For $i \ne j$ with $i, j \ge 2$, step 9 gives $B(e_i, e_j) = 0$.
    For $j \ge 2$, $B(e_1, e_j) = f(e_j) = 0$, and $B(e_j, e_1) = 0$ by symmetry.
    So $e_1, \dots, e_n$ is an orthogonal basis, which completes the induction.
13. Apply step 4 to the form $B$ of step 1.
    By step 3, $Q(x_1 e_1 + \dots + x_n e_n) = a_1 x_1^2 + \dots + a_n x_n^2$ with $a_i = Q(e_i)$.

## Idea

In an orthogonal basis the cross terms $x_i x_j$ disappear, so it is enough to build such a basis.
Pick a vector $e_1$ with $Q(e_1) \ne 0$, and pass to the hyperplane of vectors that are orthogonal to it.
Induction handles the hyperplane.
If no such $e_1$ exists, the identity $2B(u, v) = B(u + v, u + v) - B(u, u) - B(v, v)$ shows that the form is zero, and this is where the characteristic enters.

## Variants

[[Lagrange's method|BDT6XBCRDJ]] proves the same theorem in coordinates, by completing squares one variable at a time.
In matrix form the proof is a symmetric row and column reduction: each row operation on $A$ is followed by the same column operation, and the result is $P^{\mathsf{T}} A P$ with $P$ invertible.
Over $\mathbb{R}$, [[the principal axis theorem|0PR5P9Z4KM]] gives an orthonormal basis for the dot product at the same time, but its proof needs the spectral theorem.
