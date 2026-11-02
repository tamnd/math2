---
tag: HJXA140M0C
kind: definition
name: Convex cone
msc: [52A20, 46A55]
defines: 6VE4KA12VD
uses: [000AYPA9AJ, 02AS45T3H9]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_cone
---

## Definition

Let $V$ be a real [[vector space|000AYPA9AJ]].
A subset $C \subseteq V$ is a *convex cone* if for all $x, y \in C$ and all real numbers $\alpha > 0$ and $\beta > 0$,
$$\alpha x + \beta y \in C.$$

## Remarks

Equivalently, $C$ is closed under addition and under multiplication by positive scalars.
Equivalently again, $C$ is [[convex|02AS45T3H9]] and $t x \in C$ for all $x \in C$ and $t > 0$.

Example: the nonnegative orthant $\R^n_{\ge 0} = \set{x \in \R^n : x_i \ge 0 \text{ for all } i}$.
If $x, y$ have nonnegative coordinates and $\alpha, \beta > 0$, then each coordinate $\alpha x_i + \beta y_i$ is nonnegative.

Non-example: the closed unit disc in $\R^2$ is convex, but $(1, 0)$ lies in it and $2 \cdot (1, 0) = (2, 0)$ does not.

Conventions differ: many authors also allow $\alpha = \beta = 0$, so that every nonempty convex cone contains $0$.
A convex cone that contains $0$ is called a pointed cone in some texts.
The same definition works over any ordered field in place of $\R$.
