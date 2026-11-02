---
tag: 6PXHVPFTAS
kind: concept
name: d'Alembert's functional equation
msc: [39B22, 39B52]
specializes: [SRAN4EKWS0]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_equation
---

## Summary

d'Alembert's functional equation is the [[functional equation|SRAN4EKWS0]] $f(x + y) + f(x - y) = 2 f(x) f(y)$ for an unknown function $f \colon \R \to \R$.
It is the addition rule of the cosine, written as an equation.
Its continuous solutions are $f = 0$, $f(x) = \cos(ax)$ and $f(x) = \cosh(ax)$ with $a \in \R$.
Versions on groups, with $x - y$ replaced by $x y^{-1}$, are a main topic of the theory of functional equations on groups.

## Explanations

### L1 human

The [[cosine|08WFZP6P89]] satisfies $\cos(x + y) + \cos(x - y) = 2 \cos x \cos y$.
The equation turns this identity around and asks for all functions with the same property.
For example, $\cosh x = (e^x + e^{-x})/2$ also satisfies it.
Up to stretching the variable and the trivial solution $0$, the cosine and the hyperbolic cosine are the only continuous solutions.
