---
tag: RNDKD74V17
kind: definition
name: Mosco convergence
msc: [49J45, 49J40, 49J53]
defines: KH0V6QA2ZN
uses: [NW9MM370A5, 03J5RAKB30, P6KHVSTPZV, 0GSZ7B0CGR, 033RZ32T4Q, 0T3RZQXDYD, 4A82S5FVRT]
sources:
  - url: https://en.wikipedia.org/wiki/Mosco_convergence
    locator: Definition
---

## Definition

Let $X$ be a real [[normed space|03J5RAKB30]].
Write $x_n \rightharpoonup x$ for convergence in the [[weak topology|P6KHVSTPZV]] $\sigma(X, X^*)$ and $x_n \to x$ for convergence in norm, where $X^*$ is the [[continuous dual space|4A82S5FVRT]] of $X$.
Let $F_n \colon X \to [-\infty, +\infty]$ for $n \in \N$ and $F \colon X \to [-\infty, +\infty]$ be functions with values in the [[extended real line|0GSZ7B0CGR]].
The sequence $(F_n)$ *Mosco converges* to $F$ if the following two conditions hold for every $x \in X$.

1. (Weak lower bound.) For every sequence $(x_n)$ in $X$ with $x_n \rightharpoonup x$,
$$F(x) \le \liminf_{n \to \infty} F_n(x_n).$$
2. (Strong recovery sequence.) There is a sequence $(x_n)$ in $X$ with $x_n \to x$ and
$$F(x) \ge \limsup_{n \to \infty} F_n(x_n).$$

The indicator function of a set $K \subseteq X$ in convex analysis is $0$ on $K$ and $+\infty$ outside $K$.
Subsets $K_n \subseteq X$ Mosco converge to $K \subseteq X$ if their indicator functions do.

## Remarks

For sets the two conditions read as follows.
If $n_k$ is increasing, $x_k \in K_{n_k}$ and $x_k \rightharpoonup x$, then $x \in K$.
Every $x \in K$ is the norm limit of a sequence with $x_n \in K_n$.
The notation $F = \operatorname{M\text{-}lim}_n F_n$ is common.
If $X$ is finite-dimensional, weak and norm convergence agree, and Mosco convergence is [[Γ-convergence|NW9MM370A5]].

Example: let $F$ be convex and lower semicontinuous, and let $F_n = F$ for all $n$.
Then $(F_n)$ Mosco converges to $F$.
The recovery sequence $x_n = x$ gives clause 2.
For clause 1, a convex lower semicontinuous function is also weakly lower semicontinuous, because its closed sublevel sets are convex and hence weakly closed.

Non-example: in the sequence space $\ell^2$ with unit vectors $e_n$, let $K_n = \set{e_n}$ and $K = \set{0}$.
Clause 1 holds, since $e_n \rightharpoonup 0$.
Clause 2 fails at $0$: every choice $x_n \in K_n$ is $x_n = e_n$, and $\norm{e_n - 0} = 1$ for all $n$.
