---
tag: ENXCWPTG92
kind: statement
role: theorem
name: Siegel's theorem on meromorphic function fields
msc: [32J10, 32A20]
uses: [JSGWAN2RJV, W6FTSF57T1, D7TR0YWR9H]
about: [F0GF0JEZTG]
sources:
  - url: https://en.wikipedia.org/wiki/Moishezon_manifold
---

## Statement

Let $X$ be a compact, connected [[complex manifold|JSGWAN2RJV]] of dimension $n$, and let $\mathcal{M}(X)$ be its field of [[meromorphic functions|W6FTSF57T1]].
Then the [[transcendence degree|D7TR0YWR9H]] of $\mathcal{M}(X)$ over $\C$ is at most $n$.
Equivalently, any $n + 1$ meromorphic functions on $X$ satisfy a nonzero polynomial relation with complex coefficients.

## Remarks

Proof idea: let $f_1, \ldots, f_{n+1}$ be meromorphic on $X$ and consider all polynomials of degree at most $k$ in them.
These form a space of dimension of order $k^{n+1}$.
Cover $X$ by finitely many polydiscs and use a Schwarz lemma.
This shows that such a polynomial expression vanishing to high order at finitely many chosen points vanishes identically.
The number of conditions needed grows only like $k^n$.
For large $k$ some nonzero polynomial in the $f_i$ is therefore identically zero.

Example: on a compact Riemann surface ($n = 1$), any two meromorphic functions are algebraically dependent; for $\hat\C$, $f$ and $g$ are both rational functions of $z$.

Compactness is necessary: on the non-compact manifold $\C$, the meromorphic functions $z$ and $e^z$ are algebraically independent, so the transcendence degree is at least $2 > 1$.

In terms of the [[algebraic dimension|F0GF0JEZTG]], the theorem says $a(X) \le \dim X$.
The field $\mathcal{M}(X)$ is moreover finitely generated over $\C$, so it is the function field of an algebraic variety of dimension $a(X)$.

## Explanations

### L1 human

On a compact complex manifold of dimension $n$ there cannot be more than $n$ independent meromorphic functions.
Any $n + 1$ of them are tied together by a polynomial equation, just as $x$ and $y$ are tied by $x^2 + y^2 = 1$ on a circle.
This mirrors algebraic geometry, where an $n$-dimensional variety has a function field of transcendence degree $n$.

### L2 human

The theorem makes the [[algebraic dimension|F0GF0JEZTG]] a number between $0$ and $\dim X$, and the case of equality defines [[Moishezon manifolds|8ZW9P9JRQD]].
It shows that compact complex manifolds behave like algebraic varieties as far as their meromorphic functions go, even when they are far from algebraic.
The proof uses only local estimates and compactness, in the spirit of the Schwarz lemma.
