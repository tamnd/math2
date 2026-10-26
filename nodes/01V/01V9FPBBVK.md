---
tag: 01V9FPBBVK
kind: statement
role: theorem
name: Symmetry of second derivatives
aliases: [equality-of-mixed-partials]
msc: [26B05]
uses: [0EY05Z9RPN, 02RSXVM1ZN, 0135XZZQ8M]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetry_of_second_derivatives
    locator: Sufficiency of twice-differentiability
  - url: https://en.wikipedia.org/wiki/Symmetry_of_second_derivatives
    locator: Requirement of continuity
  - url: https://en.wikipedia.org/wiki/Symmetry_of_second_derivatives
    locator: History
same_as:
  wikidata: Q1503239
  wikipedia: Symmetry of second derivatives
---

## Statement

Let $U \subseteq \mathbb{R}^n$ be open, let $f \colon U \to \mathbb{R}^m$, and let $a \in U$.
Suppose that $f$ is [[differentiable|0135XZZQ8M]] at each point of $U$, and that the derivative $Df \colon U \to L(\mathbb{R}^n, \mathbb{R}^m)$ is differentiable at $a$.
Then the second derivative $D^2 f(a)$ is a symmetric bilinear map: $D^2 f(a)(u, v) = D^2 f(a)(v, u)$ for all $u, v \in \mathbb{R}^n$.
In particular, $\dfrac{\partial^2 f}{\partial x_i \, \partial x_j}(a) = \dfrac{\partial^2 f}{\partial x_j \, \partial x_i}(a)$ for all $i, j$.

## Remarks

Here $D^2 f(a)$ is the [[iterated derivative|0EY05Z9RPN]] of order $2$, and $D^2 f(a)(e_i, e_j)$ is the mixed [[partial derivative|02RSXVM1ZN]] $\partial_i \partial_j f(a)$.
The hypothesis is that $f$ is twice differentiable at $a$. It holds when the second partial derivatives are continuous near $a$, which gives [[Schwarz's theorem|0NNQY8WCW6]].
The existence of the second partial derivatives at $a$ is not enough: there is a [[function with unequal mixed partial derivatives|01NN8NY497]].

## History

Euler published a proposed proof in 1740, and many incomplete proofs followed over more than a century.
In 1867 Lindelöf analysed the earlier proofs and gave a counterexample to the general claim.
Schwarz gave the first rigorous proof six years later, and Jordan gave in 1883 the general version that most textbooks use.

## Explanations

### L1 human

The theorem says that the order of two differentiations does not matter, when $f$ is regular enough.
For $f(x, y) = x^3 y^2$, differentiating first in $x$ and then in $y$ gives $6 x^2 y$, and the other order gives $6 x^2 y$ too.
