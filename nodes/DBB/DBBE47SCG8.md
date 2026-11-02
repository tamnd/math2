---
tag: DBBE47SCG8
kind: definition
name: Nelson–Aalen estimator
msc: [62N02, 62G05]
defines: 93GK2SPBKV
uses: [Y959NKQ3XW, MY8ZZP84NP, 0SSS6ERQ0S]
sources:
  - url: https://en.wikipedia.org/wiki/Nelson–Aalen_estimator
---

## Definition

Let $(\tilde t_1, \delta_1), \dots, (\tilde t_n, \delta_n)$ be right-[[censored|MY8ZZP84NP]] observations of a lifetime, with $\delta_i = 1$ for an event and $\delta_i = 0$ for a censored time.
Let $t_{(1)} < \dots < t_{(m)}$ be the distinct event times, $d_j$ the number of events at $t_{(j)}$, and $n_j = \#\set{i : \tilde t_i \ge t_{(j)}}$ the number at risk just before $t_{(j)}$.
The *Nelson–Aalen estimator* of the cumulative [[hazard function|Y959NKQ3XW]] $H$ is
$$\hat H(t) = \sum_{j \,:\, t_{(j)} \le t} \frac{d_j}{n_j}, \qquad t \ge 0,$$
with the empty sum equal to $0$.

## Remarks

In counting process notation, with $N(t)$ the number of observed events up to $t$ and $Y(t)$ the number at risk at $t$, the [[estimator|0SSS6ERQ0S]] is $\hat H(t) = \int_0^t \frac{dN(s)}{Y(s)}$, with $0/0 = 0$.
A common variance estimator is $\sum_{j : t_{(j)} \le t} d_j / n_j^2$.
The survival estimate $e^{-\hat H(t)}$ is at least the Kaplan–Meier estimate, since $e^{-x} \ge 1 - x$ for all $x$.

Example: for the observations $2, 3^+, 5, 7$, with $3^+$ censored, $(n_j, d_j)$ is $(4, 1)$ at $2$, $(2, 1)$ at $5$ and $(1, 1)$ at $7$.
So $\hat H = 0$ on $[0, 2)$, $1/4$ on $[2, 5)$, $3/4$ on $[5, 7)$ and $7/4$ from $7$ on.

Non-example: the cumulative sum $\sum_{t_{(j)} \le t} d_j / n$, which divides by the initial sample size $n$, is not the Nelson–Aalen estimator.
It ignores that subjects leave the risk set, and it underestimates the cumulative hazard.
