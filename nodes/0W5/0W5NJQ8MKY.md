---
tag: 0W5NJQ8MKY
kind: definition
name: Harmonic function
msc: [31B05]
defines: 0DEB0JMN0W
uses: [0XQ2ZVN1PZ, 05RCT1522R, 0TCBZMEYGN]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_function
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Harmonic_function
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Harmonic_function
    locator: The mean value property
inventory: [1RRM250VSA]
---

## Definition

Let $U \subseteq \mathbb{R}^n$ be open.
A function $u \colon U \to \mathbb{R}$ is harmonic on $U$ if $u$ is of [[class C^2|0TCBZMEYGN]] on $U$ and its [[Laplacian|0XQ2ZVN1PZ]] vanishes on $U$:
$$\Delta u = \frac{\partial^2 u}{\partial x_1^2} + \dots + \frac{\partial^2 u}{\partial x_n^2} = 0.$$

## Remarks

Each affine function is harmonic. In the plane, $x^2 - y^2$, $x y$ and $e^x \sin y$ are harmonic, and so is $\ln(x^2 + y^2)$ on $\mathbb{R}^2 \setminus \{0\}$.
On $\mathbb{R}^3 \setminus \{0\}$, $1 / \|x\|$ is harmonic. It is the potential of a unit point charge at the origin.
The real and imaginary parts of a holomorphic function of $z = x + i y$ are harmonic functions of $(x, y)$.
Mean value property: let the closed ball of centre $a$ and radius $r$ lie in $U$. Then $u(a)$ is the average of $u$ on the sphere of radius $r$ about $a$, and also on the ball.

## Explanations

### L1 human

A harmonic function has no local bumps or dips: its value at each point is the average of its values around the point.
A stretched rubber sheet held at fixed heights on its rim has a harmonic height function inside.
