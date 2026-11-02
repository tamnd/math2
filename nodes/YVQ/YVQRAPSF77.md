---
tag: YVQRAPSF77
kind: statement
role: theorem
name: d'Alembert's formula
msc: [35L05, 35C05, 35L15]
uses: [5EHD2XBQDG]
about: [5EHD2XBQDG]
sources:
  - url: https://en.wikipedia.org/wiki/D%27Alembert%27s_formula
same_as:
  wikidata: Q2388753
  wikipedia: D'Alembert's formula
---

## Statement

Let $c > 0$, let $g \in C^2(\R)$ and let $h \in C^1(\R)$.
Define $u \colon \R \times [0, \infty) \to \R$ by
$$u(x, t) = \frac{g(x + ct) + g(x - ct)}{2} + \frac{1}{2c} \int_{x - ct}^{x + ct} h(s)\, ds.$$
Then $u \in C^2(\R \times [0, \infty))$, $u$ solves the [[wave equation|5EHD2XBQDG]] $u_{tt} = c^2 u_{xx}$ on $\R \times (0, \infty)$, and $u(x, 0) = g(x)$, $u_t(x, 0) = h(x)$ for all $x \in \R$.
Moreover, $u$ is the only $C^2$ solution of this initial value problem.

## Remarks

The change of variables $\xi = x + ct$, $\eta = x - ct$ turns the equation into $u_{\xi\eta} = 0$.
Hence every $C^2$ solution has the form $u = F(x + ct) + G(x - ct)$, and the two initial conditions determine $F$ and $G$ up to a constant that cancels.
This argument also proves uniqueness.
Example: with $g = 0$ and $h = \cos$, the formula gives $u(x, t) = \frac{1}{2c}\big(\sin(x + ct) - \sin(x - ct)\big) = \frac{1}{c}\cos x \sin(ct)$, a standing wave.
The value $u(x, t)$ depends only on the data in the interval $[x - ct, x + ct]$, which shows finite speed of propagation in one dimension.
If $g$ is only continuous, the formula still defines a function, but it is a weak solution rather than a classical one.

## Explanations

### L1 human

The formula solves the vibrating string problem on an infinitely long string in closed form.
The initial shape $g$ splits into two halves, one moving left and one moving right at speed $c$.
The initial velocity $h$ adds the average of $h$ over the interval that a signal can reach in time $t$.
So what happens at a point depends only on what happened nearby, within distance $ct$.

### L2 human

d'Alembert's formula is the first explicit solution formula in a PDE course and the basis for the other dimensions.
By the method of spherical means, it gives Kirchhoff's formula in dimension $3$, and then by descent Poisson's formula in dimension $2$.
On the half line, the formula combined with an odd or even reflection of the data solves the problems with Dirichlet or Neumann boundary condition.
For the inhomogeneous equation $u_{tt} - c^2 u_{xx} = f$, Duhamel's principle adds the term $\frac{1}{2c}\int_0^t \int_{x - c(t - s)}^{x + c(t - s)} f(y, s)\, dy\, ds$.
