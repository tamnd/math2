---
tag: SVNXZ5JP35
kind: problem
name: Congruence subgroup problem
msc: [19B37, "20G30", "11F06"]
uses: [MWBDFS2KJ5, 0BXA4Q0JHW, GA81VVQHEP, 0DTXBQPA2S, CG9EH0TN27, 1H6R856P3C, 4XWG6S7R4Z]
about: [1H6R856P3C, 4XWG6S7R4Z]
sources:
  - url: https://en.wikipedia.org/wiki/Congruence_subgroup
    locator: The congruence subgroup problem
history:
  posed_by: "Hyman Bass, John Milnor and Jean-Pierre Serre"
  first_stated: "1967"
---

## Problem

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] with [[ring of integers|0BXA4Q0JHW]] $\mathcal{O}$.
Let $G \subseteq GL_n$ be a [[linear algebraic group|GA81VVQHEP]] defined over $K$, and let $\Gamma = G(K) \cap GL_n(\mathcal{O})$ be the corresponding [[arithmetic group|4XWG6S7R4Z]].
For a nonzero ideal $\mathfrak{q}$ of $\mathcal{O}$, let $\Gamma(\mathfrak{q})$ be the kernel of reduction $\Gamma \to GL_n(\mathcal{O}/\mathfrak{q})$.
A subgroup of $\Gamma$ is a [[congruence subgroup|1H6R856P3C]] if it contains some $\Gamma(\mathfrak{q})$.
Every congruence subgroup has finite [[index|0DTXBQPA2S]] in $\Gamma$.
Let $\widehat{\Gamma}$ be the [[profinite completion|CG9EH0TN27]] of $\Gamma$ and let $\overline{\Gamma} = \varprojlim_{\mathfrak{q}} \Gamma/\Gamma(\mathfrak{q})$ be its congruence completion.
The natural map $\widehat{\Gamma} \to \overline{\Gamma}$ is surjective, and its kernel $C(\Gamma)$ is the *congruence kernel*.

1. Is every subgroup of finite index in $\Gamma$ a congruence subgroup, that is, is $C(\Gamma)$ trivial?
2. In general, is $C(\Gamma)$ finite, and what is it?

## Remarks

The classical case is $\Gamma = SL_2(\Z)$, where the answer is negative.
Felix Klein already knew that it has subgroups of finite index that are not congruence subgroups, and $C(SL_2(\Z))$ is infinite.
For $SL_n(\Z)$ with $n \ge 3$, Bass–Lazard–Serre and Mennicke showed that every subgroup of finite index is a congruence subgroup.
The [[Bass–Milnor–Serre theorem|PYPSVTYTZ8]] extends this to $SL_n(\mathcal{O})$ with $n \ge 3$.
There $C(\Gamma)$ is trivial when $K$ has a real embedding.
When $K$ is totally imaginary, $C(\Gamma)$ is cyclic of order the number of roots of unity in $K$.
Bass, Milnor and Serre posed the problem for general groups $G$ in their 1967 paper.
Serre treated $SL_2$ over rings of $S$-integers in 1970 and conjectured that the answer depends on the rank of the group.
The problem is solved for many groups and remains open in some cases, for example some forms of type $A_n$ and some lattices of real rank one.
Its solution for $SL_n$ goes through relative $SK_1$ groups, which is why it belongs to algebraic K-theory.

## Explanations

### L1 human

Reducing integer matrices modulo a number $m$ gives a map onto a finite group of matrices, and its kernel is a subgroup of finite index.
The problem asks whether every subgroup of finite index arises from such reductions.
For $2 \times 2$ matrices the answer is no, but for larger matrices over the integers the answer is yes.
In general it asks how far the finite quotients of an arithmetic group are explained by arithmetic modulo ideals.
