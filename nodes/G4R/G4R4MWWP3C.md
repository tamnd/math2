---
tag: G4R4MWWP3C
kind: statement
role: theorem
name: Hilbert's inequality
msc: [26D15]
uses: [09FTAET5Z4]
about: [09FTAET5Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_inequality
same_as:
  wikidata: Q3153998
  wikipedia: Hilbert's inequality
---

## Statement

Let $n \ge 1$ and let $u_1, \dots, u_n$ be [[complex numbers|09FTAET5Z4]].
Then
$$\Big| \sum_{\substack{1 \le r, s \le n \\ r \ne s}} \frac{u_r \overline{u_s}}{r - s} \Big| \le \pi \sum_{r=1}^{n} \abs{u_r}^2.$$

## Remarks

Proof idea: the function $\varphi(t) = i(\pi - t)$ on $(0, 2\pi)$ has Fourier coefficients $1/k$ for $k \ne 0$ and $0$ for $k = 0$, and $\abs{\varphi} \le \pi$.
So the double sum equals $\frac{1}{2\pi} \int_0^{2\pi} \varphi(t) \, \abs{P(t)}^2 \, dt$ for the trigonometric polynomial $P(t) = \sum_r u_r e^{-i r t}$.
Bounding $\abs{\varphi}$ by $\pi$ and using [[Parseval's identity|047RFCNVSK]] $\frac{1}{2\pi} \int_0^{2\pi} \abs{P}^2 = \sum_r \abs{u_r}^2$ gives the result.

The constant $\pi$ cannot be replaced by a smaller one that works for all $n$.

A closely related inequality, also called Hilbert's inequality, says that for nonnegative $a_m, b_n$,
$$\sum_{m=1}^{\infty} \sum_{n=1}^{\infty} \frac{a_m b_n}{m + n} \le \pi \Big( \sum_{m=1}^{\infty} a_m^2 \Big)^{1/2} \Big( \sum_{n=1}^{\infty} b_n^2 \Big)^{1/2}.$$

## Explanations

### L1 human

Hilbert's inequality controls a double sum in which each pair of terms is weighted by $1/(r - s)$.
These weights do not shrink fast, and they change sign, so it is not obvious that the sum is small.
The inequality says it is never more than $\pi$ times the total squared size of the numbers.

### L2 human

The matrix with entries $1/(r - s)$ for $r \ne s$ is a discrete version of the Hilbert transform.
The inequality says that this matrix has operator norm at most $\pi$ on $\C^n$ for every $n$, uniformly in $n$.
The proof is a model of a common technique: write a matrix as the Fourier coefficients of a bounded function, then use Parseval's identity.
