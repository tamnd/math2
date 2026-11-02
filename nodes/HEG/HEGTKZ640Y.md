---
tag: HEGTKZ640Y
kind: definition
name: Hausdorff summation
msc: ["40G05", "40C05"]
defines: PK3RGWY032
uses: [M6311DWJ1E, 0QE8STGJH2, 092GEF38YD]
sources:
  - url: https://en.wikipedia.org/wiki/Divergent_series
---

## Definition

Let $(\mu_n)_{n \ge 0}$ be a sequence of real numbers.
Define its iterated differences by $\Delta^0 \mu_k = \mu_k$ and $\Delta^{j+1} \mu_k = \Delta^j \mu_k - \Delta^j \mu_{k+1}$, so that
$$\Delta^j \mu_k = \sum_{i=0}^{j} (-1)^i \binom{j}{i} \mu_{k+i}.$$
The *Hausdorff matrix* of $(\mu_n)$ is the lower triangular matrix $H_\mu = (h_{nk})$ with
$$h_{nk} = \binom{n}{k} \Delta^{n-k} \mu_k \quad (0 \le k \le n), \qquad h_{nk} = 0 \quad (k > n).$$
A [[sequence|0QE8STGJH2]] $(s_k)$ of complex numbers is *Hausdorff summable* by $H_\mu$ to $s$ if $t_n = \sum_{k=0}^{n} h_{nk} s_k \to s$ as $n \to \infty$.
A series is Hausdorff summable if the sequence of its partial sums is.

## Remarks

Example: for $\mu_n = \frac{1}{n+1} = \int_0^1 t^n \, dt$ one gets $\Delta^{n-k} \mu_k = \int_0^1 t^k (1 - t)^{n-k} \, dt = \frac{k! \, (n-k)!}{(n+1)!}$.
So $h_{nk} = \frac{1}{n+1}$, and $t_n = \frac{s_0 + \cdots + s_n}{n+1}$ is the Cesàro mean.
Similarly, $\mu_n = 2^{-n}$ gives $h_{nk} = \binom{n}{k} 2^{-n}$, the Euler $(E, 1)$ means.

Non-example of regularity: for $\mu_0 = 1$ and $\mu_n = 0$ for $n \ge 1$, one has $\Delta^{n-k} \mu_k = 0$ for $k \ge 1$ and $\Delta^n \mu_0 = 1$.
So $t_n = s_0$ for all $n$, and the method sends every sequence to its first term.

Hausdorff showed that $H_\mu$ is regular if and only if $\mu_n = \int_0^1 t^n \, d\chi(t)$ for a function $\chi$ of bounded variation on $[0, 1]$ with $\chi(0) = 0$, $\chi(1) = 1$ and $\chi$ continuous at $0$.
In the non-example, $\chi$ jumps from $0$ to $1$ at $0$, which violates the last condition.
