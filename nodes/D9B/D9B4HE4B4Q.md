---
tag: D9B4HE4B4Q
kind: statement
role: theorem
name: Kolmogorov's inequality
msc: ["60E15", 60F15]
uses: [0GQ938GDE0, 0WQNRCNY3M, 0477R9PYAE, 0PNRKMRC55]
about: [0477R9PYAE]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov%27s_inequality
same_as:
  wikidata: Q1747439
  wikipedia: Kolmogorov's inequality
---

## Statement

Let $X_1, \dots, X_n$ be [[independent|0GQ938GDE0]] real [[random variables|0PNRKMRC55]] with $E[X_k] = 0$ and $E[X_k^2] < \infty$ for each $k$.
Let $S_k = X_1 + \cdots + X_k$ for $1 \le k \le n$.
Then for every $\lambda > 0$,
$$P\left(\max_{1 \le k \le n} \abs{S_k} \ge \lambda\right) \le \frac{\operatorname{Var}(S_n)}{\lambda^2} = \frac{1}{\lambda^2} \sum_{k=1}^{n} E[X_k^2].$$

## Remarks

Let $\tau$ be the first $k$ with $\abs{S_k} \ge \lambda$.
The event $\set{\tau = k}$ depends only on $X_1, \dots, X_k$.
By independence the cross term $E[S_k (S_n - S_k) \mathbf{1}_{\tau = k}]$ vanishes, so $E[S_n^2 \mathbf{1}_{\tau = k}] \ge E[S_k^2 \mathbf{1}_{\tau = k}] \ge \lambda^2 P(\tau = k)$.
Summing over $k$ gives $\lambda^2 P(\tau \le n) \le E[S_n^2]$.

The bound has the same right side as [[Chebyshev's inequality|02HZ1BK3MW]] for the single variable $S_n$, but it controls the whole path $S_1, \dots, S_n$.
It is a special case of [[Doob's martingale inequality|4G53E7BRXF]], since $(S_k)$ is a [[martingale|0D0GBNDKDH]].

Example: let the $X_k$ be independent signs, equal to $1$ or $-1$ with probability $1/2$ each.
Then the probability that $\abs{S_k} \ge \lambda$ for some $k \le n$ is at most $n / \lambda^2$.
With $\lambda = 10 \sqrt{n}$ this is at most $1/100$.

## Explanations

### L1 human

A sum of independent centred random steps rarely wanders far from zero.
Chebyshev's inequality says this for the final position.
Kolmogorov's inequality says that the same bound holds for the farthest point reached along the way.

### L2 human

The inequality is the key step in the proof that a series $\sum X_k$ of independent centred variables with $\sum \operatorname{Var}(X_k) < \infty$ converges almost surely.
That result leads to [[Kolmogorov's three-series theorem|TTTFQ693RJ]] and to the [[strong law of large numbers|0DFWHQ839T]] for independent variables with suitable finite variances.
