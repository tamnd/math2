---
tag: 0EFDDXTVD6
kind: definition
name: Convergence in probability
msc: [60F05]
defines: 0QA1HBD9Z4
uses: [0DKRR22AEQ]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_of_random_variables
    locator: Convergence in probability
---

## Definition

Let $X, X_1, X_2, \dots$ be real random variables on one probability space $(\Omega, \mathcal{F}, P)$.
The sequence $(X_n)$ converges in probability to $X$ if for each $\varepsilon > 0$,
$$\lim_{n \to \infty} P\left(|X_n - X| > \varepsilon\right) = 0.$$
One writes $X_n \xrightarrow{P} X$.

## Remarks

The limit is unique up to equality almost surely.
If $X_n \to X$ in probability, then a subsequence of $(X_n)$ converges to $X$ almost surely.
The weak law of large numbers is a result about convergence in probability.
Example: let $X_n$ be $1$ with probability $1/n$ and $0$ otherwise. Then $X_n \to 0$ in probability.

## Explanations

### L1 human

Convergence in probability means that, for large $n$, $X_n$ is very likely to be close to $X$.
It does not say that one fixed run of the experiment gives a convergent sequence.
