---
tag: B5ZWZHMD12
kind: definition
name: Differentiation operator p
msc: [44A45, 44A40]
defines: BB15T3J891
uses: [0V1EJCT8G6, 0BYWRWFT4F]
sources:
  - url: https://en.wikipedia.org/wiki/Operational_calculus
---

## Definition

Let $C^1[0, \infty)$ be the space of continuously differentiable functions $f \colon [0, \infty) \to \C$, with the one-sided [[derivative|0V1EJCT8G6]] at $0$.
The *differentiation operator* $p \colon C^1[0, \infty) \to C[0, \infty)$ is $p f = f'$.
Its companion, the integration operator $p^{-1} \colon C[0, \infty) \to C^1[0, \infty)$, is
$$(p^{-1} f)(t) = \int_0^t f(\tau) \, d\tau.$$

## Remarks

The two operators satisfy
$$p \, p^{-1} f = f \quad (f \in C[0, \infty)), \qquad p^{-1} p f = f - f(0) \quad (f \in C^1[0, \infty)).$$
The first identity is the fundamental theorem of calculus: $p^{-1} f$ is the [[antiderivative|0BYWRWFT4F]] of $f$ that vanishes at $0$.
So $p^{-1}$ is a right inverse of $p$ but not a left inverse.

Example: for $f(t) = e^{at}$, $p f = a f$, and $p^{-1} f = (e^{at} - 1)/a$ for $a \ne 0$; then $p \, p^{-1} f = e^{at} = f$.

Non-example of a two-sided inverse: for the constant $f = 1$, $p^{-1} p f = p^{-1} 0 = 0 \ne 1$; the clause $p^{-1} p = \id$ fails exactly because $f(0) \ne 0$.

In the Mikusiński calculus, the integration operator is convolution with the constant $1$, and the corresponding element $s = 1/l$ of the field of operators satisfies $s f = f' + f(0)$, which repairs the defect above.
