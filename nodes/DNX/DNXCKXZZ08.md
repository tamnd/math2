---
tag: DNXCKXZZ08
kind: definition
name: RCA0
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
defines: XQENB067R3
uses: [DC60FYCSPM, Y92NXGEQBD, GE43CSZTS9, 1QD0KDDGYJ]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Base system RCA0
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: Recursive comprehension
---

## Definition

$\mathsf{RCA}_0$ is the subsystem of second-order arithmetic in which a set exists when it is computable from given sets, and induction holds for $\Sigma^0_1$ formulas.

$\mathsf{RCA}_0$ is the subsystem of [[second-order arithmetic|DC60FYCSPM]] whose axioms are the following.

1. The basic axioms of $\mathsf{Z}_2$, as in the [[definition of second-order arithmetic|Y92NXGEQBD]].
2. $\Sigma^0_1$ induction: for every $\Sigma^0_1$ formula $\varphi(n)$ of $L_2$, with any parameters, the universal closure of the first formula below.
3. $\Delta^0_1$ comprehension: for every $\Sigma^0_1$ formula $\varphi(n)$ and every $\Pi^0_1$ formula $\psi(n)$, with any parameters, in which $X$ is not free, the universal closure of the second formula below.

$$\big(\varphi(0) \wedge \forall n \, (\varphi(n) \to \varphi(n + 1))\big) \to \forall n \, \varphi(n)$$
$$\forall n \, \big(\varphi(n) \leftrightarrow \psi(n)\big) \to \exists X \, \forall n \, \big(n \in X \leftrightarrow \varphi(n)\big)$$

Here $\Sigma^0_1$ and $\Pi^0_1$ are the classes of the [[arithmetical hierarchy|GE43CSZTS9]] for $L_2$.
A $\Sigma^0_1$ formula has the form $\exists k \, \theta$, where $\theta$ is built from atomic formulas, including $t \in X$, with bounded number quantifiers only, and a $\Pi^0_1$ formula has the form $\forall k \, \theta$.

## Notation

The name stands for "recursive comprehension axiom", and the subscript $0$ marks the restriction of induction.
The set induction axiom of $\mathsf{Z}_2$ is the instance of clause 2 for the formula $n \in X$, so $\mathsf{RCA}_0$ contains it.
Some authors write $\mathsf{RCA}$ for the system with the full [[induction scheme|1QD0KDDGYJ]].

## Remarks

Clause 2 limits induction to $\Sigma^0_1$ formulas.
This is enough to prove that definitions by primitive recursion give functions, and it keeps the first-order strength of the system at $\mathrm{I}\Sigma_1$.
With the full induction scheme, the system would prove every theorem of Peano arithmetic, including the consistency of $\mathrm{I}\Sigma_1$, which $\mathsf{RCA}_0$ does not prove.

Clause 3 asks for two definitions of the same set, one with an existential and one with a universal number quantifier.
In a computation this means that we can search for a proof that $n$ is in and for a proof that $n$ is out at the same time, and one search must succeed.
So the family of computable sets satisfies clause 3, because a set that is computably enumerable with a computably enumerable complement is computable.
Clause 3 does not ask that $\mathsf{RCA}_0$ prove the equivalence $\varphi \leftrightarrow \psi$.
The equivalence is the hypothesis of the instance, so the axiom applies inside a model whenever the equivalence holds there.

For a family that fails clause 3, add the halting set $K$ to the computable sets.
The complement of $K$ is defined from $K$ by $n \notin K$, which is both $\Sigma^0_1$ and $\Pi^0_1$ in the parameter $K$, but the complement is not in the family.
The [[concept of RCA0|XQENB067R3]] gives the models and theorems of the system.

## Explanations

### L1 human

$\mathsf{RCA}_0$ allows a set to exist when a computer, with the given sets as helpers, can decide membership in it.
It allows induction for statements of the form "there is a number $k$ such that a checkable condition holds".

### L2 human

To use clause 3, give two descriptions of a set: one of the form "some witness exists", and one of the form "every candidate passes a test".
For a function $f$, the set $\{ n : \exists k \, f(k) = n \}$ has only the first form, and it need not exist in $\mathsf{RCA}_0$.
If $f$ is strictly increasing, then $f(k) \ge k$ for all $k$, so $n$ is in the range exactly when $\exists k \le n \, f(k) = n$.
This condition is bounded, so it has both forms, and the range exists.
