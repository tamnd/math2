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

We define the system $\mathsf{ACA}_0$, in which every set that can be described with quantifiers over numbers exists.

A formula of $L_2$ is *arithmetical* when it has no set quantifiers.
It may have free set variables, which act as parameters, and any number of number quantifiers.
*Arithmetical comprehension* is the scheme of all universal closures of
$$\exists X\, \forall n\, \big(n \in X \leftrightarrow \varphi(n)\big),$$
where $\varphi$ is arithmetical and $X$ is not free in $\varphi$.

$\mathsf{ACA}_0$ is the subsystem of [[second-order arithmetic|DC60FYCSPM]] whose axioms are the basic axioms, the set induction axiom, and arithmetical comprehension, as in the [[definition of second-order arithmetic|Y92NXGEQBD]].

## Notation

The name abbreviates "arithmetical comprehension axiom".
The system $\mathsf{ACA}$ adds the induction scheme for all formulas of $L_2$.

## Remarks

The restriction to arithmetical formulas is the heart of the definition.
A formula without set quantifiers can be checked by looking at numbers and at the given parameter sets only, so the set it defines is computable from a finite jump of the parameters.
Once a set quantifier enters, the definition may refer to all sets, and we reach the stronger systems [[ATR0|TMJJSN9PDP]] and [[Π¹₁-CA0|VPGQM418AG]].

The condition that $X$ is not free in $\varphi$ blocks circular definitions.
Without it, the instance with $\varphi(n) \equiv n \notin X$ would assert a set $X$ with $n \in X \leftrightarrow n \notin X$, which is a contradiction.

The single set induction axiom is enough to give induction for every arithmetical formula.
Given such a formula $\psi(n)$, arithmetical comprehension forms the set $\{ n : \psi(n) \}$, and the set induction axiom applies to that set.
In particular $\mathsf{ACA}_0$ contains [[RCA0|DNXCKXZZ08]]: $\Delta^0_1$ comprehension is a case of arithmetical comprehension, and $\Sigma^0_1$ induction follows in the way just described.

For an example, the [[Turing jump|60P2XWY5QX]] of $X$ is defined by "$\exists s$, the program $e$ with oracle $X$ halts on input $x$ within $s$ steps", which is arithmetical, so $\mathsf{ACA}_0$ proves that every set has a jump.
In the same way, the set of nodes of a tree $T$ that have extensions of every length is defined by an arithmetical formula with parameter $T$, so it exists.

For a case that fails, the formula "there is a set $Y$ that is a path through the tree with index $n$" has a set quantifier.
So arithmetical comprehension does not give the set of indices of trees that have a path, and indeed that set is not arithmetical in general.

The concept of [[ACA0|NAASTN80QN]] gives the models, the equivalents and the strength of the system.

## Explanations

### L1 human

$\mathsf{ACA}_0$ lets a set exist whenever we can describe its members with "for every number" and "there is a number".
For example, the set of even numbers and the set of programs that halt both exist.
It does not allow descriptions of the form "there is a set such that".

### L2 human

Arithmetical comprehension is equivalent over $\mathsf{RCA}_0$ to $\Sigma^0_1$ comprehension and to the [[statement that the range of every one-to-one function exists|3MQ39PRCYJ]].
So to justify an instance, we may climb the arithmetical hierarchy one quantifier at a time.
For "$e$ is the index of a total program", first form by $\Sigma^0_1$ comprehension the set $H$ of pairs $(e, x)$ such that program $e$ halts on $x$.
The set of $e$ with some pair $(e, x)$ outside $H$ is $\Sigma^0_1$ in $H$, so it exists too, and its complement is the set of indices of total programs.
Watch out: $\mathsf{ACA}_0$ has induction for arithmetical formulas, but not for formulas with set quantifiers.
