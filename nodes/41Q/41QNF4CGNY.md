---
tag: 41QNF4CGNY
kind: problem
name: Numerical inversion of the Laplace transform
msc: [65R10, 44A10, 65R32]
uses: [05XT5AVJBK, 07WBTX1MHA, TRTN840ZB0, 5KNAXNHRY6, D6QKPBS2EN, WAMRHWW82R]
about: [07WBTX1MHA, 0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_Laplace_transform
history:
  posed_by: "Emil L. Post"
  first_stated: "1930"
  notes: "Post's 1930 real inversion formula is the earliest well-documented basis for approximate inversion from values on the real axis; the attribution is to this earliest known formulation. Dedicated numerical methods followed, notably the 1966 book of Bellman, Kalaba and Lockett and the methods of Gaver and Weeks."
---

## Problem

Let $f \colon [0, \infty) \to \R$ be a function whose [[Laplace transform|05XT5AVJBK]]
$$F(s) = \int_0^\infty f(t) e^{-s t} \, dt$$
converges for $\operatorname{Re} s > \sigma_0$, for some real $\sigma_0$.
Suppose that $F$ can be evaluated, exactly or with small errors, at finitely many points $s$ with $\operatorname{Re} s > \sigma_0$.
In a variant of the problem, only real points $s$ are allowed.
Give an algorithm that, for a given $t > 0$, computes an approximation of $f(t)$ from finitely many values of $F$, with control of the error.

## Remarks

This is the numerical form of the [[inverse Laplace transform|07WBTX1MHA]].
It has no single solution: there are many methods, and each works well for some classes of functions $F$.
Methods that use complex values of $F$ approximate the [[Bromwich integral|5KNAXNHRY6]].
Examples are Talbot's method, which deforms the contour to the left, and methods based on a Fourier series in $t$ on a finite interval.
Methods that use only real values of $F$ build on [[Post's inversion formula|D6QKPBS2EN]] and accelerate its slow convergence; the Gaver–Stehfest method is of this type.
Another approach, due to Weeks, expands $f$ in a series of [[Laguerre polynomials|WAMRHWW82R]] times an exponential factor and computes the coefficients from values of $F$ on a vertical line.
Inversion from real values only is unstable, because of the [[ill-posedness of real Laplace inversion|TRTN840ZB0]]: very different functions $f$ can have transforms that differ very little on $(0, \infty)$.
So real-axis methods need high-precision arithmetic, and no method works uniformly well for all $f$, in particular for $f$ with jumps or fast oscillations.

## Explanations

### L1 human

In engineering one often solves a problem in the Laplace domain and gets a formula for $F(s)$ but no closed form for its inverse.
Numerical inversion means getting numbers $f(t)$ back from such a formula on a computer.
For example, for $F(s) = 1/(s + 1)$ the answer is $f(t) = e^{-t}$, and a good method should reproduce this value at, say, $t = 1$.
The task is harder than it looks, because small errors in $F$ can turn into large errors in $f$.
