---
tag: 8M5GCC6J3T
kind: definition
name: Typical set
msc: [94A17, 94A29]
defines: 6J90EN65VQ
uses: [0D6J4B671D, 00MRN0FARV, Y86E072V0V, 5P7AA5QR7T]
sources:
  - url: https://en.wikipedia.org/wiki/Typical_set
---

## Definition

Let $\mathcal{X}$ be a finite set and let $p$ be a [[probability mass function|0D6J4B671D]] on $\mathcal{X}$, with [[Shannon entropy|Y86E072V0V]] $H = -\sum_x p(x) \log_2 p(x)$.
For $x^n = (x_1, \dots, x_n) \in \mathcal{X}^n$, let $p(x^n) = p(x_1) \cdots p(x_n)$.
For $n \ge 1$ and $\varepsilon > 0$, the *typical set* is
$$A_\varepsilon^{(n)} = \set{x^n \in \mathcal{X}^n : p(x^n) > 0 \text{ and } \abs{-\tfrac1n \log_2 p(x^n) - H} \le \varepsilon}.$$
Equivalently, $x^n \in A_\varepsilon^{(n)}$ when $2^{-n(H + \varepsilon)} \le p(x^n) \le 2^{-n(H - \varepsilon)}$.

## Remarks

Let $X_1, X_2, \dots$ be [[independent and identically distributed|00MRN0FARV]] with law $p$.
The [[asymptotic equipartition property|5P7AA5QR7T]] gives the main properties.

1. $P((X_1, \dots, X_n) \in A_\varepsilon^{(n)}) > 1 - \varepsilon$ for all large $n$.
2. $\abs{A_\varepsilon^{(n)}} \le 2^{n(H + \varepsilon)}$ for every $n$.
3. $\abs{A_\varepsilon^{(n)}} \ge (1 - \varepsilon) 2^{n(H - \varepsilon)}$ for all large $n$.

Example: for a fair coin, $H = 1$ and $p(x^n) = 2^{-n}$ for every sequence, so $A_\varepsilon^{(n)} = \set{0, 1}^n$ for every $\varepsilon > 0$.

Non-example: for a coin with $p(1) = 0.9$ and small $\varepsilon$, the all-ones sequence is not typical for large $n$.
Indeed $-\frac1n \log_2 0.9^n = \log_2 \frac{1}{0.9} \approx 0.152$, while $H \approx 0.469$.

This is the *weakly typical* set; the *strongly typical* set asks instead that each letter $a$ occur about $n p(a)$ times.

## Explanations

### L1 human

A sequence is typical when its probability is about what the entropy predicts, $2^{-nH}$.
