---
tag: 8P9EX19MEW
kind: proof
name: Proof that R[x] is an integral domain iff R is
msc: [13F20]
proves: 0B5Z1EC66J
uses: [0GYGHKX834, 0Q9EZS90GY, 09S3PFBEPM, 0T233AZ1GE, 0DPF6WRZW6]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_ring
    locator: Properties that pass from R to R[X]
---

## Proof

Let $R$ be a [[commutative ring|0GYGHKX834]]. We identify $r \in R$ with the constant polynomial $(r, 0, 0, \dots)$ of the [[polynomial ring|0Q9EZS90GY]] $R[x]$.

1. The ring $R[x]$ is commutative, because $R$ is commutative and the coefficient $\sum_{i + j = n} a_i b_j$ of a product is symmetric in the two factors.
2. For $r, s \in R$, the product of the constant polynomials $r$ and $s$ is the constant polynomial $r s$. This follows from the product formula, since only $c_0 = r s$ can be nonzero.
3. Two constant polynomials $r$ and $s$ are equal exactly when $r = s$, since polynomials are equal when all their coefficients are equal.

First suppose that $R$ is an [[integral domain|09S3PFBEPM]].

4. The identity of $R[x]$ is the constant $1$ and its zero is the constant $0$. By step 3 and $1 \neq 0$ in $R$, we get $1 \neq 0$ in $R[x]$.
5. Let $f, g \in R[x]$ with $f \neq 0$ and $g \neq 0$. Their [[degrees|0DPF6WRZW6]] are integers $\deg f \ge 0$ and $\deg g \ge 0$.
6. By the [[degree of a product|0T233AZ1GE]], $\deg(f g) = \deg f + \deg g \ge 0$. So $\deg(f g) \ne -\infty$, and $f g \neq 0$.
7. By steps 1, 4 and 6, $R[x]$ is an integral domain.

Now suppose that $R[x]$ is an integral domain.

8. The ring $R$ is commutative by hypothesis.
9. In $R[x]$ the constants $1$ and $0$ differ. By step 3, $1 \neq 0$ in $R$.
10. Let $a, b \in R$ with $a b = 0$. By step 2, the product of the constants $a$ and $b$ is the constant $0$ in $R[x]$.
11. Since $R[x]$ is an integral domain, the constant $a$ or the constant $b$ is $0$. By step 3, $a = 0$ or $b = 0$.
12. By steps 8, 9 and 11, $R$ is an integral domain. This proves both directions.

## Idea

The leading coefficient of a product of two polynomials is the product of their leading coefficients. If $R$ has no zero divisors, this coefficient is not zero, so the product is not zero. Conversely, $R$ sits inside $R[x]$ as the constants, so zero divisors in $R$ would be zero divisors in $R[x]$.
