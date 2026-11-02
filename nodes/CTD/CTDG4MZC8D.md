---
tag: CTDG4MZC8D
kind: statement
role: theorem
name: Wald's equation
msc: [60G50, 62L10, 60G40]
uses: [00MRN0FARV, WND87FBAKC, 0WQNRCNY3M, 04VZE3FZXF, 9CWYNB9003, DC9HZT2HVJ]
about: [WND87FBAKC]
sources:
  - url: https://en.wikipedia.org/wiki/Wald%27s_equation
same_as:
  wikidata: Q937458
  wikipedia: Wald's equation
---

## Statement

Let $X_1, X_2, \dots$ be [[independent and identically distributed|00MRN0FARV]] real random variables with $E\abs{X_1} < \infty$.
Let $S_n = X_1 + \cdots + X_n$.
Let $N$ be a [[stopping time|WND87FBAKC]] with values in $\set{1, 2, \dots}$ with respect to the filtration $\mathcal{F}_n = \sigma(X_1, \dots, X_n)$, and assume $E[N] < \infty$.
Then
$$E[S_N] = E[N] \, E[X_1],$$
where $E$ is the [[expectation|0WQNRCNY3M]].

## Remarks

Write $S_N = \sum_{i \ge 1} X_i \mathbf{1}_{\set{N \ge i}}$.
The event $\set{N \ge i}$ is the complement of $\set{N \le i - 1}$, so it depends only on $X_1, \dots, X_{i-1}$ and is independent of $X_i$.
Hence $E[X_i \mathbf{1}_{\set{N \ge i}}] = E[X_1] \, P(N \ge i)$, and summing over $i$ gives $E[X_1] \sum_i P(N \ge i) = E[X_1] \, E[N]$.
The same computation with $\abs{X_i}$ shows that the series converges absolutely, which justifies exchanging sum and expectation.

The hypothesis $E[N] < \infty$ is necessary.
For the simple symmetric [[random walk|04VZE3FZXF]], with $P(X_i = 1) = P(X_i = -1) = 1/2$, let $N$ be the first $n$ with $S_n = 1$.
Then $N$ is finite with probability one and $S_N = 1$, so $E[S_N] = 1$, while $E[X_1] = 0$; here $E[N] = \infty$.

## Explanations

### L1 human

A gambler plays a game many times and decides when to stop using only what has happened so far.
Wald's equation says that the expected total winnings equal the expected number of games times the expected winnings per game.
So no stopping strategy turns a fair game into a profitable one, provided the expected number of games is finite.

### L2 human

Wald's equation is a key tool in [[sequential analysis|9CWYNB9003]], where it gives the expected sample size of the sequential probability ratio test from the drift of the log-likelihood ratio.
It is also used in renewal theory and queueing theory.
It can also be derived from the [[optional stopping theorem|DC9HZT2HVJ]] applied to the martingale $S_n - n E[X_1]$.
