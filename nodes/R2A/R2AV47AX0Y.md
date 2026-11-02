---
tag: R2AV47AX0Y
kind: definition
name: Bernstein–Sato polynomial
msc: [14F10, 32S40, 32C38]
defines: 7M5P2A0BZ6
uses: [0SDC934R52, 98QE7KY55W]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein%E2%80%93Sato_polynomial
---

## Definition

Let $f \in \C[x_1, \dots, x_n]$ be a nonzero [[polynomial|0SDC934R52]].
Let $D_n = \C[x_1, \dots, x_n]\langle \partial_1, \dots, \partial_n \rangle$ be the [[Weyl algebra|98QE7KY55W]] of polynomial differential operators.
Let $D_n[s]$ be the ring of polynomials in a new central variable $s$ with coefficients in $D_n$.
The operators of $D_n[s]$ act on expressions $g \, f^{s}$ with $g$ in $\C[x, s, 1/f]$ by the usual rules, with $\partial_i (f^s) = s \, (\partial_i f) \, f^{s-1}$.
The set of polynomials $b(s) \in \C[s]$ for which there is $P(s) \in D_n[s]$ with
$$P(s) \, f^{s+1} = b(s) \, f^s$$
is an ideal of $\C[s]$.
The *Bernstein–Sato polynomial* $b_f(s)$ is the monic generator of this ideal.

## Remarks

Bernstein proved that this ideal is nonzero, so $b_f$ exists.
For a nonconstant $f$, $s + 1$ divides $b_f(s)$, as one sees by setting $s = -1$.

Example: $f = x_1^2 + \cdots + x_n^2$ and $P = \Delta = \partial_1^2 + \cdots + \partial_n^2$.
One has $\partial_i (f^{s+1}) = 2 (s + 1) x_i f^s$, and then
$$\Delta (f^{s+1}) = 2(s+1) \left( n f^s + 2s \sum_i x_i^2 f^{s-1} \right) = 4 (s + 1) \left( s + \tfrac{n}{2} \right) f^s.$$
So $(s+1)(s + n/2)$ lies in the ideal; it is in fact $b_f(s)$.

Non-example: for $f = x_1$, the polynomial $(s + 1)(s + 2)$ lies in the ideal, with $P = (s + 2) \partial_1$, but it is not $b_f$.
It is not of least degree, since $\partial_1 (x_1^{s+1}) = (s+1) x_1^s$ gives $b_f(s) = s + 1$.

The same definition works for a germ of holomorphic function, with the ring of differential operators with convergent power series coefficients; this gives the local $b$-function at a point.
