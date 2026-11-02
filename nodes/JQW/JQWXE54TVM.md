---
tag: JQWXE54TVM
kind: definition
name: Dual abelian variety
msc: [14K30, 14K05]
defines: HZXSESHC8P
uses: [R7W03TXRS9, 7JCF2TE3V5, 3Z9DCWYXQZ]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_abelian_variety
---

## Definition

Let $A$ be an [[abelian variety|R7W03TXRS9]] over a field $k$, with unit $e \in A(k)$.
For a point $x$ of $A$, let $t_x \colon A \to A$ be translation by $x$.
Let $\bar{k}$ be an algebraic closure of $k$.
Let $\operatorname{Pic}^0(A)$ be the subgroup of the [[Picard group|3Z9DCWYXQZ]] of classes of [[line bundles|7JCF2TE3V5]] $L$ with $t_x^{*} L \cong L$ for all $x \in A(\bar{k})$.
The *dual abelian variety* of $A$ is an abelian variety $A^\vee$ over $k$ with a line bundle $P$ on $A \times_k A^\vee$, the Poincaré bundle, such that:

1. $P$ restricted to $\set{e} \times A^\vee$ is trivial;
2. $P$ restricted to $A \times \set{y}$ lies in $\operatorname{Pic}^0$ for every point $y$ of $A^\vee$;
3. $(A^\vee, P)$ is universal, in the following sense.
   Let $T$ be a $k$-scheme and $L$ a line bundle on $A \times_k T$.
   Assume $L$ is trivial on $\set{e} \times T$ and in $\operatorname{Pic}^0$ on each fibre $A \times \set{t}$.
   Then there is a unique morphism $f \colon T \to A^\vee$ with $L \cong (\id_A \times f)^{*} P$.

## Remarks

The pair $(A^\vee, P)$ exists and is unique up to unique isomorphism.
When $k$ is algebraically closed, clause 3 with $T = \operatorname{Spec} k$ gives a bijection $A^\vee(k) \cong \operatorname{Pic}^0(A)$.
The dimension of $A^\vee$ equals the dimension of $A$, and $(A^\vee)^\vee \cong A$.

Example: let $E$ be an elliptic curve over an algebraically closed field with origin $O$.
The map $P \mapsto \mathcal{O}_E(P - O)$ is a bijection from $E(k)$ onto the line bundles of degree $0$, and these are exactly the translation-invariant ones.
So $E^\vee \cong E$.

Non-example: the full Picard group of $E$ is not the dual.
The line bundle $\mathcal{O}_E(O)$ has degree $1$, and $t_x^{*} \mathcal{O}_E(O) \cong \mathcal{O}_E(O)$ fails for every $x \ne O$, so it is not in $\operatorname{Pic}^0(E)$.

Over $\C$, if $A = V / \Lambda$, then $A^\vee$ is the quotient of the space of $\C$-antilinear forms $f$ on $V$ by the lattice of those $f$ with $\operatorname{Im} f(\Lambda) \subseteq \Z$.
