---
tag: 31DQH72ZJP
kind: statement
role: theorem
name: Cauchy integral on Lipschitz curves
msc: [42B20, "30E20", 42A50]
uses: [0AW1E6YTJY, SASP14MA1Z, NSCEBXM7ZM, HTMCEARGDD]
about: [HTMCEARGDD]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_integral_operators_on_closed_curves
---

## Statement

Let $A \colon \R \to \R$ be a function that satisfies a [[Lipschitz condition|0AW1E6YTJY]], and let $\Gamma$ be its graph $\set{x + iA(x) : x \in \R}$ in $\C$.
For $\varepsilon > 0$ and $f$ continuous with compact support on $\R$, let
$$C_\varepsilon f(x) = \frac{1}{\pi i} \int_{\abs{x - y} > \varepsilon} \frac{f(y) \, (1 + iA'(y))}{(y - x) + i(A(y) - A(x))} \, dy, \quad x \in \R.$$
Then there is a constant $C$, depending only on $\norm{A'}_{L^\infty}$, such that
$$\norm{C_\varepsilon f}_{L^2(\R)} \le C \norm{f}_{L^2(\R)}$$
for all $\varepsilon > 0$ and all such $f$.
So the Cauchy integral on $\Gamma$ extends to a bounded operator on the [[Lp space|SASP14MA1Z]] $L^2(\R)$.

## Remarks

The operator $C_\varepsilon f$ is the truncated Cauchy integral $\frac{1}{\pi i}\int \frac{F(\zeta)}{\zeta - z} \, d\zeta$ over $\Gamma$, written in the parameter $x$, with $F(y + iA(y)) = f(y)$ and $z = x + iA(x)$.
A Lipschitz function is differentiable almost everywhere, with $A'$ bounded, so the formula makes sense.
Let $Hf(x) = \frac{1}{\pi} \lim_{\varepsilon \to 0} \int_{\abs{x - y} > \varepsilon} \frac{f(y)}{x - y} \, dy$ be the [[Hilbert transform|NSCEBXM7ZM]].
For $A = 0$ the curve is the real line and the operator is $iH$.
So the theorem generalizes the $L^2$ bound of the Hilbert transform.

The case of small $\norm{A'}_{L^\infty}$ is due to Calderón.
Expanding the kernel in powers of $A(y) - A(x)$ writes the operator as a series of Calderón commutators, and the series converges when $\norm{A'}_{L^\infty}$ is small.
The general case, for every Lipschitz function $A$, was proved by Coifman, McIntosh and Meyer.
Since the kernel is a Calderón–Zygmund kernel, the $L^2$ bound also gives boundedness on $L^p(\R)$ for $1 < p < \infty$.

## Explanations

### L1 human

The Cauchy integral is the basic way to build holomorphic functions from values on a curve.
On a smooth curve it behaves like the Hilbert transform on the line.
The theorem says that the same good behaviour holds on much rougher curves.
They may have corners, as long as they are graphs of Lipschitz functions, such as the graph of $\abs{x}$.

### L2 human

The theorem is a central example of a [[singular integral operator|HTMCEARGDD]] whose kernel is not of convolution type.
It is the starting point for the method of layer potentials on Lipschitz domains, which solves the Dirichlet problem for the Laplacian on domains with rough boundary.
