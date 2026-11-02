---
tag: EJE15QHXZN
kind: definition
name: Dirichlet kernel
msc: [42A20, 42A24]
defines: 3JY4BVE4DW
uses: [J3NJQ5FZJ5, G12KXDHPPS, 2Z29JN3VES]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_kernel
---

## Definition

Let $N \ge 0$ be an integer.
The *Dirichlet kernel* of order $N$ is the [[trigonometric polynomial|J3NJQ5FZJ5]] $D_N \colon \R \to \R$ given by
$$D_N(x) = \sum_{n=-N}^{N} e^{inx} = 1 + 2 \sum_{n=1}^{N} \cos nx.$$

## Remarks

Summing the geometric progression gives $D_N(x) = \frac{\sin((N + \frac{1}{2}) x)}{\sin(x/2)}$ for $x \notin 2\pi\Z$, and $D_N(x) = 2N + 1$ for $x \in 2\pi\Z$.
It is even, $2\pi$-periodic, and $\frac{1}{2\pi} \int_{-\pi}^{\pi} D_N(x) \, dx = 1$, since only the term $n = 0$ contributes.
For $f$ integrable and $2\pi$-periodic, the partial sums of its [[Fourier series|G12KXDHPPS]] are the [[convolutions|2Z29JN3VES]]
$$S_N f(x) = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x - t) D_N(t) \, dt.$$
Example: $D_1(x) = 1 + 2 \cos x$, and indeed $\frac{\sin(3x/2)}{\sin(x/2)} = 3 - 4 \sin^2(x/2) = 1 + 2 \cos x$.
Non-example: $\sum_{n=0}^{N} e^{inx}$ is not a Dirichlet kernel, since its sum is not symmetric in $n$; it is not real-valued for $N \ge 1$.
Some authors use the factor $\frac{1}{2\pi}$ in $D_N$ itself, or the period $1$ with $D_N(x) = \sum_{\abs{n} \le N} e^{2\pi i n x}$.
