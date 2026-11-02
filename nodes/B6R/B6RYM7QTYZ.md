---
tag: B6RYM7QTYZ
kind: statement
role: proposition
name: Density of simple functions in Lp
msc: ["46E30", 28A20]
uses: [SASP14MA1Z, 7WMBX7M4P6, P15VQS5DJ9, 0BSJSX7ME2]
about: [SASP14MA1Z, 7WMBX7M4P6]
sources:
  - url: https://en.wikipedia.org/wiki/Lp_space
---

## Statement

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]] and let $1 \le p < \infty$.
Let $S$ be the set of [[simple functions|7WMBX7M4P6]] $s = \sum_{i=1}^{n} a_i \mathbf{1}_{A_i}$ with $A_i \in \Sigma$ and $\mu(A_i) < \infty$ for each $i$.
Then $S$ is a [[dense|0BSJSX7ME2]] subset of [[$L^p(\mu)$|SASP14MA1Z]].

## Remarks

For $f \ge 0$ in $L^p$, take simple functions $0 \le s_n \le f$ that increase pointwise to $f$.
Each $s_n$ vanishes outside a set of finite measure, because $s_n^p \le f^p$ is integrable.
Since $\abs{f - s_n}^p \le f^p$, the [[dominated convergence theorem|BYNV84PF86]] gives $\norm{f - s_n}_p \to 0$.
A general $f$ is split into the positive and negative parts of its real and imaginary parts.

The hypothesis $p < \infty$ is necessary.
On $\R$ with [[Lebesgue measure|2Z2QVWZ262]], the constant function $1$ lies in $L^\infty$, but every $s \in S$ vanishes outside a set of finite measure, so $\norm{1 - s}_\infty \ge 1$.
In $L^\infty(\mu)$ the set of all simple functions, without the condition $\mu(A_i) < \infty$, is dense.

On $\R^n$ the result is the first step towards the density of step functions and of continuous functions with compact support in $L^p$, $1 \le p < \infty$.

## Explanations

### L1 human

Every function in $L^p$ can be approximated as well as one wants by a staircase function that takes only finitely many values.
The steps of the staircase sit on sets of finite measure.
This lets one prove a fact about all of $L^p$ by checking it on indicator functions of sets and then passing to the limit.

### L2 human

The standard way to prove an inequality or an identity on $L^p$ is to check it on a dense class and extend it by continuity.
Simple functions are the first such class; they are used in the proof of the [[dual of Lp|Q1V7ZNS332]] and in interpolation theorems such as the [[Riesz–Thorin theorem|AGRKRG1TMJ]].
For $p = \infty$ the density of all simple functions is a uniform approximation, which is why the finite measure condition must then be dropped.
