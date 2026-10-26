---
tag: 02STTYFBVY
kind: definition
name: Polar form of a quadratic form
msc: [15A63, "11E04"]
defines: 0HYFWKKY3C
uses: [0HZNE5QZDJ, 0744CN4MDA]
sources:
  - url: https://en.wikipedia.org/wiki/Polarization_of_an_algebraic_form
    locator: Examples
---

## Definition

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $Q$ be a [[quadratic form|0RBQS1JJCR]] on $V$.
The *polar form* of $Q$ is the map $B_Q \colon V \times V \to F$ with
$$B_Q(u, v) = Q(u + v) - Q(u) - Q(v).$$

## Remarks

$B_Q$ is a [[symmetric bilinear form|0AXZNE5XNH]], and $B_Q(v, v) = 2 Q(v)$ for all $v$.
For $Q(x) = x^T A x$ on $F^n$, $B_Q(x, y) = x^T (A + A^T) y$.
Many authors divide by $2$ when the characteristic is not $2$, so that the result $B$ satisfies $B(v, v) = Q(v)$; see [[the associated form|0KRVRV5V80]].
This construction is the degree $2$ case of the polarisation of homogeneous polynomials.

## Explanations

### L1 human

The polar form recovers a bilinear form from a quadratic form.
For $Q(x) = x^2$ on $\R$, the polar form is $(x + y)^2 - x^2 - y^2 = 2xy$.
It is the algebraic form of the [[polarisation identity|05FKHRT0B4]] for inner products.
