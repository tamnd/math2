---
tag: E4P30YHWEQ
kind: definition
name: Differential equations in Banach spaces
msc: [34G10, 34G20, 47D06]
defines: JN7362WCD8
uses: [06GZ956657, 06EKW1AKXF, 0NT64JV96A, 0FXDW992DS, 020M04FN1H]
sources:
  - url: https://en.wikipedia.org/wiki/Abstract_differential_equation
---

## Definition

Let $X$ be a [[Banach space|06GZ956657]] over $\R$ or $\C$ with norm $\norm{\cdot}$, and let $J \subseteq \R$ be an interval.
A function $u \colon J \to X$ is *differentiable* at $t \in J$ if the limit $u'(t) = \lim_{h \to 0} \frac{u(t + h) - u(t)}{h}$ exists in the norm of $X$.
Let $D \subseteq X$ and $F \colon J \times D \to X$.
A *differential equation in $X$* is the equation $u'(t) = F(t, u(t))$.
A *(classical) solution* on $J$ is a continuously differentiable $u \colon J \to X$ with $u(t) \in D$ and $u'(t) = F(t, u(t))$ for all $t \in J$.
In the main linear case, $F(t, u) = A u + f(t)$, where $A \colon D(A) \to X$ is a linear operator, $D = D(A)$ and $f \colon J \to X$.
The [[initial value problem|0FXDW992DS]] $u' = A u$, $u(0) = u_0$ is the *abstract Cauchy problem*.

## Remarks

Example: if $A$ is a bounded operator on $X$, then $u(t) = e^{tA} u_0 = \sum_{k \ge 0} \frac{t^k}{k!} A^k u_0$ solves the abstract Cauchy problem on $\R$.
The series converges in [[operator norm|06EKW1AKXF]] since $\norm{A^k} \le \norm{A}^k$, and term-by-term differentiation gives $u' = A u$.
For $X = \R^n$ this is the [[matrix exponential|020M04FN1H]] solution of a linear system of [[ordinary differential equations|0NT64JV96A]].

Non-example: take $X = C([0, 1])$ with the supremum norm and $u(t) = (s \mapsto \abs{s - t})$ for $t \in [0, 1]$.
For each fixed $s$, the number $u(t)(s)$ has a derivative in $t$ for $t \neq s$, equal to $-\sgn(s - t)$.
But the difference quotients $\frac{u(t + h) - u(t)}{h}$ do not converge in the supremum norm: their pointwise limit $s \mapsto -\sgn(s - t)$ is not continuous for $0 < t < 1$.
So $u$ is not differentiable as a map into $X$, and it is not a classical solution of any differential equation in $X$.

When $A$ is closed but unbounded, the Cauchy problem is well posed exactly when $A$ generates a strongly continuous semigroup $T(t)$, and then $u(t) = T(t) u_0$.

## Explanations

### L1 human

The unknown is a moving point in a Banach space, and its velocity is computed in the norm of that space.
Bounded operators behave like matrices; unbounded ones, such as derivatives in space, need more care.
