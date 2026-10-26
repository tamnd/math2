---
tag: 0NNQY8WCW6
kind: statement
role: theorem
name: Schwarz's theorem for C^2 functions
aliases: [clairaut-theorem, schwarz-theorem]
msc: [26B05]
uses: [01V9FPBBVK, 02RSXVM1ZN, 0TCBZMEYGN]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetry_of_second_derivatives
    locator: Schwarz's theorem
---

## Statement

Let $U \subseteq \mathbb{R}^n$ be open and let $f \colon U \to \mathbb{R}$ be of [[class C^2|0TCBZMEYGN]] on $U$.
Then for all $i, j \in \{1, \dots, n\}$ and each $a \in U$,
$$\frac{\partial^2 f}{\partial x_i \, \partial x_j}(a) = \frac{\partial^2 f}{\partial x_j \, \partial x_i}(a).$$

## Remarks

A function of class $C^2$ is twice differentiable at each point, so this is a case of the [[symmetry of second derivatives|01V9FPBBVK]].
The result is also called Clairaut's theorem. By induction, for a function of class $C^k$ the [[partial derivatives|02RSXVM1ZN]] of order at most $k$ do not depend on the order of differentiation.
So for $C^k$ functions one can use [[multi-index notation|0PJXBR6QA3]] $\partial^\alpha f$ without ambiguity.

## Explanations

### L1 human

If the second partial derivatives are continuous, then $f_{xy} = f_{yx}$.
This saves work: in a $C^2$ function of $n$ variables, only $n(n+1)/2$ of the $n^2$ second partial derivatives can differ.
