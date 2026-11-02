---
tag: 9F6B05QAWH
kind: example
name: Multiplication operator
msc: [47B38, 47B15]
illustrates: [X71XRPJR7D]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplication_operator
---

## Example

Let $(\Omega, \mu)$ be a $\sigma$-finite measure space and let $\varphi \colon \Omega \to \C$ be an essentially bounded measurable function.
The *multiplication operator* $M_\varphi$ on the [[Lebesgue space|SASP14MA1Z]] $L^2(\Omega, \mu)$ is
$$(M_\varphi f)(x) = \varphi(x) f(x).$$

Check of the main properties:

1. $M_\varphi$ is bounded with $\norm{M_\varphi} = \norm{\varphi}_\infty$, since $\int \abs{\varphi f}^2 \, d\mu \le \norm{\varphi}_\infty^2 \int \abs{f}^2 \, d\mu$, and $\sigma$-finiteness gives sets of finite positive measure on which $\abs{\varphi}$ is close to $\norm{\varphi}_\infty$.
2. Its adjoint is $M_{\bar\varphi}$, because $\int \varphi f \bar g \, d\mu = \int f \, \overline{\bar\varphi g} \, d\mu$.
3. It is a normal operator, since $M_\varphi M_{\bar\varphi} = M_{\abs{\varphi}^2} = M_{\bar\varphi} M_\varphi$.
4. Its [[spectrum|BMKATJ802A]] is the essential range of $\varphi$.

A concrete case: on $L^2[0, 1]$ with Lebesgue measure, take $\varphi(x) = x$.
Then $M_\varphi$ is self-adjoint and positive, its spectrum is $[0, 1]$, and it has no eigenvalues: $x f(x) = \lambda f(x)$ almost everywhere forces $f = 0$ almost everywhere.

## Remarks

The spectral theorem for bounded normal operators says that every bounded normal operator on a separable Hilbert space is unitarily equivalent to a multiplication operator of this form.
So multiplication operators are, up to unitary equivalence, all the normal operators.

## Explanations

### L1 human

A multiplication operator multiplies every function by one fixed function $\varphi$.
It is the infinite-dimensional version of a diagonal matrix, with the values of $\varphi$ playing the role of the diagonal entries.
Multiplying by $x$ on $[0, 1]$ has a whole interval as its spectrum, yet no function is an eigenvector, which shows how the spectrum can differ from the set of eigenvalues.
