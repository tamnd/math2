---
tag: R0XSPP9VVM
kind: definition
name: Jones calculus
msc: [78A10, 15A04]
defines: D3XTQ5Z2QA
uses: [PJ8ZSJ0QDW, 0AR68JTMDT]
sources:
  - url: https://en.wikipedia.org/wiki/Jones_calculus
---

## Definition

Let a fully polarized monochromatic plane wave travel along the $z$ axis, with complex field amplitudes $E_x, E_y$ as for the [[polarization of light|PJ8ZSJ0QDW]].
Its *Jones vector* is $J = (E_x, E_y)^T \in \C^2 \setminus \set{0}$, and its intensity is $J^* J = \abs{E_x}^2 + \abs{E_y}^2$.
A linear optical element that does not depolarize is represented by a *Jones matrix* $M \in \C^{2 \times 2}$.
It maps the input vector $J$ to the output vector $MJ$.
*Jones calculus* is the rule that elements $M_1, \dots, M_n$, crossed in this order, act as the product $M_n \cdots M_1$.

## Remarks

A lossless element has a [[unitary|0AR68JTMDT]] Jones matrix, since it preserves the intensity $J^* J$.
Jones vectors that differ by a nonzero complex factor describe the same polarization state.
The matrices depend on the choice of axes and of the sign convention for phases.

Example: the linear polarizer with transmission axis at angle $\theta$ to the $x$ axis has
$$P_\theta = \begin{pmatrix} \cos^2\theta & \cos\theta \sin\theta \\ \cos\theta\sin\theta & \sin^2\theta \end{pmatrix}.$$
On horizontal light $J = (1, 0)^T$ it gives $P_\theta J = \cos\theta \, (\cos\theta, \sin\theta)^T$, of intensity $\cos^2\theta$.
A quarter-wave plate with fast axis along $x$ has, up to a global phase, the matrix $\operatorname{diag}(1, i)$.
It turns light polarized at $45°$, with $J = (1, 1)^T/\sqrt2$, into $(1, i)^T/\sqrt2$, which is circularly polarized.

Non-example: an ideal depolarizer turns every input into unpolarized light.
Unpolarized light has no Jones vector, so a depolarizer has no Jones matrix; the Mueller calculus is needed for it.
