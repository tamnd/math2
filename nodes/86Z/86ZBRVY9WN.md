---
tag: 86ZBRVY9WN
kind: proof
name: Proof that every polynomial has a root in some extension field
msc: [12F05]
proves: 0VG02M1FEZ
uses: [0QA8CHH8MG, 0WQ1A8SHTZ, 00EHX6FWC0, 00X2A9G9W3, 0BDX4MBKT4, 0T233AZ1GE, 019NFGFPR5, 0AWMPX35CW, 0M893X7YY7, 09N7DZ7SDB, 0VFW4Y69BT, 0GK1WB9R98, 06K7SARZKR, 0ZN39QDTP9, 0N5QW9K7MH]
sources:
  - url: https://en.wikipedia.org/wiki/Splitting_field
    locator: Constructing splitting fields
  - url: https://www.jmilne.org/math/CourseNotes/FT.pdf
    locator: Chapter 1, Stem fields
---

## Proof

1. Let $K$ be a [[field|0QA8CHH8MG]] and $f \in K[x]$ with $\deg f \ge 1$. The [[units|019NFGFPR5]] of $K[x]$ are the nonzero constants, by the [[degree of a product|0T233AZ1GE]].
2. Among the [[monic|0BDX4MBKT4]] divisors of $f$ of degree at least $1$, choose one, $g$, of least degree. One exists: $f$ times the inverse of its leading coefficient.
3. The polynomial $g$ is [[irreducible|00X2A9G9W3]]. It is nonzero and not a unit, since $\deg g \ge 1$.
4. Suppose $g = a b$ with $a, b \in K[x]$ both of degree at least $1$. Then $\deg a < \deg g$, and $a$ times the inverse of its leading coefficient is a monic divisor of $f$. This contradicts the choice of $g$.
5. So in every factorisation $g = a b$, one factor has degree $0$, so it is a unit. Write $f = g k$ with $k \in K[x]$.
6. Let $L = K[x]/(g)$, the [[quotient ring|0VFW4Y69BT]]. Since $g$ is irreducible, [[$L$ is a field|0AWMPX35CW]].
7. The map $K \to L$, $c \mapsto c + (g)$, is a ring homomorphism from a field to a nonzero ring. So it is [[injective|09N7DZ7SDB]]. As in [[adjoining a root|0M893X7YY7]], we identify $K$ with its image, so $L/K$ is a [[field extension|0WQ1A8SHTZ]].
8. Let $\alpha = x + (g) \in L$. For every $h \in K[x]$, the quotient map is a ring homomorphism that fixes $K$, so $h + (g) = h(\alpha)$.
9. In particular $g(\alpha) = g + (g) = 0$. Then $f(\alpha) = g(\alpha) k(\alpha) = 0$, so $\alpha$ is a [[root|00EHX6FWC0]] of $f$ in $L$.
10. Since $g$ is monic, irreducible and $g(\alpha) = 0$, the [[minimal polynomial|0GK1WB9R98]] $m_\alpha$ of $\alpha$ [[divides|06K7SARZKR]] $g$. As $\deg m_\alpha \ge 1$, the cofactor is a unit, and since both are monic, $g = m_\alpha$.
11. By Step 8, $L = \set{ h(\alpha) : h \in K[x] }$. By the [[structure of simple extensions|0ZN39QDTP9]], this set is $K(\alpha)$, so $L = K(\alpha)$.
12. By the [[degree of a simple extension|0N5QW9K7MH]], $[L : K] = \deg m_\alpha = \deg g$.
13. Since $f = g k$ with $f \ne 0$, we have $k \ne 0$ and $\deg f = \deg g + \deg k \ge \deg g$. So $[L : K] \le \deg f$, and $f$ has the root $\alpha$ in $L$.

## Idea

Pick an irreducible factor $g$ of $f$ and force a root of $g$ to exist by working modulo $g$. The quotient $K[x]/(g)$ is a field because $g$ is irreducible, and the class of $x$ is a root of $g$, hence of $f$. Its degree over $K$ is $\deg g$, which is at most $\deg f$.
