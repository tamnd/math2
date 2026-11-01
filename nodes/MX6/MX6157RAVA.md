---
tag: MX6157RAVA
kind: statement
role: theorem
name: Bernstein inequalities
msc: ["60E15", "60F10"]
uses: [0GQ938GDE0, 0WQNRCNY3M, 0477R9PYAE, 014PEBGDYF]
about: [0GQ938GDE0]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein_inequalities_(probability_theory)
same_as:
  wikidata: Q826791
  wikipedia: Bernstein inequalities (probability theory)
---

## Statement

Let $X_1, \dots, X_n$ be [[independent|0GQ938GDE0]] real random variables with $E[X_i] = 0$ for each $i$.
Assume that there is a constant $M > 0$ with $\abs{X_i} \le M$ almost surely for each $i$.
Let $\sigma^2 = \sum_{i=1}^n E[X_i^2]$.
Then for every $t \ge 0$,
$$P\left(\sum_{i=1}^n X_i \ge t\right) \le \exp\left(-\frac{t^2 / 2}{\sigma^2 + M t / 3}\right).$$

## Remarks

Proof idea: for $\lambda > 0$, the bound $\abs{X_i} \le M$ gives $E[e^{\lambda X_i}] \le \exp\left(E[X_i^2] \, \frac{e^{\lambda M} - 1 - \lambda M}{M^2}\right)$.
The [[Chernoff bound|014PEBGDYF]] with the best $\lambda$ then gives Bennett's inequality, and an elementary estimate of the resulting function gives the bound above.
Applying the bound to $-X_i$ gives the same bound for the lower tail, so $P(\abs{\sum_i X_i} \ge t)$ is at most twice the right-hand side.
For small $t$, the exponent is about $-t^2 / (2 \sigma^2)$, as for a normal variable with the true variance $\sigma^2$.
For large $t$, it is about $-3t / (2M)$, an exponential tail.
Example: take $n$ independent centred variables with $\abs{X_i} \le 1$ and $E[X_i^2] = p$ small.
[[Hoeffding's inequality|0WPDNXGSSN]] gives the exponent $-t^2 / (2n)$.
Bernstein gives about $-t^2 / (2np)$ when $t$ is much smaller than $np$, which is much better.
The name covers a family of related bounds; other versions replace the bound $\abs{X_i} \le M$ by moment conditions $E[\abs{X_i}^k] \le \frac{k!}{2} E[X_i^2] M^{k-2}$ for all $k \ge 2$.

## Explanations

### L1 human

A sum of many small independent random pieces is rarely far from its mean.
Bernstein's inequality says how rare, and it uses the actual variance of the pieces, not only their range.
When the pieces have small variance, it gives much stronger bounds than inequalities that see only the range.

### L2 human

Bernstein's inequality sits between [[Hoeffding's inequality|0WPDNXGSSN]], which uses only bounds on the range, and the [[central limit theorem|0EPZC4Z1FC]], which describes the normal approximation but gives no bound for finite $n$.
Its tail is Gaussian for moderate deviations and exponential for large ones, which matches the behaviour of sub-exponential variables.
It is a standard tool in statistics, randomized algorithms and the theory of empirical processes.
