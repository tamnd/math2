---
tag: ~b8eba9e2
kind: statement
role: theorem
name: Lagrange multipliers
aliases: [lagrange-multiplier-theorem, method-of-lagrange-multipliers]
msc: [90C46]
uses: [~4a494398, ~f1a69b70, ~35460963, ~896c035b, ~c4a20657, ~1adf7722]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange_multiplier
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Lagrange_multiplier
    locator: Multiple constraints
same_as:
  wikidata: Q598870
  wikipedia: Lagrange multiplier
---

## Statement

Let $U \subseteq \mathbb{R}^n$ be open, let $m < n$, and let $f \colon U \to \mathbb{R}$ and $g = (g_1, \dots, g_m) \colon U \to \mathbb{R}^m$ be of [[class C^1|~1adf7722]].
Let $M = \{x \in U : g(x) = 0\}$, and let $a \in M$ be a [[local extremum|~f1a69b70]] of the restriction of $f$ to $M$.
Suppose that the [[gradients|~35460963]] $\nabla g_1(a), \dots, \nabla g_m(a)$ are linearly independent.
Then there is a unique $\lambda = (\lambda_1, \dots, \lambda_m) \in \mathbb{R}^m$ such that
$$\nabla f(a) = \lambda_1 \nabla g_1(a) + \dots + \lambda_m \nabla g_m(a).$$

## Remarks

The numbers $\lambda_i$ are the Lagrange multipliers. Equivalently, $(a, \lambda)$ is a critical point of the Lagrangian $L(x, \lambda) = f(x) - \lambda \cdot g(x)$.
The hypothesis on the gradients is the constraint qualification. It says that the [[Jacobian matrix|~896c035b]] $Dg(a)$ has rank $m$.
The proof uses the [[implicit function theorem|~c4a20657]]. Near $a$, the set $M$ is the graph of a $C^1$ function of $n - m$ variables. The gradient of $f$ is orthogonal to the tangent space of $M$ at $a$.
The condition is necessary, not sufficient. Each candidate point needs a further check, for example a comparison of values on a compact set $M$.

## Explanations

### L1 human

At a constrained extremum, a small move along the constraint set does not change $f$ to first order.
So $\nabla f(a)$ has no component along the constraint set, and it is a combination of the normals $\nabla g_i(a)$.
This turns a constrained problem into a system of $n + m$ equations in $n + m$ unknowns.
