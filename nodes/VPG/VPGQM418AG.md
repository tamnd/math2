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

We define the system $\Pi^1_1\text{-}\mathsf{CA}_0$, in which every set defined by one universal quantifier over sets exists.

A formula $\varphi$ of $L_2$ is $\Pi^1_1$ if it has the form $\forall Y\, \psi$ with $\psi$ arithmetical, as in the [[analytical hierarchy|M6JGF4TPM6]].
Free number and set variables are allowed in $\varphi$ as parameters.
*$\Pi^1_1$ comprehension* is the scheme of all universal closures of
$$\exists X\, \forall n\, \big(n \in X \leftrightarrow \varphi(n)\big),$$
where $\varphi(n)$ is $\Pi^1_1$ and $X$ is not free in $\varphi$.

$\Pi^1_1\text{-}\mathsf{CA}_0$ is the subsystem of [[second-order arithmetic|Y92NXGEQBD]] whose axioms are the basic axioms, the set induction axiom, and $\Pi^1_1$ comprehension.

## Notation

The subscript $0$ shows that induction is the single set induction axiom, and not the scheme for all formulas.
The same system is also written $\Pi^1_1$-$\mathsf{CA}_0$, with a plain hyphen.

## Remarks

The quantifier $\forall Y$ ranges over all sets, including the set $X$ that the scheme is about to form.
This is the impredicative feature of the scheme.
The matrix $\psi$ must be arithmetical, so a single block of universal set quantifiers is allowed, and no existential set quantifier after it.
The condition that $X$ is not free in $\varphi$ blocks circular definitions, as for arithmetical comprehension.

Comprehension for $\Sigma^1_1$ formulas follows.
For $\varphi$ in $\Pi^1_1$, the set $\{ n : \varphi(n) \}$ exists, and $\Delta^0_1$ comprehension gives its complement $\{ n : \neg \varphi(n) \}$.

Every arithmetical formula is $\Pi^1_1$ with a dummy set quantifier.
So $\Pi^1_1\text{-}\mathsf{CA}_0$ contains arithmetical comprehension, and with it [[RCA0|DNXCKXZZ08]] and $\mathsf{ACA}_0$.

For an example, "$e$ is the index of a computable well-ordering" is $\Pi^1_1$.
So the [[set of indices of computable well-orderings|EBS4CXD8TP]] exists in $\Pi^1_1\text{-}\mathsf{CA}_0$.

For a case outside the scheme, a formula $\forall Y\, \exists Z\, \psi$ with $\psi$ arithmetical is $\Pi^1_2$, and comprehension for it is not part of $\Pi^1_1\text{-}\mathsf{CA}_0$.

The concept of [[Π¹₁-CA0|T21WETAHN5]] gives the models, the equivalents and the strength of the system.

## Explanations

### L1 human

$\Pi^1_1$ comprehension forms the set of all numbers with a property that may say "for all sets $Y$".
Such properties include "this computable order is a well-ordering" and "this computable tree has no infinite path".

### L2 human

To use the scheme, write the property in the form $\forall Y\, \psi$ with $\psi$ arithmetical, and check that the set to be formed does not occur in it.
For "the tree $T_k$ has no path", the formula is $\forall Y\, \neg (Y \text{ is a path through } T_k)$, and "is a path" is arithmetical.
Watch out: a property with two alternating set quantifiers, such as "for every $Y$ there is a $Z$ with $\psi(n, Y, Z)$", is outside the scheme.
