---
tag: D3G13ZQ2AQ
kind: definition
name: Closure of an operator
msc: [47A05, 47B25]
defines: TRC892PJNN
uses: [3TWMBFQJJ8, VM7B38PA87, 3RCAY97W1E, 0QEAJB91GZ]
sources:
  - url: https://en.wikipedia.org/wiki/Unbounded_operator
    locator: Closed linear operators
---

## Definition

Let $X$ and $Y$ be normed spaces, and let $T$ be a [[closable operator|3TWMBFQJJ8]] from $X$ to $Y$.
The *closure* of $T$ is the operator $\overline{T}$ whose [[graph|3RCAY97W1E]] is the [[closure|0QEAJB91GZ]] of the graph of $T$:
$$\Gamma(\overline{T}) = \overline{\Gamma(T)} \subseteq X \times Y.$$

## Remarks

Explicitly, $x \in D(\overline{T})$ if and only if there is a sequence $(x_n)$ in $D(T)$ with $x_n \to x$ such that $(T x_n)$ converges, and then $\overline{T} x = \lim T x_n$.
The operator $\overline{T}$ is [[closed|VM7B38PA87]], it extends $T$, and it is contained in every closed extension of $T$.

Example: on $C[0, 1]$ with the supremum norm, let $T$ be differentiation on polynomials.
Every $f \in C^1[0, 1]$ is a limit of polynomials $p_n$ with $p_n' \to f'$ uniformly: take polynomials $q_n \to f'$ uniformly and set $p_n(x) = f(0) + \int_0^x q_n$.
Combined with the closedness of differentiation on $C^1[0, 1]$, this gives $D(\overline{T}) = C^1[0, 1]$ and $\overline{T} f = f'$.

Non-example: an operator that is not closable has no closure, because the closure of its graph contains a pair $(0, y)$ with $y \ne 0$ and is not a graph.

A closed operator is its own closure.
A subspace $D \subseteq D(\overline{T})$ with $\overline{T|_D} = \overline{T}$ is called a *core* of $\overline{T}$.
