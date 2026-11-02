---
tag: MCCXNPGGSH
kind: definition
name: Cesàro means of Fourier series
msc: [42A24, 40G05]
defines: MA8X1G11DH
uses: [G12KXDHPPS, 5NN2YZZR3V, 08R2V9GZF7, DCCA2T9GKH]
sources:
  - url: https://en.wikipedia.org/wiki/Fej%C3%A9r%27s_theorem
---

## Definition

Let $f \colon \R \to \C$ be a $2\pi$-periodic function that is integrable on $[-\pi, \pi]$, with [[Fourier coefficients|5NN2YZZR3V]] $\hat f(k)$, $k \in \Z$.
For $n \ge 0$ let $S_n f(x) = \sum_{k=-n}^{n} \hat f(k) e^{ikx}$ be the partial sums of its [[Fourier series|G12KXDHPPS]].
For $N \ge 1$, the $N$-th *Cesàro mean* (or Fejér mean) of the Fourier series of $f$ is
$$\sigma_N f(x) = \frac{1}{N} \sum_{n=0}^{N-1} S_n f(x).$$

## Remarks

Counting how often each frequency occurs in $S_0 f, \ldots, S_{N-1} f$ gives
$$\sigma_N f(x) = \sum_{\abs{k} < N} \left( 1 - \frac{\abs{k}}{N} \right) \hat f(k) e^{ikx} = \frac{1}{2\pi} \int_{-\pi}^{\pi} F_N(t) f(x - t) \, dt,$$
where $F_N$ is the [[Fejér kernel|DCCA2T9GKH]].
So $\sigma_N f$ is a trigonometric polynomial of degree at most $N - 1$.
It is the [[Cesàro mean|08R2V9GZF7]] of order $1$ of the sequence $(S_n f(x))_{n \ge 0}$.

Example: for $f(x) = \cos x$, $S_0 f = 0$ and $S_n f = \cos x$ for $n \ge 1$.
So $\sigma_N f = \frac{N-1}{N} \cos x$, which tends to $f$.

Non-example: the Abel–Poisson means $\sum_k r^{\abs{k}} \hat f(k) e^{ikx}$ also average the Fourier series, but with the weights $r^{\abs{k}}$ instead of $1 - \abs{k}/N$; they are a different method, the [[Abel–Poisson summation|RZZ78GXP5F]].
