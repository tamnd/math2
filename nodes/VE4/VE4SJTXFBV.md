---
tag: VE4SJTXFBV
kind: definition
name: Day terms
msc: [08B05, 08B10]
defines: B0YKA8401M
uses: [AJNZJD8442, PKD440G2XW, QAQAS3JWXW, Y203PPTS61]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_lattice
---

## Definition

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of algebras and let $n \ge 1$.
*Day terms* for $\mathcal{V}$ are quaternary terms $m_0, m_1, \dots, m_n$ such that $\mathcal{V}$ satisfies the following [[identities|PKD440G2XW]]:

1. $m_0(x, y, z, u) = x$ and $m_n(x, y, z, u) = u$.
2. $m_i(x, y, y, x) = x$ for every $i \le n$.
3. $m_i(x, x, u, u) = m_{i+1}(x, x, u, u)$ for every even $i < n$.
4. $m_i(x, y, y, u) = m_{i+1}(x, y, y, u)$ for every odd $i < n$.

## Remarks

Day's theorem says that $\mathcal{V}$ is a [[congruence-modular variety|QAQAS3JWXW]] if and only if $\mathcal{V}$ has Day terms for some $n$.
Example: if $p$ is a [[Mal'cev term|Y203PPTS61]] for $\mathcal{V}$, then $m_0 = x$, $m_1 = p(u, z, y)$, $m_2 = u$ are Day terms.
The checks are $m_1(x, y, y, x) = p(x, y, y) = x$, $m_1(x, x, u, u) = p(u, u, x) = x = m_0(x, x, u, u)$, and $m_1(x, y, y, u) = p(u, y, y) = u = m_2(x, y, y, u)$.
For groups this gives $m_1(x, y, z, u) = u z^{-1} y$.
Non-example: with $n = 1$, the terms $m_0 = x$ and $m_1 = u$ are not Day terms in any nontrivial variety.
Clause 3 for $i = 0$ reads $x = u$, which holds only in one-element algebras.

## Explanations

### L1 human

Day terms are a chain of four-input formulas that witness, by equations alone, that a variety has modular congruence lattices.
