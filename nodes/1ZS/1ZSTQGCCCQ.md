---
tag: 1ZSTQGCCCQ
kind: definition
name: Sequential analysis
msc: [62L10]
defines: 9CWYNB9003
uses: [WND87FBAKC, 087P03NEND, 0DKRR22AEQ]
sources:
  - url: https://en.wikipedia.org/wiki/Sequential_analysis
---

## Definition

Let $X_1, X_2, \dots$ be [[random variables|0DKRR22AEQ]] observed one at a time, and let $\mathcal{F}_n = \sigma(X_1, \dots, X_n)$ be the information after $n$ observations, with $\mathcal{F}_0$ trivial.
Let $D$ be a set of possible decisions, such as "accept $H_0$" and "reject $H_0$".
A *sequential procedure* is a pair $(N, \delta)$ such that:

1. $N$ is a [[stopping time|WND87FBAKC]] with respect to $(\mathcal{F}_n)_{n \ge 0}$, called the stopping rule.
2. $\delta$ is a terminal decision rule: on the event $\set{N = n}$, the decision $\delta$ is a function of $(X_1, \dots, X_n)$ with values in $D$.

*Sequential analysis* is the study of sequential procedures, in particular of their error probabilities and of the distribution of the sample size $N$.

## Remarks

Example: in a [[test|087P03NEND]] about the mean of $X_i \in \set{0, 1}$, the rule "stop at the first $n$ with $\abs{\sum_{i \le n} (2X_i - 1)} = 5$, and reject $H_0$ if the sum is positive" is a sequential procedure.
The event $\set{N = n}$ depends only on $X_1, \dots, X_n$, so $N$ is a stopping time.
Non-example: "stop at the $n$ for which $X_n$ is the largest of the first $100$ observations" is not a sequential procedure.
Deciding whether $N = n$ needs future observations, so clause 1 fails.
A procedure with $N = m$ constant is the usual fixed-sample procedure, so fixed-sample statistics is a special case.
