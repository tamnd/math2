---
tag: ZTDC9MC2Y4
kind: concept
name: Brown–Douglas–Fillmore theory
msc: [19K33, 46L80, 47A53]
sources:
  - url: https://en.wikipedia.org/wiki/Calkin_algebra
---

## Summary

Brown–Douglas–Fillmore theory, or BDF theory, classifies extensions of the algebra $C(X)$ of continuous functions on a compact metric space $X$ by the [[compact operators|2WAZF1RV2Y]].
Such an extension is the same as an injective unital $*$-homomorphism from $C(X)$ into the [[Calkin algebra|6FE7JZ2VF1]].
Their classes form an abelian group $\operatorname{Ext}(X)$.
BDF showed that $\operatorname{Ext}$ is a homology theory, now identified with odd [[K-homology|41XX3KF72X]].
It solved the question of which essentially normal operators are compact perturbations of normal operators: for $X \subseteq \C$ the obstruction is the [[Fredholm index|2V9Q4KHY1T]].

## Explanations

### L1 human

A normal operator is one that commutes with its adjoint, and such operators are well understood by the spectral theorem.
An operator is essentially normal when it commutes with its adjoint up to a compact error.
BDF theory asks when such an operator is a normal operator plus a compact operator.
The unilateral shift is essentially normal, but it has Fredholm index $-1$, and this rules out such a decomposition.
BDF showed that for operators with planar essential spectrum the index is the only obstruction.
