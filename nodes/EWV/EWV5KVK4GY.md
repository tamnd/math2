---
tag: EWV5KVK4GY
kind: definition
name: Macdonald polynomial
msc: ["05E05", 33D52]
defines: VYP9PB000X
uses: [PAJEHWXW6M, 0ZNXZB4HNB, 0JV30XN73Z]
sources:
  - url: https://en.wikipedia.org/wiki/Macdonald_polynomials
---

## Definition

Let $\Lambda$ be the ring of [[symmetric functions|PAJEHWXW6M]] in variables $x = (x_1, x_2, \dots)$ with coefficients in the field $\Q(q, t)$.
For a [[partition|0JV30XN73Z]] $\lambda$, let $m_\lambda$ be the monomial symmetric function and let $p_\lambda = p_{\lambda_1} p_{\lambda_2} \cdots$ be the product of [[power sums|0ZNXZB4HNB]].
Let $z_\lambda = \prod_{i \ge 1} i^{m_i} m_i!$, where $m_i$ is the number of parts of $\lambda$ equal to $i$.
Define a bilinear form on $\Lambda$ by
$$\ip{p_\lambda}{p_\mu}_{q,t} = \delta_{\lambda\mu} \, z_\lambda \prod_{i} \frac{1 - q^{\lambda_i}}{1 - t^{\lambda_i}}.$$
For partitions $\lambda, \mu$ of the same number, write $\mu \le \lambda$ (dominance order) if $\mu_1 + \dots + \mu_k \le \lambda_1 + \dots + \lambda_k$ for all $k$.
The *Macdonald polynomials* are the unique family $(P_\lambda(x; q, t))_\lambda$ in $\Lambda$ such that:

1. $P_\lambda = m_\lambda + \sum_{\mu < \lambda} c_{\lambda\mu} m_\mu$ for some $c_{\lambda\mu} \in \Q(q, t)$.
2. $\ip{P_\lambda}{P_\mu}_{q,t} = 0$ for $\lambda \ne \mu$.

## Remarks

The existence and uniqueness of this family is a theorem of Macdonald; it is not automatic, because dominance is only a partial order.

Example: for $\lambda = (2)$, $P_{(2)} = m_{(2)} + \frac{(1+q)(1-t)}{1-qt} m_{(1,1)}$.
Check: $m_{(2)} = p_2$ and $m_{(1,1)} = \tfrac12 (p_1^2 - p_2)$, and $z_{(2)} = z_{(1,1)} = 2$.
Then $\ip{p_2}{m_{(1,1)}}_{q,t} = -\frac{1-q^2}{1-t^2}$ and $\ip{m_{(1,1)}}{m_{(1,1)}}_{q,t} = \frac{(1-q)(1-qt)}{(1-t)(1-t^2)}$, so $\ip{P_{(2)}}{P_{(1,1)}}_{q,t} = 0$ with $P_{(1,1)} = m_{(1,1)}$.

Non-example: the Schur function $s_{(2)} = m_{(2)} + m_{(1,1)}$ satisfies clause 1 but not clause 2 when $q \ne t$.
Indeed $\ip{s_{(2)}}{m_{(1,1)}}_{q,t} = \frac{(1-q)(t-q)}{(1-t)(1-t^2)} \ne 0$.

At $q = t$ the form is the Hall inner product and $P_\lambda = s_\lambda$.
At $q = 0$, $P_\lambda$ is the Hall–Littlewood polynomial $P_\lambda(x; t)$.
