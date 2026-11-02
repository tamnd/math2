---
tag: 85Y0XMYHGG
kind: definition
name: Unitization
msc: [46H05, 16S99]
defines: 7SB03M850M
uses: [0CD87SFM2N, 4DJ4V5VBSH]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_algebra
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $A$ be an [[associative algebra|3CTW1P4HBP]] over $\mathbb{K}$, with or without a unit.
The *unitization* of $A$ is the vector space $A^+ = \mathbb{K} \times A$ with the product
$$(\lambda, a)(\mu, b) = (\lambda \mu,\ \lambda b + \mu a + a b).$$
It is an associative algebra over $\mathbb{K}$ with unit $(1, 0)$.
The map $a \mapsto (0, a)$ embeds $A$ in $A^+$ as a [[two-sided ideal|0CD87SFM2N]] of codimension $1$.

## Remarks

One writes $(\lambda, a)$ as $\lambda 1 + a$.
Every algebra homomorphism $\varphi$ from $A$ to a unital algebra $B$ extends uniquely to a unital homomorphism $A^+ \to B$, by $\lambda 1 + a \mapsto \lambda 1_B + \varphi(a)$.
If $A$ is a [[normed algebra|4DJ4V5VBSH]], then $\norm{(\lambda, a)} = \abs{\lambda} + \norm{a}$ makes $A^+$ a normed algebra, complete when $A$ is complete.
Indeed $\abs{\lambda \mu} + \norm{\lambda b + \mu a + a b} \le (\abs{\lambda} + \norm{a})(\abs{\mu} + \norm{b})$.
For a C*-algebra $A$ one uses another norm on $A^+$, which makes it a C*-algebra.
The construction adds a new unit even when $A$ already has one.

Example: for $A = C_0(\R)$, the complex continuous functions that tend to $0$ at infinity, $A^+$ is isomorphic to the functions $f + \lambda$ with $f \in A$ and $\lambda \in \C$.
These are the continuous functions on $\R$ with one common limit at $+\infty$ and $-\infty$.
They are the continuous functions on the one-point compactification of $\R$.

Non-example: the componentwise product $(\lambda, a)(\mu, b) = (\lambda \mu, a b)$ on $\mathbb{K} \times A$ gives no unitization when $A \neq 0$.
For it, $(1, 0)(\mu, b) = (\mu, 0)$, so $(1, 0)$ is not a unit.
