---
tag: MKB74TX3Z8
kind: concept
name: ATR0
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
uses: [DC60FYCSPM, NAASTN80QN, 01CGSJ0GNQ, C72RBH0CDR]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Arithmetical transfinite recursion ATR0
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: The big five subsystems of second-order arithmetic
---

## Summary

Any two countable [[well-orderings|01CGSJ0GNQ]] are comparable: one is isomorphic to an initial segment of the other.
Over $\mathsf{RCA}_0$ this statement is equivalent to $\mathsf{ATR}_0$, the system in which every arithmetical construction can be iterated along every countable well-ordering.
Its axioms are those of [[ACA0|NAASTN80QN]] together with arithmetical transfinite recursion, as in the [[formal definition|TMJJSN9PDP]].
For each arithmetical formula $\theta(n, Y)$, with $H_j$ the $j$-th column of $H$ and $H^j$ the part of $H$ below $j$, the scheme says:
$$\forall W\, \Big(\mathrm{WO}(W) \to \exists H\, \forall j \in \mathrm{field}(W)\, \forall n\, \big(n \in H_j \leftrightarrow \theta(n, H^j)\big)\Big).$$
$\mathsf{ATR}_0$ is the fourth of the big five systems of reverse mathematics, and its [[proof-theoretic ordinal|C72RBH0CDR]] is $\Gamma_0$.

## Motivation

Some theorems need the Turing jump iterated transfinitely often.
The classical proof that two well-orderings are comparable builds the comparison map by recursion along one of them.
The Cantor-Bendixson analysis of a closed set of reals removes isolated points again and again, along countable ordinals.
$\mathsf{ACA}_0$ iterates the jump only finitely often, and arithmetical transfinite recursion is the next step: any arithmetical step, along any well-ordering that the system can see.

## Notation

The name abbreviates "arithmetical transfinite recursion".
$\mathrm{WO}(W)$ is the $\Pi^1_1$ statement that $W$ codes a countable well-ordering.
A set $H$ as in the scheme is a *hierarchy along $W$ for $\theta$*.
The system $\mathsf{ATR}$ adds the induction scheme for all formulas of $L_2$.

## Remarks

### Comparing two well-orderings

Let $W_1$ be $\omega + 1$, the natural numbers followed by one top element $\top$.
Let $W_2$ be $\omega + \omega$, two copies of the natural numbers, one after the other.
The comparison map $F$ is built by recursion along $W_1$: $F(a)$ is the least element of $W_2$ above all values $F(a')$ with $a' <_{W_1} a$.
So $F(n)$ is $n$ in the first copy, and $F(\top)$ is $0$ in the second copy.
The map $F$ is an isomorphism of $W_1$ onto an initial segment of $W_2$.
Each step "the least element above all earlier values" is arithmetical in the earlier part of the hierarchy, so this is an instance of the scheme.

### The jump along ω

For $W = (\mathbb{N}, <)$ and the step "$n$ is in the Turing jump of $Y$", a hierarchy has columns $\emptyset', \emptyset'', \emptyset''', \ldots$ up to Turing equivalence.
So [[ATR0 proves that the ω-th jump exists|MF6AG57W3W]], a set that [[ACA0|9KPCZ6NA32]] does not prove to exist.
With a parameter $X$ in the step, $\mathsf{ATR}_0$ proves that $X^{(\omega)}$ exists for every $X$.

### Models

The [[full model|CAA7K3VF59]], with all subsets of $\mathbb{N}$, is a model of $\mathsf{ATR}_0$.
More generally, every [[β-model|J0Z2GNJZ2W]] is a model of $\mathsf{ATR}_0$.
The [[arithmetical sets|9KPCZ6NA32]] form a model of $\mathsf{ACA}_0$ but not of $\mathsf{ATR}_0$, since the hierarchy of jumps along $\omega$ is missing.
Unlike $\mathsf{ACA}_0$, the system $\mathsf{ATR}_0$ has no least $\omega$-model.
The [[hyperarithmetical sets|NS1HWGTD8E]] are the intersection of all its $\omega$-models, but they do not form a model of $\mathsf{ATR}_0$.

### Equivalents

Over $\mathsf{RCA}_0$, each of the following is equivalent to $\mathsf{ATR}_0$.

- Any two countable well-orderings are comparable.
- Every uncountable closed subset of $\mathbb{R}$ contains a [[perfect set|628242KN0T]].
- The Lusin separation theorem: two disjoint analytic subsets of $\mathbb{R}$ can be separated by a Borel set.
- [[Ulm's theorem|D8A4VEQR98]] for countable reduced abelian $p$-groups.
- Open determinacy: every open game on $\mathbb{N}^{\mathbb{N}}$ is determined.

### Strength

$\mathsf{ATR}_0$ contains $\mathsf{ACA}_0$ properly, and it is properly contained in [[Π¹₁-CA0|T21WETAHN5]].
Since it proves that $X^{(\omega)}$ exists, it proves that there is a countable coded $\omega$-model of $\mathsf{ACA}_0$, and so it proves the consistency of $\mathsf{ACA}_0$.
Its proof-theoretic ordinal is the [[Feferman-Schütte ordinal|CNN7BK5YAW]] $\Gamma_0$.
It proves the same $\Pi^1_1$ sentences as Feferman's system $\mathsf{IR}$ of predicative analysis.
For this reason it is the system of predicative reductionism, in the sense of [[predicative mathematics|43BSXNWQBG]].

### Watch out

A model of $\mathsf{ATR}_0$ can contain a linear order that it takes for a well-ordering, but which has a descending sequence outside the model.
The well-orderings of the model agree with the true ones only in $\beta$-models.
The scheme iterates arithmetical steps only, so a step such as "$n$ is in the hyperjump of $Y$" is not allowed.
And $\mathsf{ATR}_0$ does not prove transfinite induction along well-orderings for every formula of $L_2$.

### History

Harvey Friedman introduced $\mathsf{ATR}_0$, and he proved that it is equivalent to the comparability of countable well-orderings.
Simpson's book *Subsystems of Second Order Arithmetic* (1999) gives the system and its equivalents a full chapter.

### Try it

First, in the example of comparing $\omega + 1$ with $\omega + \omega$, which order is the shorter one?
The order $\omega + 1$, since $F$ maps it onto the initial segment of $\omega + \omega$ below $1$ in the second copy.

Second, does the scheme give a hierarchy of jumps along the order of the negative integers?
No: that order has the descending sequence $-1, -2, -3, \ldots$, so it is not a well-ordering, and the scheme does not apply.

## Explanations

### L1 human

$\mathsf{ATR}_0$ allows one to repeat an arithmetical construction transfinitely often, along any countable well-ordering.
At each stage the construction may use the results of all earlier stages.
This is the strength needed to compare two well-orderings, and to analyze closed sets of reals by removing isolated points again and again.

### L2 human

A proof in $\mathsf{ATR}_0$ usually defines an object by transfinite recursion along a well-ordering, with an arithmetical step.
A reversal to $\mathsf{ATR}_0$ usually goes through comparability: from two well-orderings, one builds an instance of the theorem whose solution gives a comparison map.
For example, the Cantor-Bendixson process on a closed set runs along the countable ordinals until it stops, and the stages form a hierarchy for the step "remove the isolated points".
A trap is to use transfinite induction for a formula with set quantifiers, since $\mathsf{ATR}_0$ does not prove it in general.

### L3 human

$\mathsf{ATR}_0$ is the upper limit of predicative reductionism in the sense of Feferman and Schütte, and its strength is measured by $\Gamma_0$.
Its study uses pseudo-hierarchies: hierarchies along linear orders that are not well-founded but that a model takes for well-orderings.
The hypothesis $\mathrm{WO}(W)$ of the scheme is $\Pi^1_1$, so the scheme is not comprehension for a class of formulas.
It lies strictly between arithmetical comprehension and $\Pi^1_1$ comprehension.
