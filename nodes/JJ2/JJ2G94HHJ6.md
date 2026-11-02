---
tag: JJ2G94HHJ6
kind: definition
name: Calderón–Zygmund operator
msc: [42B20, 47G10]
defines: 3SCXCW4AH3
uses: [78N6AXP9VV, SASP14MA1Z, HTMCEARGDD]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_integral
---

## Definition

Let $n \ge 1$.
A *Calderón–Zygmund operator* is a linear operator $T \colon L^2(\R^n) \to L^2(\R^n)$ such that:

1. $T$ is bounded on the [[$L^2$ space|SASP14MA1Z]], that is $\norm{Tf}_{L^2} \le C\norm{f}_{L^2}$ for some constant $C$ and all $f \in L^2(\R^n)$;
2. there is a [[Calderón–Zygmund kernel|78N6AXP9VV]] $K$ such that, for every $f \in L^2(\R^n)$ with compact support,
$$Tf(x) = \int_{\R^n} K(x, y) f(y) \, dy \quad \text{for almost every } x \notin \operatorname{supp} f.$$

## Remarks

Example: the Hilbert transform $H$ on $\R$ is a Calderón–Zygmund operator.
It is bounded on $L^2(\R)$ with norm $1$, since its multiplier $-i\sgn\xi$ has modulus $1$.
For $x$ outside the support of $f$, the principal value is an ordinary integral, so $Hf(x) = \int \frac{f(y)}{\pi(x - y)} \, dy$, and $\frac{1}{\pi(x - y)}$ is a Calderón–Zygmund kernel.

Non-example: on $\R$, let $Tf = f * \mathbf{1}_{[0, 1]}$, so $Tf(x) = \int \mathbf{1}_{[0, 1]}(x - y) f(y) \, dy$.
It is bounded on $L^2(\R)$ by Young's inequality, so clause 1 holds.
Clause 2 fails, because its kernel $\mathbf{1}_{[0, 1]}(x - y)$ jumps at $x - y = 1$.
For $y = 0$, $x = 1 - \eta$ and $x' = 1 + \eta$, the difference of the kernel values is $1$, while the bound $A(2\eta)^\delta (1 - \eta)^{-1-\delta}$ tends to $0$ as $\eta \to 0$.

The kernel does not determine the operator: the identity and the zero operator both have kernel $0$ off the diagonal.
Clause 2 is only required off the support of $f$, since near the diagonal the integral need not converge absolutely.
The [[singular integral operators|HTMCEARGDD]] with smooth mean-zero angular part are Calderón–Zygmund operators.
