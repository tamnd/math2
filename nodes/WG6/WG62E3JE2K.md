---
tag: WG62E3JE2K
kind: proof
name: Proof of Markov's inequality
msc: ["60E15"]
proves: 05PWWHYBX5
uses: [0DCT0QZVQ1, 0VSB0XF4G7, 0P7PTC8DDE]
sources:
  - url: https://en.wikipedia.org/wiki/Markov's_inequality
    locator: Proofs
---

## Proof

We compare $X$ with a multiple of an indicator function.

1. Let $X$ be a random variable with values in $[0, \infty)$ on a probability space $(\Omega, \mathcal{F}, P)$, and let $a > 0$.
2. By the definition of the [[expected value|0DCT0QZVQ1]], $E[X] \in [0, \infty]$. If $E[X] = \infty$, the right side is $\infty$ and the inequality holds. So assume $E[X] < \infty$.
3. Let $A = \set{X \ge a}$, an event, and let $\mathbf{1}_A$ be its [[indicator function|0VSB0XF4G7]].
4. We claim $a \mathbf{1}_A \le X$ pointwise. On $A$, the left side is $a$ and $X \ge a$. Off $A$, the left side is $0$ and $X \ge 0$.
5. The integral of an indicator is the probability of its set, so $E[a \mathbf{1}_A] = a P(A)$.
6. By step 4, $X - a \mathbf{1}_A \ge 0$. The integral of a nonnegative function is nonnegative, so $E[X - a \mathbf{1}_A] \ge 0$.
7. Both $X$ and $a \mathbf{1}_A$ are integrable. By [[linearity of expectation|0P7PTC8DDE]] and step 5, $E[X] - a P(A) \ge 0$.
8. Dividing by $a > 0$ gives $P(X \ge a) \le E[X]/a$.

## Idea

The variable $X$ is at least $a$ on the event $\set{X \ge a}$ and at least $0$ elsewhere. So $X$ dominates $a$ times the indicator of that event. Taking expectations turns this pointwise bound into the inequality.
