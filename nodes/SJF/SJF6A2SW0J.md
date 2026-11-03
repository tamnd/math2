---
tag: SJF6A2SW0J
kind: definition
name: Relative degree
msc: [93C10, 93B18, 93B27]
defines: 115PDNE89R
uses: [PJWK0PKN6Q, 0V33BNKZ9S, 0299VCW1TH]
sources:
  - url: https://en.wikipedia.org/wiki/Feedback_linearization
---

## Definition

Let $W \subseteq \R^n$ be open, let $f, g \colon W \to \R^n$ be smooth [[vector fields|0299VCW1TH]] and let $h \colon W \to \R$ be a [[smooth function|0V33BNKZ9S]].
Consider the system $x' = f(x) + g(x) u$, $y = h(x)$ with scalar input $u$ and scalar output $y$.
For a smooth function $\lambda$ write $L_f \lambda = \nabla \lambda \cdot f$ for its [[Lie derivative|PJWK0PKN6Q]] along $f$, and $L_f^k$ for the $k$-fold iterate, with $L_f^0 \lambda = \lambda$.
The system has *relative degree* $r \ge 1$ at a point $x_0 \in W$ if:

1. $L_g L_f^k h(x) = 0$ for all $x$ in a neighbourhood of $x_0$ and all $k$ with $0 \le k \le r - 2$;
2. $L_g L_f^{r-1} h(x_0) \ne 0$.

## Remarks

Along a solution, clause 1 gives $y^{(k)} = L_f^k h(x)$ for $k < r$, and clause 2 shows that $y^{(r)} = L_f^r h(x) + L_g L_f^{r-1} h(x)\, u$ depends on $u$.
Example: for $x_1' = x_2$, $x_2' = -\sin x_1 + u$, $y = x_1$, one has $f = (x_2, -\sin x_1)$, $g = (0, 1)$, $L_g h = 0$, $L_f h = x_2$ and $L_g L_f h = 1$, so the relative degree is $2$ at every point.
With the output $y = x_2$ instead, $L_g h = 1$ and the relative degree is $1$.
Non-example: for the same system with $y = x_1^2$, one has $L_g h = 0$ everywhere and $L_g L_f h = 2 x_1$.
This vanishes at $x_0 = 0$ but not on a neighbourhood of $0$, so no $r$ satisfies the definition at $0$.
For a linear system $x' = A x + b u$, $y = c x$, the relative degree is the least $r$ with $c A^{r-1} b \ne 0$.
It equals the degree of the denominator minus the degree of the numerator of the transfer function.
