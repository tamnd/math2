---
tag: S1WS18QEGJ
kind: example
name: Quintic equation
msc: ["12E12", 12F10]
illustrates: [163A2WQQJX, 4CMPPTSJNP]
uses: [02BPKD7TMD, 0194DY35BG, 00KAFBR32E, J7YS0DA3HQ, 0J53NE674D, VHCWCFA3MX]
sources:
  - url: https://en.wikipedia.org/wiki/Quintic_function
---

## Example

A quintic equation is an equation $ax^5 + bx^4 + cx^3 + dx^2 + ex + g = 0$ with $a \ne 0$.
Consider the quintic $f(x) = x^5 - 4x + 2$ over $\Q$.

1. $f$ is irreducible over $\Q$ by [[Eisenstein's criterion|02BPKD7TMD]] at $2$, as $2$ divides $-4$ and $2$ but not $1$, and $4$ does not divide $2$.
2. $f(-2) = -22$, $f(0) = 2$, $f(1) = -1$ and $f(2) = 26$, so by the [[intermediate value theorem|00KAFBR32E]] $f$ has at least three real roots.
3. $f'(x) = 5x^4 - 4$ has exactly two real zeros, so by [[Rolle's theorem|0194DY35BG]] $f$ has at most three real roots.
4. Hence $f$ has exactly three real roots and two nonreal roots.

By the [[theorem on prime degree polynomials with two nonreal roots|4CMPPTSJNP]], the Galois group of $f$ over $\Q$ is $S_5$.
Since [[$S_5$ is not solvable|0J53NE674D]], [[Galois' theorem on solvability|VHCWCFA3MX]] shows that $f$ is not [[solvable by radicals|J7YS0DA3HQ]].
By contrast, $x^5 - 2$ is solvable by radicals: its roots are $\sqrt[5]{2}\, \zeta^k$, with $\zeta = e^{2\pi i/5}$ and $k = 0, \dots, 4$.

## Explanations

### L1 human

The equation $x^5 - 4x + 2 = 0$ has five complex solutions, and they can be computed to any accuracy.
But none of them can be written using only whole numbers, arithmetic and $n$-th roots.
This concrete equation shows that the [[Abel–Ruffini theorem|163A2WQQJX]] is about specific equations, not only about a general formula.
