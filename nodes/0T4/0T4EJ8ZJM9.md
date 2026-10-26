---
tag: 0T4EJ8ZJM9
kind: counterexample
name: Dirichlet function
msc: [26A15]
uses: [0EEE2CZB2A, 0MVDQEAB60]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_function
    locator: Topological properties
same_as:
  wikidata: Q948386
  wikipedia: Dirichlet function
---

## Counterexample

Let $f \colon \mathbb{R} \to \mathbb{R}$ be given by $f(x) = 1$ for rational $x$ and $f(x) = 0$ for irrational $x$.
Then $f$ is not [[continuous at|0EEE2CZB2A]] any point.
Indeed, each real $a$ is the limit of a sequence of rationals and of a sequence of irrationals. Their images tend to $1$ and to $0$, so one of them does not tend to $f(a)$.

## Remarks

The function $f$ is the indicator function of $\mathbb{Q}$.
Every rational number is a period of $f$.
The function is [[not Riemann integrable|03Z4JC4YRJ]] on any interval with more than one point.

## Explanations

### L1 human

Rational and irrational numbers lie mixed together in every small interval.
So the function jumps between $0$ and $1$ near every point, and it has no limit anywhere.
