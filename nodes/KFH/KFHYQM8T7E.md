---
tag: KFHYQM8T7E
kind: statement
role: proposition
name: Jacobi–Anger expansion
msc: [33C10, 42A16]
uses: [CZCMRDWDYW, G12KXDHPPS]
about: [CZCMRDWDYW]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi%E2%80%93Anger_expansion
same_as:
  wikidata: Q1099204
  wikipedia: Jacobi–Anger expansion
---

## Statement

Let $J_n$ denote the [[Bessel function of the first kind|CZCMRDWDYW]] of integer order $n$.
For all $z \in \C$ and $\theta \in \R$,
$$e^{iz \cos\theta} = \sum_{n=-\infty}^{\infty} i^n J_n(z)\, e^{in\theta}, \qquad e^{iz \sin\theta} = \sum_{n=-\infty}^{\infty} J_n(z)\, e^{in\theta},$$
and both series converge absolutely and uniformly in $\theta$.

## Remarks

The generating function of the Bessel functions is $\exp\left( \frac{z}{2} \left( t - \frac{1}{t} \right) \right) = \sum_{n \in \Z} J_n(z)\, t^n$ for $t \ne 0$, obtained by multiplying the series of $e^{zt/2}$ and $e^{-z/(2t)}$.
Putting $t = e^{i\theta}$ gives the second formula, since $\frac{1}{2}(t - t^{-1}) = i\sin\theta$.
Replacing $\theta$ by $\theta + \frac{\pi}{2}$ turns $\sin\theta$ into $\cos\theta$ and gives the first formula.
So the expansion is the [[Fourier series|G12KXDHPPS]] of the periodic function $\theta \mapsto e^{iz\sin\theta}$, and its Fourier coefficients are $J_n(z)$.
Example: at $\theta = 0$ the second formula gives $1 = \sum_{n} J_n(z) = J_0(z) + 2\sum_{k \ge 1} J_{2k}(z)$, using $J_{-n} = (-1)^n J_n$.

## Explanations

### L1 human

A plane wave $e^{iz\cos\theta}$ can be broken up into circular pieces, one for each whole number $n$.
The size of the $n$-th piece is the Bessel function $J_n(z)$.
This is why Bessel functions appear whenever a straight wave meets something round.

### L2 human

Taking real and imaginary parts gives expansions of $\cos(z\sin\theta)$ and $\sin(z\sin\theta)$ used in frequency modulation, where the strengths of the sidebands are Bessel values.
Reading off a Fourier coefficient gives Bessel's integral for $J_n$.
In two-dimensional scattering it expands an incident plane wave in cylindrical waves, the first step of the partial-wave method.
Multiplying two such expansions gives addition theorems for Bessel functions.
