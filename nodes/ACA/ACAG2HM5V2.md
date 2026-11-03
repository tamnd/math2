---
tag: ACAG2HM5V2
kind: definition
name: Norm residue symbol
msc: [11S31, 19F15]
defines: GBDFSDV23C
uses: [J85FZEQG38, 0WX11EA3F3, SHEN158T3M, 0XTY86BZKY, WFG4YMBYVQ]
sources:
  - url: https://en.wikipedia.org/wiki/Symbol_(number_theory)
---

## Definition

Let $K$ be a [[local field|J85FZEQG38]], and let $n \ge 1$ be an integer prime to the characteristic of $K$.
Assume that $K$ contains the group $\mu_n$ of $n$-th [[roots of unity|0WX11EA3F3]], of order $n$.
Let $K^{ab}$ be the maximal abelian extension of $K$, and let $\theta \colon K^\times \to \Gal(K^{ab}/K)$ be the reciprocity map of [[local class field theory|SHEN158T3M]].
For $a, b \in K^\times$, choose $\beta$ in an algebraic closure of $K$ with $\beta^n = b$; then $K(\beta) \subseteq K^{ab}$.
The *norm residue symbol* of degree $n$ is
$$(a, b)_n = \frac{\theta(a)(\beta)}{\beta} \in \mu_n.$$

## Remarks

The value lies in $\mu_n$ because $\theta(a)(\beta)$ is again an $n$-th root of $b$, and it does not depend on the choice of $\beta$, since $\theta(a)$ fixes $\mu_n \subseteq K$.
The symbol is multiplicative in each variable, satisfies $(a, 1 - a)_n = 1$ for $a \ne 0, 1$, and $(a, b)_n = 1$ if and only if $a$ is a norm from $K(\beta)$ to $K$.
Some books use $\theta(b)$ acting on an $n$-th root of $a$ instead; the two conventions give inverse values.

Example: for $n = 2$ and $K = \R$, the reciprocity map sends $a < 0$ to complex conjugation and $a > 0$ to the identity of $\Gal(\C/\R)$.
For $a = b = -1$ and $\beta = i$, $(-1, -1)_2 = \bar{i}/i = -1$, the value of the [[Hilbert symbol|WFG4YMBYVQ]].

Non-example: the field $\Q_3$ does not contain a primitive cube root of unity, since $\mu(\Q_3) = \set{\pm 1}$.
So the norm residue symbol of degree $3$ is not defined on $\Q_3$; the definition needs $\mu_n \subseteq K$.
