---
tag: 0MFJJV97RJ
kind: concept
name: Norm induced by an inner product
msc: ["46C05", "15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
specializes: [0V2WP9B1MF]
uses: [0QVNCJXRY3, 0F7FQS6XY6]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Norm properties
  - url: https://en.wikipedia.org/wiki/Norm_(mathematics)
    locator: Euclidean norm
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Summary

The induced norm is the length that an inner product gives to each vector: pair the vector with itself and take the square root.
It turns the algebra of the inner product into lengths and distances.
Let $V$ be an [[inner product space|0QVNCJXRY3]] over $\mathbb{R}$ or $\mathbb{C}$.
The *norm induced by the inner product* is the map $V \to \mathbb{R}$ given by
$$\norm{x} = \sqrt{\ip{x}{x}},$$
the nonnegative [[square root|0F7FQS6XY6]].
The root exists, because the axioms make $\ip{x}{x}$ a real number with $\ip{x}{x} \geq 0$.
The [[formal definition|0KG4D8AP6G]] states this, and the result is a [[norm|0V2WP9B1MF]] in the sense of analysis.

## Motivation

In $\mathbb{R}^2$ the length of $(x_1, x_2)$ is $\sqrt{x_1^2 + x_2^2}$, by the theorem of Pythagoras.
This is $\sqrt{x \cdot x}$, the square root of the dot product of the vector with itself.
In an abstract inner product space there is no picture, but the formula $\sqrt{\ip{x}{x}}$ still makes sense, so we take it as the definition of length.
The positivity axiom of the inner product is exactly the condition that makes the square root possible.

Once there is a length, there is a distance $d(x, y) = \norm{x - y}$.
This lets us say how far a polynomial is from a function it approximates, or how large the error of a numerical solution is.
The later sub-area on [[least squares|0BYTQ4X1HC]] minimizes exactly such a distance.

## Notation

We write $\norm{x}$, and $\norm{x}_2$ when other norms are present; some books write $\abs{x}$.
When two inner products are present, $\norm{x}_1 = \sqrt{\ip{x}{x}_1}$ and so on.
Many formulas use $\norm{x}^2$ in place of $\ip{x}{x}$.
A *unit vector* is a vector $u$ with $\norm{u} = 1$.

## Remarks

### Lengths in four spaces

On $\mathbb{R}^n$ with the dot product, the induced norm is the [[Euclidean length|0XKBKGTCPC]], and $\norm{(3, 4)} = \sqrt{9 + 16} = 5$.
On $\mathbb{C}^n$ with the [[standard inner product|TFZ8DYVJ1J]], each entry contributes the square of its modulus:
$$\norm{(1 + i, 2)}^2 = \abs{1 + i}^2 + \abs{2}^2 = 2 + 4 = 6.$$
On $M_2(\mathbb{C})$ with the [[trace inner product|JVH9RZ7QAB]], the induced norm is the [[Frobenius norm|JT8Q204E4R]], the square root of $\sum_{j, k} \abs{a_{jk}}^2$.
On $\mathcal{P}_2(\mathbb{R})$ with the [[integral inner product|W6NJ22XGWT]],
$$\norm{t} = \sqrt{\int_0^1 t^2 \, dt} = \frac{1}{\sqrt{3}}.$$

### The rules of a length

The first two rules come straight from the axioms.
Positivity says $\norm{x} \geq 0$, with $\norm{x} = 0$ only for $x = 0$, by the positivity axiom.
Homogeneity says $\norm{ax} = \abs{a} \, \norm{x}$ for every scalar $a$, because the scalar leaves the first slot as $a$ and the second slot as $\overline{a}$:
$$\ip{ax}{ax} = a\overline{a}\ip{x}{x} = \abs{a}^2 \norm{x}^2.$$
The third rule, the [[triangle inequality|SRN4T2G6AM]] $\norm{x + y} \leq \norm{x} + \norm{y}$, needs the [[Cauchy-Schwarz inequality|0RFWW56Y22]].
With all three, the induced norm is a norm, and $d(x, y) = \norm{x - y}$ is a distance.

The square of a sum expands like a binomial, with a real middle term:
$$\norm{x + y}^2 = \norm{x}^2 + \ip{x}{y} + \ip{y}{x} + \norm{y}^2 = \norm{x}^2 + 2\operatorname{Re}\ip{x}{y} + \norm{y}^2.$$
The step uses $\ip{y}{x} = \overline{\ip{x}{y}}$, and a number plus its conjugate is twice its real part.
From this expansion come the [[parallelogram law|026HPGYGS4]] and the [[polarization identity|05FKHRT0B4]], which recovers the inner product from the norm.

### Unit vectors and normalization

Every nonzero vector points in the direction of exactly one unit vector, namely $x / \norm{x}$.
This step is [[normalization|M2FAMD9HZN]], and it works by homogeneity with $a = 1/\norm{x}$.
For $x = (3, 4)$ the unit vector is $(0.6, 0.8)$.
Check: $0.36 + 0.64 = 1$.
In $\mathcal{P}_2(\mathbb{R})$ with the integral inner product, the unit vector in the direction of $t$ is $\sqrt{3}\, t$.

### What it is not

The [[maximum norm on $\mathbb{R}^2$|J5V8HEYXCM]], $\max(\abs{x_1}, \abs{x_2})$, is a norm, but no inner product induces it, because it fails the parallelogram law.
The [[taxicab length|WW2RB40VYX]] $\abs{x_1} + \abs{x_2}$ fails it too.
For $x = (1, 0)$ and $y = (0, 1)$ the law asks for $\norm{x + y}^2 + \norm{x - y}^2 = 2\norm{x}^2 + 2\norm{y}^2$, but the taxicab length gives
$$2^2 + 2^2 = 8 \neq 4 = 2 \cdot 1 + 2 \cdot 1.$$
The map $x \mapsto \ip{x}{x}$ without the square root is not a norm.
On $\mathbb{R}$ with $\ip{x}{y} = xy$ it gives $4$ at $x = 2$, while homogeneity asks for $2 \cdot 1 = 2$.

### Watch out

The norm of a sum is not the sum of the norms.
For $x = (1, 0)$ and $y = (0, 1)$ in $\mathbb{R}^2$, $\norm{x + y} = \sqrt{2}$, while $\norm{x} + \norm{y} = 2$.
Equality $\norm{x + y} = \norm{x} + \norm{y}$ holds only when one vector is a nonnegative real multiple of the other.

Over $\mathbb{C}$ two more traps wait.
The square norm is $\sum_k \abs{x_k}^2$, not $\sum_k x_k^2$, and for $x = (1, i)$ the wrong formula gives $1 + i^2 = 0$.
In the expansion of $\norm{x + y}^2$ the middle term is $2\operatorname{Re}\ip{x}{y}$, not $2\ip{x}{y}$.

### Try it

First, find the length of $(1, 2, 2)$ in $\mathbb{R}^3$ and the unit vector in its direction.
The length is $\sqrt{1 + 4 + 4} = 3$, and the unit vector is $(\tfrac13, \tfrac23, \tfrac23)$.

Second, find $\norm{(i, 1 - i)}$ in $\mathbb{C}^2$.
The square norm is $\abs{i}^2 + \abs{1 - i}^2 = 1 + 2 = 3$, so the norm is $\sqrt{3}$.

Third, if $\norm{x} = 2$ in a complex inner product space, what is $\norm{(3 - 4i) x}$?
It is $\abs{3 - 4i} \cdot 2 = 5 \cdot 2 = 10$.

## Explanations

### L1 human

The norm of a vector is its length.
We get it from the inner product: pair the vector with itself, then take the square root.
For the arrow $(3, 4)$ in the plane, the dot product with itself is $9 + 16 = 25$, and the square root is $5$.
Dividing a nonzero vector by its length gives a vector of length $1$ in the same direction.
For $(3, 4)$ this is $(0.6, 0.8)$.

### L2 human

Here is a typical use: how far apart are the polynomials $p = t$ and $q = t^2$, for $\ip{p}{q} = \int_0^1 p(t) q(t) \, dt$?
The difference is $p - q = t - t^2$, so we square it and integrate:
$$\norm{p - q}^2 = \int_0^1 (t^2 - 2t^3 + t^4) \, dt = \frac13 - \frac12 + \frac15 = \frac{1}{30}.$$
So $d(p, q) = 1/\sqrt{30} \approx 0.18$.
The two curves are close on $[0, 1]$, and the number measures how close, on average over the interval.
Watch out for the sum: $\norm{t} + \norm{t^2} = 1/\sqrt{3} + 1/\sqrt{5} \approx 1.02$, while
$$\norm{t + t^2}^2 = \frac13 + \frac12 + \frac15 = \frac{31}{30}, \qquad \norm{t + t^2} \approx 1.017.$$
This is the typical use of the induced norm: it measures the error between a function and its approximation.

### L3 human

The induced norm is the bridge from algebra to analysis, because it makes each inner product space a normed space and a metric space.
Among all norms, the induced ones are exactly those that satisfy the parallelogram law, by the [[Jordan-von Neumann theorem|46WGVM5VS6]].
The unit sphere of an induced norm on $\mathbb{R}^n$ is an ellipsoid, while the unit sphere of the maximum norm is the surface of a cube.
In finite dimension all norms are equivalent, so the topology does not depend on the inner product, but the geometry does.
In infinite dimension the induced norm defines convergence, and completeness for it gives a [[Hilbert space|HM2HHE3J51]].
