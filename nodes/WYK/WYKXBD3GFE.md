---
tag: WYKXBD3GFE
kind: example
name: Torsion-free groups form a universal Horn class
aliases: [torsion-free-groups-universal-horn-class, torsion-free-groups-quasivariety]
msc: ["03C52", "20A15"]
topics: [JYJHB4YBAH]
audience: grad
instance_of: [9A4CYWXPEA, WRXEKT4NQS]
uses: [9A4CYWXPEA, PEMNN32A43, G5S1M9, WRXEKT4NQS, 94GVY3APPQ, APF4KHZ976]
sources:
  - book: isbn:9780521587136
---

## Example

Let $L = \set{\cdot, {}^{-1}, e}$.
A [[group|G5S1M9]] is [[torsion-free|PEMNN32A43]] if $x^n = e$ implies $x = e$ for every $n \ge 1$.
The class of torsion-free groups is a [[universal Horn class|9A4CYWXPEA]], and in fact a [[quasivariety|WRXEKT4NQS]].

1. The group axioms are identities, such as $\forall x \forall y \forall z \, ((xy)z = x(yz))$, $\forall x \, (xe = x)$ and $\forall x \, (x x^{-1} = e)$.
2. For each $n \ge 1$ the sentence $\tau_n = \forall x \, (x^n = e \rightarrow x = e)$ is a [[quasi-identity|94GVY3APPQ]], where $x^n$ is the product of $n$ copies of $x$.
3. A group satisfies every $\tau_n$ exactly when it is torsion-free, so the class is the class of models of the identities and the $\tau_n$.
4. So the class is closed under subgroups, direct products and reduced products. For a direct check on products: if $(g_i)^n = e$ in $\prod_i G_i$, then $g_i^n = e$ in each factor, so each $g_i = e$.

## Remarks

The class is not a variety: $\mathbb{Z}$ is torsion-free, and its homomorphic image $\mathbb{Z} / 2\mathbb{Z}$ is not.
The sentences $\tau_p$ for primes $p$ already suffice, since an element of finite order $m > 1$ has a power of prime order.
No finite set of axioms suffices, by [[this theorem|APF4KHZ976]]; for finitely many primes, $\mathbb{Z} / q\mathbb{Z}$ with a larger prime $q$ satisfies the corresponding $\tau_p$.
The torsion groups behave in the opposite way: $\prod_{n \ge 1} \mathbb{Z} / n\mathbb{Z}$ is a product of finite groups, and the element $(1, 1, 1, \ldots)$ has infinite order.
So the torsion groups are not closed under products and form no universal Horn class.
Torsion-free abelian groups also form a quasivariety, by adding the identity $\forall x \forall y \, (xy = yx)$.

## Explanations

### L1 human

In a torsion-free group, no element other than the identity returns to the identity when you repeat it.
The whole numbers under addition are like this: adding $3$ to itself never gives $0$.
A clock with $12$ hours is not: adding $12$ hours brings you back.
The rule "if $x$ repeated $n$ times is the identity, then $x$ is the identity" is an "if, then" rule, so it survives products and subgroups.

### L2 human

We check the axiom $\tau_2$ in a product and see how it fails in a quotient.

1. In $\mathbb{Z} \times \mathbb{Z}$, the element $(a, b)$ satisfies $2(a, b) = (0, 0)$ only if $2a = 0$ and $2b = 0$, so $a = b = 0$.
2. In $\mathbb{Z} / 2\mathbb{Z}$, the element $1$ satisfies $1 + 1 = 0$ with $1 \ne 0$, so $\tau_2$ fails.
3. The quotient map $\mathbb{Z} \to \mathbb{Z} / 2 \mathbb{Z}$ is a surjective homomorphism, so quasi-identities are not preserved by homomorphic images.

The pattern applies to every quasivariety that is not a variety: some quotient breaks a hypothesis-conclusion law.
A trap is to treat torsion-freeness as one first-order sentence; it is the infinite conjunction of the $\tau_n$, and no finite part of it defines the class.
