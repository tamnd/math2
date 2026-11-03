---
tag: CT69XTRW2K
kind: statement
role: theorem
name: BCH bound
msc: [94B15, 94B65]
uses: [E04GGZ1Q91, M2X88AXM17, 0EHM5ZP5QH, Q3JWBZ7EFY]
about: [E04GGZ1Q91, YY5ZM93GBY]
sources:
  - url: https://en.wikipedia.org/wiki/BCH_code
---

## Statement

Let $q$ be a prime power and let $n \ge 2$ with $\gcd(n, q) = 1$.
Let $\beta$ be a [[primitive $n$-th root of unity|0EHM5ZP5QH]] in an extension field of $\F_q$.
Let $C$ be a [[cyclic code|E04GGZ1Q91]] of length $n$ over $\F_q$, with codewords written as polynomials $c(x) = c_0 + c_1 x + \cdots + c_{n-1} x^{n-1}$.
Suppose that there are integers $b \ge 0$ and $\delta \ge 2$ such that
$$c(\beta^{b}) = c(\beta^{b+1}) = \cdots = c(\beta^{b+\delta-2}) = 0 \quad \text{for every } c \in C.$$
Then every nonzero codeword of $C$ has at least $\delta$ nonzero coordinates, so the [[minimum distance|M2X88AXM17]] of $C$ is at least $\delta$.

## Remarks

Suppose a nonzero codeword $c$ has its nonzero coordinates among the positions $j_1 < \cdots < j_w$ with $w \le \delta - 1$.
The $w$ conditions $c(\beta^{b+i}) = 0$ for $0 \le i \le w - 1$ form a square linear system in $c_{j_1}, \dots, c_{j_w}$ with matrix $\big(\beta^{(b+i) j_k}\big)_{i,k}$.
After taking out the factor $\beta^{b j_k}$ from column $k$, this is a [[Vandermonde matrix|Q3JWBZ7EFY]] in the distinct elements $\beta^{j_1}, \dots, \beta^{j_w}$, so it is invertible, and $c = 0$, a contradiction.

The bound is the reason why a [[BCH code|YY5ZM93GBY]] of designed distance $\delta$ has minimum distance at least $\delta$.
The roots must be consecutive powers: it is the run of exponents $b, \dots, b + \delta - 2$ that produces the Vandermonde matrix.
The bound need not be sharp.
For $n = 23$, $q = 2$ and a suitable choice of $\beta$, the binary Golay code has the roots $\beta^i$ for $i$ in $\set{1, 2, 3, 4, 6, 8, 9, 12, 13, 16, 18}$.
The longest run is $1, 2, 3, 4$, so the bound gives $d \ge 5$, while the true minimum distance is $7$.

## Explanations

### L1 human

A codeword of a cyclic code can be viewed as a polynomial.
If all codewords vanish at several consecutive powers of a root of unity, then no nonzero codeword can have only a few nonzero coefficients.
The number of consecutive roots, plus one, is a guaranteed lower bound on the distance between codewords.

### L2 human

The bound turns a question about weights of codewords, which is hard in general, into a question about roots, which one controls when choosing the generator polynomial.
It is the design principle of BCH and [[Reed–Solomon codes|5VBWJ7EFTX]].
The proof is the invertibility of a Vandermonde matrix.
Several refinements exist, for codes whose roots form several runs, but the basic form above is the one used to design codes.
