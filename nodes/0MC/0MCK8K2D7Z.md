---
tag: 0MCK8K2D7Z
kind: statement
role: proposition
name: Epsilon characterisation of Cauchy sequences
msc: ["54E35"]
uses: [063W5JMY85, 0692CGQF00]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_sequence
    locator: In a metric space
---

## Statement

Let $(X, d)$ be a [[metric space|063W5JMY85]] and let $(x_n)_{n \ge 1}$ be a sequence in $X$.
For each $N \ge 1$, let $T_N = \{x_n : n \ge N\}$.
Then the following two conditions are equivalent:

1. For each real $\varepsilon > 0$ there is an integer $N$ such that $d(x_m, x_n) < \varepsilon$ for all $m, n \ge N$.
2. The [[diameters|0692CGQF00]] $\operatorname{diam}(T_N)$ tend to $0$ as $N \to \infty$.

The sequence $(x_n)$ is a Cauchy sequence when it satisfies these conditions.

## Remarks

Condition 1 is the usual definition of a Cauchy sequence.
Each convergent sequence is a Cauchy sequence: if $x_n \to x$, then $d(x_m, x_n) \le d(x_m, x) + d(x, x_n)$.
In $\mathbb{Q}$ with the usual metric, the decimal approximations $1, 1.4, 1.41, 1.414, \ldots$ of $\sqrt{2}$ form a Cauchy sequence that does not converge in $\mathbb{Q}$.
Each Cauchy sequence is [[bounded|0P953MG05E]].

## Explanations

### L1 human

The terms of a Cauchy sequence get closer and closer to each other.
You can check this without knowing a limit, and this is the point. A Cauchy sequence looks as if it converges. But the space can have no point for it to converge to.
