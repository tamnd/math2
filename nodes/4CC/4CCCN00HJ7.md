---
tag: 4CCCN00HJ7
kind: proof
name: Proof that polynomials of degree two or three are irreducible iff they have no roots
msc: ["12E05"]
proves: 0VNE161QCK
uses: [0QA8CHH8MG, 00X2A9G9W3, 00EHX6FWC0, 0K3MWA7DMC, 0T233AZ1GE, 019NFGFPR5, 0125QVNCFQ]
methods: [0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Irreducible_polynomial
    locator: Simple examples
---

## Proof

1. Let $K$ be a [[field|0QA8CHH8MG]] and let $f \in K[x]$ with $\deg f \in \set{2, 3}$.
2. We first find the [[units|019NFGFPR5]] of $K[x]$. If $u v = 1$ in $K[x]$, then $\deg u + \deg v = 0$ by the [[degree of a product|0T233AZ1GE]]. So $\deg u = 0$, and $u$ is a nonzero constant.
3. Conversely, a nonzero constant $c \in K$ has the inverse $c^{-1} \in K$. So the units of $K[x]$ are exactly the polynomials of degree $0$.
4. Since $\deg f \ge 1$, the polynomial $f$ is nonzero and, by Step 3, it is not a unit.
5. Suppose that $f$ has a [[root|00EHX6FWC0]] $c \in K$. By the [[factor theorem|0K3MWA7DMC]], $f = (x - c) g$ for some $g \in K[x]$.
6. By the degree of a product, $\deg g = \deg f - 1 \ge 1$. By Step 3, neither $x - c$ nor $g$ is a unit. So $f$ is not [[irreducible|00X2A9G9W3]].
7. This proves: if $f$ is irreducible, then $f$ has no root in $K$.
8. Now suppose that $f$ has no root in $K$. Let $f = g h$ with $g, h \in K[x]$. We show that $g$ or $h$ is a unit.
9. Since $f \ne 0$, both $g$ and $h$ are nonzero. By the degree of a product, $\deg g + \deg h = \deg f \le 3$.
10. Suppose that neither $g$ nor $h$ is a unit. By Step 3, $\deg g \ge 1$ and $\deg h \ge 1$.
11. If both degrees were at least $2$, their sum would be at least $4$, which contradicts Step 9. So one factor, say $g$, has degree $1$.
12. Write $g = a x + b$ with $a, b \in K$ and $a \ne 0$. Then $g(-b/a) = -b + b = 0$.
13. [[Evaluation|0125QVNCFQ]] at $-b/a$ is a ring homomorphism. So $f(-b/a) = g(-b/a) \, h(-b/a) = 0$, and $-b/a$ is a root of $f$ in $K$.
14. This contradicts the assumption of Step 8. So $g$ or $h$ is a unit.
15. With Step 4, $f$ is irreducible over $K$. Together with Step 7, $f$ is irreducible over $K$ if and only if it has no root in $K$.

## Idea

A factorisation into two factors of positive degree splits the degree $2$ or $3$ as a sum of two positive integers. One of them must be $1$, and a factor of degree $1$ gives a root. Conversely, a root $c$ gives the factor $x - c$.
