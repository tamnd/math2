---
tag: X1DB08QJHK
kind: definition
name: Fractional iteration
msc: [39B12, 26A18]
defines: 5M3THA1S6E
uses: [0EPAT51DXQ, AYVTR2ES5B, 0PSKT5W817, 27C6J3YNZY, CPE1ANDDJ0, VTJV7JVJEA, 68SHB7Z721]
sources:
  - url: https://en.wikipedia.org/wiki/Iterated_function
---

## Definition

Let $X$ be a set and let $f \colon X \to X$ be a [[function|0EPAT51DXQ]].
A *fractional iteration* of $f$ is a family $(f^t)_{t \ge 0}$ of functions $f^t \colon X \to X$ such that:

1. $f^0 = \id_X$, the [[identity function|0PSKT5W817]] of $X$.
2. $f^1 = f$.
3. $f^s \circ f^t = f^{s+t}$ for all real $s, t \ge 0$.

## Remarks

Example: on $X = (0, \infty)$, let $f(x) = \frac{x}{1 + x}$ and $f^t(x) = \frac{x}{1 + tx}$.
Clauses 1 and 2 hold by substitution, and clause 3 holds since $f^s(f^t(x)) = \frac{x/(1+tx)}{1 + sx/(1+tx)} = \frac{x}{1 + (s+t)x}$.

Non-example: on $X = \R$, the family $f^t(x) = (1 + t) x$ satisfies clauses 1 and 2 for $f(x) = 2x$, but fails clause 3, since $f^1(f^1(x)) = 4x \ne 3x = f^2(x)$.

Clause 3 with integer $s, t$ forces $f^n$ to be the usual [[iterate|AYVTR2ES5B]], and $f^{1/n}$ is an [[iterative root|27C6J3YNZY]] of order $n$.
In terms of $F(x, t) = f^t(x)$, clause 3 is the [[translation equation|CPE1ANDDJ0]] $F(F(x, t), s) = F(x, s + t)$.
If $\Psi \colon X \to \R$ is a bijective solution of [[Schröder's equation|VTJV7JVJEA]] $\Psi \circ f = \lambda \Psi$ with $\lambda > 0$, then $f^t = \Psi^{-1} \circ (\lambda^t \Psi)$ is a fractional iteration.
If $A \colon X \to \R$ is a bijective solution of the [[Abel equation|68SHB7Z721]] $A \circ f = A + 1$, then $f^t = A^{-1} \circ (A + t)$ is one.
Some authors also call a family indexed by all real $t$, or only by rational $t$, a fractional iteration.
