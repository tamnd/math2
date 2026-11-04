---
tag: W5N7GWHAKZ
kind: proof
name: Proof of the reduction modulo p test for irreducibility
msc: ["12E05"]
proves: 0KWWEXW0RN
uses: [00X2A9G9W3, 0BDX4MBKT4, 0QFV5Y1Z5X, 0SP14DZN0G, 0DQMDSVSXJ, 0NV6E43P4A, 0T233AZ1GE, 019NFGFPR5, 000JFQGDXG, 0QKVE1GD9A, 055HT85T3S, 05K3J8J8T2]
sources:
  - url: https://en.wikipedia.org/wiki/Irreducible_polynomial
    locator: Over the integers and finite fields
---

## Proof

1. Let $f \in \Z[x]$ be [[monic|0BDX4MBKT4]], let $p$ be a prime, and assume that $\bar{f}$ is [[irreducible|00X2A9G9W3]] in $\F_p[x]$. Here $\F_p = \Z/p\Z$ is a [[field|0NV6E43P4A]].
2. Let $\pi \colon \Z[x] \to \F_p[x]$ reduce each coefficient modulo $p$. By the [[universal property of the polynomial ring|0DQMDSVSXJ]], applied to $\Z \to \F_p$ and $x \mapsto x$, the map $\pi$ is a ring homomorphism. Also $\pi(f) = \bar{f}$.
3. If $g \in \Z[x]$ is monic, then $\pi(g)$ is monic with $\deg \pi(g) = \deg g$, because the leading coefficient $1$ reduces to $1 \ne 0$.
4. Over a field $F$, the [[units|019NFGFPR5]] of $F[x]$ are the nonzero constants. Indeed, $u v = 1$ forces $\deg u = 0$ by the [[degree of a product|0T233AZ1GE]], and a nonzero constant has an inverse in $F$.
5. By the same degree argument, the units of $\Z[x]$ are the units of $\Z$, that is, $\pm 1$.
6. Since $\bar{f}$ is irreducible, it is not a unit, so $\deg \bar{f} \ge 1$ by Step 4. By Step 3, $\deg f = \deg \bar{f} \ge 1$. So $f$ is nonzero and not a unit of $\Z[x]$.
7. Suppose that $f = g h$ with $g, h \in \Z[x]$. Their leading coefficients multiply to $1$, so both are $1$ or both are $-1$.
8. In the second case, replace $g, h$ by $-g, -h$. This does not change the product, and $g$ is a unit if and only if $-g$ is. So we may assume that $g$ and $h$ are monic.
9. By Step 2, $\bar{f} = \pi(g) \, \pi(h)$. Since $\bar{f}$ is irreducible, $\pi(g)$ or $\pi(h)$ is a unit, say $\pi(g)$. By Step 4, $\deg \pi(g) = 0$.
10. By Step 3, $\deg g = 0$. A monic polynomial of degree $0$ is the constant $1$, so $g$ is a unit.
11. By Steps 6 to 10, $f$ is irreducible in $\Z[x]$.
12. The monic polynomial $f$ is [[primitive|0SP14DZN0G]]: an integer that divides every coefficient divides the leading coefficient $1$, so it is $\pm 1$.
13. The ring $\Z$ is a [[Euclidean domain|000JFQGDXG]], hence a [[principal ideal domain|0QKVE1GD9A]], hence a [[unique factorisation domain|055HT85T3S]], with [[field of fractions|05K3J8J8T2]] $\Q$.
14. By [[Gauss's lemma|0QFV5Y1Z5X]], with Steps 11 to 13, $f$ is irreducible in $\Q[x]$.

## Idea

Reduction modulo $p$ is a ring homomorphism, and it keeps the degree of a monic polynomial. So a factorisation of $f$ into monic factors of positive degree would give one of $\bar{f}$. Gauss's lemma then moves irreducibility from $\Z[x]$ to $\Q[x]$.
