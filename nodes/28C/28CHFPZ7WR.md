---
tag: 28CHFPZ7WR
kind: definition
name: Dispersion relation
msc: [78A40, 35L05, 35Q60]
defines: R5P8M6SBG7
uses: [GC5BDZ6QBC, NM024G378A, 5EHD2XBQDG]
sources:
  - url: https://en.wikipedia.org/wiki/Dispersion_relation
---

## Definition

Let $P(\tau, \xi)$ be a polynomial in $\tau \in \C$ and $\xi \in \C^d$ with complex coefficients, and consider the linear [[partial differential equation|GC5BDZ6QBC]] with constant coefficients $P(\partial_t, \nabla) u = 0$ for $u \colon \R^d \times \R \to \C$.
For $k \in \R^d$ and $\omega \in \C$, the [[plane wave|NM024G378A]] $u(x, t) = e^{i(k \cdot x - \omega t)}$ is a solution exactly when
$$P(-i\omega, \, i k) = 0.$$
This equation between $\omega$ and $k$ is the *dispersion relation* of the equation.
It may be solvable for $\omega$ as a function $\omega = W(k)$ on an open set of wave vectors.
Then the function $W$ is also called the dispersion relation, one function for each branch.

## Remarks

The equivalence holds because $\partial_t$ acts on the plane wave as multiplication by $-i\omega$ and $\nabla$ as multiplication by $i k$.
For systems such as Maxwell's equations one takes a vector amplitude, and the condition becomes that a matrix built from $\omega$ and $k$ is singular.
The equation is called non-dispersive when every branch is linear in $\abs{k}$, and dispersive otherwise.
In a linear medium with refractive index $n(\omega)$, the dispersion relation of light is $\abs{k} = n(\omega) \, \omega / c$.

Example: for the [[wave equation|5EHD2XBQDG]] $u_{tt} - c^2 \Delta u = 0$, $P(\tau, \xi) = \tau^2 - c^2 \xi \cdot \xi$, and $P(-i\omega, ik) = -\omega^2 + c^2 \abs{k}^2$, so the relation is $\omega = \pm c \abs{k}$.
For the Klein–Gordon equation $u_{tt} - c^2 \Delta u + m^2 u = 0$, which also models light in a cold plasma, the relation is $\omega^2 = c^2 \abs{k}^2 + m^2$, which is dispersive.

Non-example: the pair $\omega = 2c$, $k = (1, 0, 0)$ does not satisfy the dispersion relation of the wave equation, since $-4c^2 + c^2 \neq 0$; so $e^{i(x - 2ct)}$ is not a solution.

## Explanations

### L1 human

Put a plane wave into a linear equation with constant coefficients.
Derivatives turn into multiplication by $-i\omega$ and $ik$, so the equation becomes a polynomial equation in $\omega$ and $k$.
That polynomial equation is the dispersion relation: it lists the allowed frequencies for each wavelength.
