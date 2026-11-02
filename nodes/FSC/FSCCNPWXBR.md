---
tag: FSCCNPWXBR
kind: definition
name: Jack function
msc: ["05E05", 33C52]
defines: WW7H1KNXK8
uses: [PAJEHWXW6M, 0JV30XN73Z, 0ZNXZB4HNB]
sources:
  - url: https://en.wikipedia.org/wiki/Jack_function
---

## Definition

Let $\alpha$ be a positive real number, and let $\Lambda$ be the ring of [[symmetric functions|PAJEHWXW6M]] in variables $x = (x_1, x_2, \dots)$ with real coefficients.
For a [[partition|0JV30XN73Z]] $\lambda$ with $\ell(\lambda)$ parts, let $m_\lambda$ be the monomial symmetric function and $p_\lambda = p_{\lambda_1} p_{\lambda_2} \cdots$ the product of [[power sums|0ZNXZB4HNB]].
Let $z_\lambda = \prod_{i \ge 1} i^{m_i} m_i!$, where $m_i$ is the number of parts of $\lambda$ equal to $i$.
Define a bilinear form on $\Lambda$ by $\langle p_\lambda, p_\mu \rangle_\alpha = \delta_{\lambda\mu}\, z_\lambda\, \alpha^{\ell(\lambda)}$, and write $\mu < \lambda$ for the strict dominance order on partitions of the same number.
The *monic Jack functions* are the unique family $(P_\lambda^{(\alpha)})_\lambda$ in $\Lambda$ such that:

1. $P_\lambda^{(\alpha)} = m_\lambda + \sum_{\mu < \lambda} c_{\lambda\mu} m_\mu$ for some coefficients $c_{\lambda\mu}$;
2. $\langle P_\lambda^{(\alpha)}, P_\mu^{(\alpha)} \rangle_\alpha = 0$ for $\lambda \ne \mu$.

For a box $s$ of the Young diagram of $\lambda$, let $a(s)$ be the number of boxes to its right.
Let $l(s)$ be the number of boxes below $s$.
The *Jack function* is $J_\lambda^{(\alpha)} = c_\lambda(\alpha)\, P_\lambda^{(\alpha)}$ with $c_\lambda(\alpha) = \prod_{s \in \lambda} \big(\alpha\, a(s) + l(s) + 1\big)$.

## Remarks

Example: in degree $2$, $P_{(2)}^{(\alpha)} = m_{(2)} + \frac{2}{1+\alpha} m_{(1,1)}$ and $P_{(1,1)}^{(\alpha)} = m_{(1,1)}$.
Check: $m_{(2)} = p_2$ and $m_{(1,1)} = \frac12 (p_1^2 - p_2)$, so $P_{(2)}^{(\alpha)} = \frac{\alpha}{1+\alpha} p_2 + \frac{1}{1+\alpha} p_1^2$.
With $\langle p_2, p_2 \rangle_\alpha = 2\alpha$ and $\langle p_1^2, p_1^2 \rangle_\alpha = 2\alpha^2$, one gets $\langle P_{(2)}^{(\alpha)}, m_{(1,1)} \rangle_\alpha = \frac12 \left( -\frac{2\alpha^2}{1+\alpha} + \frac{2\alpha^2}{1+\alpha} \right) = 0$.
The normalization gives $J_{(2)}^{(\alpha)} = (1+\alpha) m_{(2)} + 2 m_{(1,1)}$ and $J_{(1,1)}^{(\alpha)} = 2 m_{(1,1)}$.

Non-example: the Schur function $s_{(2)} = m_{(2)} + m_{(1,1)}$ satisfies clause 1 but fails clause 2 for $\alpha \ne 1$, since $\langle s_{(2)}, m_{(1,1)} \rangle_\alpha = \frac{\alpha^2 - \alpha}{2}$.

At $\alpha = 1$ the form is the Hall inner product, $P_\lambda^{(1)} = s_\lambda$, and $J_\lambda^{(1)}$ is $s_\lambda$ times the product of the hook lengths of $\lambda$.
At $\alpha = 2$, $J_\lambda^{(2)}$ are the zonal polynomials.
Existence of the family is a theorem; it is not automatic, because dominance is only a partial order.
Restricting to $n$ variables gives the Jack polynomials $J_\lambda^{(\alpha)}(x_1, \dots, x_n)$, which vanish when $\ell(\lambda) > n$.
