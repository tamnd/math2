---
tag: M6A75DMQJT
kind: statement
role: proposition
name: Walras's law
msc: [91B50, 91B24]
uses: [HGMHZSM0XQ, EQPEPJ7QQZ, JGP0Q56FRY]
about: [HGMHZSM0XQ]
sources:
  - url: https://en.wikipedia.org/wiki/Walras%27s_law
same_as:
  wikidata: Q1089697
  wikipedia: Walras's law
---

## Statement

Let an [[exchange economy|HGMHZSM0XQ]] have $L$ goods and $I$ consumers with endowments $\omega_i \in \R^L_+$ and [[preference relations|JGP0Q56FRY]] $\succsim_i$ on $\R^L_+$.
Assume each $\succsim_i$ is locally nonsatiated.
This means: for every bundle $x$ and every $\varepsilon > 0$ there is a bundle $y$ within distance $\varepsilon$ of $x$ with $y \succ_i x$.
Let $p \in \R^L$ have all entries positive, and let $x_i(p)$ be a best bundle of consumer $i$ in the budget set $\set{x \in \R^L_+ : p \cdot x \le p \cdot \omega_i}$.
Let $z(p) = \sum_i (x_i(p) - \omega_i)$ be the aggregate excess demand.
Then
$$p \cdot z(p) = 0.$$
Consequently, if $L - 1$ of the markets clear at $p$, that is $z_\ell(p) = 0$ for $L - 1$ goods $\ell$, then the last market clears too.

## Remarks

By local nonsatiation, a best bundle exhausts the budget: if $p \cdot x_i(p) < p \cdot \omega_i$, then nearby bundles are still affordable and one of them is strictly preferred.
So $p \cdot x_i(p) = p \cdot \omega_i$ for each $i$, and summing over $i$ gives $p \cdot z(p) = 0$.
If $z_\ell(p) = 0$ for all $\ell \ne k$, then $p_k z_k(p) = 0$ and $p_k > 0$, so $z_k(p) = 0$.

Example: for two consumers with utility $\sqrt{x y}$ and endowments $(1, 0)$ and $(0, 1)$, one finds $z(p) = \left( \frac{p_2 - p_1}{2 p_1}, \frac{p_1 - p_2}{2 p_2} \right)$.
Then $p \cdot z(p) = \frac{p_2 - p_1}{2} + \frac{p_1 - p_2}{2} = 0$ for every $p$, even though $z(p) \ne 0$ unless $p_1 = p_2$.

Local nonsatiation is needed: a consumer who is satiated at a bundle inside the budget set may leave money unspent, and then $p \cdot z(p) < 0$ is possible.

## Explanations

### L1 human

Everyone spends exactly what their goods are worth, so the total value of what people want to buy equals the total value of what they want to sell.
Hence if there is too much demand in one market, there must be too little demand, measured in money, somewhere else.
And if all markets but one balance, the last one balances automatically.

### L2 human

Walras's law reduces the number of independent equilibrium conditions from $L$ to $L - 1$.
Together with homogeneity of degree zero of $z$, it means that one may fix one price as numéraire and solve $L - 1$ equations in $L - 1$ unknowns.
It is one of the few restrictions that aggregate excess demand must satisfy; the [[Sonnenschein–Mantel–Debreu theorem|H8J1J00JXX]] says that, roughly, it is the only one besides continuity and homogeneity.
In an economy with production the same law holds when firm profits are paid out to consumers.
