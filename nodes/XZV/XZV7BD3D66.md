---
tag: XZV7BD3D66
kind: definition
name: Primitive recursive function
msc: [03D20]
defines: 5NVA2JRHPV
uses: [0MWKJ44V5A, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_recursive_function
---

## Definition

The class of *primitive recursive functions* is the smallest class of [[functions|0EPAT51DXQ]] $f \colon \N^k \to \N$, for $k \ge 0$, with the following properties.

1. It contains the constant function $0$ of arity $0$, and the successor function $S(x) = x + 1$.
2. It contains the projections $P^k_i(x_1, \ldots, x_k) = x_i$ for $1 \le i \le k$.
3. It is closed under composition: if $g \colon \N^m \to \N$ and $h_1, \ldots, h_m \colon \N^k \to \N$ are in the class, so is $\bar x \mapsto g(h_1(\bar x), \ldots, h_m(\bar x))$.
4. It is closed under primitive recursion: if $g \colon \N^k \to \N$ and $h \colon \N^{k+2} \to \N$ are in the class, so is the function $f \colon \N^{k+1} \to \N$ given below.

$$f(0, \bar x) = g(\bar x), \qquad f(y + 1, \bar x) = h(y, f(y, \bar x), \bar x).$$

Here $\N = \set{0, 1, 2, \ldots}$ is the set of [[natural numbers|0MWKJ44V5A]].

## Remarks

Example: addition is primitive recursive.
Take $g = P^1_1$ and $h(y, z, x) = S(P^3_2(y, z, x))$, which are in the class by clauses 1, 2 and 3.
Clause 4 gives $f(0, x) = x$ and $f(y + 1, x) = f(y, x) + 1$, so $f(y, x) = x + y$.
In the same way, multiplication, exponentiation, the factorial and truncated subtraction are primitive recursive.

Non-example: the [[Ackermann function|N470JF7ZJX]] is total and computable but not primitive recursive.
Its diagonal $n \mapsto A(n, n)$ eventually exceeds every unary function in the class.

A set or relation is primitive recursive when its characteristic function is.
