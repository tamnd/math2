---
tag: WA0SE56FVH
kind: concept
name: Reinhardt domain
msc: [32Q02, 32A05]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Summary

A Reinhardt domain is a domain in $\C^n$ that is unchanged when each coordinate is rotated by its own angle.
Such a domain is determined by the set of absolute values $(\abs{z_1}, \dots, \abs{z_n})$ of its points.
[[Polydiscs|DJBWP7D3M8]] and the [[unit ball|PDQ9KW9FAP]] are Reinhardt domains.
They are the natural domains of convergence of [[power series in several variables|R3QTCPTJK7]].
They also give the first examples of the extension phenomena of [[several complex variables|BH57D2FBNR]].

## Explanations

### L1 human

Multiply the first coordinate of a point by $e^{i\theta_1}$, the second by $e^{i\theta_2}$, and so on.
This turns each coordinate around the origin of its own complex plane without changing its size.
A Reinhardt domain contains, with each point, all the points obtained in this way.
So one can draw it as a region in the "absolute value space" of points $(\abs{z_1}, \dots, \abs{z_n})$, which is a part of $[0, \infty)^n$.
For example, the unit polydisc of $\C^2$ is drawn as the square $[0, 1) \times [0, 1)$, and the unit ball as a quarter of a disc.
