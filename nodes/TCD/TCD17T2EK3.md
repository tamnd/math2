---
tag: TCD17T2EK3
kind: definition
name: Indirect utility function
msc: [91B42, 91B16]
defines: N9S29DKCY8
uses: [A56BG7XYM6, GZZS4MTDG9, EQPEPJ7QQZ, 0R3H5PANRQ]
sources:
  - url: https://en.wikipedia.org/wiki/Indirect_utility_function
---

## Definition

Let $u \colon \R^n_{\ge 0} \to \R$ be a continuous [[utility function|GZZS4MTDG9]].
Let $p \in \R^n$ be a price vector with all entries positive and let $w > 0$ be a wealth.
The *indirect utility* at $(p, w)$ is
$$v(p, w) = \max \set{u(x) : x \in \R^n_{\ge 0},\ p \cdot x \le w},$$
the optimal value of the [[utility maximization problem|A56BG7XYM6]].
The map $(p, w) \mapsto v(p, w)$ is the *indirect utility function* of $u$.

## Remarks

The maximum exists because $u$ is continuous and the budget set is compact and nonempty.
For a general utility one uses the [[supremum|0R3H5PANRQ]] instead.
If $u$ has a [[Marshallian demand|EQPEPJ7QQZ]] $x(p, w)$, then $v(p, w) = u(x(p, w))$.
Example: for $u(x_1, x_2) = \sqrt{x_1 x_2}$, the demand is $(w / (2 p_1), w / (2 p_2))$, so $v(p, w) = w / (2\sqrt{p_1 p_2})$.
A function that grows with some price, such as $p_1 w$, is not the indirect utility of any utility function.
Indeed, a larger price shrinks the budget set and cannot raise the maximum.
For continuous $u$, $v$ is nonincreasing in $p$, nondecreasing in $w$, quasiconvex, and $v(t p, t w) = v(p, w)$ for $t > 0$.
