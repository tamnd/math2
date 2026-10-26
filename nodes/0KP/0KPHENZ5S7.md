---
tag: 0KPHENZ5S7
kind: object
name: Dirac delta function
aliases: [unit-impulse, dirac-delta]
msc: [46F10]
uses: [09C4JP7Y0M, 05XT5AVJBK]
sources:
  - url: https://en.wikipedia.org/wiki/Dirac_delta_function
    locator: As a distribution
  - url: https://en.wikipedia.org/wiki/Dirac_delta_function
    locator: As a measure
  - url: https://en.wikipedia.org/wiki/Dirac_delta_function
    locator: Properties
same_as:
  wikidata: Q209675
  wikipedia: Dirac delta function
---

## Description

Let $C_c^\infty(\mathbb{R})$ be the space of infinitely differentiable functions $\varphi : \mathbb{R} \to \mathbb{C}$ that vanish outside a bounded set.
The Dirac delta is the distribution $\delta$ that maps each test function $\varphi \in C_c^\infty(\mathbb{R})$ to $\delta[\varphi] = \varphi(0)$.
Informally, one writes $\int_{-\infty}^{\infty} \delta(t)\, \varphi(t)\, dt = \varphi(0)$, as if $\delta$ were a function that is $0$ away from $0$ and has total integral $1$.
No actual function has this property. The delta is a generalized function.

## Remarks

As a measure, $\delta$ gives the mass $1$ to each set that contains $0$ and the mass $0$ to the other sets.
The shifted delta $\delta(t - a)$ maps $\varphi$ to $\varphi(a)$. For $a > 0$, its Laplace transform is $e^{-a s}$, and for $a = 0$ the usual convention gives $1$.
In the sense of distributions, $\delta$ is the derivative of the [[Heaviside step function|09C4JP7Y0M]].
In differential equations, $\delta(t - a)$ models an impulse: a large force that acts for a very short time around $t = a$.

## Explanations

### L1 human

The delta function is an idealized spike at $0$, infinitely tall and infinitely thin, with area $1$.
It is not a real function. But it makes sense when we integrate it against a smooth function, and the result is the value of that function at $0$.
