---
tag: KTDW7MF7SF
kind: proof
name: Proof of the remainder theorem
msc: [13F20]
proves: 0TEDQH56RW
uses: [0GYGHKX834, 0Q9EZS90GY, 0GJ7T0NK49, 0125QVNCFQ, 0DPF6WRZW6]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_remainder_theorem
    locator: Direct proof
---

## Proof

Let $R$ be a [[commutative ring|0GYGHKX834]], let $f = a_0 + a_1 x + \dots + a_n x^n \in R[x]$ and let $c \in R$. We first build $q$ directly, then show that every remainder of degree less than $1$ equals $f(c)$.

1. For an integer $k \ge 1$, let $S_k = \sum_{j=0}^{k-1} c^{k-1-j} x^j \in R[x]$.
2. Since $R[x]$ is commutative, $(x - c) S_k = \sum_{j=0}^{k-1} c^{k-1-j} x^{j+1} - \sum_{j=0}^{k-1} c^{k-j} x^j$.
3. The first sum has the terms $c^{k-m} x^m$ for $1 \le m \le k$. The second sum has the terms $c^{k-m} x^m$ for $0 \le m \le k - 1$.
4. All terms with $1 \le m \le k - 1$ cancel. So $(x - c) S_k = x^k - c^k$.
5. By the definition of the [[value|0GJ7T0NK49]], $f(c) = a_0 + a_1 c + \dots + a_n c^n$. So $f - f(c) = \sum_{k=1}^{n} a_k (x^k - c^k)$, where the $k = 0$ terms cancel.
6. By step 4, $f - f(c) = (x - c) q$ with $q = \sum_{k=1}^{n} a_k S_k \in R[x]$. So $f = (x - c) q + f(c)$.
7. The constant polynomial $f(c)$ has [[degree|0DPF6WRZW6]] $0$ or $-\infty$, so its degree is less than $1$. So step 6 is a division of $f$ by $x - c$ with a remainder of degree less than $1$.
8. Now let $q' \in R[x]$ and $r \in R[x]$ with $f = (x - c) q' + r$ and $\deg r < 1$. Then $r$ has no nonzero coefficient of degree at least $1$, so $r$ is a constant $r_0 \in R$.
9. The [[evaluation homomorphism|0125QVNCFQ]] at $c$ is a ring homomorphism. Applying it gives $f(c) = (c - c) q'(c) + r_0 = r_0$.
10. So every remainder of the division of $f$ by $x - c$ is the constant $f(c)$, and step 6 gives $q$ with $f = (x - c) q + f(c)$.

## Idea

Each power satisfies $x^k - c^k = (x - c)(x^{k-1} + c x^{k-2} + \dots + c^{k-1})$. Summing these identities with the coefficients of $f$ shows that $x - c$ divides $f - f(c)$. Evaluating at $c$ then shows that a constant remainder can only be $f(c)$.
