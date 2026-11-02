---
tag: 4BBW1NZ1CC
kind: definition
name: Jacobi polynomials
msc: [33C45, 42C05]
defines: TRD7DSF2KR
uses: [YZHM3HSM0F]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_polynomials
---

## Definition

Let $\alpha, \beta > -1$ be real numbers and let $n \ge 0$ be an integer.
Write $(a)_k = a (a + 1) \cdots (a + k - 1)$ for the [[Pochhammer symbol|YZHM3HSM0F]], with $(a)_0 = 1$.
The *Jacobi polynomial* of degree $n$ with parameters $\alpha, \beta$ is
$$P_n^{(\alpha, \beta)}(x) = \sum_{k=0}^{n} \frac{(n + \alpha + \beta + 1)_k \, (\alpha + k + 1)_{n-k}}{k! \, (n - k)!} \left( \frac{x - 1}{2} \right)^k.$$

## Remarks

Equivalently, $P_n^{(\alpha, \beta)}(x) = \frac{(\alpha + 1)_n}{n!} \, {}_2F_1\left( -n, n + \alpha + \beta + 1; \alpha + 1; \frac{1 - x}{2} \right)$.
Rodrigues' formula: $(1 - x)^\alpha (1 + x)^\beta P_n^{(\alpha, \beta)}(x) = \frac{(-1)^n}{2^n n!} \frac{d^n}{dx^n} \left( (1 - x)^{\alpha + n} (1 + x)^{\beta + n} \right)$.
They are orthogonal: $\int_{-1}^{1} P_m^{(\alpha, \beta)}(x) P_n^{(\alpha, \beta)}(x) (1 - x)^\alpha (1 + x)^\beta \, dx = 0$ for $m \ne n$.
Example: $P_1^{(\alpha, \beta)}(x) = (\alpha + 1) + (\alpha + \beta + 2) \frac{x - 1}{2}$; for $\alpha = \beta = 0$ this is $x$, the Legendre polynomial $P_1$.
The value at $1$ is $P_n^{(\alpha, \beta)}(1) = \frac{(\alpha + 1)_n}{n!}$, since only the term $k = 0$ survives.
Non-example: for $\alpha = -1$ the weight $(1 - x)^{-1}$ is not integrable near $x = 1$, so the clause $\alpha > -1$ fails and the orthogonality integrals diverge.
