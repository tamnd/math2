---
tag: 0BFN21TF5F
kind: statement
role: theorem
name: Path independence of line integrals
aliases: [conservative-iff-path-independent]
msc: [26B20]
uses: [05R9NF2J49, 0YS8RX87F4, 0SD237FEJD, 0FSCXYG856, 00ZEBSMNNV, 05AXG3QRKR]
sources:
  - url: https://en.wikipedia.org/wiki/Conservative_vector_field
    locator: Path independence
  - url: https://en.wikipedia.org/wiki/Conservative_vector_field
    locator: Path independence and conservative vector field
  - url: https://en.wikipedia.org/wiki/Gradient_theorem
    locator: Converse of the gradient theorem
---

## Statement

Let $U \subseteq \mathbb{R}^n$ be open and connected, and let $F \colon U \to \mathbb{R}^n$ be a continuous vector field.
The following are equivalent.

1. $F$ is [[conservative|05R9NF2J49]] on $U$.
2. For all piecewise $C^1$ curves $\gamma_1, \gamma_2$ in $U$ with the same initial point and the same end point, $\int_{\gamma_1} F \cdot d\mathbf{r} = \int_{\gamma_2} F \cdot d\mathbf{r}$.
3. For each closed piecewise $C^1$ curve $\gamma$ in $U$, $\int_\gamma F \cdot d\mathbf{r} = 0$.

## Remarks

Statement 1 implies statement 2 by the [[gradient theorem|0SD237FEJD]].
Statements 2 and 3 are equivalent: a closed curve splits into two curves with the same end points, and one uses [[reversal|0FSCXYG856]] and [[additivity|00ZEBSMNNV]].
Statement 2 implies statement 1: fix $p \in U$ and let $\phi(x) = \int_\gamma F \cdot d\mathbf{r}$ for a path $\gamma$ from $p$ to $x$. A short straight last segment in direction $e_i$ shows that $\partial \phi / \partial x_i = F_i$.
Connectedness is used to join $p$ to each point. On a disconnected set, apply the result on each component.

## Explanations

### L1 human

For a conservative field, the work from one point to another does not depend on the route.
Conversely, if the work never depends on the route, then the work from a fixed base point defines a potential for the field.
