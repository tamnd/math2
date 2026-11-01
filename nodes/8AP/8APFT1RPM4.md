---
tag: 8APFT1RPM4
kind: statement
role: theorem
name: McDiarmid's inequality
msc: ["60E15", 60G42]
uses: [0GQ938GDE0, 0WQNRCNY3M, Z57CG6W9S6, BDA5TTB1F0]
about: [0GQ938GDE0]
sources:
  - url: https://en.wikipedia.org/wiki/McDiarmid%27s_inequality
same_as:
  wikidata: Q113127691
  wikipedia: McDiarmid's inequality
---

## Statement

Let $X_1, \dots, X_n$ be [[independent|0GQ938GDE0]] random variables, with $X_i$ taking values in a measurable space $\mathcal{X}_i$.
Let $f \colon \mathcal{X}_1 \times \dots \times \mathcal{X}_n \to \R$ be measurable, and let $c_1, \dots, c_n \ge 0$ be constants with the bounded differences property: $\abs{f(x) - f(x')} \le c_i$ whenever $x$ and $x'$ differ only in the $i$-th coordinate.
Assume $c_1^2 + \dots + c_n^2 > 0$, and let $Y = f(X_1, \dots, X_n)$.
Then for every $t > 0$,
$$P(Y - E[Y] \ge t) \le \exp\left(-\frac{2 t^2}{\sum_{i=1}^n c_i^2}\right),$$
and the same bound holds for $P(Y - E[Y] \le -t)$.

## Remarks

Proof idea: let $Z_k = E[Y \mid X_1, \dots, X_k]$, the [[Doob martingale|Z57CG6W9S6]] of $Y$.
By independence and the bounded differences property, given $X_1, \dots, X_{k-1}$ the increment $Z_k - Z_{k-1}$ lies in an interval of length $c_k$.
Hoeffding's lemma then bounds its conditional moment-generating function by $e^{\lambda^2 c_k^2 / 8}$, and the argument of [[Azuma's inequality|BDA5TTB1F0]] finishes the proof.
Example: throw $m$ balls independently into $N$ bins and let $Y$ be the number of empty bins. Moving one ball changes $Y$ by at most $1$, so $P(\abs{Y - E[Y]} \ge t) \le 2 e^{-2t^2 / m}$.
With $f(x) = x_1 + \dots + x_n$ and $X_i \in [a_i, b_i]$, one gets [[Hoeffding's inequality|0WPDNXGSSN]].
Independence is needed: if $X_1 = \dots = X_n$ is a fair $0/1$ coin and $f$ is the sum, then $c_i = 1$ but $Y \in \set{0, n}$, so $P(Y - E[Y] \ge n/2) = \frac{1}{2}$, far above $e^{-n/2}$.

## Explanations

### L1 human

If a quantity depends on many independent random inputs, and no single input can change it much, then the quantity is almost constant.
McDiarmid's inequality makes this precise: the chance of a deviation $t$ decays like $e^{-2t^2 / \sum_i c_i^2}$.

### L2 human

This is the method of bounded differences.
It is often the quickest way to prove concentration in random graphs, randomized algorithms and learning theory, for instance for generalization bounds through Rademacher complexity.
It only gives concentration around the mean; estimating the mean itself needs other arguments.
Sharper results for convex Lipschitz functions follow from [[Talagrand's concentration inequality|GGEAGW4RRV]].
