---
tag: 054VXHMCA3
kind: definition
name: Complex exponential
msc: [33B10]
defines: 07GJV36896
uses: [09FTAET5Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_function
    locator: Complex exponential
  - url: https://en.wikipedia.org/wiki/Exponential_function
    locator: Power series
---

## Definition

The complex exponential is the function $\exp : \mathbb{C} \to \mathbb{C}$ given by
$$\exp z = \sum_{n=0}^{\infty} \frac{z^n}{n!} = 1 + z + \frac{z^2}{2!} + \frac{z^3}{3!} + \cdots$$
for each [[complex number|09FTAET5Z4]] $z$. The series converges absolutely for each $z \in \mathbb{C}$.
Another notation for $\exp z$ is $e^z$.

## Remarks

For real $x$, $\exp x$ is the real exponential function, and $e = \exp 1$.
For $z = x + iy$ with $x, y$ real, $e^z = e^x (\cos y + i \sin y)$. The case $x = 0$ is [[Euler's formula|04R3CY41VJ]].
By the [[product of exponentials|0WM7DJCM6G]], $e^{z + w} = e^z e^w$. So $e^z \neq 0$ for each $z$, and $|e^z| = e^{\operatorname{Re} z}$.

## Explanations

### L1 human

The power series of $e^x$ makes sense for complex numbers too, so we use it as the definition of $e^z$.
The real part of $z$ controls the size of $e^z$, and the imaginary part of $z$ controls its direction.
For example, $e^{i\pi} = -1$: the size is $e^0 = 1$ and the direction is a half turn.
