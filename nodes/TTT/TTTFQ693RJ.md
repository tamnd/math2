---
tag: TTTFQ693RJ
kind: statement
role: theorem
name: Kolmogorov's three-series theorem
msc: [60F15, 60G50]
uses: [0GQ938GDE0, 0PNRKMRC55, 0NM626FH6Q, 0ST21PGDAP, 0WQNRCNY3M, 0477R9PYAE, 0RCQZ36MME]
about: [0NM626FH6Q, 0GQ938GDE0]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov%27s_three-series_theorem
same_as:
  wikidata: Q3527233
  wikipedia: Kolmogorov's three-series theorem
---

## Statement

Let $X_1, X_2, \dots$ be [[independent|0GQ938GDE0]] real [[random variables|0PNRKMRC55]].
For $A > 0$, let $Y_n = X_n \mathbf{1}_{\set{\abs{X_n} \le A}}$, the variable $X_n$ truncated at level $A$.
Then the [[series|0NM626FH6Q]] $\sum_{n} X_n$ converges [[almost surely|0ST21PGDAP]] if and only if, for some $A > 0$, the following three series converge:

1. $\sum_{n} P(\abs{X_n} > A)$,
2. $\sum_{n} E[Y_n]$,
3. $\sum_{n} \operatorname{Var}(Y_n)$.

## Remarks

If the three series converge for some $A > 0$, then they converge for every $A > 0$.
By [[Kolmogorov's zero–one law|073Q8Z94KG]], the event that $\sum_n X_n$ converges has probability $0$ or $1$, so when the series do not all converge, $\sum_n X_n$ diverges almost surely.

Idea of the proof of sufficiency.
Series 3 and [[Kolmogorov's inequality|D9B4HE4B4Q]] show that $\sum_n (Y_n - E[Y_n])$ converges almost surely.
Series 2 then gives the convergence of $\sum_n Y_n$.
Series 1 and the [[first Borel–Cantelli lemma|0T6WS7TT77]] show that $X_n = Y_n$ for all but finitely many $n$, almost surely.
The proof of necessity uses a symmetrisation argument and a lower bound for the probability that a sum of bounded centred variables stays small.

Example: let $\varepsilon_n$ be independent signs, equal to $1$ or $-1$ with probability $1/2$ each, and let $X_n = \varepsilon_n / n^{p}$ with $p > 0$.
With $A = 1$, series 1 and 2 are $0$, and series 3 is $\sum_n n^{-2p}$.
So the random series $\sum_n \varepsilon_n / n^p$ converges almost surely if $p > 1/2$ and diverges almost surely if $p \le 1/2$.

## Explanations

### L1 human

When you add up infinitely many independent random numbers, the sum may or may not settle down.
The theorem gives an exact test with three ordinary series.
The large values must be rare, the average sizes of the small values must add up, and their fluctuations must add up.

### L2 human

The theorem completely describes the almost sure convergence of series of independent variables.
It combines [[Kolmogorov's inequality|D9B4HE4B4Q]], the [[Borel–Cantelli lemma|0T6WS7TT77]] and the zero–one law.
For independent variables, almost sure convergence, convergence in probability and convergence in distribution of $\sum_n X_n$ are equivalent, a result of Lévy.
A common use is to show that random series such as $\sum_n \varepsilon_n a_n$ converge almost surely exactly when $\sum_n a_n^2 < \infty$.
