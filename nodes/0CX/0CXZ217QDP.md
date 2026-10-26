---
tag: 0CXZ217QDP
kind: statement
role: proposition
name: Linearity of the derivative
msc: [26B05]
uses: [08EVNYZF42]
sources:
  - url: https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative
    locator: Properties
---

## Statement

Let $V$ and $W$ be normed vector spaces over $\mathbb{R}$, let $U \subseteq V$ be open, let $f, g \colon U \to W$, let $x \in U$, and let $c \in \mathbb{R}$.
Suppose that $f$ and $g$ are Fréchet differentiable at $x$, with [[Fréchet derivatives|08EVNYZF42]] $Df(x)$ and $Dg(x)$.
Then $f + g$ and $c f$ are Fréchet differentiable at $x$, and
$$D(f + g)(x) = Df(x) + Dg(x), \qquad D(c f)(x) = c \, Df(x).$$

## Remarks

The proof adds the two remainders: a sum of two terms that are $o(\|h\|)$ is again $o(\|h\|)$.
So the maps that are differentiable at $x$ form a vector space, and $f \mapsto Df(x)$ is a linear map on it.
The same rules hold for the [[partial derivatives|09EGC6F8PT]] and for the [[directional derivatives|06KWGHDN2J]].

## Explanations

### L1 human

The derivative of a sum is the sum of the derivatives, and constants come out, just as in one variable.
For example, $D(x^2 + 3 y)$ at a point $(a, b)$ is the linear map $h \mapsto 2 a h_1 + 3 h_2$, the sum of the derivatives of $x^2$ and of $3 y$.
