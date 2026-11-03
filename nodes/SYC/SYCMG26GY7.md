---
tag: SYCMG26GY7
kind: example
name: Falkner–Skan boundary layer
msc: [76D10, 34B40]
instance_of: [XXDE4YP722]
uses: [XXDE4YP722, 579J5K9K5Z, VJ752BFSQF]
sources:
  - url: https://en.wikipedia.org/wiki/Falkner–Skan_boundary_layer
same_as:
  wikidata: Q30715267
  wikipedia: Falkner–Skan boundary layer
---

## Example

Consider the steady [[Prandtl boundary layer equations|XXDE4YP722]] with kinematic viscosity $\nu > 0$.
Let the outer speed have the power form $U(x) = c \, x^m$ for $x > 0$, with constants $c > 0$ and $m > -1$.
Set $\eta = y \sqrt{\frac{(m + 1) U(x)}{2 \nu x}}$ and $\psi = \sqrt{\frac{2 \nu x U(x)}{m + 1}} \, f(\eta)$, so that $u = U(x) f'(\eta)$.
Then the boundary layer equations become the *Falkner–Skan equation*
$$f''' + f f'' + \beta \big( 1 - f'^2 \big) = 0, \qquad \beta = \frac{2 m}{m + 1},$$
with $f(0) = f'(0) = 0$ and $f'(\eta) \to 1$ as $\eta \to \infty$.
The *Falkner–Skan boundary layer* is the flow given by its solution.

Check: the term $\beta (1 - f'^2)$ comes from the pressure gradient $U U' = m c^2 x^{2m - 1}$ minus the convective term $u \, \partial_x u$.
The boundary conditions are the no-slip condition and the matching with $U$.

## Remarks

The case $m = 0$, $\beta = 0$ is the [[Blasius boundary layer|VJ752BFSQF]] (in a rescaled variable).
The case $m = 1$, $\beta = 1$ is the flow near a stagnation point, studied by Hiemenz.
For $\beta > 0$ the outer flow accelerates and the pressure decreases downstream, a favourable gradient, and the layer is thin and stable.
For $\beta < 0$ the outer flow decelerates; solutions with positive wall shear exist only down to $\beta \approx -0.199$, where $f''(0) = 0$ and the flow is on the verge of separating.
These are [[similarity solutions|579J5K9K5Z]], and they are the standard test cases for boundary layer methods.

## Explanations

### L1 human

The Blasius layer is for a stream of constant speed along a flat plate.
The Falkner–Skan family allows the outside stream to speed up or slow down like a power of the distance, as along a wedge.
When the stream speeds up, the layer hugs the wall; when it slows down, the layer thickens and eventually tends to break away.
