---
tag: VPGQM418AG
kind: definition
name: Π¹₁-CA0
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
defines: T21WETAHN5
uses: [Y92NXGEQBD, DNXCKXZZ08, M6JGF4TPM6]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Π11 comprehension Π11-CA0
---

## Definition

A formula $\varphi$ of $L_2$ is $\Pi^1_1$ if it has the form $\forall X\, \psi$ with $\psi$ arithmetical, as in the [[analytical hierarchy|M6JGF4TPM6]].
Free number and set variables are allowed in $\varphi$ as parameters.

*$\Pi^1_1$ comprehension* is the scheme
$$\exists X\, \forall n\, \big(n \in X \leftrightarrow \varphi(n)\big)$$
for every $\Pi^1_1$ formula $\varphi(n)$ in which $X$ is not free.

$\Pi^1_1\text{-}\mathsf{CA}_0$ is the subsystem of [[second-order arithmetic|Y92NXGEQBD]] whose axioms are the basic axioms, the induction axiom, and $\Pi^1_1$ comprehension.

## Notation

The subscript $0$ shows that induction is the single induction axiom, and not the scheme for all formulas.
The same system is often written $\Pi^1_1\text{-CA}_0$ or $\Pi^1_1$-$\mathsf{CA}_0$.

## Remarks

Example: every arithmetical formula is $\Pi^1_1$ with a dummy set quantifier, so $\Pi^1_1\text{-}\mathsf{CA}_0$ contains arithmetical comprehension and thus [[RCA0|DNXCKXZZ08]] and $\mathsf{ACA}_0$.

Example: "$e$ is the index of a computable well-ordering" is $\Pi^1_1$, so the [[set of indices of computable well-orderings|EBS4CXD8TP]] exists in $\Pi^1_1\text{-}\mathsf{CA}_0$.

Non-example: a formula $\forall X\, \exists Y\, \psi$ with $\psi$ arithmetical is $\Pi^1_2$, and comprehension for it is not part of $\Pi^1_1\text{-}\mathsf{CA}_0$.

Comprehension for $\Sigma^1_1$ formulas follows: the set $\set{n : \neg \varphi(n)}$ exists, and so does its complement.

## Explanations

### L1 human

$\Pi^1_1$ comprehension forms the set of all numbers with a property that may say "for all sets $X$".
Such properties include "this computable order is a well-ordering" and "this computable tree has no infinite path".

### L2 human

To use the scheme, one writes the property in the form $\forall X\, \psi$ with $\psi$ arithmetical, and checks that the set variable to be formed does not occur in $\psi$.
A typical trap is a property with two alternating set quantifiers, which is outside the scheme.
