---
tag: 7HA6EEDR9S
kind: statement
role: theorem
name: Mairhuber–Curtis theorem
msc: [41A63, 41A52, 41A05]
uses: [NY5AK617TR, 0RZH6W98HK, 00KDZRW4C0]
about: [NY5AK617TR]
sources:
  - url: https://en.wikipedia.org/wiki/Radial_basis_function_interpolation
---

## Statement

Let $d \ge 2$ and let $\Omega \subseteq \R^d$ have an [[interior point|0RZH6W98HK]].
Let $n \ge 2$ and let $u_1, \dots, u_n \colon \Omega \to \R$ be continuous.
Then some nonzero linear combination of $u_1, \dots, u_n$ has at least $n$ zeros in $\Omega$.
So $(u_1, \dots, u_n)$ is not a [[Chebyshev system|NY5AK617TR]] on any set containing these zeros, and $\Omega$ carries no Haar subspace of dimension $n \ge 2$.

## Remarks

The idea of the proof: suppose $(u_1, \dots, u_n)$ is a Chebyshev system, so $D(x_1, \dots, x_n) = \det \big( u_i(x_j) \big)$ is nonzero for distinct points.
Choose distinct $x_1, \dots, x_n$ in a small open ball inside $\Omega$.
Because $d \ge 2$, one can move $x_1$ and $x_2$ continuously inside the ball so that they exchange places, without colliding with each other or with the other points.
Along this motion $D$ changes continuously from $D(x_1, x_2, \dots)$ to $D(x_2, x_1, \dots) = -D(x_1, x_2, \dots)$, so by the intermediate value theorem it vanishes somewhere, a contradiction.

Example: the polynomials of degree at most $1$ in two variables are spanned by $1, x, y$.
They are not a Haar space on the unit square: the nonzero function $x - y$ vanishes on the whole diagonal.

In dimension $d = 1$ the argument fails, because two points of an interval cannot exchange places without meeting.
Indeed the polynomials of degree at most $n - 1$ form a Haar subspace there.

## Explanations

### L1 human

On an interval you can always fit a unique polynomial of degree $n - 1$ through $n$ points, whatever the points are.
In the plane or in space nothing of this kind is possible for a fixed family of functions.
For some placement of the points the interpolation problem breaks down.
The reason is that two points in the plane can swap places by walking around each other.

### L2 human

The theorem is why multivariate interpolation and uniform approximation behave so differently from the one-variable theory.
Uniqueness of best uniform approximation and unisolvence for all point sets cannot hold for a fixed space of functions when $d \ge 2$.
Practical methods respond by letting the space depend on the data points, as in [[radial basis function interpolation|XZ33P3HBB9]], where the basis functions are centred at the data points.
The theorem holds more generally for compact Hausdorff spaces: a Haar subspace of dimension at least $2$ exists only if the space embeds in a circle.
