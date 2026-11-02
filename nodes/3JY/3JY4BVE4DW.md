---
tag: 3JY4BVE4DW
kind: concept
name: Dirichlet kernel
msc: [42A20, 42A24]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_kernel
same_as:
  wikidata: Q906024
  wikipedia: Dirichlet kernel
---

## Summary

The Dirichlet kernel $D_N(x) = \sum_{n=-N}^{N} e^{inx}$ is the [[trigonometric polynomial|J3NJQ5FZJ5]] whose [[convolution|2Z29JN3VES]] with a periodic function gives the $N$-th partial sum of its [[Fourier series|G12KXDHPPS]].
In closed form $D_N(x) = \frac{\sin((N + \frac{1}{2}) x)}{\sin(x/2)}$.
Its integral over a period is constant, but the integral of its absolute value grows like $\log N$.
This growth is the source of most convergence problems of Fourier series, including the existence of continuous functions with divergent Fourier series.

## Explanations

### L1 human

To get the $N$-th partial Fourier sum of a function at a point, one averages the function against a fixed weight centred at that point, the Dirichlet kernel.
The kernel has a tall peak of height $2N + 1$ at $0$ and oscillates with slowly shrinking waves elsewhere, taking negative values.
Because of these negative lobes, the averaging is not a true local average, and it can be fooled by functions that oscillate in step with the kernel.
The kernel of [[Fejér|DCCA2T9GKH]], an average of Dirichlet kernels, has no negative values and behaves much better.
