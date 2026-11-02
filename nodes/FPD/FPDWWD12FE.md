---
tag: FPDWWD12FE
kind: counterexample
name: Continuous function with divergent Fourier series
msc: [42A20, 46B99]
uses: [V6Q24CHJG8, RWKQ5EP4YF, YG0042V8CJ, G12KXDHPPS, 0X3WGX95FE, 0A7KGAYHGV]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_of_Fourier_series
---

## Counterexample

There is a [[continuous|0X3WGX95FE]] $2\pi$-periodic function $f \colon \R \to \C$ whose [[Fourier series|G12KXDHPPS]] diverges at $0$; in fact $\sup_N \abs{S_N f(0)} = \infty$.

Check: let $C(\mathbb{T})$ be the Banach space of continuous $2\pi$-periodic functions with the supremum norm.
For each $N$, the map $\Lambda_N(f) = S_N f(0) = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) D_N(t) \, dt$ is a bounded linear functional on $C(\mathbb{T})$, where $D_N$ is the Dirichlet kernel.
Its norm is the [[Lebesgue constant|RWKQ5EP4YF]] $L_N = \frac{1}{2\pi} \int_{-\pi}^{\pi} \abs{D_N}$, and $L_N \to \infty$.
If $\sup_N \abs{\Lambda_N(f)}$ were finite for every $f \in C(\mathbb{T})$, the [[uniform boundedness principle|YG0042V8CJ]] would give $\sup_N L_N < \infty$, which is false.
So some $f \in C(\mathbb{T})$ has $\sup_N \abs{S_N f(0)} = \infty$, and its Fourier series diverges at $0$.

## Remarks

The [[Baire category theorem|0A7KGAYHGV]] behind the uniform boundedness principle gives more: the set of $f \in C(\mathbb{T})$ with $\sup_N \abs{S_N f(0)} = \infty$ is a dense $G_\delta$ subset of $C(\mathbb{T})$.
Paul du Bois-Reymond gave the first such function in 1873, by an explicit construction.
Continuity is thus not enough for pointwise convergence, while bounded variation or a Dini condition is.
The divergence can happen only on a set of measure zero for $f \in L^2$, by [[Carleson's theorem|FBH6KG484Z]].
By the [[Kahane–Katznelson theorem|42DDDZHP7F]], every set of measure zero is the divergence set of some continuous function.
For integrable functions, [[Kolmogorov's example|25V2MHPHZ7]] diverges everywhere.

## Explanations

### L1 human

One might expect every continuous periodic function to have a convergent Fourier series, but this is false.
The partial sums at a point are averages against a kernel whose total absolute size grows without bound.
A continuous function that oscillates in step with the kernel, at more and more frequencies, makes these averages grow without bound.
