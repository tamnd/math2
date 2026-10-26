---
tag: 0TX2YH2FQS
kind: definition
name: Symmetric bilinear form associated with a quadratic form
msc: [15A63, "11E04"]
defines: 0KRVRV5V80
uses: [0HZNE5QZDJ, 02STTYFBVY, 0744CN4MDA]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Definitions
---

## Definition

Let $F$ be a field of characteristic not $2$, and let $V$ be a finite-dimensional vector space over $F$.
Let $Q$ be a [[quadratic form|0RBQS1JJCR]] on $V$.
The *symmetric bilinear form associated with* $Q$ is
$$B(u, v) = \tfrac{1}{2} \bigl( Q(u + v) - Q(u) - Q(v) \bigr) \qquad (u, v \in V).$$

## Remarks

$B$ is a [[symmetric bilinear form|0AXZNE5XNH]] with $B(v, v) = Q(v)$, and it is the only one.
Conversely, each symmetric bilinear form $B$ gives the quadratic form $v \mapsto B(v, v)$; the two constructions are inverse to each other.
For $Q(x) = x^T A x$ with $A$ symmetric, $B(x, y) = x^T A y$.
It is half of the [[polar form|0HYFWKKY3C]] of $Q$.

## Explanations

### L1 human

Outside characteristic $2$, quadratic forms and symmetric bilinear forms are the same thing in two forms.
From $B$, we get $Q$ by putting the same vector twice.
From $Q$, we get $B$ by this formula.
