---
tag: 08EVNYZF42
kind: definition
name: Fréchet derivative
msc: [46G05]
defines: 06EH97V2A7
uses: [0XPR1E85W0]
sources:
  - url: https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative
    locator: Definition
---

## Definition

Let $V$ and $W$ be normed vector spaces over $\mathbb{R}$, let $U \subseteq V$ be an open set, let $f \colon U \to W$, and let $x \in U$.
A bounded linear map $A \colon V \to W$ is a Fréchet derivative of $f$ at $x$ when
$$\lim_{h \to 0} \frac{\|f(x + h) - f(x) - A h\|_W}{\|h\|_V} = 0.$$
The limit is over $h \in V \setminus \{0\}$ with $x + h \in U$.
When such an $A$ exists, $f$ is Fréchet differentiable at $x$, with the notation $Df(x) = A$ or $f'(x) = A$.

## Remarks

The Fréchet derivative is unique when it exists, see the [[uniqueness of the derivative|0762WAE49P]].
For $V = W = \mathbb{R}$, a linear map $A$ is multiplication by a number $a$. Then the condition says that $f$ has the derivative $a$ at $x$ in the usual sense.
For $V = \mathbb{R}^n$ and $W = \mathbb{R}^m$, each linear map is bounded, and $Df(x)$ is the [[total derivative|0FNKFT8H6E]] of $f$ at $x$. Its matrix is the [[Jacobian matrix|047NDTEPCV]].
If $f$ is Fréchet differentiable at $x$, then $f$ is continuous at $x$.

## Explanations

### L1 human

Near $x$, the change $f(x + h) - f(x)$ is close to $A h$, a linear function of the step $h$.
The error is small even compared with the length of the step, when the step is short.
So $A$ plays the role of the slope of a tangent line, but now the tangent object is a linear map.
