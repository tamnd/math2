---
tag: 04JAY9DGB7
kind: statement
role: theorem
name: Dirichlet's approximation theorem
msc: [11J04]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet%27s_approximation_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Dirichlet%27s_approximation_theorem
    locator: Proof by the pigeonhole principle
same_as:
  wikidata: Q1227703
  wikipedia: Dirichlet's approximation theorem
---

## Statement

Let $\alpha$ be a real number and let $N$ be a positive integer.
Then there are integers $p$ and $q$ with $1 \le q \le N$ and
$$|q \alpha - p| \le \frac{1}{N + 1}.$$

## Remarks

A corollary: if $\alpha$ is irrational, then $\left| \alpha - \frac{p}{q} \right| < \frac{1}{q^2}$ for infinitely many fractions $p / q$.
The proof uses the pigeonhole principle. Among the $N + 1$ fractional parts of $0, \alpha, 2\alpha, \dots, N\alpha$, two lie in one of $N + 1$ intervals of length $\frac{1}{N + 1}$.
The [[convergents|0E70M92FE3]] of the continued fraction of $\alpha$ give such fractions explicitly.

## Explanations

### L1 human

Each real number has fractions $p/q$ very close to it, with an error much smaller than $1/q$.
The theorem gives the bound $1/q^2$ for infinitely many denominators when $\alpha$ is irrational.
