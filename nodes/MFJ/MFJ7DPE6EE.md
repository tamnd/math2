---
tag: MFJ7DPE6EE
kind: definition
name: Patch test
msc: [74S05, 65N30]
defines: KFMV57EXB6
uses: [CGYM9VZC39, 98GZ9DVHTA]
sources:
  - url: https://en.wikipedia.org/wiki/Patch_test_(finite_elements)
---

## Definition

Let an element formulation of the [[finite element method in structural mechanics|CGYM9VZC39]] for linear elasticity be given.
A *patch* is a mesh of a few such elements, with at least one node in the interior, in general with distorted element shapes.
Let $u^*(x) = c + A x$ be a displacement field with a constant vector $c$ and a constant matrix $A$.
Its strain $\tfrac12(A + A^T)$ is constant, and with no body force it is an exact solution of the equilibrium equations.
Solve the finite element problem on a patch with the boundary nodal displacements set equal to $u^*$.
The element *passes the patch test* if, for every patch and every such $u^*$, this solution:

1. equals $u^*$ at every interior node;
2. has strain equal to $\tfrac12(A + A^T)$ everywhere in the patch.

## Remarks

Example: the linear triangle (constant strain triangle) passes.
Its trial space contains every linear field, the discrete problem is the Galerkin projection onto a space that contains $u^*$, and the exact solution $u^*$ is therefore reproduced.
The same argument works for every conforming element whose trial space contains the linear fields.

Non-example: the incompatible quadrilateral element of Wilson adds internal displacement modes that are discontinuous between elements.
It fails the test on patches of quadrilaterals that are not parallelograms: the computed strain is not constant, so clause 2 fails.
Modified versions of this element were designed to pass it.

Other versions prescribe tractions instead of displacements on the boundary, or test higher-order fields for higher-order elements.
