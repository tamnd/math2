---
tag: TRKEGEZGGZ
kind: definition
name: Jet
msc: [58A20]
defines: 1QE0Z0756D
uses: [F45VQ47GPV, 0V33BNKZ9S, 09EGC6F8PT, 0ZZ4RHTR9X, 7SWSRGDT4A]
sources:
  - url: https://en.wikipedia.org/wiki/Jet_(mathematics)
---

## Definition

Let $M$ and $N$ be [[smooth manifolds|F45VQ47GPV]], let $p \in M$ and let $k \ge 0$ be an integer.
Let $f$ and $g$ be [[smooth maps|0V33BNKZ9S]] into $N$, each defined on an open neighbourhood of $p$ in $M$.
Then $f$ and $g$ have the *same $k$-jet at $p$* if both conditions hold.

1. $f(p) = g(p)$.
2. Take a chart $x$ of $M$ around $p$ and a chart $y$ of $N$ around $f(p)$. Then $y \circ f \circ x^{-1}$ and $y \circ g \circ x^{-1}$ have equal [[partial derivatives|09EGC6F8PT]] of every order $1, \dots, k$ at $x(p)$.

This is an equivalence relation.
The *$k$-jet of $f$ at $p$*, written $j^k_p f$, is the equivalence class of $f$.
The set of all $k$-jets at $p$ of maps from $M$ to $N$ is written $J^k_p(M, N)$.

## Remarks

Condition 2 does not depend on the charts, by the chain rule.
Indeed, the derivatives up to order $k$ of a composite depend only on those of its factors.
The jet $j^k_p f$ depends only on the [[germ|7SWSRGDT4A]] of $f$ at $p$.
For $M = \R^n$ and $N = \R$, the $k$-jet of $f$ at $p$ is the same data as its [[Taylor polynomial|0ZZ4RHTR9X]] of degree $k$ at $p$.

Example: on $\R$, $f(x) = \sin x$ and $g(x) = x$ have the same $2$-jet at $0$.
Indeed $f(0) = g(0) = 0$, $f'(0) = g'(0) = 1$ and $f''(0) = g''(0) = 0$.

Non-example: $f(x) = e^x$ and $g(x) = 1 + x$ have the same $1$-jet at $0$ but not the same $2$-jet.
Condition 2 fails for order $2$, since $f''(0) = 1$ and $g''(0) = 0$.
