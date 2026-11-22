---
tag: 02STTYFBVY
kind: definition
name: Polar form of a quadratic form
msc: ["15A63", "11E04"]
defines: 0HYFWKKY3C
topics: [6TSCEW8QMK]
audience: ug1
uses: [0HZNE5QZDJ, 0744CN4MDA]
sources:
  - url: https://en.wikipedia.org/wiki/Polarization_of_an_algebraic_form
    locator: Examples
---

## Definition

The polar form of a quadratic form is the bilinear map that measures how far the form is from being additive.
Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $Q$ be a [[quadratic form|0HZNE5QZDJ]] on $V$.
The *polar form* of $Q$ is the map $b_Q \colon V \times V \to F$ with
$$b_Q(u, v) = Q(u + v) - Q(u) - Q(v) \qquad (u, v \in V).$$

## Remarks

The definition uses no division, so it makes sense in every characteristic.
The definition of a quadratic form already requires $b_Q$ to be bilinear, and $b_Q$ is symmetric because $u + v = v + u$.
So $b_Q$ is a [[symmetric bilinear form|0744CN4MDA]], and putting $u = v$ gives $b_Q(v, v) = Q(2v) - 2Q(v) = 2Q(v)$.

A small example: for $Q(x) = x^{\mathsf{T}} A x$ on $F^n$, with any square matrix $A$, expanding gives
$$b_Q(x, y) = x^{\mathsf{T}} A y + y^{\mathsf{T}} A x = x^{\mathsf{T}} (A + A^{\mathsf{T}})\, y.$$
For $Q(x) = x^2$ on $\mathbb{R}$ this is $(x + y)^2 - x^2 - y^2 = 2xy$.

Many authors divide by $2$ when the characteristic is not $2$, so that the result $B$ satisfies $B(v, v) = Q(v)$; that half is [[the associated symmetric bilinear form|0TX2YH2FQS]].
Outside characteristic $2$, [[quadratic forms and symmetric bilinear forms correspond|VN9AG8JKYT]] by this construction.
In characteristic $2$, $b_Q(v, v) = 0$ for every $v$, and [[the correspondence fails|ZEGSCCVGZF]].
[[The concept of the polar form|0HYFWKKY3C]] works out these cases.

## Explanations

### L1 human

The polar form recovers a product of two vectors from a quadratic form.
For $Q(x) = x^2$ on the real line, the polar form is $(x + y)^2 - x^2 - y^2 = 2xy$, twice the ordinary product.
It is the algebraic side of the [[polarization identity|05FKHRT0B4]] for inner products.
