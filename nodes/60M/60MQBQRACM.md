---
tag: 60MQBQRACM
kind: definition
name: Closable operator
msc: [47A05, 47B25]
defines: 3TWMBFQJJ8
uses: [KRJX5RA0PW, VM7B38PA87, 3RCAY97W1E, 0QEAJB91GZ]
sources:
  - url: https://en.wikipedia.org/wiki/Unbounded_operator
    locator: Closed linear operators
---

## Definition

Let $X$ and $Y$ be normed spaces, and let $T$ be an [[unbounded operator|KRJX5RA0PW]] from $X$ to $Y$.
The operator $T$ is *closable* if it has an extension $S \supseteq T$ that is a [[closed operator|VM7B38PA87]].

## Remarks

The following are equivalent.

1. The operator $T$ is closable.
2. The [[closure|0QEAJB91GZ]] of the [[graph|3RCAY97W1E]] $\Gamma(T)$ in $X \times Y$ is the graph of an operator.
3. For every sequence $(x_n)$ in $D(T)$ with $x_n \to 0$ and $T x_n \to y$, one has $y = 0$.

Example: on $C[0, 1]$ with the supremum norm, let $D(T)$ be the space of polynomials and $Tp = p'$.
If $p_n \to 0$ and $p_n' \to g$ uniformly, then $p_n(x) - p_n(0) = \int_0^x p_n'$ gives $0 = \int_0^x g$ for all $x$, so $g = 0$; hence $T$ is closable.

Non-example: on $L^2(0, 1)$, let $D(T) = C[0, 1]$ and $Tf = f(0) \cdot \mathbf{1}$, where $\mathbf{1}$ is the constant function $1$.
The functions $f_n(x) = \max(0, 1 - n x)$ satisfy $f_n \to 0$ in $L^2(0, 1)$ but $T f_n = \mathbf{1}$ for all $n$, so $T$ is not closable.
