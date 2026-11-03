---
tag: YNR9AX3HSS
kind: definition
name: Restricted Lie algebra
msc: [17B50]
defines: MW1DW7182Y
uses: [HKYYR1SZQW, 5JJYBJ6A8K, 54XSPNAM1J, 1ZB13N78XW]
sources:
  - url: https://en.wikipedia.org/wiki/Restricted_Lie_algebra
---

## Definition

Let $F$ be a field of [[characteristic|1ZB13N78XW]] $p > 0$, and let $\mathfrak{g}$ be a [[Lie algebra|5JJYBJ6A8K]] over $F$.
For $x \in \mathfrak{g}$ let $\operatorname{ad} x \colon y \mapsto [x, y]$ be its [[adjoint map|54XSPNAM1J]].
For $x, y \in \mathfrak{g}$ and $1 \le i \le p - 1$, let $s_i(x, y)$ be the element such that $i \, s_i(x, y)$ is the coefficient of $\lambda^{i-1}$ in $(\operatorname{ad}(\lambda x + y))^{p-1}(x)$, a polynomial in a variable $\lambda$.
A *$p$-map* on $\mathfrak{g}$ is a map $x \mapsto x^{[p]}$ from $\mathfrak{g}$ to $\mathfrak{g}$ such that, for all $x, y \in \mathfrak{g}$ and $a \in F$:

1. $\operatorname{ad}(x^{[p]}) = (\operatorname{ad} x)^p$.
2. $(a x)^{[p]} = a^p x^{[p]}$.
3. $(x + y)^{[p]} = x^{[p]} + y^{[p]} + \sum_{i=1}^{p-1} s_i(x, y)$.

A *restricted Lie algebra* is a Lie algebra over $F$ together with a $p$-map.

## Remarks

Example: let $A$ be an associative algebra over $F$ with bracket $[x, y] = xy - yx$, and put $x^{[p]} = x^p$.
Clause 1 holds because $\operatorname{ad} x = L_x - R_x$, where the left and right multiplications $L_x$ and $R_x$ commute, so $(\operatorname{ad} x)^p = L_x^p - R_x^p = \operatorname{ad}(x^p)$ in characteristic $p$.
Clause 2 is clear, and clause 3 is Jacobson's formula for $(x + y)^p$ in an associative algebra.
In particular $\mathfrak{gl}_n(F)$ is restricted with the matrix $p$-th power.
Non-example: on $\mathfrak{gl}_n(F)$ with $F \ne \F_p$, the identity map $x \mapsto x$ is not a $p$-map, since clause 2 fails for $a \in F$ with $a^p \ne a$.
If $\mathfrak{g}$ has trivial centre, there is at most one $p$-map, because clause 1 determines $x^{[p]}$.
The algebra of derivations of any algebra over $F$ is restricted with $D^{[p]} = D^p$, since the Leibniz rule gives $D^p(ab) = D^p(a) b + a D^p(b)$ in characteristic $p$.
