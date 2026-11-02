---
tag: TE3STTNSCK
kind: definition
name: Periodic point
msc: [37C25, 37B02, 37-01]
defines: T75CZ5H47N
uses: [AYVTR2ES5B, R6QVS6P21N]
sources:
  - url: https://en.wikipedia.org/wiki/Periodic_point
    locator: Iterated functions
---

## Definition

Let $X$ be a set, let $f \colon X \to X$ be a map, and let $f^n$ denote the $n$-th [[iterate|AYVTR2ES5B]] of $f$.
A point $x \in X$ is a *periodic point* of $f$ if there is an integer $n \ge 1$ with $f^n(x) = x$.
Such an $n$ is a *period* of $x$.
Equivalently, $x$ is a [[fixed point|R6QVS6P21N]] of $f^n$ for some $n \ge 1$.

## Remarks

If $n$ is a period of $x$, so is every positive multiple of $n$, since $f^{kn}(x) = (f^n)^k(x) = x$.
The orbit $\set{x, f(x), \dots, f^{n-1}(x)}$ of a periodic point is a finite set, called a periodic orbit or cycle.
A point $x$ is *eventually periodic*, or preperiodic, if some $f^m(x)$ with $m \ge 0$ is periodic.

Example: for $f(x) = x^2 - 1$ on $\R$, the point $0$ is periodic with period $2$.
Indeed $f(0) = -1$ and $f(-1) = 0$, so $f^2(0) = 0$.

Non-example: for the same $f$, the point $1$ is not periodic.
One has $f(1) = 0$, after which the orbit alternates between $-1$ and $0$ and never returns to $1$.
So $1$ is eventually periodic but not periodic.
