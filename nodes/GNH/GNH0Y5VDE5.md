---
tag: GNH0Y5VDE5
kind: statement
role: proposition
name: Reduction of a first-kind Volterra equation to the second kind
msc: [45D05]
uses: [H6ZGEDM4VV, ATPSAHYG7C, WG4GVC9HR8]
about: [H6ZGEDM4VV]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_integral_equation
---

## Statement

Let $a < b$, let $\Delta = \set{(t, s) : a \le s \le t \le b}$, and let $K \colon \Delta \to \C$ be continuous, with continuous partial derivative $\partial K / \partial t$ on $\Delta$ and $K(t, t) \ne 0$ for all $t \in [a, b]$.
Let $f \colon [a, b] \to \C$ be continuously differentiable.
Let $x \colon [a, b] \to \C$ be continuous.
Consider the [[Volterra equation of the first kind|H6ZGEDM4VV]]
$$\int_a^t K(t, s) \, x(s) \, ds = f(t), \quad t \in [a, b].$$
Then $x$ solves it if and only if $f(a) = 0$ and $x$ solves the [[Volterra equation of the second kind|ATPSAHYG7C]]
$$x(t) = \frac{f'(t)}{K(t, t)} - \int_a^t \frac{1}{K(t, t)} \frac{\partial K}{\partial t}(t, s) \, x(s) \, ds, \quad t \in [a, b].$$
Consequently, if $f(a) = 0$, the first-kind equation has exactly one continuous solution, and if $f(a) \ne 0$ it has none.

## Remarks

Proof idea: by the Leibniz rule, the derivative of $\int_a^t K(t, s) \, x(s) \, ds$ is $K(t, t) \, x(t) + \int_a^t \partial_t K(t, s) \, x(s) \, ds$.
So differentiating the first-kind equation gives the second-kind equation after division by $K(t, t)$.
Conversely, a solution of the second-kind equation makes both sides of the first-kind equation have the same derivative, and both vanish at $t = a$ when $f(a) = 0$.
The new kernel $-\partial_t K(t, s) / K(t, t)$ is continuous, so [[unique solvability|WG4GVC9HR8]] applies.
Example: $\int_0^t e^{t - s} x(s) \, ds = t$ gives $x(t) = 1 - \int_0^t e^{t - s} x(s) \, ds = 1 - t$, and indeed $\int_0^t e^{t - s} (1 - s) \, ds = t$.
The hypothesis $K(t, t) \ne 0$ matters: for $K(t, s) = t - s$, differentiation gives another first-kind equation $\int_a^t x(s) \, ds = f'(t)$, and one needs a second differentiation.
For the weakly singular kernel $(t - s)^{-1/2}$ the reduction does not apply, and one uses the [[Abel inversion formula|TDMXFY06A2]] instead.

## Explanations

### L1 human

An equation of the first kind hides the unknown inside an integral.
Differentiating with respect to $t$ brings it out, because the derivative of an integral with variable upper limit contains the integrand at that limit.
If the kernel does not vanish on the diagonal, one can divide and obtain an equation of the second kind, which is well understood.

### L2 human

The reduction shows that a first-kind Volterra equation with a good kernel is about as hard as one differentiation.
The price is that the data $f$ must be differentiable, and errors in $f$ are amplified by the derivative, which is the source of ill-posedness in practice.
When $K(t, t) = 0$ but $\partial_t K(t, t) \ne 0$, differentiating twice gives the same kind of reduction, under the corresponding smoothness assumptions and with the conditions $f(a) = f'(a) = 0$.
