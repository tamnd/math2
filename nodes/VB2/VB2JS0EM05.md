---
tag: VB2JS0EM05
kind: statement
role: theorem
name: Hencky's theorems on slip lines
msc: [74C05, 74G05]
uses: [PSBT777WYE]
about: [PSBT777WYE]
sources:
  - url: https://en.wikipedia.org/wiki/Slip_line_field
---

## Statement

Consider a plane strain [[slip-line field|PSBT777WYE]] of a rigid–perfectly plastic material with shear yield stress $k$.
Let $p$ be the hydrostatic pressure and $\phi$ the slip-line angle, in a region where the stress is continuously differentiable.

1. (Hencky's equations.) The quantity $p + 2k\phi$ is constant along each $\alpha$-line, and $p - 2k\phi$ is constant along each $\beta$-line.
2. (Hencky's first theorem.) Let $\alpha_1$ and $\alpha_2$ be two $\alpha$-lines. Let a $\beta$-line meet them at two points. The angle between the tangents to $\alpha_1$ and $\alpha_2$ at these points is the same for every $\beta$-line that meets both. The change of $p$ between these points is also the same for every such $\beta$-line. The same holds with the roles of $\alpha$ and $\beta$ exchanged.
3. (Hencky's second theorem.) Let $R$ be the radius of curvature of the $\alpha$-lines at their points of intersection with a $\beta$-line. Then $\abs{\partial R / \partial s} = 1$, where $s$ is arc length along the $\beta$-line. The same holds with the roles of $\alpha$ and $\beta$ exchanged.

## Remarks

The equations in (1) come from writing the equilibrium equations in coordinates along the slip lines.
The yield condition removes the shear terms and leaves one ordinary differential relation along each characteristic.
For (2), take two $\alpha$-lines and two $\beta$-lines meeting at the corners $A, B, C, D$ of a curvilinear quadrilateral.
The sides $AB$ and $DC$ lie on the $\alpha$-lines, and $AD$ and $BC$ on the $\beta$-lines.
Applying (1) along the four sides and eliminating $p$ gives $\phi_B - \phi_A = \phi_C - \phi_D$, or equivalently $\phi_D - \phi_A = \phi_C - \phi_B$, which is the first theorem.
The second theorem follows from the first by letting the two lines of the first family come together.
A consequence of (2) is that if one segment of a slip line between two lines of the other family is straight, then all corresponding segments are straight.
This is why fields made of straight lines and centred fans appear so often.

## Explanations

### L1 human

Slip lines in a flowing metal cannot bend in an arbitrary way.
Hencky's theorems say that the turning of one family of lines, measured between two fixed lines, is the same wherever you look.
This rigidity lets an engineer draw the whole net of lines from a few boundary pieces.

### L2 human

The stress equations of plane strain perfect plasticity form a hyperbolic system whose characteristics are the slip lines.
Hencky's equations are the Riemann invariants of this system: $p \pm 2k\phi$ are carried unchanged along the characteristics.
With them one solves boundary value problems by marching from the boundary, as in the [[method of characteristics|7XAPBCJK3B]].
Hencky's theorems describe the geometry that any such net must have, and Prandtl's fan solution for a flat punch is the simplest example of it.
