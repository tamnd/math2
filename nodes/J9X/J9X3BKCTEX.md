---
tag: J9X3BKCTEX
kind: definition
name: Fisher market
msc: [91B50, 91B26, 91A68]
defines: SDDGP6VV3B
uses: [YTBPB52K27, GZZS4MTDG9]
sources:
  - url: https://en.wikipedia.org/wiki/Fisher_market
---

## Definition

A *Fisher market* consists of $m$ divisible goods, each available in one unit, and $n$ buyers.
Buyer $i$ has a budget $B_i > 0$ and a [[utility function|GZZS4MTDG9]] $u_i \colon \R^m_+ \to \R$.
Given prices $p \in \R^m_+$, the budget set of buyer $i$ is $\set{x \in \R^m_+ : p \cdot x \le B_i}$.
A *market equilibrium* is a pair $(p, x)$ of prices $p \in \R^m_+$ and bundles $x_1, \dots, x_n \in \R^m_+$ such that:

1. each $x_i$ maximizes $u_i$ over the budget set of buyer $i$;
2. for each good $j$, $\sum_i x_{ij} \le 1$, with equality whenever $p_j > 0$.

## Remarks

Example: one good and two buyers with $B_1 = 1$, $B_2 = 2$ and $u_i(x) = x$.
At price $p = 3$ buyer $1$ buys $1/3$ and buyer $2$ buys $2/3$, each spending the whole budget, which is optimal since utility increases in $x$.
The total is $1$, so the market clears and $(3, (1/3, 2/3))$ is an equilibrium.

Non-example: at price $p = 2$ the buyers demand $1/2$ and $1$, together $3/2 > 1$, so clause 2 fails.

The common case is linear utilities $u_i(x) = \sum_j v_{ij} x_j$ with $v_{ij} \ge 0$.
A Fisher market is an exchange economy in which one extra good, money, is held only by buyers and valued only by sellers.
So its equilibria are [[competitive equilibria|YTBPB52K27]] of that economy.
For linear utilities, the equilibrium allocations are the optimal solutions of the Eisenberg–Gale convex program, which maximizes $\sum_i B_i \log u_i(x_i)$ subject to $\sum_i x_{ij} \le 1$ and $x \ge 0$.
