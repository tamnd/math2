---
tag: BDA5TTB1F0
kind: statement
role: theorem
name: Azuma's inequality
msc: ["60E15", 60G42]
uses: [0D0GBNDKDH, 0TTDGTEFMN, 0WPDNXGSSN]
about: [0D0GBNDKDH]
sources:
  - url: https://en.wikipedia.org/wiki/Azuma%27s_inequality
same_as:
  wikidata: Q2410467
  wikipedia: Azuma's inequality
---

## Statement

Let $(X_k)_{k = 0}^n$ be a [[martingale|0D0GBNDKDH]] with respect to a filtration $(\mathcal{F}_k)_{k = 0}^n$.
Assume that there are constants $c_1, \dots, c_n > 0$ with $\abs{X_k - X_{k-1}} \le c_k$ almost surely for $k = 1, \dots, n$.
Then for every $t > 0$,
$$P(X_n - X_0 \ge t) \le \exp\left(-\frac{t^2}{2 \sum_{k=1}^n c_k^2}\right),$$
and hence $P(\abs{X_n - X_0} \ge t) \le 2 \exp\left(-\frac{t^2}{2 \sum_{k=1}^n c_k^2}\right)$.

## Remarks

Proof idea: let $D_k = X_k - X_{k-1}$. Since $E[D_k \mid \mathcal{F}_{k-1}] = 0$ and $D_k \in [-c_k, c_k]$, Hoeffding's lemma applied to the [[conditional expectation|0TTDGTEFMN]] gives $E[e^{\lambda D_k} \mid \mathcal{F}_{k-1}] \le e^{\lambda^2 c_k^2 / 2}$.
By induction $E[e^{\lambda (X_n - X_0)}] \le e^{\lambda^2 \sum_k c_k^2 / 2}$, and Markov's inequality with $\lambda = t / \sum_k c_k^2$ gives the bound.
For independent centred $D_k$ the result is a form of [[Hoeffding's inequality|0WPDNXGSSN]], and it is also called the Azuma–Hoeffding inequality.
Example: for a simple random walk $X_n = D_1 + \dots + D_n$ with independent fair $\pm 1$ steps, $P(X_n \ge t) \le e^{-t^2 / (2n)}$.

## Explanations

### L1 human

A martingale is a fair game: on average each step adds nothing.
Suppose each step can change the fortune by at most a fixed amount.
Then the total after $n$ steps is very unlikely to be far from the start.
When each step is at most $1$, the chance of being more than $t$ away drops like $e^{-t^2 / (2n)}$.

### L2 human

Azuma's inequality is applied to [[Doob martingales|Z57CG6W9S6]] $X_k = E[f \mid \mathcal{F}_k]$ of a function $f$ of independent variables, revealed one at a time.
This gives concentration of quantities such as the chromatic number of a random graph, and it leads to [[McDiarmid's inequality|8APFT1RPM4]].
