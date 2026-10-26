---
tag: 0GYDV9FE98
kind: statement
role: theorem
name: Second derivative test in several variables
aliases: [second-partial-derivative-test]
msc: [49K10]
uses: [0SCSQWXRA4, 01RBSSGMY5, 00N3T18QNA, 04CPG9K1C4, 0P30YYZN85, 0TCBZMEYGN]
sources:
  - url: https://en.wikipedia.org/wiki/Second_partial_derivative_test
    locator: Functions of many variables
  - url: https://en.wikipedia.org/wiki/Second_partial_derivative_test
    locator: Functions of two variables
same_as:
  wikidata: Q7443745
  wikipedia: Second partial derivative test
---

## Statement

Let $U \subseteq \mathbb{R}^n$ be open, let $f \colon U \to \mathbb{R}$ be of [[class C^2|0TCBZMEYGN]] on $U$, and let $a \in U$ with $\nabla f(a) = 0$.
Let $H = H_f(a)$ be the [[Hessian matrix|0SCSQWXRA4]] of $f$ at $a$.

1. If $H$ is [[positive definite|01RBSSGMY5]], then $f$ has a strict [[local minimum|04CPG9K1C4]] at $a$.
2. If $H$ is negative definite, then $f$ has a strict local maximum at $a$.
3. If $H$ has a positive and a negative eigenvalue, then $a$ is a [[saddle point|00N3T18QNA]] of $f$.

In the other cases the test gives no conclusion.

## Remarks

For $n = 2$, let $D = f_{xx}(a) f_{yy}(a) - f_{xy}(a)^2$ be the determinant of $H$. If $D > 0$ and $f_{xx}(a) > 0$, then $a$ is a local minimum. If $D > 0$ and $f_{xx}(a) < 0$, then $a$ is a local maximum. If $D < 0$, then $a$ is a saddle point.
The proof uses the [[second-order Taylor expansion|0P30YYZN85]]. If $H$ is positive definite, then $h^{\mathsf{T}} H h \ge m \|h\|^2$ for some $m > 0$, and this term dominates the remainder.
The functions $x^4 + y^4$, $-(x^4 + y^4)$ and $x^4 - y^4$ all have zero Hessian at the origin. The origin is a minimum, a maximum and a saddle point, respectively, so the test cannot decide when $H$ is singular and semidefinite.
By Sylvester's criterion, $H$ is positive definite if and only if all its leading principal minors are positive.

## Explanations

### L1 human

At a critical point the tangent plane is flat, so the second derivatives decide the shape of the graph.
If the graph bends upward in every direction, the point is a minimum. If it bends down in every direction, the point is a maximum.
If it bends up in some directions and down in others, the point is a saddle.
