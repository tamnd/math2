---
tag: CR4G3BVR2M
kind: definition
name: K1 of a C*-algebra
msc: [46L80, 19K99]
defines: 7NTVTHC7CG
uses: [M2WFY1D3SZ, KK9S67F8CA]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_K-theory
---

## Definition

Let $A$ be a [[C*-algebra|M2WFY1D3SZ]] and let $\widetilde{A}$ be its unitization.
If $A$ is unital, one may use $A$ itself, which gives the same group.
For $n \ge 1$, let $U_n(\widetilde{A})$ be the group of [[unitary elements|KK9S67F8CA]] of $M_n(\widetilde{A})$, and let $U_\infty(\widetilde{A})$ be the disjoint union of the $U_n(\widetilde{A})$.
Let $u \in U_n(\widetilde{A})$ and $v \in U_m(\widetilde{A})$.
Write $u \sim_1 v$ if, for some $k \ge \max(n, m)$, the unitaries $\operatorname{diag}(u, 1_{k-n})$ and $\operatorname{diag}(v, 1_{k-m})$ lie in the same path component of $U_k(\widetilde{A})$ for the norm topology.
The group $K_1(A)$ is the set $U_\infty(\widetilde{A})/\sim_1$ with the operation $[u] + [v] = [\operatorname{diag}(u, v)]$.

## Remarks

The operation is well defined, abelian, and every class has the inverse $[u]^{-1} = [u^*]$, so $K_1(A)$ is an abelian group with neutral element $[1]$.
Commutativity comes from the fact that $\operatorname{diag}(u, v)$ is homotopic to $\operatorname{diag}(v, u)$, and also to $\operatorname{diag}(uv, 1)$.
Example: for $A = C(\mathbb{T})$, the class of the unitary $z \mapsto z$ generates $K_1(A) \cong \Z$, and the isomorphism is given by the winding number of $z \mapsto \det u(z)$.
Non-example of a nonzero class: in $M_n(\C)$ every unitary is $e^{ih}$ for a self-adjoint $h$, so $t \mapsto e^{ith}$ joins it to $1$, and $K_1(M_n(\C)) = 0$.
A $*$-homomorphism $\varphi \colon A \to B$ induces $\varphi_* \colon K_1(A) \to K_1(B)$.
There is a natural isomorphism $K_1(A) \cong K_0(SA)$, where $SA = C_0(\R) \otimes A$ is the suspension of $A$.
