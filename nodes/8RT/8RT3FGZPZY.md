---
tag: 8RT3FGZPZY
kind: definition
name: Shape operator
msc: [53A05]
defines: DQCD11X1VM
uses: [6080X3FAD4, 9KHQR16P1B, MAJ3DH7MZS, 0BJDQ2HBH1, 0MB8HQW495]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_geometry_of_surfaces
---

## Definition

Let $S \subseteq \R^3$ be a [[regular surface|6080X3FAD4]], let $W \subseteq S$ be open in $S$, and let $N \colon W \to \R^3$ be a smooth unit [[normal vector|0BJDQ2HBH1]] field.
For $p \in W$, the differential $dN_p$ maps the tangent plane $T_p S$ into itself, because $\ip{N}{N} = 1$.
The *shape operator* of $S$ at $p$ is the linear map
$$S_p = -dN_p \colon T_p S \to T_p S.$$

## Remarks

The map $S_p$ is [[self-adjoint|0MB8HQW495]] for the inner product of $T_p S$, and $\ip{S_p v}{w} = I\!I_p(v, w)$, where $I\!I_p$ is the polar form of the [[second fundamental form|9KHQR16P1B]].
In a local parametrisation, the matrix of $S_p$ in the basis $x_u, x_v$ is
$$\begin{pmatrix} E & F \\ F & G \end{pmatrix}^{-1} \begin{pmatrix} e & f \\ f & g \end{pmatrix},$$
with $E, F, G$ from the [[first fundamental form|MAJ3DH7MZS]] and $e, f, g$ from the second.
Example: on the sphere of radius $r$ centred at $0$ with the outer normal $N(p) = p / r$, one has $dN_p = \frac{1}{r} \id$, so $S_p = -\frac{1}{r} \id$.
With the inner normal, $S_p = \frac{1}{r} \id$.
Non-example: on a Möbius strip there is no global continuous unit normal, so the shape operator is defined only locally, up to sign.
