---
tag: NY6FVCX61P
kind: definition
name: Closed operator
msc: [47A05, 47B25]
defines: VM7B38PA87
uses: [KRJX5RA0PW, 3RCAY97W1E, 0ZCK8DQYN1, GXM8BX8YM7]
sources:
  - url: https://en.wikipedia.org/wiki/Closed_linear_operator
---

## Definition

Let $X$ and $Y$ be normed spaces, and let $T$ be an [[unbounded operator|KRJX5RA0PW]] from $X$ to $Y$ with domain $D(T)$.
The operator $T$ is *closed* if its [[graph|3RCAY97W1E]] $\Gamma(T)$ is a [[closed subset|0ZCK8DQYN1]] of $X \times Y$.

## Remarks

Equivalently, $T$ is closed when, for every sequence $(x_n)$ in $D(T)$ with $x_n \to x$ in $X$ and $T x_n \to y$ in $Y$, one has $x \in D(T)$ and $Tx = y$.

Example: on $X = Y = C[0, 1]$ with the supremum norm, let $D(T) = C^1[0, 1]$ and $Tf = f'$.
If $f_n \to f$ and $f_n' \to g$ uniformly, then $f_n(x) = f_n(0) + \int_0^x f_n'$ gives $f(x) = f(0) + \int_0^x g$, so $f \in C^1[0, 1]$ and $f' = g$.
Hence $T$ is closed, although it is not bounded.

Non-example: the same formula with $D(S)$ the space of polynomials is not closed.
The Taylor polynomials $p_n$ of $e^x$ converge uniformly to $e^x$ and $p_n' = p_{n-1}$ converges to $e^x$, but $e^x$ is not a polynomial, so it is not in $D(S)$.

Every bounded operator defined on all of $X$ is closed.
If $X$ and $Y$ are Banach spaces and $T$ is closed with $D(T) = X$, then $T$ is bounded, by the [[closed graph theorem|GXM8BX8YM7]].
