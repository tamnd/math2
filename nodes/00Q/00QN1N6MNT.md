---
tag: 00QN1N6MNT
kind: definition
name: Positive definite quadratic form
msc: [15A63, "11E04"]
defines: 0RP20HFYM3
uses: [0HZNE5QZDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_quadratic_form
    locator: lead section
---

## Definition

Let $V$ be a finite-dimensional real vector space, and let $Q$ be a [[quadratic form|0RBQS1JJCR]] on $V$.
The form $Q$ is *positive definite* when
$$Q(v) > 0 \qquad \text{for all } v \in V \text{ with } v \ne 0.$$

## Remarks

$Q(x) = x^T A x$ with $A$ symmetric is positive definite if and only if $A$ is a [[positive definite matrix|0KX66CZMBB]].
Equivalently, the signature of $Q$ is $(n, 0, 0)$, with $n = \dim V$.
The form $x^2 + y^2$ is positive definite on $\R^2$; the forms $x^2 - y^2$ and $x^2$ are not.
$Q$ is positive definite if and only if its associated symmetric bilinear form is an inner product.

## Explanations

### L1 human

A positive definite quadratic form is positive everywhere except at the origin.
Its graph is a bowl with the lowest point at the origin.
Such forms describe squared lengths for different inner products.
