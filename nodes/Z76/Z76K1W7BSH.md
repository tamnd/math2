---
tag: Z76K1W7BSH
kind: definition
name: Zolotarev polynomials
msc: [41A50, 41A10, 33C45]
defines: R8SNG5TBKJ
uses: [7N4988HN3P, 0DPF6WRZW6, M6EAR1JHPP]
sources:
  - url: https://en.wikipedia.org/wiki/Zolotarev_polynomials
---

## Definition

Let $n \ge 2$ be an integer and let $\sigma$ be a real number.
Let $\mathcal{Z}_{n,\sigma}$ be the set of real polynomials of the form
$$p(x) = x^n + \sigma x^{n-1} + q(x),$$
where $q$ is any real polynomial of [[degree|0DPF6WRZW6]] at most $n - 2$.
The *Zolotarev polynomial* $Z_{n,\sigma}$ is the element of $\mathcal{Z}_{n,\sigma}$ with the least value of $\max_{-1 \le x \le 1} \abs{p(x)}$.

## Remarks

The minimiser exists and is unique.
Indeed $Z_{n,\sigma} = g - q^*$, where $g(x) = x^n + \sigma x^{n-1}$ and $q^*$ is the [[best approximation|7N4988HN3P]] of $g$ in the uniform norm on $[-1, 1]$ by polynomials of degree at most $n - 2$.

Example: for $\sigma = 0$ the Zolotarev polynomial is $2^{1-n} T_n$, where $T_n$ is the [[Chebyshev polynomial|M6EAR1JHPP]].
Check: $2^{1-n} T_n$ is monic, its coefficient of $x^{n-1}$ is $0$ because $T_n$ is even or odd, and no monic polynomial of degree $n$ has a smaller maximum on $[-1, 1]$.

Non-example: for $n = 2$ and $\sigma = 0$, the polynomial $x^2$ lies in $\mathcal{Z}_{2,0}$ but is not $Z_{2,0}$.
Its maximum on $[-1, 1]$ is $1$, while $x^2 - 1/2$ has maximum $1/2$.

Some authors normalise the second coefficient as $-n\sigma$ instead of $\sigma$; the family of polynomials is the same.
