---
tag: GCV10B5HES
kind: statement
role: theorem
name: Slutsky's theorem
msc: ["60F05", "62E20"]
uses: [0SRYJGXKR4, 0QA1HBD9Z4, CFRN0G7GDB]
about: [0SRYJGXKR4]
sources:
  - url: https://en.wikipedia.org/wiki/Slutsky%27s_theorem
same_as:
  wikidata: Q643826
  wikipedia: Slutsky's theorem
---

## Statement

For each $n \ge 1$, let $X_n$ and $Y_n$ be real random variables on one probability space.
Let $X$ be a real random variable and $c \in \R$ a constant.
Assume that $X_n \to X$ [[in distribution|0SRYJGXKR4]] and $Y_n \to c$ [[in probability|0QA1HBD9Z4]].
Then, in distribution:

1. $X_n + Y_n \to X + c$;
2. $Y_n X_n \to c X$;
3. $X_n / Y_n \to X / c$, provided $c \ne 0$, where $X_n / Y_n$ is given any fixed value on the event $\set{Y_n = 0}$.

## Remarks

Proof idea: since the limit of $Y_n$ is a constant, the pair $(X_n, Y_n)$ converges in distribution to $(X, c)$.
Each of the three maps $(x, y) \mapsto x + y$, $xy$ and $x/y$ is continuous at the points $(x, c)$, so the [[continuous mapping theorem|CFRN0G7GDB]] applies.
Example: let $X_1, X_2, \dots$ be i.i.d. with mean $\mu$ and variance $\sigma^2 \in (0, \infty)$, with [[sample mean|03Y6AQ2S0J]] $\bar{X}_n$ and sample standard deviation $S_n$. The [[central limit theorem|0EPZC4Z1FC]] gives $\sqrt{n}(\bar{X}_n - \mu)/\sigma \to N(0, 1)$, and the law of large numbers gives $S_n \to \sigma$ in probability; so $\sqrt{n}(\bar{X}_n - \mu)/S_n \to N(0, 1)$ in distribution.
The limit $c$ must be a constant.
Let $Z$ be standard normal and $X_n = Z$; the variables $Z$ and $-Z$ have the same law.
With $Y_n = -Z$ one gets $X_n + Y_n = 0$, and with $Y_n = Z$ one gets $2Z$.
So convergence in law of both terms does not determine the law of the limit of the sum.
The theorem holds in the same way for random vectors, and for random matrices $Y_n$ that converge in probability to a constant matrix $C$.
For the quotient $Y_n^{-1} X_n$ one needs $C$ to be invertible.

## Explanations

### L1 human

Suppose one sequence settles into a random limit law and another settles down to a fixed number.
Then their sum, product and quotient behave as if the second sequence were already that number.
This is what allows statisticians to replace an unknown parameter by an estimate of it in an approximate normal law.

### L2 human

Slutsky's theorem is used constantly in asymptotic statistics, together with the [[central limit theorem|0EPZC4Z1FC]] and the delta method.
It justifies the use of estimated standard errors in confidence intervals and test statistics such as the Student $t$ statistic for large samples.
It follows from the [[continuous mapping theorem|CFRN0G7GDB]] applied to the pair $(X_n, Y_n)$.
Its key point is that joint convergence comes for free when one limit is constant.
