---
tag: DKRTRRG3V4
kind: definition
name: Inductive type
msc: [03B38, 68N15]
defines: Q80JWCWNKX
uses: [Q48KGV33AH, M6W6ZB4PPX, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Inductive_type
---

## Definition

Work in a dependent [[type theory|Q48KGV33AH]] with function types and a universe of types.
An *inductive type* $T$ is declared by a finite list of constructors $c_1, \dots, c_k$.
Each constructor has a type of the form $c_i : A_{i,1} \to \cdots \to A_{i,m_i} \to T$.
The declaration must satisfy *strict positivity*.
This means that each argument type $A_{i,j}$ either does not mention $T$, or has the form $B_1 \to \cdots \to B_r \to T$ where no $B_l$ mentions $T$.
The declaration adds the following rules.

1. Formation: $T$ is a type.
2. Introduction: each $c_i$ is a term of its declared type.
3. Elimination: for every [[type family|M6W6ZB4PPX]] $P$ over $T$, a function $f : \Pi_{x : T} P(x)$ is given by one case for each constructor.
   In the case of $c_i$, the value at $c_i\, a_1 \cdots a_{m_i}$ may use the values of $f$ at the arguments $a_j$ of type $T$.
4. Computation: $f(c_i\, a_1 \cdots a_{m_i})$ reduces to the case of $c_i$ applied to $a_1, \dots, a_{m_i}$ and to those values of $f$.

## Remarks

Example: the natural numbers are the inductive type $\N$ with constructors $\mathsf{zero} : \N$ and $\mathsf{succ} : \N \to \N$.
Strict positivity holds, since the only argument of $\mathsf{succ}$ is $\N$ itself.
Rule 3 is the [[induction|0ASJVEFA9J]] principle: to give $f : \Pi_{n : \N} P(n)$ one gives $f(\mathsf{zero}) : P(\mathsf{zero})$ and, for each $n$, $f(\mathsf{succ}\, n) : P(\mathsf{succ}\, n)$ computed from $n$ and $f(n)$.

Non-example: a type $D$ with one constructor $\mathsf{lam} : (D \to D) \to D$ is rejected.
The argument type $D \to D$ mentions $D$ to the left of an arrow, so strict positivity fails.
Accepting $D$ would allow the term $(\lambda x.\, x\, x)(\lambda x.\, x\, x)$ of the untyped lambda calculus to be encoded, which gives a term of type $D$ with no normal form.
A similar type with a constructor $(T \to \bot) \to T$, where $\bot$ is the empty type, would give a closed term of $\bot$, that is, a proof of falsity.

Other standard examples are lists, with $\mathsf{nil}$ and $\mathsf{cons}$, and binary trees.
Inductive families, such as vectors of a given length, allow the constructors to target different instances $T(a)$ of a type family.
