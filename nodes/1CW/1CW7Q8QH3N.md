---
tag: 1CW7Q8QH3N
kind: statement
role: theorem
name: Heaviside expansion theorem
msc: [44A10, 44A45]
uses: [0V49JEZW06, 07WBTX1MHA, 030VFEREKG]
about: [07WBTX1MHA]
sources:
  - url: https://en.wikipedia.org/wiki/Operational_calculus
---

## Statement

Let $P$ and $Q$ be polynomials with complex coefficients with $\deg P < \deg Q$.
Suppose that $Q$ has $n = \deg Q$ distinct roots $a_1, \dots, a_n$.
Then $P/Q$ is the [[Laplace transform|0V49JEZW06]], for $\operatorname{Re} s > \max_k \operatorname{Re} a_k$, of the function
$$f(t) = \sum_{k=1}^n \frac{P(a_k)}{Q'(a_k)} \, e^{a_k t}, \qquad t \ge 0.$$

## Remarks

Since the roots are simple, the [[partial fraction decomposition|030VFEREKG]] of $P/Q$ is $\sum_k c_k / (s - a_k)$.
Multiplying by $s - a_k$ and letting $s \to a_k$ gives $c_k = P(a_k) / Q'(a_k)$, because $Q(s)/(s - a_k) \to Q'(a_k)$.
Each term $c_k/(s - a_k)$ is the Laplace transform of $c_k e^{a_k t}$ on $\operatorname{Re} s > \operatorname{Re} a_k$.

Example: $P = 1$, $Q(s) = s^2 + 1$, with roots $\pm i$ and $Q'(s) = 2s$.
The theorem gives $f(t) = \frac{e^{it}}{2i} + \frac{e^{-it}}{-2i} = \sin t$, the [[inverse Laplace transform|07WBTX1MHA]] of $1/(s^2 + 1)$.

In Heaviside's form, the response to a unit step is $\varphi(p) H$ with $\varphi = P/Q$, $\deg P \le \deg Q$ and $Q(0) \ne 0$.
If the roots $a_k$ of $Q$ are simple, the theorem applied to $P(s)/(s Q(s))$ gives, for $t \ge 0$,
$$\varphi(p) H = \frac{P(0)}{Q(0)} + \sum_k \frac{P(a_k)}{a_k Q'(a_k)} e^{a_k t}.$$

The hypothesis of simple roots is needed: $1/s^2$ is the transform of $t$, which is not a combination of exponentials.
For repeated roots, the residue formula gives terms $t^j e^{a_k t}$ instead.

## Explanations

### L1 human

A rational function of $s$ breaks into simple pieces $c/(s - a)$, and each piece is the transform of an exponential $c\,e^{at}$.
The theorem gives a direct recipe for the numbers $c$, without solving a system of equations.
So the inverse transform of a rational function with simple poles can be written down at once.

### L2 human

The coefficient $P(a_k)/Q'(a_k)$ is the residue of $P/Q$ at $a_k$, and the theorem is the special case of the residue form of the inverse Laplace transform, $f(t) = \sum_k \operatorname{Res}_{s = a_k} \left( e^{st} P(s)/Q(s) \right)$.
It is the main tool for solving linear constant-coefficient systems by the [[Heaviside operational calculus|QQ98C2AXZP]] or by the Laplace transform, because their transfer functions are rational.
The exponents $a_k$ are the natural frequencies of the system, and the theorem expresses the response as a superposition of its modes.
