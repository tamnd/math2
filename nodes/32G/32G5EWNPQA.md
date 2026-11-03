---
tag: 32G5EWNPQA
kind: definition
name: Bertrand competition
msc: [91B54, 91A10, 91A80]
defines: YA9SSGCKY3
uses: [5MZTZRC3CZ, 745WYP9YJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Bertrand_competition
---

## Definition

Let $n \ge 2$ firms produce one homogeneous good, let $D \colon \R_+ \to \R_+$ be the market demand function, and let firm $i$ have constant marginal cost $c_i \ge 0$.
The *Bertrand game* is the [[normal-form game|5MZTZRC3CZ]] in which:

1. each firm $i$ chooses a price $p_i \ge 0$, all at the same time;
2. buyers buy only from the firms with the lowest price $\underline p = \min_j p_j$, and the demand $D(\underline p)$ is split equally among the $k$ firms that charge $\underline p$;
3. the payoff of firm $i$ is $(p_i - c_i) D(p_i)/k$ if $p_i = \underline p$, and $0$ otherwise.

A *Bertrand equilibrium* is a [[Nash equilibrium|745WYP9YJ0]] of this game.

## Remarks

Example: two firms with $c_1 = c_2 = c$ and $D(p) > 0$ for $p$ near $c$.
Then $p_1 = p_2 = c$ is an equilibrium: both earn $0$, and a firm that raises its price sells nothing, while one that lowers it sells below cost.
It is the only one, if $D$ is positive and continuous near $c$.
If the lowest price exceeds $c$, a firm can undercut it slightly and capture the whole market.
If one firm charges $c$ and the other more, the first can raise its price a little, stay the cheapest, and earn a positive profit.
If a firm charges less than $c$ and sells, it loses money and would rather raise its price.

Non-example: $p_1 = p_2 = p > c$, with $D(p) > 0$, is not an equilibrium.
Each firm earns $(p - c) D(p) / 2$, but a price slightly below $p$ earns close to $(p - c) D(p)$, twice as much.

The conclusion depends on the assumptions of identical goods, no capacity limits and equal costs.
With capacity constraints or differentiated goods, prices above cost can be equilibria.
When firms choose quantities instead, the model becomes [[Cournot competition|S5HGX1PNZR]].
