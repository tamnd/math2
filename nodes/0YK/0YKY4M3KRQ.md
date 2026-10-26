---
tag: 0YKY4M3KRQ
kind: definition
name: Principal branch
aliases: [principal-branch-of-the-logarithm]
msc: [30A99]
defines: 017BPGVEE8
uses: [03CPD1HGF3, 0X2FY491PF, 0SQSQP748R, 0KW2X0TFBX]
sources:
  - url: https://en.wikipedia.org/wiki/Principal_value
    locator: Principal values of standard functions
  - url: https://en.wikipedia.org/wiki/Complex_logarithm
    locator: Principal value
---

## Definition

Let $F$ be a [[multivalued function|03CPD1HGF3]] on a set $X \subseteq \mathbb{C}$, so that $F(z)$ is a set of complex numbers for each $z \in X$.
A principal branch of $F$ is a function $f$ on $X$ with $f(z) \in F(z)$ for each $z \in X$, chosen by a standard convention. Its value $f(z)$ is the principal value of $F$ at $z$.
For the main functions of complex analysis, the conventions are these. Let $z \neq 0$, and let $\operatorname{Arg} z \in (-\pi, \pi]$ be the [[principal value of the argument|0SQSQP748R]].

- The principal [[logarithm|0X2FY491PF]] is $\operatorname{Log} z = \ln |z| + i \operatorname{Arg} z$, where $\ln$ is the real natural logarithm.
- The principal square root is $\sqrt{z} = e^{\frac{1}{2} \operatorname{Log} z}$.
- For $w \in \mathbb{C}$, the principal [[power|0ZV9A7EV0F]] is $z^w = e^{w \operatorname{Log} z}$.

## Remarks

The imaginary part of $\operatorname{Log} z$ is in $(-\pi, \pi]$. For example, $\operatorname{Log} i = i\pi/2$ and $\operatorname{Log}(-1) = i\pi$.
These principal branches are continuous and holomorphic on $\mathbb{C} \setminus (-\infty, 0]$, see [[the principal logarithm is holomorphic off the branch cut|0XVGJE7Q04]]. They are not continuous at the points of $(-\infty, 0)$.
Some authors use $\operatorname{Arg} z \in [0, 2\pi)$ instead. This gives a different principal branch.

## Explanations

### L1 human

A multivalued function gives many values at a point. The principal branch is the rule that everybody agrees on for picking one value.
For the logarithm, the rule is to take the angle between $-180$ and $180$ degrees.
