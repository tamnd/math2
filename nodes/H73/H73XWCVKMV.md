---
tag: H73XWCVKMV
kind: definition
name: Master equation
msc: [82C31, 60J27, 82C05]
defines: VHQA7XPMQ4
uses: [TWQFE0FZZS, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Master_equation
---

## Definition

Let $S$ be a finite or countable set of states.
For each pair $x \ne y$ in $S$, let $w(x \to y) \ge 0$ be a transition rate, and assume $\sum_{y \ne x} w(x \to y) < \infty$ for every $x$.
The *master equation* with these rates is the system of [[ordinary differential equations|0NT64JV96A]]
$$\frac{d}{dt} P_t(x) = \sum_{y \ne x} \big( w(y \to x) \, P_t(y) - w(x \to y) \, P_t(x) \big), \qquad x \in S,$$
for a family $(P_t)_{t \ge 0}$ of probability distributions on $S$.

## Remarks

With the matrix $Q(x, y) = w(x \to y)$ for $x \ne y$ and $Q(x, x) = -\sum_{y \ne x} w(x \to y)$, the equation reads $\frac{d}{dt} P_t = P_t Q$, with $P_t$ as a row vector.
This is the Kolmogorov forward equation of the [[continuous-time Markov chain|TWQFE0FZZS]] with rate matrix $Q$, and $P_t(x)$ is the probability that the chain is in state $x$ at time $t$.
For finite $S$ the solution is $P_t = P_0 e^{tQ}$.

Example: for $S = \set{0, 1}$ with $w(0 \to 1) = a$ and $w(1 \to 0) = b$, where $a, b > 0$, the equation for $P_t(1)$ is $\frac{d}{dt} P_t(1) = a P_t(0) - b P_t(1) = a - (a + b) P_t(1)$.
Its solution is $P_t(1) = \frac{a}{a + b} + \big(P_0(1) - \frac{a}{a + b}\big) e^{-(a + b)t}$, which tends to $\frac{a}{a + b}$.

Non-example: the system $\frac{d}{dt} P_t(x) = \sum_{y \ne x} w(y \to x) P_t(y)$, without the loss term, is not a master equation; it does not conserve $\sum_x P_t(x)$, so $P_t$ does not stay a probability distribution.

A distribution $\pi$ is stationary when the right side vanishes; it satisfies *detailed balance* when $w(y \to x) \pi(y) = w(x \to y) \pi(x)$ for all $x \ne y$, which is a stronger condition.
