---
tag: 03Z4JC4YRJ
kind: counterexample
name: The Dirichlet function is not Riemann integrable
msc: [26A42]
uses: [0T4EJ8ZJM9, 09FQT057T7, 021XJAQVDC]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_function
    locator: Integration properties
---

## Counterexample

Let $f \colon [0, 1] \to \mathbb{R}$ be the [[Dirichlet function|0T4EJ8ZJM9]]: $f(x) = 1$ for rational $x$ and $f(x) = 0$ for irrational $x$.
Each subinterval of positive length contains both rational and irrational numbers. So for each partition $P$, $U(f, P) = 1$ and $L(f, P) = 0$.
The upper [[Darboux integral|09FQT057T7]] is $1$ and the lower one is $0$. So $f$ is [[not Riemann integrable|021XJAQVDC]].

## Remarks

The function is bounded, so the failure is not caused by unboundedness.
The function is Lebesgue integrable, with Lebesgue integral $0$, since $\mathbb{Q}$ has measure zero.
It is the pointwise limit of Riemann integrable functions. So pointwise limits do not keep Riemann integrability.

## Explanations

### L1 human

Every Riemann sum of this function is $1$ or $0$ or in between, depending only on the choice of tags.
So the sums cannot settle down to one number.
