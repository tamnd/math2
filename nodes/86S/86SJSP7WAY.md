---
tag: 86SJSP7WAY
kind: definition
name: Gradient flow on a manifold
msc: ["37C10", "58E05", 57R70]
defines: AFRP1AAPV9
uses: [7CBT4SM83Y, 0V33BNKZ9S, 0ABK9V9Y64, 06738GGWWK]
sources:
  - url: https://en.wikipedia.org/wiki/Gradient-like_vector_field
---

## Definition

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]] and let $f \colon M \to \R$ be a [[smooth function|0V33BNKZ9S]].
The [[gradient|0ABK9V9Y64]] of $f$ is the vector field $\nabla f$ on $M$ with $g(\nabla f, X) = df(X)$ for every tangent vector $X$.
The *(negative) gradient flow* of $f$ is the [[flow|06738GGWWK]] $\varphi$ of $-\nabla f$.
So it is the solution of
$$\frac{\partial}{\partial t} \varphi_t(x) = -\nabla f\big(\varphi_t(x)\big), \qquad \varphi_0(x) = x,$$
defined on its maximal domain.

## Remarks

Along a flow line, $\frac{d}{dt} f(\varphi_t(x)) = -\abs{\nabla f}^2 \le 0$, with equality exactly at [[critical points|0YTCMFB4HC]] of $f$.
So $f$ is a Lyapunov function for the flow, and the rest points of the flow are the critical points of $f$.
If $M$ is compact, the flow is defined for all $t \in \R$.

Example: on $\R^2$ with the Euclidean metric, let $f(x, y) = x^2 - y^2$.
Then $-\nabla f = (-2x, 2y)$ and $\varphi_t(x, y) = (e^{-2t} x, e^{2t} y)$.
The origin is the only rest point, and the flow has the familiar saddle picture.

Non-example: on $\R^2$, the rotation field $X(x, y) = (-y, x)$ is not $-\nabla f$ for any smooth $f$.
Its flow has closed orbits, but $f$ would strictly decrease along a nonconstant flow line of a gradient flow, so it could not return to its starting point.

The flow depends on the metric $g$, not only on $f$.
A vector field $X$ with $df(X) < 0$ away from the critical points, and of a standard form near them, is called gradient-like for $f$.
Such fields serve the same purposes in Morse theory.
For a Morse function and a generic metric, the gradient flow is a [[Morse–Smale system|7AMQ8GS78Y]].
