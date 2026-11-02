---
tag: 9VW7VX0SXB
kind: definition
name: Constructive analysis
msc: ["03F60", "03F65"]
defines: HEB1VQW0DQ
uses: [F1P5SZ1XPH, 08J2M1JYAG, 0QZMTN5AXX, 00KAFBR32E, 0RYYK8PG4S]
sources:
  - url: https://en.wikipedia.org/wiki/Constructive_analysis
---

## Definition

*Constructive analysis* is real and functional analysis developed within [[constructivism|F1P5SZ1XPH]], with intuitionistic logic.
In Bishop's approach, the basic notions are these.

1. A *real number* is a sequence $(x_n)_{n \ge 1}$ of rational numbers that is *regular*: $\abs{x_m - x_n} \le \frac{1}{m} + \frac{1}{n}$ for all $m, n \ge 1$.
2. Two real numbers $(x_n)$ and $(y_n)$ are *equal* if $\abs{x_n - y_n} \le \frac{2}{n}$ for all $n \ge 1$.
3. A real number $(x_n)$ is *positive* if $x_n > \frac{1}{n}$ for some $n$, and $x < y$ means that $y - x$ is positive.

Functions, continuity and other notions are then defined so that each existence statement comes with a method of construction.

## Remarks

A regular sequence is a [[Cauchy sequence|0QZMTN5AXX]] with an explicit modulus of convergence, and it defines a classical [[real number|08J2M1JYAG]].
Example: the sequence $x_n = \sum_{k=0}^{n} \frac{1}{k!}$ is regular, since $\abs{x_m - x_n} \le \sum_{k > n} \frac{1}{k!} \le \frac{1}{n}$ for $m > n \ge 1$; it defines $e$.
Non-example: the statement "for every real $x$, either $x = 0$ or $x \ne 0$" is not a theorem of constructive analysis.
A proof would give a method to decide, for each regular sequence, whether all its terms stay within $\frac{2}{n}$ of $0$.
Such a method would need the [[law of excluded middle|0RYYK8PG4S]] for statements about infinitely many terms.
The [[intermediate value theorem|00KAFBR32E]] holds in an approximate form: if $f$ is continuous on $[0, 1]$ with $f(0) < 0 < f(1)$, then for each $\varepsilon > 0$ there is $x$ with $\abs{f(x)} < \varepsilon$.
