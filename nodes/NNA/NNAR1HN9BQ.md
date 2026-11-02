---
tag: NNAR1HN9BQ
kind: definition
name: Γ-convergence
msc: [49J45]
defines: NW9MM370A5
uses: [0VKD1TP7F3, 0GSZ7B0CGR, 0G9EKM0E15, 033RZ32T4Q, 0T3RZQXDYD]
sources:
  - url: https://en.wikipedia.org/wiki/Γ-convergence
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]].
Let $F_n \colon X \to [-\infty, +\infty]$ for $n \in \N$ and $F \colon X \to [-\infty, +\infty]$ be functions with values in the [[extended real line|0GSZ7B0CGR]].
The [[sequence|0G9EKM0E15]] $(F_n)$ *Γ-converges* to $F$ if the following two conditions hold for every $x \in X$.

1. (Lower bound.) For every sequence $(x_n)$ in $X$ with $x_n \to x$,
$$F(x) \le \liminf_{n \to \infty} F_n(x_n).$$
2. (Recovery sequence.) There is a sequence $(x_n)$ in $X$ with $x_n \to x$ and
$$F(x) \ge \limsup_{n \to \infty} F_n(x_n).$$

The function $F$ is then called the *Γ-limit* of $(F_n)$, written $F = \Gamma\text{-}\lim_n F_n$.
Here $\liminf$ is the [[limit inferior|033RZ32T4Q]] and $\limsup$ is the [[limit superior|0T3RZQXDYD]].

## Remarks

The two conditions together give $F(x) = \lim_n F_n(x_n)$ along the recovery sequence.
A Γ-limit is unique when it exists, and it is always lower semicontinuous.
For a family $(F_\varepsilon)_{\varepsilon > 0}$, one says that $F_\varepsilon$ Γ-converges to $F$ as $\varepsilon \to 0$ if $F_{\varepsilon_k}$ Γ-converges to $F$ for every sequence $\varepsilon_k \to 0$.
The same definition with neighbourhoods instead of sequences works in any topological space, and it agrees with this one in metric spaces.

Example: $F_n(x) = \sin(nx)$ on $\R$ Γ-converges to the constant $F = -1$.
The lower bound holds because $\sin(n x_n) \ge -1$ for every $n$.
For a recovery sequence, pick $x_n$ with $\abs{x_n - x} \le 2\pi/n$ and $\sin(n x_n) = -1$; then $x_n \to x$ and $F_n(x_n) = -1$.

Non-example: let $F(0) = 1$ and $F(x) = 0$ for $x \ne 0$, and let $F_n = F$ for all $n$.
The constant sequence does not Γ-converge to $F$: for $x_n = 1/n \to 0$ one has $\liminf_n F_n(x_n) = 0 < 1 = F(0)$, so the lower bound fails at $0$.
Its Γ-limit is the function $0$, the lower semicontinuous envelope of $F$.
