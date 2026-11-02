---
tag: 64VN7KYGHK
kind: definition
name: Quasi-identity
msc: ["08C15", "03C52"]
defines: 94GVY3APPQ
uses: [3YYKGWJJND, PKD440G2XW]
sources:
  - url: https://en.wikipedia.org/wiki/Quasivariety
---

## Definition

Let $\sigma$ be an algebraic signature and let $X$ be a set of variables.
A *quasi-identity* of type $\sigma$ is an expression
$$s_1 \approx t_1 \wedge \cdots \wedge s_n \approx t_n \rightarrow s \approx t,$$
where $n \ge 0$ and $s_1, t_1, \ldots, s_n, t_n, s, t$ are [[terms|3YYKGWJJND]] of type $\sigma$ over $X$.
A $\sigma$-algebra $A$ *satisfies* this quasi-identity if every assignment $h \colon X \to A$ with $h(s_i) = h(t_i)$ for all $i \le n$ also has $h(s) = h(t)$.
Here $h(u)$ denotes the value of the term $u$ in $A$ under $h$.

## Remarks

A quasi-identity with $n = 0$ is an [[identity|PKD440G2XW]] $s \approx t$.

Example: the right cancellation law $x \cdot z \approx y \cdot z \rightarrow x \approx y$ is satisfied by every group.
Indeed, if $a z = b z$ in a group, then multiplying on the right by $z^{-1}$ gives $a = b$.

Non-example: the monoid $(\Z, \cdot, 1)$ does not satisfy this quasi-identity.
The assignment $x \mapsto 1$, $y \mapsto 2$, $z \mapsto 0$ satisfies the hypothesis $1 \cdot 0 = 2 \cdot 0$ but not the conclusion $1 = 2$.

In first-order terms, a quasi-identity stands for the universal sentence $\forall \bar x \, (s_1 = t_1 \wedge \cdots \wedge s_n = t_n \rightarrow s = t)$.
Another example is $x^2 \approx 1 \rightarrow x \approx 1$, which a group satisfies exactly when it has no element of order $2$.
This property cannot be expressed by identities, since the class of such groups is not closed under quotients: the additive group $\Z$ has it, and its quotient $\Z / 2\Z$ does not.
