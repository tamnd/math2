---
tag: FC34XP2DQV
kind: definition
name: Polynomial operation
msc: [08A40]
defines: XP67WCPQ59
uses: [N9M2N27END, DCSXXT4SER, 1G0B73WPX8]
sources:
  - url: https://en.wikipedia.org/wiki/Clone_(algebra)
---

## Definition

Let $A$ be an algebra and let $n \ge 1$.
An operation $p \colon A^n \to A$ is an $n$-ary *polynomial operation* of $A$ if the following holds.
There are $m \ge 0$, an $(n + m)$-ary [[term operation|N9M2N27END]] $t^A$ of $A$, and elements $c_1, \ldots, c_m \in A$ such that
$$p(a_1, \ldots, a_n) = t^A(a_1, \ldots, a_n, c_1, \ldots, c_m)$$
for all $a_1, \ldots, a_n \in A$.

## Remarks

Equivalently, the polynomial operations of $A$ are the term operations of the algebra $A_A$ obtained from $A$ by adding a constant symbol for each element of $A$.
Every term operation is a polynomial operation, with $m = 0$.
An equivalence relation on $A$ is a [[congruence|DCSXXT4SER]] exactly when it is preserved by every unary polynomial operation of $A$.
For a commutative ring $R$, the polynomial operations of $R$ are the [[polynomial functions|1G0B73WPX8]] $R^n \to R$ given by polynomials with coefficients in $R$.

Example: in the group $(\Z, +, -, 0)$, the map $p(a) = 2a + 5$ is a polynomial operation.
Take $t = (x_1 + x_1) + x_2$ and $c_1 = 5$; then $t^A(a, 5) = 2a + 5$.

Non-example: on $(\Z, +, -, 0)$ the map $a \mapsto a^2$ is not a polynomial operation.
By induction on terms, every unary polynomial operation of this group has the form $a \mapsto k a + c$ with $k, c \in \Z$.
The map $a \mapsto a^2$ is not of this form, since its values $0, 1, 4$ at $0, 1, 2$ are not in arithmetic progression.
