---
tag: 43DXNAFZ9T
kind: statement
role: theorem
name: Interlacing of zeros of orthogonal polynomials
msc: [42C05, 33C45]
uses: [8TXASARQN1, FQTXV6BQZG, DARX1KZRHZ, 8QQPVNR80F]
about: [8TXASARQN1]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_polynomials
---

## Statement

Let $\mu$ be a positive Borel measure on $\R$ with finite moments of all orders and infinite [[support|FQTXV6BQZG]].
Let $(p_n)_{n \ge 0}$ be a sequence of real [[orthogonal polynomials|8TXASARQN1]] for $\mu$, and let $I$ be the smallest closed interval that contains the support of $\mu$.

1. For every $n \ge 1$, the polynomial $p_n$ has $n$ distinct real zeros, and all of them lie in the interior of $I$.
2. Let $x_{n,1} < \cdots < x_{n,n}$ be the zeros of $p_n$. Then the zeros of $p_n$ and $p_{n+1}$ strictly interlace:
$$x_{n+1,k} < x_{n,k} < x_{n+1,k+1} \quad \text{for } k = 1, \dots, n.$$

## Remarks

For part 1, let $y_1, \dots, y_m$ be the zeros of odd multiplicity of $p_n$ in the interior of $I$, the points where $p_n$ changes sign.
Suppose $m < n$.
Then $p_n(x) \prod_j (x - y_j)$ does not change sign on $I$ and is not zero $\mu$-almost everywhere, so its integral against $\mu$ is not zero.
But $\prod_j (x - y_j)$ has degree $m < n$, and $p_n$ is orthogonal to all polynomials of lower degree, a contradiction.
Part 2 follows from the three-term recurrence through the Christoffel–Darboux formula.
If the leading coefficients are positive, it gives $p_{n+1}'(x) p_n(x) - p_{n+1}(x) p_n'(x) > 0$ for all real $x$.
Evaluating at consecutive zeros of $p_{n+1}$ shows that $p_n$ changes sign between them.

Example: for the Legendre polynomials, $p_1 = x$ has the zero $0$, and $p_2 = \frac12(3x^2 - 1)$ has the zeros $\pm 1/\sqrt{3}$.
Indeed $-1/\sqrt{3} < 0 < 1/\sqrt{3}$, and all lie in $(-1, 1)$.

## Explanations

### L1 human

The $n$-th orthogonal polynomial crosses the axis exactly $n$ times, inside the region where the measure lives.
Moreover, the crossings of consecutive polynomials alternate: between two crossings of one there is exactly one crossing of the other.
This regular pattern is a fingerprint of orthogonality.

### L2 human

The zeros of $p_n$ are the eigenvalues of the $n \times n$ truncated Jacobi matrix, the symmetric [[tridiagonal matrix|DARX1KZRHZ]] built from the recurrence coefficients.
In this language, interlacing is the [[Cauchy interlacing theorem|8QQPVNR80F]] for a matrix and its principal submatrix.
The zeros of $p_n$ are the nodes of Gaussian quadrature for $\mu$, and the fact that they are real, simple and inside $I$ is what makes that quadrature work.
As $n \to \infty$, the counting measures of the zeros, divided by $n$, describe the asymptotic distribution of the zeros, a central topic of the theory.
