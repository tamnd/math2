---
tag: RWKQ5EP4YF
kind: statement
role: proposition
name: Lebesgue constants of the Dirichlet kernel
msc: [42A20, 42A05]
uses: [3JY4BVE4DW, 0X3WGX95FE]
about: [3JY4BVE4DW]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_kernel
---

## Statement

For an integer $N \ge 1$, let $D_N$ be the [[Dirichlet kernel|3JY4BVE4DW]] of order $N$ and let
$$L_N = \frac{1}{2\pi} \int_{-\pi}^{\pi} \abs{D_N(x)} \, dx$$
be its $N$-th *Lebesgue constant*.
Then
$$L_N = \frac{4}{\pi^2} \log N + O(1) \qquad \text{as } N \to \infty.$$
In particular $L_N \to \infty$.
Let $C(\mathbb{T})$ be the space of [[continuous|0X3WGX95FE]] $2\pi$-periodic functions with the supremum norm.
Then $L_N$ is the operator norm of the partial sum map $f \mapsto S_N f$ on $C(\mathbb{T})$.
It is also the norm of the linear functional $f \mapsto S_N f(0)$ on $C(\mathbb{T})$.

## Remarks

For the estimate, use $\abs{\sin(x/2)} \le \abs{x}/2$ and compare $\abs{\sin((N + \frac{1}{2}) x)}$ on each interval between consecutive zeros with its mean value $\frac{2}{\pi}$.
Summing over about $N$ intervals gives a harmonic sum, hence the $\log N$.
The norm of $f \mapsto S_N f(0) = \frac{1}{2\pi} \int f(-t) D_N(t) \, dt$ is at most $L_N$, and it equals $L_N$ by testing on continuous functions that approximate $\operatorname{sgn} D_N$.
Example: $L_0 = 1$ and $L_N > 1$ for $N \ge 1$; the values grow very slowly, like $0.405 \log N$.

## Explanations

### L1 human

The Dirichlet kernel has integral $1$, but the integral of its absolute value is much larger and grows like a constant times $\log N$.
This number measures how much a partial Fourier sum can amplify a bounded function.
Since the amplification is unbounded, partial Fourier sums of bounded continuous functions can become unbounded.

### L2 human

By the uniform boundedness principle, the unboundedness of $L_N$ implies that some continuous function has a Fourier series that diverges at $0$.
It also implies that $S_N f$ does not converge to $f$ in $L^1(\mathbb{T})$ for every $f \in L^1(\mathbb{T})$, because the norm of $S_N$ on $L^1$ is also $L_N$.
On the positive side, $\abs{S_N f - f} \le (1 + L_N) E_N(f)$, where $E_N(f)$ is the distance from $f$ to trigonometric polynomials of degree at most $N$; combined with Jackson's theorem this gives the Dini–Lipschitz criterion.
The Fejér kernel, which has $L^1$ norm $1$, avoids the problem and gives Fejér's theorem.
