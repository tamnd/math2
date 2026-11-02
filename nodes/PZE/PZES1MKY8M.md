---
tag: PZES1MKY8M
kind: definition
name: Relational clone
msc: [08A40, 08A02]
defines: MC25MTN2N7
uses: [05AVARPXA2, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Clone_(algebra)
---

## Definition

Let $A$ be a nonempty set.
Let $\Gamma$ be a set of finitary relations on $A$.
A *primitive positive formula* over $\Gamma$ is a formula of the form
$$\exists y_1 \cdots \exists y_k \, \bigl(\varphi_1 \wedge \cdots \wedge \varphi_r\bigr).$$
Here each $\varphi_j$ is an equation $z_1 = z_2$ or an atomic formula $R(z_1, \dots, z_m)$ with $R \in \Gamma$ of arity $m$.
The $z_i$ are variables.
A relation $S \subseteq A^p$ is *primitive positive definable* from $\Gamma$ if $S = \set{(a_1, \dots, a_p) \in A^p : \psi(a_1, \dots, a_p)}$.
Here $\psi(x_1, \dots, x_p)$ is a primitive positive formula over $\Gamma$ with free variables $x_1, \dots, x_p$.
A *relational clone* on $A$ is a set $\Gamma$ of finitary relations on $A$ such that:

1. $\Gamma$ contains the binary equality relation $\set{(a, a) : a \in A}$.
2. $\Gamma$ contains the empty relation of each arity.
3. Every relation that is primitive positive definable from $\Gamma$ belongs to $\Gamma$.

## Remarks

Example: for any set $F$ of operations on $A$, the set $\operatorname{Inv}(F)$ of all relations preserved by every $f \in F$ is a relational clone.
Check: equality and empty relations are preserved by every operation.
If the relations in a primitive positive formula are preserved by $f$, so is the defined relation, because $f$ can be applied to the witnesses $y_i$ too.
Non-example: on $\set{0, 1}$, the set consisting of equality, the empty relations and the single relation $R = \set{(0, 1)}$ is not a relational clone.
The formula $\exists y \, R(x, y)$ defines the unary relation $\set{0}$, which is not in this set.
Conventions differ slightly between texts on whether the empty relation is included.
