---
tag: K6EV57QFYG
kind: statement
role: theorem
name: Strang splitting
msc: [65L06, 65M22, 65F60]
uses: [020M04FN1H, KH7EPKDCH3]
about: [020M04FN1H]
sources:
  - url: https://en.wikipedia.org/wiki/Strang_splitting
---

## Statement

Let $A$ and $B$ be complex $d \times d$ matrices and let $e^{M}$ denote the [[matrix exponential|020M04FN1H]].

1. As $h \to 0$,
$$e^{hA/2}\, e^{hB}\, e^{hA/2} - e^{h(A + B)} = O(h^3).$$
2. For each $t > 0$, as $n \to \infty$,
$$\left( e^{tA/(2n)}\, e^{tB/n}\, e^{tA/(2n)} \right)^n - e^{t(A + B)} = O(n^{-2}).$$

## Remarks

For clause 1, expand both sides in powers of $h$: the terms of order $0$, $1$ and $2$ agree, because the symmetric product gives $\frac{h^2}{2}\left(\frac{A^2}{4} + \frac{A^2}{4} + B^2 + AB + BA + \frac{A^2}{2}\right) = \frac{h^2}{2}(A + B)^2$.
For clause 2, write the difference of $n$-th powers as a telescoping sum of $n$ terms.
Each term is a local error $O(n^{-3})$ multiplied by matrices of norm at most $e^{t(\norm{A} + \norm{B})}$.
The [[Lie–Trotter product formula|KH7EPKDCH3]] uses $e^{tA/n} e^{tB/n}$ instead, and its error is only $O(n^{-1})$; the symmetric arrangement gains one order.
If $AB = BA$, both splittings are exact.
In applications, $e^{hA}$ and $e^{hB}$ are replaced by the flows $\varphi^A$ and $\varphi^B$ of $u' = A(u)$ and $u' = B(u)$ for nonlinear operators.
The composition $\varphi^A_{h/2} \circ \varphi^B_h \circ \varphi^A_{h/2}$ is still a method of order $2$ for smooth problems.

## Explanations

### L1 human

Some evolution equations are a sum of two parts, each easy to solve alone.
Strang splitting advances the first part half a step, the second part a full step, and the first part another half step.
Doing the halves on both sides makes the error much smaller than doing one part after the other.

### L2 human

Strang splitting is used for reaction-diffusion equations, for the Schrödinger equation (kinetic and potential parts, solved by FFT and pointwise), and for advection in several dimensions.
Consecutive half steps of $A$ merge, so the cost is nearly that of the first-order Lie–Trotter splitting.
The leapfrog method for Hamiltonian systems is the Strang splitting of the kinetic and potential flows.
