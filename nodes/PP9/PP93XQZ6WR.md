---
tag: PP93XQZ6WR
kind: proof
name: Proof of the diagonalisation of a quadratic form by an orthogonal basis
msc: ["11E04", 15A63]
proves: 0Z3FEWZ8HA
uses: [0HZNE5QZDJ, 0TX2YH2FQS, 0744CN4MDA, 0P799D6AMN, 05Q4JD6XEH, 0RJF668P1T, 02YFME3RGW, 0W4FSW1TVB, 05G2G0P224, 0VTQTPQGAV, 0EVHJFTG9Z, 096V7H13H9]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf
    locator: Theorem 4.7
---

## Proof

We reduce the statement to the existence of an orthogonal basis, which we prove by induction on $n$.

1. Let $B(u, v) = \frac12 \bigl( Q(u + v) - Q(u) - Q(v) \bigr)$ be the [[symmetric bilinear form associated with|0TX2YH2FQS]] $Q$. It is defined since $2 \ne 0$ in $F$.
2. By the definition of a [[quadratic form|0HZNE5QZDJ]], $B$ is a [[bilinear form|0P799D6AMN]]. The formula is unchanged when $u$ and $v$ are swapped, so $B$ is [[symmetric|0744CN4MDA]].
3. For $v \in V$, the rule $Q(av) = a^2 Q(v)$ gives $Q(2v) = 4 Q(v)$. So $B(v, v) = \frac12 \bigl( 4 Q(v) - 2 Q(v) \bigr) = Q(v)$.
4. Suppose $(e_1, \dots, e_n)$ is a basis that is [[orthogonal|05Q4JD6XEH]] for $B$. Let $a_i = Q(e_i)$.
5. By steps 3 and 4 and bilinearity, $Q(\sum_i x_i e_i) = \sum_{i,j} x_i x_j B(e_i, e_j) = \sum_i a_i x_i^2$. So it suffices to find a $B$-orthogonal basis.
6. We prove by induction on $n$: every symmetric bilinear form on an $n$-dimensional space over $F$ has an orthogonal [[basis|0VTQTPQGAV]]. For $n \le 1$, every basis is orthogonal, since there are no two distinct indices.
7. Let $n \ge 2$, and assume the claim in dimension $n - 1$. Let $B$ be a symmetric bilinear form on $V$ with $\dim V = n$.
8. Suppose first that $B(v, v) = 0$ for all $v$. Expanding by bilinearity and symmetry, $B(u + v, u + v) = B(u, u) + 2 B(u, v) + B(v, v)$.
9. So $2 B(u, v) = 0$, and $B(u, v) = 0$ for all $u, v$. Then every basis of $V$ is orthogonal.
10. Otherwise choose $e_1 \in V$ with $c = B(e_1, e_1) \ne 0$. The map $f(v) = B(e_1, v)$ is a [[linear map|0RJF668P1T]] from $V$ to $F$.
11. Since $f(e_1) = c \ne 0$, the image of $f$ is all of $F$, which has dimension $1$. Let $W$ be the [[kernel|02YFME3RGW]] of $f$.
12. By the [[rank–nullity theorem|0W4FSW1TVB]], $\dim W = n - 1$.
13. The restriction of $B$ to $W \times W$ is a symmetric bilinear form on $W$. By the induction hypothesis, $W$ has a basis $e_2, \dots, e_n$ that is orthogonal for $B$.
14. The family $e_1, \dots, e_n$ is [[linearly independent|0EVHJFTG9Z]]. Indeed, let $c_1 e_1 + \cdots + c_n e_n = 0$. Applying $f$ gives $c_1 c = 0$, since $f(e_i) = 0$ for $i \ge 2$.
15. So $c_1 = 0$. Then $c_2 e_2 + \cdots + c_n e_n = 0$, and $c_2 = \cdots = c_n = 0$ since $e_2, \dots, e_n$ is a basis of $W$.
16. By the [[definition of dimension|05G2G0P224]] and [[the basis criterion|096V7H13H9]], the $n$ independent vectors $e_1, \dots, e_n$ form a basis of $V$.
17. For $2 \le i \ne j$, $B(e_i, e_j) = 0$ by step 13. For $j \ge 2$, $B(e_1, e_j) = f(e_j) = 0$, and $B(e_j, e_1) = 0$ by symmetry.
18. So $e_1, \dots, e_n$ is an orthogonal basis, which completes the induction.
19. Apply step 6 to the form $B$ of step 1. By step 5, $Q(x_1 e_1 + \cdots + x_n e_n) = a_1 x_1^2 + \cdots + a_n x_n^2$ with $a_i = Q(e_i)$.

## Idea

In an orthogonal basis the cross terms $x_i x_j$ disappear, so it is enough to build such a basis. Pick a vector $e_1$ with $Q(e_1) \ne 0$ and pass to the hyperplane of vectors orthogonal to it. Induction finishes the job, and if no such $e_1$ exists the form is zero.
