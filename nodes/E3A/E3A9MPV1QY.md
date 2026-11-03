---
tag: E3A9MPV1QY
kind: statement
role: theorem
name: Fano's inequality
msc: [94A17, 94A24, 62B10]
uses: [0X2J0VY6DN, F3ZNDD6GG7, GW25TGD33J]
about: [F3ZNDD6GG7]
sources:
  - url: https://en.wikipedia.org/wiki/Fano%27s_inequality
same_as:
  wikidata: Q1624376
  wikipedia: Fano's inequality
---

## Statement

Let $X$ be a [[discrete random variable|0X2J0VY6DN]] with values in a finite set $\mathcal{X}$ with $\abs{\mathcal{X}} \ge 2$.
Let $Y$ be a discrete random variable on the same probability space, and let $\hat{X} = g(Y)$ for a function $g$ with values in $\mathcal{X}$.
Let $P_e = P(\hat{X} \ne X)$ be the error probability, and let $h(t) = -t \log t - (1 - t) \log (1 - t)$, with the same base of logarithm everywhere.
Then
$$H(X \mid Y) \le h(P_e) + P_e \log (\abs{\mathcal{X}} - 1),$$
where $H(X \mid Y)$ is the [[conditional entropy|F3ZNDD6GG7]].

## Remarks

Proof idea: let $E$ be the indicator of the event $\hat{X} \ne X$.
Expand $H(E, X \mid Y)$ in two ways: it equals $H(X \mid Y)$, since $E$ is a function of $X$ and $Y$, and it equals $H(E \mid Y) + H(X \mid E, Y) \le h(P_e) + P_e \log (\abs{\mathcal{X}} - 1)$.
For the last step, $H(X \mid E = 0, Y) = 0$, and given $E = 1$ and $Y$ the variable $X$ lies in the set $\mathcal{X} \setminus \set{g(Y)}$ of $\abs{\mathcal{X}} - 1$ elements.

In bits, using $h(P_e) \le 1$, the inequality gives the weaker but common form $P_e \ge \frac{H(X \mid Y) - 1}{\log_2 \abs{\mathcal{X}}}$.

Example: let $X$ be uniform on $\set{1, \dots, 8}$ and independent of $Y$.
Then $H(X \mid Y) = 3$ bits, and the bound gives $P_e \ge \frac{3 - 1}{3} = \frac23$; the exact best error is $\frac78$.

The full inequality is sharp here: $h(\frac78) + \frac78 \log_2 7 = 3$, and $t \mapsto h(t) + t \log_2 7$ is increasing on $[0, \frac78]$, so it gives exactly $P_e \ge \frac78$.

## Explanations

### L1 human

If you try to guess $X$ from an observation $Y$, and much uncertainty about $X$ remains after seeing $Y$, then you must often guess wrong.
Fano's inequality turns this into a lower bound on the error probability in terms of the conditional entropy.

### L2 human

The inequality is the key step in the converse of the [[noisy-channel coding theorem|PR3NJB0SKG]].
There, a small error probability forces $H(W \mid Y^n)$ to be small compared with $n$.
The [[data processing inequality|BGH1T3HKPV]] then bounds the rate by the capacity.
In statistics it gives lower bounds for the minimax risk of estimation, by reducing estimation to a test among finitely many hypotheses.
Here $h$ is the [[binary entropy function|GW25TGD33J]] in the chosen base.
