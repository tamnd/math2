---
tag: RW8DQQYJMR
kind: definition
name: Differential Galois theory
msc: [12H05, 34M15]
defines: EEZS4H8QPH
uses: [T43TQ817XC, TB53Y5NMJD, 0WQ1A8SHTZ, 0QA8CHH8MG]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_Galois_theory
---

## Definition

Let $(K, \partial)$ be a [[differential field|T43TQ817XC]].
Let $(L, \partial)$ be a differential field that is a [[field extension|0WQ1A8SHTZ]] of $K$, with derivation equal to $\partial$ on $K$.
The *differential Galois group* $\Gal_\partial(L/K)$ is the group, under composition, of the field automorphisms $\sigma \colon L \to L$ such that:

1. $\sigma(a) = a$ for all $a \in K$.
2. $\sigma(\partial b) = \partial(\sigma b)$ for all $b \in L$.

Differential Galois theory is the study of these groups.
The main case is a [[Picard–Vessiot extension|TB53Y5NMJD]] $L$ of $K$ for a linear differential equation.
There the field of constants of $K$ is assumed algebraically closed of characteristic $0$.

## Remarks

Example: let $K = \C(x)$ with $\partial = d/dx$ and $L = K(e^x)$, the Picard–Vessiot extension of $y' = y$.
An element $\sigma$ of $\Gal_\partial(L/K)$ satisfies $\partial(\sigma e^x) = \sigma(e^x)$, so $\sigma(e^x)/e^x$ has derivative $0$ and is a nonzero constant $c \in \C$.
Each $c \in \C^\times$ gives such a $\sigma$, because $e^x$ is transcendental over $K$, so $\Gal_\partial(L/K) \cong \C^\times$.
Non-example: let $K = \C$ with $\partial = 0$ and $L = \C(x)$ with $\partial = d/dx$; the field automorphism $\sigma$ of $L$ over $\C$ with $\sigma(x) = 2x$ satisfies clause 1 but fails clause 2, since $\partial(\sigma x) = 2$ while $\sigma(\partial x) = 1$.
The elements of $\Gal_\partial(\C(x)/\C)$ are the maps $x \mapsto x + c$ with $c \in \C$, so this group is isomorphic to $(\C, +)$.
For a Picard–Vessiot extension for an equation of order $n$, the group acts on the $n$-dimensional space of solutions over the constants $C$ and is a Zariski-closed subgroup of $\mathrm{GL}_n(C)$.
