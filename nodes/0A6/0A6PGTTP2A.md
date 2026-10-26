---
tag: 0A6PGTTP2A
kind: definition
name: Linear equation with constant coefficients
msc: [34A30]
defines: 0SWTJ5VC07
uses: [0PB7K8M7FG]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_differential_equation
    locator: Homogeneous equation with constant coefficients
---

## Definition

Let $n \ge 1$, let $a_0, \dots, a_{n-1}$ be real numbers, let $I$ be an open interval and let $b : I \to \mathbb{R}$ be continuous.
A linear equation with constant coefficients is a [[linear differential equation|0PB7K8M7FG]] of the form
$$y^{(n)} + a_{n-1}\, y^{(n-1)} + \dots + a_1\, y' + a_0\, y = b(x).$$
Its homogeneous equation is the case $b = 0$, which we consider on $I = \mathbb{R}$.

## Remarks

The function $e^{r x}$ solves the homogeneous equation if and only if $r$ is a root of the [[characteristic equation|0QDXMG46QW]] $r^n + a_{n-1} r^{n-1} + \dots + a_0 = 0$.
The roots of this polynomial give a [[fundamental system|0H4KNNCHPY]]. See the cases of [[distinct real roots|0HJ0HDA6W7]], [[repeated roots|0HRVY67CNV]] and [[complex conjugate roots|0BEZX8F2XW]].
The [[harmonic oscillator|0YG0ZJPTWG]] $x'' + \omega^2 x = 0$ is an example of order $2$.

## Explanations

### L1 human

When the coefficients are constants, the derivative of $e^{r x}$ is $r e^{r x}$, again a multiple of the same function.
So the equation becomes a polynomial equation in $r$.
This changes calculus into algebra.
