---
tag: CYT8JNNWXH
kind: statement
role: theorem
name: Pólya's theorem on integer-valued entire functions
msc: ["30D15", "30D20"]
uses: [0419794R0T, 092GEF38YD, 9P8D8YAHQS]
about: [0419794R0T]
sources:
  - url: https://en.wikipedia.org/wiki/Integer-valued_polynomial
---

## Statement

Let $f$ be an [[entire function|0419794R0T]] such that $f(n) \in \Z$ for every integer $n \ge 0$.
Let $M(r)$ be the maximum of $\abs{f(z)}$ on the circle $\abs{z} = r$.
If
$$\limsup_{r \to \infty} \frac{\log M(r)}{r} < \log 2,$$
then $f$ is a polynomial.

## Remarks

The idea of the proof uses the Newton series $f(z) = \sum_{k \ge 0} \Delta^k f(0) \binom{z}{k}$, where $\Delta g(z) = g(z+1) - g(z)$ and $\binom{z}{k}$ is the [[binomial coefficient|092GEF38YD]] polynomial.
The differences $\Delta^k f(0) = \sum_{j=0}^{k} (-1)^{k-j} \binom{k}{j} f(j)$ are integers.
A contour integral estimate shows that the growth bound forces $\Delta^k f(0) \to 0$, so $\Delta^k f(0) = 0$ for all large $k$, and the series is a polynomial.
The constant $\log 2$ is sharp: $f(z) = 2^z = e^{z \log 2}$ takes integer values at the nonnegative integers, is not a polynomial, and has $\log M(r) = r \log 2$.

## Explanations

### L1 human

Polynomials such as $z(z-1)/2$ take integer values at all nonnegative integers.
So does $2^z$, which grows exponentially.
Pólya's theorem says that any entire function with integer values at $0, 1, 2, \dots$ that grows more slowly than $2^z$ must be a polynomial.
So the growth of $2^z$ is the smallest possible for such a function that is not a polynomial.

### L2 human

The condition says that $f$ is of [[exponential type|9P8D8YAHQS]] less than $\log 2$.
The polynomials that the theorem produces are integer-valued polynomials, which are exactly the integer combinations of the polynomials $\binom{z}{k}$.
The theorem started a series of arithmetic results on entire functions.
In these results, integrality conditions on values combined with growth bounds force algebraic behaviour.
