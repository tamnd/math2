---
tag: CWP26Y1TCZ
kind: definition
name: Double series
msc: [40B05]
defines: PAXCH4FFSV
uses: [WK5V372TG3, QYTGCW1GTK, 09FTAET5Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Series_(mathematics)
---

## Definition

Let $(a_{m,n})_{m, n \in \N}$ be a [[double sequence|WK5V372TG3]] of [[complex numbers|09FTAET5Z4]].
The double series $\sum_{m, n = 0}^{\infty} a_{m,n}$ is the double sequence of rectangular partial sums
$$S_{M,N} = \sum_{m=0}^{M} \sum_{n=0}^{N} a_{m,n}.$$
The double series converges to $s \in \C$ if $(S_{M,N})$ converges to $s$ in the sense of [[Pringsheim|QYTGCW1GTK]].
That is, for every $\varepsilon > 0$ there is $K$ with $\abs{S_{M,N} - s} < \varepsilon$ for all $M, N \ge K$.

## Remarks

Example: for $a_{m,n} = 2^{-m} 3^{-n}$ one has $S_{M,N} = \left(\sum_{m \le M} 2^{-m}\right)\left(\sum_{n \le N} 3^{-n}\right)$.
The two factors tend to $2$ and $\tfrac32$, so the double series converges to $3$.
Non-example: for $a_{m,n} = 1$ when $m = n$ and $0$ otherwise, $S_{M,N} = \min(M, N) + 1$, which is unbounded, so the double series diverges.
A convergent double series can have unbounded terms.
With $a_{0,n} = n$, $a_{1,n} = -n$ and $a_{m,n} = 0$ for $m \ge 2$, one has $S_{M,N} = 0$ for all $M \ge 1$.
So it converges to $0$, although its rows do not form convergent series.

## Explanations

### L1 human

A double series is the sum of all entries of an infinite table, taken as the limit of sums over larger and larger rectangles.
