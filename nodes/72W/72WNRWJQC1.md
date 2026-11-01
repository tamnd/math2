---
tag: 72WNRWJQC1
kind: statement
role: theorem
name: Explicit formula
msc: [11M26, 11N05]
uses: [B8AKSVBE5Z, 1XWBY4N0VT, 0NK8JTE1NN, 04DXAFN2ES]
about: [B8AKSVBE5Z, 1XWBY4N0VT]
sources:
  - url: https://en.wikipedia.org/wiki/Explicit_formulae_for_L-functions
---

## Statement

Let $\psi$ be the second [[Chebyshev function|B8AKSVBE5Z]] and $\zeta$ the [[Riemann zeta function|1XWBY4N0VT]].
For $x > 1$, let $\psi_0(x) = \psi(x)$ if $x$ is not a prime power, and $\psi_0(x) = \psi(x) - \frac{1}{2} \log p$ if $x = p^k$ with $p$ prime and $k \ge 1$.
Let $\rho$ run over the nontrivial zeros of $\zeta$, those with $0 < \operatorname{Re} \rho < 1$, each counted with its multiplicity.
Then
$$\psi_0(x) = x - \lim_{T \to \infty} \sum_{\abs{\operatorname{Im} \rho} < T} \frac{x^{\rho}}{\rho} - \log(2\pi) - \frac{1}{2} \log\!\left(1 - x^{-2}\right).$$

## Remarks

This is the explicit formula of Riemann and von Mangoldt.
The proof starts from Perron's formula: for $c > 1$,
$$\psi_0(x) = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} \left(-\frac{\zeta'(s)}{\zeta(s)}\right) \frac{x^s}{s} \, ds,$$
because $-\zeta'(s)/\zeta(s) = \sum_n \Lambda(n) n^{-s}$ with the [[von Mangoldt function|0NK8JTE1NN]] $\Lambda$.
Moving the line of integration to the left picks up residues.
The pole at $s = 1$ gives $x$, and each nontrivial zero gives $-x^\rho/\rho$.
The point $s = 0$ gives $-\zeta'(0)/\zeta(0) = -\log(2\pi)$.
Each trivial zero $-2n$ gives $x^{-2n}/(2n)$, and these terms add up to $-\frac{1}{2}\log(1 - x^{-2})$.
The sum over zeros converges only conditionally, so the order of summation matters.
Heuristically, the [[prime number theorem|0EHBY5Y84N]] $\psi(x) \sim x$ reflects that each term $x^\rho/\rho$ is $o(x)$, since $\operatorname{Re} \rho < 1$.
A rigorous proof along these lines also needs a zero-free region to control the whole sum.

## Explanations

### L1 human

The formula writes a prime-counting function exactly as a main term $x$ plus a sum of waves, one for each zero of the zeta function.
The real part of a zero gives the size of its wave, and the imaginary part gives its frequency.
This is why the zeros of zeta control the distribution of the primes.

### L2 human

Under the [[Riemann hypothesis|VCGF9YR36X]] each term has size $\abs{x^\rho} = \sqrt{x}$, and a truncated form of the formula gives $\psi(x) = x + O(\sqrt{x} \log^2 x)$.
Weil generalized the formula to a symmetric identity between a sum over the zeros of an L-function and a sum over prime powers, for a class of test functions.
Similar formulas hold for [[Dirichlet L-functions|9D2Z543EJQ]], and they give the distribution of primes in arithmetic progressions.
