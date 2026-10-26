---
tag: 0W0KVBM54S
kind: definition
name: Cyclotomic polynomial
msc: [11T22]
defines: 08KEYFAH66
uses: [0Q9EZS90GY, 0BDX4MBKT4]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclotomic_polynomial
    locator: lead section
---

## Definition

Let $n \ge 1$ be an integer.
The $n$-th cyclotomic polynomial is
$$\Phi_n(x) = \prod_{\substack{1 \le k \le n \\ \gcd(k, n) = 1}} \left(x - e^{2 \pi i k / n}\right) \in \mathbb{C}[x].$$
Its roots are the primitive $n$-th roots of unity: the complex numbers $\zeta$ with $\zeta^n = 1$ and $\zeta^m \neq 1$ for $0 < m < n$.

## Remarks

The polynomial $\Phi_n$ is [[monic|0BDX4MBKT4]] of degree $\varphi(n)$, where $\varphi$ is Euler's totient function.
For each $n \ge 1$, $x^n - 1 = \prod_{d \mid n} \Phi_d(x)$. By induction on $n$, this shows that $\Phi_n$ has integer coefficients.
The first values are $\Phi_1 = x - 1$, $\Phi_2 = x + 1$, $\Phi_3 = x^2 + x + 1$, $\Phi_4 = x^2 + 1$ and $\Phi_6 = x^2 - x + 1$.
For a prime $p$, $\Phi_p = x^{p-1} + x^{p-2} + \dots + x + 1$.

## Explanations

### L1 human

The $n$-th roots of unity are the corners of a regular $n$-gon on the unit circle.
The cyclotomic polynomial $\Phi_n$ collects only the corners that are not roots of unity of a smaller order.
The name means "circle dividing".
