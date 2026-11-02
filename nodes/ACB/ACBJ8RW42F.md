---
tag: ACBJ8RW42F
kind: definition
name: Summability kernel
msc: [42A24, 42A85]
defines: 1QC5206K07
uses: [0X3WGX95FE, 0ATF6Q0633]
sources:
  - url: https://en.wikipedia.org/wiki/Dirac_delta_function
---

## Definition

A *summability kernel* is a sequence $(k_n)_{n \ge 1}$ of [[continuous|0X3WGX95FE]] $2\pi$-[[periodic functions|0ATF6Q0633]] $k_n \colon \R \to \C$ such that:

1. $\frac{1}{2\pi} \int_{-\pi}^{\pi} k_n(t) \, dt = 1$ for every $n$.
2. There is a constant $C$ with $\frac{1}{2\pi} \int_{-\pi}^{\pi} \abs{k_n(t)} \, dt \le C$ for every $n$.
3. For every $\delta$ with $0 < \delta < \pi$, $\int_{\delta \le \abs{t} \le \pi} \abs{k_n(t)} \, dt \to 0$ as $n \to \infty$.

## Remarks

For an integrable $2\pi$-periodic $f$, the convolutions $k_n * f(x) = \frac{1}{2\pi} \int_{-\pi}^{\pi} k_n(t) f(x - t) \, dt$ tend to $f$ in $L^1$.
If $f$ is continuous, they tend to $f$ uniformly.
A kernel with $k_n \ge 0$ is called positive; then clause 2 follows from clause 1 with $C = 1$.

Example: the [[Fejér kernel|DCCA2T9GKH]] $F_N(t) = \sum_{\abs{j} < N} \left(1 - \frac{\abs{j}}{N}\right) e^{ijt} = \frac{1}{N} \left( \frac{\sin(Nt/2)}{\sin(t/2)} \right)^2$.
Its mean is the coefficient of $e^{0}$, which is $1$.
It is nonnegative, so clause 2 holds with $C = 1$.
For $\delta \le \abs{t} \le \pi$ it is at most $\frac{1}{N \sin^2(\delta/2)}$, which gives clause 3.

Non-example: the [[Dirichlet kernel|3JY4BVE4DW]] $D_n(t) = \sum_{\abs{j} \le n} e^{ijt}$ satisfies clause 1, but $\frac{1}{2\pi} \int_{-\pi}^{\pi} \abs{D_n}$ grows like a constant times $\log n$, so clause 2 fails.

Kernels indexed by a continuous parameter are treated the same way; the [[Poisson kernel|TCYSWCTYYM]] $P_r$ with $r \to 1^-$ is the main example.
A summability kernel is a bounded [[approximate identity|CDYXTW3PJF]] of the convolution algebra $L^1(\mathbb{T})$.
