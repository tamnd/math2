---
tag: 11VC51YHQJ
kind: statement
role: theorem
name: Weierstrass factorization theorem
msc: ["30D20", "30D10"]
uses: [0419794R0T, 0CEGEASY49, ACSF58HYDH, 0RMVS7RXZX]
about: [0419794R0T, ACSF58HYDH]
sources:
  - url: https://en.wikipedia.org/wiki/Weierstrass_factorization_theorem
same_as:
  wikidata: Q1330788
  wikipedia: Weierstrass factorization theorem
---

## Statement

For an integer $p \ge 0$, let $E_p$ be the elementary factor
$$E_0(z) = 1 - z, \qquad E_p(z) = (1 - z) \exp\left(z + \frac{z^2}{2} + \cdots + \frac{z^p}{p}\right) \quad (p \ge 1).$$

1. Let $(a_n)$ be a finite or infinite sequence of nonzero complex numbers with $\abs{a_n} \to \infty$ if it is infinite. Then there is an [[entire function|0419794R0T]] whose [[zeros|0CEGEASY49]] are exactly the points $a_n$. The multiplicity of each zero is the number of times it occurs in the sequence.
2. Let $f$ be an entire function that is not identically zero. Let $m \ge 0$ be the order of the zero of $f$ at $0$. Let $(a_n)$ be the nonzero zeros of $f$, repeated according to multiplicity. Then there are an entire function $g$ and integers $p_n \ge 0$ such that
$$f(z) = z^m e^{g(z)} \prod_{n} E_{p_n}\!\left(\frac{z}{a_n}\right),$$
where the product converges uniformly on compact subsets of $\C$.

## Remarks

The key estimate is $\abs{1 - E_p(z)} \le \abs{z}^{p+1}$ for $\abs{z} \le 1$.
Choose the $p_n$ so that $\sum_n (r / \abs{a_n})^{p_n + 1} < \infty$ for every $r > 0$, for example $p_n = n - 1$.
Then the [[Weierstrass product|ACSF58HYDH]] converges and has the prescribed zeros.
For part 2, the quotient of $f$ by $z^m$ times this product is entire and has no zeros.
So it is $e^{g}$ for an entire $g$, because $\C$ is simply connected.
A classical example is [[Euler's sine product|DQEHD56649]] $\sin(\pi z) = \pi z \prod_{n \ge 1} (1 - z^2/n^2)$.
The convergence factors are needed: for $a_n = n$ the product $\prod_n (1 - z/n)$ diverges, while $\prod_n (1 - z/n) e^{z/n}$ converges.

## Explanations

### L1 human

A polynomial is determined, up to a constant factor, by its roots: it is a constant times a product of factors $z - a$.
The theorem extends this to entire functions, which can have infinitely many zeros.
The plain factors $1 - z/a_n$ may give a product that does not converge, so each factor gets an exponential correction that is close to $1$ near $0$.
What is left after removing all zeros is a function without zeros, which is the exponential of an entire function.

### L2 human

Part 1 shows that any sequence tending to infinity is the zero set of some entire function.
As a consequence, every [[meromorphic function|0NSD1TPHR0]] on $\C$ is a quotient of two entire functions: multiply it by an entire function with zeros at its poles.
The theorem leaves $g$ and the $p_n$ very free.
For functions of finite order the [[Hadamard factorization theorem|KYSR7NHNFQ]] makes both choices precise.
The companion result for poles and principal parts is [[Mittag-Leffler's theorem|X4R2GY1F6J]].
