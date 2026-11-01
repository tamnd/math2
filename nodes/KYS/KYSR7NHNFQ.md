---
tag: KYSR7NHNFQ
kind: statement
role: theorem
name: Hadamard factorization theorem
msc: ["30D20", "30D15"]
uses: [0419794R0T, SHF8Z7GMFX, ACSF58HYDH, 0CEGEASY49, 11VC51YHQJ]
about: [0419794R0T, SHF8Z7GMFX]
sources:
  - url: https://en.wikipedia.org/wiki/Hadamard_factorization_theorem
same_as:
  wikidata: Q117481504
  wikipedia: Hadamard factorization theorem
---

## Statement

Let $f$ be an [[entire function|0419794R0T]] that is not identically zero and has finite [[order|SHF8Z7GMFX]] $\rho$.
Let $p$ be the integer with $p \le \rho < p + 1$.
Let $m \ge 0$ be the order of the [[zero|0CEGEASY49]] of $f$ at $0$.
Let $(a_n)$ be the nonzero zeros of $f$, repeated according to multiplicity.
Let $E_p(z) = (1 - z) \exp(z + z^2/2 + \cdots + z^p/p)$, with $E_0(z) = 1 - z$.
Then $\sum_n \abs{a_n}^{-(p+1)} < \infty$.
Moreover, there is a polynomial $g$ of degree at most $p$ such that
$$f(z) = z^m e^{g(z)} \prod_{n} E_p\!\left(\frac{z}{a_n}\right)$$
for all $z \in \C$, where the product converges uniformly on compact sets.

## Remarks

The proof first bounds the number $n(r)$ of zeros in the disc $\abs{z} \le r$ by [[Jensen's formula|497K99BQ4Y]]: $n(r) = O(r^{\rho + \varepsilon})$ for every $\varepsilon > 0$.
This gives the convergence of $\sum_n \abs{a_n}^{-(p+1)}$, so the [[Weierstrass product|ACSF58HYDH]] with the fixed index $p$ converges.
The quotient of $f$ by $z^m$ times the product is $e^{g}$ with $g$ entire.
Lower bounds for the product away from its zeros show that $g$ is a polynomial of degree at most $\rho$.
For example, $\sin(\pi z)$ has order $1$, so $p = 1$ and $\sin(\pi z) = \pi z \prod_{n \ne 0} (1 - z/n) e^{z/n}$.
The finite order hypothesis is necessary: $f(z) = e^{e^z}$ has no zeros and infinite order, and $f = e^{g}$ with $g(z) = e^z$, which is not a polynomial.

## Explanations

### L1 human

The theorem refines the [[Weierstrass factorization theorem|11VC51YHQJ]] for entire functions that do not grow too fast.
For such a function, all convergence factors can be taken of the same small degree.
The leftover zero-free factor is the exponential of a polynomial, not of an arbitrary entire function.
So the zeros determine the function up to a few constants.

### L2 human

A useful consequence: an entire function of finite order that is not an integer has infinitely many zeros.
Indeed, with finitely many zeros the factorization gives a polynomial times $e^{g}$ with $g$ a polynomial, whose order is an integer.
Another consequence is that an entire function of finite order without zeros is $e^{g}$ with $g$ a polynomial.
The theorem is a basic tool for the Riemann zeta function, through the product formula of the function $\xi$, and for the [[Laguerre–Pólya class|X9SRCEENV3]].
