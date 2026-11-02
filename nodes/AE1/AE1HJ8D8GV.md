---
tag: AE1HJ8D8GV
kind: statement
role: theorem
name: Calderón–Zygmund theorem
msc: [42B20]
uses: [HTMCEARGDD, SASP14MA1Z, H4C888M5AZ, K1YKXVPVDG, R1PHMVBJ9J]
about: [HTMCEARGDD]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_integral_operators_of_convolution_type
---

## Statement

Let $n \ge 1$ and let $K$ be a locally integrable function on $\R^n \setminus \set{0}$.
Assume that there is a constant $A$ such that:

1. $\abs{K(x)} \le A\abs{x}^{-n}$ for all $x \ne 0$;
2. $\int_{\abs{x} \ge 2\abs{y}} \abs{K(x - y) - K(x)} \, dx \le A$ for all $y \ne 0$;
3. $\int_{r < \abs{x} < R} K(x) \, dx = 0$ for all $0 < r < R$.

For $\varepsilon > 0$, let $T_\varepsilon f(x) = \int_{\abs{y} > \varepsilon} K(y) f(x - y) \, dy$.
Then for each $1 < p < \infty$ there is a constant $C$, depending only on $n$ and $p$, such that
$$\norm{T_\varepsilon f}_{L^p(\R^n)} \le C A \norm{f}_{L^p(\R^n)} \quad \text{for all } f \in L^p(\R^n) \text{ and } \varepsilon > 0.$$
Moreover, the operators $T_\varepsilon$ are of weak type $(1, 1)$, uniformly in $\varepsilon$.

## Remarks

The proof has three steps.
The three conditions together give a uniform bound on the Fourier transforms of the truncated kernels, hence a uniform $L^2$ bound by the Plancherel theorem.
The [[Calderón–Zygmund lemma|K1YKXVPVDG]] splits $f$ into a bounded good part and a bad part with mean zero on disjoint cubes.
Condition 2 controls the operator on the bad part away from the cubes, and this gives the weak type $(1, 1)$ bound.
The [[Marcinkiewicz interpolation theorem|R1PHMVBJ9J]] then gives $1 < p \le 2$, and duality gives $2 \le p < \infty$.

Example: on $\R$, $K(x) = \frac{1}{\pi x}$ satisfies condition 1 with $A = 1/\pi$, and condition 3 because $K$ is odd.
For condition 2, $\abs{K(x - y) - K(x)} = \frac{\abs{y}}{\pi \abs{x}\abs{x - y}} \le \frac{2\abs{y}}{\pi x^2}$ when $\abs{x} \ge 2\abs{y}$, whose integral is $2/\pi$.
So the truncated Hilbert transforms are bounded on $L^p(\R)$ uniformly in $\varepsilon$, which recovers the [[M. Riesz theorem|PJFH51Z48M]].

The cancellation condition 3 is needed.
For $K(x) = \abs{x}^{-n}$, conditions 1 and 2 hold, but $T_\varepsilon f(x)$ grows like $\log(1/\varepsilon)$ for $f$ equal to $1$ near $x$.
The conclusion fails for $p = 1$ and $p = \infty$, as already for the Hilbert transform.

## Explanations

### L1 human

Integrating a function against a kernel of size $\abs{x}^{-n}$ is dangerous, since this kernel is not integrable near $0$ or near infinity.
Suppose the kernel is smooth on average, and its positive and negative values balance on every shell.
The theorem says that the integral then gives an operator that preserves $L^p$ size, for $1 < p < \infty$.
The Hilbert transform and the Riesz transforms are the main examples.

### L2 human

This is the central theorem of the theory of [[singular integral operators|HTMCEARGDD]].
Its method, an $L^2$ bound, the Calderón–Zygmund decomposition and interpolation, also proves the Hörmander–Mikhlin multiplier theorem and the bounds for maximal functions.
It extends to non-convolution operators, the [[Calderón–Zygmund operators|3SCXCW4AH3]], once an $L^2$ bound is known; the [[T(1) theorem|3FBF628XEF]] gives a test for that $L^2$ bound.
