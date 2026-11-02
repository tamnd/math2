---
tag: FE8EYTGMRS
kind: definition
name: Iterative root
msc: [39B12, 26A18]
defines: 27C6J3YNZY
uses: [0EPAT51DXQ, AYVTR2ES5B]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_square_root
---

## Definition

Let $X$ be a set, let $f \colon X \to X$ be a [[function|0EPAT51DXQ]], and let $n \ge 1$ be an integer.
An *iterative root of order $n$* of $f$ is a function $g \colon X \to X$ such that
$$g^n = f,$$
where $g^n = g \circ \cdots \circ g$ is the $n$-th [[iterate|AYVTR2ES5B]] of $g$.

## Remarks

Example: on $X = \R$, the map $g(x) = x + 1$ is an iterative root of order $3$ of $f(x) = x + 3$.
Check: $g^2(x) = x + 2$ and $g^3(x) = x + 3 = f(x)$.

Non-example: $g(x) = 3x$ is not an iterative root of order $3$ of $f(x) = x + 3$, since $g^3(x) = 27x \ne x + 3$.

The roots of order $2$ are the [[functional square roots|E7890PHMGP]].
Roots are rarely unique: both $2x$ and $-2x$ are iterative roots of order $2$ of $4x$.
Some maps have no continuous root of a given order.
If $g \colon \R \to \R$ were continuous with $g^2(x) = -x$, then $g$ would be injective, hence strictly monotone.
Then $g^2$ would be increasing, but $x \mapsto -x$ is decreasing.
For odd $n$ the same map has the root $g(x) = -x$, since $(-1)^n = -1$.
