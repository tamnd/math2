---
tag: N05N7W1BAB
kind: definition
name: Jackson integral
msc: [05A30, 33D60]
defines: 7EMPA6M8S7
uses: [GFSDMJHHVA, PMJT3FZE0Y]
sources:
  - url: https://en.wikipedia.org/wiki/Jackson_integral
---

## Definition

Let $0 < q < 1$, let $a, b \in \R$, and let $f$ be a real or complex function defined at the points $a q^k$ and $b q^k$ for all integers $k \ge 0$.
The *Jackson integral* of $f$ from $0$ to $a$ is
$$\int_0^a f(x) \, d_q x = (1 - q)\, a \sum_{k=0}^{\infty} q^k f(a q^k),$$
when the series converges.
The Jackson integral from $a$ to $b$ is
$$\int_a^b f(x) \, d_q x = \int_0^b f(x) \, d_q x - \int_0^a f(x) \, d_q x.$$

## Remarks

Example: for an integer $n \ge 0$,
$$\int_0^1 x^n \, d_q x = (1 - q) \sum_{k=0}^{\infty} q^{k(n+1)} = \frac{1 - q}{1 - q^{n+1}} = \frac{1}{[n+1]_q},$$
the [[q-analog|GFSDMJHHVA]] of $\int_0^1 x^n \, dx = \frac{1}{n+1}$.

Non-example: $f(x) = 1/x$ on $(0, 1]$ has no Jackson integral from $0$ to $1$, since the terms $q^k f(q^k) = 1$ do not tend to $0$.

If $f$ is continuous on $[0, a]$, the sum is a Riemann sum for the partition by the points $a q^k$, and it tends to $\int_0^a f(x)\, dx$ as $q \to 1^-$.
If $f$ is bounded near $0$, then $F(x) = \int_0^x f(t) \, d_q t$ satisfies $D_q F = f$ for the [[q-derivative|PMJT3FZE0Y]] $D_q F(x) = \frac{F(qx) - F(x)}{(q - 1) x}$, $x \ne 0$.
