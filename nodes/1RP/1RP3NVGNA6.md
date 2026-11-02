---
tag: 1RP3NVGNA6
kind: statement
role: theorem
name: Szegő recurrence and Verblunsky coefficients
msc: [42C05, 33C47, "30E05"]
uses: [3F9G3DRQ62]
about: [3F9G3DRQ62]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_polynomials_on_the_unit_circle
---

## Statement

Let $\mu$ be a probability measure on the unit circle $\partial\mathbb{D}$ with infinite support, and let $\Phi_n$ be its monic [[orthogonal polynomials|3F9G3DRQ62]].
For a polynomial $p$ of degree at most $n$, let $p^*(z) = z^n \, \overline{p(1/\bar z)}$ be its reversed polynomial of order $n$; so $\Phi_n^*$ has constant term $1$.

1. There are complex numbers $\alpha_0, \alpha_1, \alpha_2, \dots$ with $\abs{\alpha_n} < 1$ such that for every $n \ge 0$
$$\Phi_{n+1}(z) = z \, \Phi_n(z) - \overline{\alpha_n} \, \Phi_n^*(z).$$
They are given by $\alpha_n = -\overline{\Phi_{n+1}(0)}$ and are called the *Verblunsky coefficients* of $\mu$.
2. The norms satisfy $\norm{\Phi_{n+1}}^2 = (1 - \abs{\alpha_n}^2) \norm{\Phi_n}^2$, so $\norm{\Phi_n}^2 = \prod_{j=0}^{n-1} (1 - \abs{\alpha_j}^2)$.
3. (Verblunsky's theorem) Let $\mathbb{D}$ be the open unit disk. The map $\mu \mapsto (\alpha_n)_{n \ge 0}$ is a bijection from the probability measures on $\partial\mathbb{D}$ with infinite support onto the sequences in $\mathbb{D}$.

## Remarks

For part 1, the polynomial $\Phi_{n+1} - z\Phi_n$ has degree at most $n$.
It is orthogonal to $z, z^2, \dots, z^n$, because $\Phi_{n+1}$ is, and multiplication by $z$ is unitary on $L^2(\mu)$ and maps $\Phi_n \perp \set{1, \dots, z^{n-1}}$ onto $z\Phi_n \perp \set{z, \dots, z^n}$.
The polynomials of degree at most $n$ orthogonal to $z, \dots, z^n$ form a one-dimensional space spanned by $\Phi_n^*$, which gives the recurrence.
Taking norms, with $\norm{z\Phi_n} = \norm{\Phi_n^*} = \norm{\Phi_n}$, gives part 2, and $\norm{\Phi_{n+1}} > 0$ forces $\abs{\alpha_n} < 1$.
Part 3 builds $\mu$ from any sequence in $\mathbb{D}$ by running the recurrence and taking a weak limit of the measures $\abs{\varphi_n(e^{i\theta})}^{-2} d\theta/2\pi$.

Example: for $d\mu = d\theta/2\pi$, $\Phi_n(z) = z^n$ and $\Phi_n^* = 1$, so $\Phi_{n+1} = z\Phi_n$ and all $\alpha_n = 0$.
Conversely, by part 3, the uniform measure is the only one with all Verblunsky coefficients zero.

Infinite support is needed.
If $\mu$ is supported on $N$ points, then $L^2(\mu)$ has dimension $N$ and $\Phi_N$ has norm $0$; the recurrence ends with $\abs{\alpha_{N-1}} = 1$.

## Explanations

### L1 human

On the real line, orthogonal polynomials are built step by step by a rule with two numbers per step.
On the unit circle the rule is simpler: one complex number $\alpha_n$ per step, of modulus less than $1$.
Every measure on the circle gives such a sequence, and every such sequence comes from exactly one measure.
So the sequence of Verblunsky coefficients is a complete, free set of coordinates for measures on the circle.

### L2 human

The recurrence turns questions about the measure $\mu$ into questions about the sequence $(\alpha_n)$.
For example, [[Szegő's theorem|SZ8ARMDEMY]] says that $\sum \abs{\alpha_n}^2 < \infty$ exactly when $\log$ of the density of $\mu$ is integrable.
The $\alpha_n$ are the entries of the CMV matrix, the unitary analogue of the Jacobi matrix, which represents multiplication by $z$ on $L^2(\mu)$.
In prediction theory and signal processing the same numbers appear as reflection coefficients, computed by the Levinson algorithm from the moments of $\mu$.
