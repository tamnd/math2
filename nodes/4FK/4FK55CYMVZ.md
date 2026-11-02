---
tag: 4FK55CYMVZ
kind: definition
name: Pringsheim convergence
msc: [40B05, 40A05]
defines: QYTGCW1GTK
uses: [B70G8FYPG0]
sources:
  - url: https://en.wikipedia.org/wiki/Iterated_limit
---

## Definition

Let $(a_{m,n})_{m, n \ge 1}$ be a [[double sequence|B70G8FYPG0]] of real or complex numbers, and let $L$ be a number.
The double sequence *converges to $L$ in the sense of Pringsheim* if the following holds.
For every $\varepsilon > 0$ there is an integer $N$ such that $\abs{a_{m,n} - L} < \varepsilon$ for all $m \ge N$ and $n \ge N$.
Then $L$ is unique; it is called the *double limit* and is written $\lim_{m, n \to \infty} a_{m,n} = L$.

## Remarks

Example: $a_{m,n} = \frac{1}{m} + \frac{1}{n}$ converges to $0$, because $m, n \ge N$ gives $\abs{a_{m,n}} \le \frac{2}{N}$, which is less than $\varepsilon$ once $N > 2/\varepsilon$.
Non-example: $a_{m,n} = \frac{m}{m+n}$ has no double limit, because $a_{N,N} = \frac12$ while $a_{N,n} \to 0$ as $n \to \infty$, so no single $L$ works for $\varepsilon = \frac14$.
A Pringsheim convergent double sequence need not be bounded: put $a_{1,n} = n$ and $a_{m,n} = 0$ for $m \ge 2$; the double limit is $0$, yet the first row diverges.
So the double limit may exist while an iterated limit $\lim_m \lim_n a_{m,n}$ does not; the [[Moore–Osgood theorem|QN2210XCST]] gives conditions under which they agree.

## Explanations

### L1 human

Both indices must be large at the same time.
It is not enough to send one index to infinity first and then the other.
