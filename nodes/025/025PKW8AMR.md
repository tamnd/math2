---
tag: 025PKW8AMR
kind: statement
role: theorem
name: Uniqueness of solutions for Lipschitz vector fields
msc: [34A12]
uses: [055VVSN00V, 04SW7WECS8, 07EJHQYR9A, 075VBY4K4X]
sources:
  - url: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem
    locator: Theorem
  - url: https://en.wikipedia.org/wiki/Gr%C3%B6nwall%27s_inequality
    locator: lead section
---

## Statement

Let $D$ be an open subset of $\mathbb{R} \times \mathbb{R}^n$ and let $f : D \to \mathbb{R}^n$ be continuous.
Assume that $f$ is locally Lipschitz in $x$. That is, each point of $D$ has a neighbourhood $V \subseteq D$ and a constant $K \ge 0$ such that $\|f(t, x) - f(t, y)\| \le K \|x - y\|$ whenever $(t, x), (t, y) \in V$.
Let $I$ be an interval, and let $\gamma_1, \gamma_2 : I \to \mathbb{R}^n$ be two [[solutions|04SW7WECS8]] of $x' = f(t, x)$ whose graphs lie in $D$.
If $\gamma_1(t_0) = \gamma_2(t_0)$ for one $t_0 \in I$, then $\gamma_1(t) = \gamma_2(t)$ for all $t \in I$.

## Remarks

So an [[initial value problem|075VBY4K4X]] for such an $f$ has at most one solution on each interval that contains $t_0$.
Proof idea: the function $u(t) = \|\gamma_1(t) - \gamma_2(t)\|$ satisfies $u(t) \le K \left| \int_{t_0}^{t} u(s)\, ds \right|$ near $t_0$. Then [[Grönwall's inequality|07EJHQYR9A]] gives $u = 0$. A connectedness argument extends this to all of $I$.
A $C^1$ function $f$ is locally Lipschitz in $x$.
Without the Lipschitz condition, uniqueness can fail. See the [[non-uniqueness example|00K7ASZ1PR]].

## Explanations

### L1 human

Two solutions of a Lipschitz equation that meet at one time are the same solution.
So the graphs of different solutions never cross or touch.
