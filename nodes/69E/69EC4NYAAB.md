---
tag: 69EC4NYAAB
kind: statement
role: theorem
name: Perpendicular axis theorem
msc: ["70E15"]
uses: [08ANASGBXV, V8RK0F7B5B]
about: [08ANASGBXV]
sources:
  - url: https://en.wikipedia.org/wiki/Perpendicular_axis_theorem
same_as:
  wikidata: Q995926
  wikipedia: Perpendicular axis theorem
---

## Statement

Let a body lie in the plane $z = 0$ of $\R^3$, with a mass distribution of finite total mass.
Let $I_x$, $I_y$ and $I_z$ be its [[moments of inertia|08ANASGBXV]] about the $x$-, $y$- and $z$-axes.
Then
$$I_z = I_x + I_y.$$

## Remarks

For a point of the body at $(x, y, 0)$, the squared distances to the three axes are $y^2$, $x^2$ and $x^2 + y^2$.
So $I_z = \int (x^2 + y^2)\,dm = \int y^2\,dm + \int x^2\,dm = I_x + I_y$.
The hypothesis that the body is flat is needed: a uniform ball of mass $M$ and radius $R$ centred at the origin has $I_x = I_y = I_z = \tfrac25 M R^2$, so $I_z \ne I_x + I_y$.

Example: a uniform disc of mass $M$ and radius $R$ in the plane $z = 0$, centred at the origin, has $I_z = \tfrac12 M R^2$.
By symmetry $I_x = I_y$, so the theorem gives $I_x = I_y = \tfrac14 M R^2$ without a new integral.

## Explanations

### L1 human

Take a flat object, such as a plate or a ring.
Its moment of inertia about the axis sticking straight out of the plane is the sum of the moments about two perpendicular axes in the plane.
This follows from Pythagoras: the squared distance to the out-of-plane axis is the sum of the squared distances to the two in-plane axes.

### L2 human

The theorem often saves an integral, as for the disc, where the in-plane moments follow from the easy out-of-plane one.
Combined with the [[parallel axis theorem|V8RK0F7B5B]], it gives the moments of inertia of flat bodies about many axes.
It is the planar case of a fact about the inertia tensor: its diagonal entries satisfy $I_{zz} \le I_{xx} + I_{yy}$.
Equality holds exactly when all the mass lies in the plane $z = 0$.
