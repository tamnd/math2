---
tag: FFJMRQNF96
kind: definition
name: Lindeberg's condition
msc: [60F05]
defines: VJ3BVREDWN
uses: [0GQ938GDE0, 0PNRKMRC55, 0WQNRCNY3M, 0477R9PYAE, 0RCQZ36MME]
sources:
  - url: https://en.wikipedia.org/wiki/Lindeberg%27s_condition
---

## Definition

Let $X_1, X_2, \dots$ be [[independent|0GQ938GDE0]] real [[random variables|0PNRKMRC55]] with finite [[variances|0477R9PYAE]].
Let $\mu_k = E[X_k]$, let $\sigma_k^2 = \operatorname{Var}(X_k)$, and let $s_n^2 = \sigma_1^2 + \cdots + \sigma_n^2$, with $s_n > 0$ for all $n$.
The sequence satisfies *Lindeberg's condition* if, for every $\varepsilon > 0$,
$$\lim_{n \to \infty} \frac{1}{s_n^2} \sum_{k=1}^{n} E\left[(X_k - \mu_k)^2 \, \mathbf{1}_{\set{\abs{X_k - \mu_k} > \varepsilon s_n}}\right] = 0.$$

## Remarks

The Lindeberg central limit theorem states that under this condition $(S_n - \sum_{k \le n} \mu_k) / s_n$ converges in distribution to a standard normal variable, where $S_n = X_1 + \cdots + X_n$.

Example: an i.i.d. sequence with variance $\sigma^2 \in (0, \infty)$ satisfies the condition.
Here $s_n^2 = n \sigma^2$, and the sum equals $\sigma^{-2} E[(X_1 - \mu_1)^2 \mathbf{1}_{\set{\abs{X_1 - \mu_1} > \varepsilon \sigma \sqrt{n}}}]$.
It tends to $0$ by dominated convergence, since $E[(X_1 - \mu_1)^2] < \infty$.

Non-example: let $X_1$ be standard normal and $X_k = 0$ for $k \ge 2$.
Then $s_n = 1$ for all $n$, and the sum equals $E[X_1^2 \mathbf{1}_{\set{\abs{X_1} > \varepsilon}}] > 0$, which does not tend to $0$.
In this case one variable carries all the variance.

The condition implies Feller's condition $\max_{k \le n} \sigma_k^2 / s_n^2 \to 0$.
The Lyapunov condition, $s_n^{-2-\delta} \sum_{k \le n} E[\abs{X_k - \mu_k}^{2+\delta}] \to 0$ for some $\delta > 0$, implies Lindeberg's condition and is often easier to check.
