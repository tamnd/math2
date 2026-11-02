---
tag: 21FMF8VKXY
kind: definition
name: Period-doubling cascade
msc: ["37E05", 39A28, 39A33]
defines: 6J921PEDN2
uses: [EE9X3NZW81, NQDTTZ59X8, 3W358BSRN2]
sources:
  - url: https://en.wikipedia.org/wiki/Period-doubling_bifurcation
---

## Definition

Let $I \subseteq \R$ be an open interval and let $f_\mu \colon X \to X$, $\mu \in I$, be a family of maps of a set $X \subseteq \R$ with $(\mu, x) \mapsto f_\mu(x)$ smooth.
A *period-doubling cascade* of the family is a strictly increasing sequence of parameters $\mu_1 < \mu_2 < \mu_3 < \cdots$ in $I$ with a limit $\mu_\infty \in I$, such that for each $k \ge 1$:

1. for $\mu$ slightly less than $\mu_k$, the family has an attracting [[periodic solution|3W358BSRN2]] of prime period $2^{k-1}$;
2. at $\mu = \mu_k$ this cycle undergoes a [[period-doubling bifurcation|NQDTTZ59X8]]: it loses stability, and an attracting cycle of prime period $2^k$ is born from it.

## Remarks

Example: the logistic family $f_r(x) = r x (1 - x)$ on $[0, 1]$ has such a cascade with $r_1 = 3$ and $r_2 = 1 + \sqrt{6} \approx 3.449$.
At $r_1 = 3$ the fixed point $1 - 1/r$ has multiplier $f_r'(1 - 1/r) = 2 - r = -1$, and a $2$-cycle appears.
The limit is $r_\infty \approx 3.5699$.

Non-example: the family $f_\mu(x) = \mu x$ on $\R$ has no period-doubling cascade.
Its only possible attracting cycle is the fixed point $0$ for $\abs{\mu} < 1$, and it never has an attracting cycle of period $2$, so clause 2 fails already for $k = 1$.

For typical smooth unimodal families with a quadratic maximum, such as the logistic family, the ratios $(\mu_k - \mu_{k-1})/(\mu_{k+1} - \mu_k)$ tend to the Feigenbaum constant $\delta \approx 4.6692$.
