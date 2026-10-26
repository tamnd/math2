---
tag: ~9db1e4cc
kind: statement
role: theorem
name: Curl-free vector field on a convex set is conservative
aliases: [poincare-lemma-for-vector-fields]
msc: [26B12]
uses: [~979a322d, ~94fe5da2, ~7d806e54, ~300da8c7, ~4f892e84, ~e6672d67]
sources:
  - url: https://en.wikipedia.org/wiki/Conservative_vector_field
    locator: Irrotational vector fields
  - url: https://en.wikipedia.org/wiki/Poincar%C3%A9_lemma
    locator: Direct proof
---

## Statement

Let $U \subseteq \mathbb{R}^3$ be open and convex, and let $F \colon U \to \mathbb{R}^3$ be a vector field of class $C^1$ with $\nabla \times F = 0$ on $U$.
Then $F$ is [[conservative|~94fe5da2]] on $U$.
Explicitly, for a fixed $p \in U$, the function
$$\phi(x) = \int_0^1 F\big(p + t (x - p)\big) \cdot (x - p) \, dt$$
satisfies $\nabla \phi = F$ on $U$.

## Remarks

The integral $\phi(x)$ is the [[line integral|~e6672d67]] of $F$ along the segment from $p$ to $x$. Convexity makes sure that this segment lies in $U$.
To prove $\nabla \phi = F$, [[differentiate under the integral sign|~4f892e84]] and use $\partial_j F_i = \partial_i F_j$, which is the condition $\nabla \times F = 0$.
The same proof works in $\mathbb{R}^n$ under the condition $\partial_j F_i = \partial_i F_j$ for all $i, j$, and on star-shaped open sets.
The result holds more generally on simply connected open sets. It [[fails on some other open sets|~0744e9de]]. With the [[converse|~300da8c7]], it gives: on a convex open set, a $C^1$ field is conservative if and only if its curl is zero.

## Explanations

### L1 human

On a convex set, a field with no swirl is the gradient of a potential.
You build the potential by computing the work of the field along straight segments from one base point.
