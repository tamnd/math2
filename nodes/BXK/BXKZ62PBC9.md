---
tag: BXKZ62PBC9
kind: definition
name: Dirac bundle
msc: [53C27, 58J60, 15A66]
defines: K0GVMM3YPF
uses: [7CBT4SM83Y, A38B1QFK20, 31Q0RDPZ00, CAZYGE1T4E, 5ZYRRVE8BW, 3DXGJTEQZH, PYYQQKAZ0C, PWG3GKZG80]
sources:
  - url: https://en.wikipedia.org/wiki/Dirac_operator
---

## Definition

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]], and let $\mathrm{Cl}(M)$ be its Clifford bundle, whose fibre at $x$ is the [[Clifford algebra|A38B1QFK20]] of $(T_x M, g_x)$ with $v \cdot v = -g(v, v)$.
The [[Levi-Civita connection|CAZYGE1T4E]] induces a connection on $\mathrm{Cl}(M)$.
A *Dirac bundle* over $M$ is a real or complex vector bundle $S \to M$ with these data and properties.

1. $S$ is a bundle of left [[Clifford modules|31Q0RDPZ00]] over $\mathrm{Cl}(M)$.
That is, a smooth bundle map $\mathrm{Cl}(M) \otimes S \to S$, $\varphi \otimes \psi \mapsto \varphi \cdot \psi$, makes each fibre $S_x$ a module over $\mathrm{Cl}(T_x M)$.
2. $S$ has a Riemannian or Hermitian metric $\ip{\cdot}{\cdot}$ such that $\ip{e \cdot \psi_1}{e \cdot \psi_2} = \ip{\psi_1}{\psi_2}$ for every unit vector $e \in T_x M$ and all $\psi_1, \psi_2 \in S_x$.
3. $S$ has a [[connection|5ZYRRVE8BW]] $\nabla$ that preserves this metric.
4. $\nabla_X(\varphi \cdot \psi) = (\nabla_X \varphi) \cdot \psi + \varphi \cdot \nabla_X \psi$ for every vector field $X$, every section $\varphi$ of $\mathrm{Cl}(M)$ and every section $\psi$ of $S$.

The *Dirac operator* of $S$ is $D \psi = \sum_{i=1}^n e_i \cdot \nabla_{e_i} \psi$ for a local orthonormal frame $e_1, \ldots, e_n$.

## Remarks

Clause 2 is equivalent to the skew-adjointness of Clifford multiplication by each tangent vector.
Clauses 2 to 4 make $D$ formally self-adjoint, and its square satisfies $D^2 = \nabla^* \nabla + \mathfrak{R}$ for an explicit curvature endomorphism $\mathfrak{R}$.
The [[spinor bundle|PYYQQKAZ0C]] of a spin manifold, with the spin connection, is a Dirac bundle, and its Dirac operator is the Atiyah–Singer operator.

Example: let $S = \Lambda^* T^*M$ with the metric and connection induced by $g$, and let $v \cdot \omega = v^\flat \wedge \omega - \iota_v \omega$.
Then $v \cdot v \cdot \omega = -(v^\flat \wedge \iota_v \omega + \iota_v(v^\flat \wedge \omega)) = -g(v, v) \, \omega$, so clause 1 holds, and clauses 2 to 4 hold because the Levi-Civita connection is metric and commutes with wedge and contraction.
Its Dirac operator is $\sum_i (e_i^\flat \wedge \nabla_{e_i} - \iota_{e_i} \nabla_{e_i}) = d + \delta$, whose square is the [[Hodge Laplacian|PWG3GKZG80]].

Non-example: on $M = \R^n$ with $n \ge 2$, take the same bundle and Clifford multiplication, but the connection $\nabla'_X = \nabla_X + dx_1(X) \, A$, where $A$ is Clifford multiplication by $e_1 = \partial_1$.
Since $A$ is skew-adjoint, $\nabla'$ still preserves the metric, so clause 3 holds.
Clause 4 fails: for $X = e_1$ and $\varphi = e_2$, it would require $A(e_2 \cdot \psi) = e_2 \cdot A\psi$, but $e_1 e_2 = -e_2 e_1 \ne e_2 e_1$.

## Explanations

### L1 human

A Dirac bundle is a bundle of Clifford modules with a metric and a connection that are compatible with Clifford multiplication, so that it carries a well-behaved Dirac operator.
