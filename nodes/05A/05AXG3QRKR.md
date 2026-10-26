---
tag: 05AXG3QRKR
kind: definition
name: Partial derivative
msc: [26B05]
defines: 09EGC6F8PT
uses: [0XPR1E85W0, 0JPCHTXWG0, 0J8Y1NCY0K]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_derivative
    locator: Definition
---

## Definition

Let $U \subseteq \mathbb{R}^n$ be an open set, let $f \colon U \to \mathbb{R}$, let $a \in U$, and let $i \in \{1, \dots, n\}$.
Let $e_i$ be the $i$-th standard basis vector of [[Euclidean space|0XPR1E85W0]] $\mathbb{R}^n$.
The partial derivative of $f$ with respect to $x_i$ at $a$ is the limit
$$\frac{\partial f}{\partial x_i}(a) = \lim_{h \to 0} \frac{f(a + h e_i) - f(a)}{h},$$
when this limit exists in $\mathbb{R}$.
Other notations for it are $\partial_i f(a)$, $D_i f(a)$ and $f_{x_i}(a)$.

## Remarks

The partial derivative is the ordinary derivative at $t = a_i$ of the function $t \mapsto f(a_1, \dots, a_{i-1}, t, a_{i+1}, \dots, a_n)$ of one variable.
So you compute it with the rules of one-variable calculus, and you treat the other variables as constants.
It is the [[directional derivative|06KWGHDN2J]] in the direction $e_i$.
The existence of all partial derivatives at $a$ does not imply that $f$ is continuous at $a$, see [[this counterexample|0TNZC55X3J]].

## Explanations

### L1 human

To find $\partial f / \partial x$, pretend that $y$ is a fixed number and differentiate in $x$ as usual.
For $f(x, y) = x^2 y + \sin y$, this gives $\partial f / \partial x = 2xy$, because $\sin y$ is a constant for this purpose.
Geometrically, it is the slope of the graph of $f$ when you walk in the $x$-direction.
