---
tag: DA3CQJ5MJ6
kind: concept
name: Lagrange basis polynomials
msc: [41A05, 65D05]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange_polynomial
---

## Summary

The Lagrange basis polynomials of distinct nodes $x_0, \dots, x_n$ are $n + 1$ polynomials of degree $n$.
Each one equals $1$ at its own node and $0$ at the other nodes.
They form a basis of the polynomials of degree at most $n$.
In this basis the coordinates of a polynomial are its values at the nodes.
So the [[Lagrange polynomial|Y7KSGE97GK]] of given data is simply the sum of the basis polynomials weighted by the data values.

## Explanations

### L1 human

Think of each basis polynomial as a switch attached to one node: it is on, with value $1$, at its node and off, with value $0$, at all the others.
To get a polynomial with prescribed values, turn on each switch with the strength you want and add them up.
For the nodes $0$ and $1$ the two basis polynomials are $1 - x$ and $x$.
Then the line with value $a$ at $0$ and $b$ at $1$ is $a(1 - x) + bx$.
The [[definition|ZCVB4ZQ0SA]] gives the general formula.
