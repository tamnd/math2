---
tag: 4PBC71YCTK
kind: definition
name: Sequential probability ratio test
msc: [62L10, 62F03]
defines: SXR93CAP1R
uses: [9CWYNB9003, 087P03NEND, 00MRN0FARV, 0VW9E4QXR6, WND87FBAKC, 03N8C8ZR4B, 04VZE3FZXF]
sources:
  - url: https://en.wikipedia.org/wiki/Sequential_probability_ratio_test
---

## Definition

Let $X_1, X_2, \dots$ be [[independent and identically distributed|00MRN0FARV]] random variables with a density $f$ with respect to a $\sigma$-finite measure.
Let $f_0 \ne f_1$ be two densities, and consider the [[hypotheses|087P03NEND]] $H_0 \colon f = f_0$ and $H_1 \colon f = f_1$.
The ratio of the [[likelihoods|0VW9E4QXR6]] after $n$ observations is
$$\Lambda_n = \prod_{i=1}^{n} \frac{f_1(X_i)}{f_0(X_i)}, \qquad \Lambda_0 = 1.$$
Let $0 < A < 1 < B$ be constants.
The *sequential probability ratio test* with boundaries $A$ and $B$ is the [[sequential procedure|9CWYNB9003]] such that:

1. It stops at the [[stopping time|WND87FBAKC]] $N = \min \set{n \ge 1 : \Lambda_n \le A \text{ or } \Lambda_n \ge B}$.
2. It rejects $H_0$ if $\Lambda_N \ge B$ and accepts $H_0$ if $\Lambda_N \le A$.

## Remarks

Example: for coin tosses $X_i \in \set{0, 1}$, let $f_0$ be the Bernoulli law with parameter $1/2$ and $f_1$ the one with parameter $2/3$.
Then each head multiplies $\Lambda_n$ by $4/3$ and each tail by $2/3$.
With $A = 1/4$ and $B = 4$, the test stops the first time the running product leaves the interval $(1/4, 4)$.

Non-example: comparing $\Lambda_{100}$ with a single threshold after exactly $100$ tosses is a fixed-sample likelihood ratio test, not an SPRT, because the stopping rule of clause 1 is not used.

Since $f_0 \ne f_1$, the time $N$ is finite with probability one under both hypotheses and has finite expectation.
In logarithms, $\log \Lambda_n$ is a [[random walk|04VZE3FZXF]] with the two absorbing barriers $\log A < 0 < \log B$.
Let $\alpha$ and $\beta$ be the error probabilities of [[type I and type II|03N8C8ZR4B]].
Wald's inequalities are $B \le (1 - \beta)/\alpha$ and $A \ge \beta/(1 - \alpha)$, and in practice the boundaries $B = (1 - \beta)/\alpha$ and $A = \beta/(1 - \alpha)$ are used as approximations.
