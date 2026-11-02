---
tag: DJM5H15WV5
kind: definition
name: Singular simplicial set
msc: [55U10, 18N50, 55N10]
defines: RWBMXQW6S5
uses: [0CNQXVBHCX, 0SY9ECQ19Q]
sources:
  - url: https://en.wikipedia.org/wiki/Simplicial_set
---

## Definition

For $n \ge 0$ let $[n] = \set{0, 1, \dots, n}$, and let
$$\abs{\Delta^n} = \set{(t_0, \dots, t_n) \in \R^{n+1} : t_i \ge 0, \ t_0 + \cdots + t_n = 1}$$
be the standard topological $n$-simplex, with vertices $e_0, \dots, e_n$.
An order-preserving map $\theta \colon [m] \to [n]$ induces the affine map $\theta_* \colon \abs{\Delta^m} \to \abs{\Delta^n}$ with $\theta_*(e_i) = e_{\theta(i)}$.
Let $X$ be a [[topological space|0CNQXVBHCX]].
The *singular [[simplicial set|WW81ARB8K9]]* $\operatorname{Sing} X$ is the simplicial set with:

1. $(\operatorname{Sing} X)_n$ the set of [[continuous maps|0SY9ECQ19Q]] $\sigma \colon \abs{\Delta^n} \to X$, called singular $n$-simplices.
2. For $\theta \colon [m] \to [n]$ order-preserving, the map $\theta^* \colon (\operatorname{Sing} X)_n \to (\operatorname{Sing} X)_m$ given by $\theta^*(\sigma) = \sigma \circ \theta_*$.

## Remarks

The identities $(\theta \circ \psi)_* = \theta_* \circ \psi_*$ and $\id_* = \id$ show that $\operatorname{Sing} X$ is a functor $\Delta^{\mathrm{op}} \to \mathrm{Set}$, that is, a simplicial set.
A continuous map $f \colon X \to Y$ induces $\operatorname{Sing} f$ by $\sigma \mapsto f \circ \sigma$, so $\operatorname{Sing}$ is a functor from spaces to simplicial sets.

Example: if $X$ is a single point, each $(\operatorname{Sing} X)_n$ has exactly one element, so $\operatorname{Sing} X$ is the terminal simplicial set $\Delta^0$.

Non-example: the simplicial set whose $n$-simplices are all functions $\abs{\Delta^n} \to X$, continuous or not, is a simplicial set, but it is not $\operatorname{Sing} X$ for $X = [0, 1]$.
It contains discontinuous functions $\abs{\Delta^1} \to [0, 1]$, which clause 1 excludes.

$\operatorname{Sing} X$ is always a Kan complex.
