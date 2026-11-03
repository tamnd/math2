---
tag: P1JZ36MV2T
kind: definition
name: General equilibrium theory
msc: [91B50, 91B24]
defines: HGMHZSM0XQ
uses: [JGP0Q56FRY, EQPEPJ7QQZ]
sources:
  - url: https://en.wikipedia.org/wiki/General_equilibrium_theory
---

## Definition

An *exchange economy* with $L$ goods and $I$ consumers consists of, for each consumer $i = 1, \dots, I$:

1. the consumption set $\R^L_+$ of bundles of goods;
2. a [[preference relation|JGP0Q56FRY]] $\succsim_i$ on $\R^L_+$;
3. an endowment $\omega_i \in \R^L_+$.

Let $p \in \R^L$ be a price vector with all $p_\ell > 0$.
Suppose that each consumer $i$ has a unique best bundle $x_i(p)$ in the budget set $\set{x \in \R^L_+ : p \cdot x \le p \cdot \omega_i}$.
This bundle is the [[Marshallian demand|EQPEPJ7QQZ]] of $i$ at wealth $p \cdot \omega_i$.
The *aggregate excess demand* is
$$z(p) = \sum_{i=1}^{I} \left( x_i(p) - \omega_i \right) \in \R^L.$$
A *general equilibrium price vector* (Walrasian equilibrium price vector) is a $p$ with all $p_\ell > 0$ and $z(p) = 0$.
At such $p$, supply equals demand in every market at once.

## Remarks

Example: let $L = I = 2$, with $u_1 = u_2 = \sqrt{x y}$, $\omega_1 = (1, 0)$ and $\omega_2 = (0, 1)$.
Each consumer spends half of the wealth on each good, so $x_1(p) = (1/2, p_1 / (2 p_2))$ and $x_2(p) = (p_2 / (2 p_1), 1/2)$.
Then $z_1(p) = (p_2 - p_1) / (2 p_1)$ and $z_2(p) = (p_1 - p_2) / (2 p_2)$, so the equilibrium prices are those with $p_1 = p_2$.

Non-example: in the same economy $p = (1, 2)$ is not an equilibrium price vector, since $z_1(1, 2) = 1/2 \ne 0$: there is excess demand for good $1$.

The excess demand is homogeneous of degree zero, $z(t p) = z(p)$ for $t > 0$, so equilibrium prices are only determined up to a positive factor.
One often normalizes them to lie in the price simplex $\set{p \ge 0 : p_1 + \cdots + p_L = 1}$.
The same notion with production and ownership of firms is the equilibrium of the [[Arrow–Debreu model|SVGN7R3RDY]].
