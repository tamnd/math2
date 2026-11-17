---
tag: K9XG0Z2N9V
kind: definition
name: ACA0
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
defines: NAASTN80QN
uses: [DC60FYCSPM, Y92NXGEQBD, DNXCKXZZ08]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Arithmetical comprehension ACA0
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: Arithmetical comprehension
---

## Definition

A formula of $L_2$ is *arithmetical* when it has no set quantifiers; it may have free set variables and number quantifiers.
*Arithmetical comprehension* is the scheme of all universal closures of
$$\exists X\, \forall n\, \big(n \in X \leftrightarrow \varphi(n)\big),$$
with $\varphi$ arithmetical and $X$ not free in $\varphi$.

$\mathsf{ACA}_0$ is the subsystem of [[second-order arithmetic|DC60FYCSPM]] whose axioms are the basic axioms, the set induction axiom, and arithmetical comprehension, as in the [[definition of second-order arithmetic|Y92NXGEQBD]].

## Notation

The name abbreviates "arithmetical comprehension axiom".
$\mathsf{ACA}_0$ contains [[RCA0|DNXCKXZZ08]]: $\Delta^0_1$ comprehension is a case of arithmetical comprehension, and $\Sigma^0_1$ induction follows from the set induction axiom applied to the set $\set{n : \varphi(n)}$.
The system $\mathsf{ACA}$ adds the induction scheme for all $L_2$ formulas.

## Remarks

Example: the formula $\exists s\, \theta(e, s, X)$ that defines the Turing jump of $X$ is arithmetical, so $\mathsf{ACA}_0$ proves that every set has a Turing jump.

Example: the set of $\sigma$ in a tree $T$ with extensions of every length is defined by an arithmetical formula with parameter $T$, so it exists in $\mathsf{ACA}_0$.

Non-example: the formula $\exists Y\, (Y \text{ is a path through } T)$ has a set quantifier, so the set of trees with a path is not given by arithmetical comprehension.

## Explanations

### L1 human

$\mathsf{ACA}_0$ allows a set to exist whenever it is described by quantifiers over numbers, with given sets as parameters.
It does not allow descriptions that quantify over sets.

### L2 human

Arithmetical comprehension is equivalent over $\mathsf{RCA}_0$ to $\Sigma^0_1$ comprehension, and to the statement that the range of every one-to-one function exists.
So to prove an instance, one may climb the arithmetical hierarchy one quantifier at a time.
A trap is to think that $\mathsf{ACA}_0$ has induction for all formulas: it has induction for arithmetical formulas, which follows from the set induction axiom, but not for formulas with set quantifiers.
