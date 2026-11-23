---
tag: T21WETAHN5
kind: concept
name: Π¹₁-CA0
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
uses: [DC60FYCSPM, MKB74TX3Z8, M6JGF4TPM6, C72RBH0CDR]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Π11 comprehension Π11-CA0
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: The big five subsystems of second-order arithmetic
---

## Summary

Every closed set of reals is the union of a perfect set and a countable set, and over $\mathsf{RCA}_0$ this Cantor-Bendixson theorem is equivalent to $\Pi^1_1\text{-}\mathsf{CA}_0$.
The system is the subsystem of [[second-order arithmetic|DC60FYCSPM]] with comprehension for $\Pi^1_1$ formulas of the [[analytical hierarchy|M6JGF4TPM6]], as in the [[formal definition|VPGQM418AG]].
For every formula $\varphi(n) \equiv \forall Y\, \psi(n, Y)$ with $\psi$ arithmetical and $X$ not free, the scheme says:
$$\exists X\, \forall n\, \big(n \in X \leftrightarrow \forall Y\, \psi(n, Y)\big).$$
It is the strongest of the big five systems of reverse mathematics, and the only impredicative one.
Its [[proof-theoretic ordinal|C72RBH0CDR]] is $\psi_0(\Omega_\omega)$ in Buchholz's notation.

## Motivation

The Cantor-Bendixson theorem writes a closed set as the union of a perfect set and a countable set.
The perfect part is defined by a statement about all paths through a tree, and this is a property with a set quantifier.
[[ATR0|MKB74TX3Z8]] can iterate the removal of isolated points, but it cannot in general form the perfect kernel.
$\Pi^1_1$ comprehension is exactly the strength needed.

## Notation

$\mathrm{HJ}(X)$ is the *hyperjump* of $X$: the set of indices $e$ such that $\Phi^X_e$ is the characteristic function of a tree on $\mathbb{N}$ with no infinite path.
The system $\Pi^1_1\text{-}\mathsf{CA}$ adds the induction scheme for all formulas of $L_2$.

## Remarks

### A closed set and its perfect kernel

Let $C = \{ 0 \} \cup \{ 2^{-n} : n \in \mathbb{N} \} \cup [2, 3]$.
Each point $2^{-n}$ is isolated in $C$, and removing these points leaves $\{ 0 \} \cup [2, 3]$.
Now $0$ is isolated, and removing it leaves $[2, 3]$, which has no isolated points.
So the perfect kernel is $[2, 3]$, and the countable part is $\{ 0 \} \cup \{ 2^{-n} : n \in \mathbb{N} \}$.
Here two rounds of removal suffice, but for a general closed set the number of rounds is a countable ordinal that we do not know in advance.

### The hyperjump

Over $\mathsf{ACA}_0$, $\Pi^1_1\text{-}\mathsf{CA}_0$ is equivalent to the statement that $\mathrm{HJ}(X)$ exists for every set $X$.
The [[set of indices of computable well-orderings|EBS4CXD8TP]] is a typical instance, and it is not hyperarithmetical.
The trees in the definition of $\mathrm{HJ}(X)$ may be infinitely branching.
For finitely branching trees, "no infinite path" means "finite", by [[König's lemma|3P2J5NWCM1]], and that is arithmetical.

### Models

The [[full model|CAA7K3VF59]], with all subsets of $\mathbb{N}$, is a model of $\Pi^1_1\text{-}\mathsf{CA}_0$.
The [[arithmetical sets|9KPCZ6NA32]] form a model of $\mathsf{ACA}_0$ but not of $\Pi^1_1\text{-}\mathsf{CA}_0$.
Over $\mathsf{ACA}_0$, the system is equivalent to the statement that for every set $X$ there is a countable coded [[β-model|J0Z2GNJZ2W]] that contains $X$.

### Equivalents

Over $\mathsf{RCA}_0$, each of the following is equivalent to $\Pi^1_1\text{-}\mathsf{CA}_0$.

- Every closed subset of $\mathbb{R}$ is the union of a perfect set and a countable set.
- Every tree on $\mathbb{N}$ has a perfect kernel.
- Every countable abelian group is the direct sum of a divisible group and a reduced group.

### Strength

$\Pi^1_1\text{-}\mathsf{CA}_0$ is equivalent to $\Sigma^1_1\text{-}\mathsf{CA}_0$, because a set exists exactly when its complement exists.
It proves every axiom of $\mathsf{ATR}_0$.
It also proves that a countable coded $\beta$-model exists.
Every $\beta$-model satisfies $\mathsf{ATR}_0$, so $\Pi^1_1\text{-}\mathsf{CA}_0$ proves the consistency of $\mathsf{ATR}_0$.
So it is strictly stronger than $\mathsf{ATR}_0$, and its ordinal $\psi_0(\Omega_\omega)$, from the [[Buchholz psi functions|E7WEFRMQTB]], is far beyond $\Gamma_0$.

### Watch out

$\Pi^1_1\text{-}\mathsf{CA}_0$ does not prove $\Pi^1_2$ comprehension.
The set formed by the scheme is defined by a quantifier over all sets, including the set being formed.
This is what makes the system impredicative, and it is why it lies beyond the [[predicative|43BSXNWQBG]] systems such as $\mathsf{ATR}_0$.

### History

The Cantor-Bendixson theorem goes back to work of Georg Cantor and Ivar Bendixson in the 1880s.
Simpson's book *Subsystems of Second Order Arithmetic* (1999) gives the system and its equivalents a full chapter.

### Try it

First, does $\Pi^1_1$ comprehension give the set of indices of computable linear orders that have a descending sequence?
Yes: that property is $\Sigma^1_1$, and $\Sigma^1_1$ comprehension follows from $\Pi^1_1$ comprehension by taking complements.

Second, what is the countable part of $\{ 0 \} \cup [1, 2]$?
It is $\{ 0 \}$, the only isolated point, and the perfect kernel is $[1, 2]$.

## Explanations

### L1 human

$\Pi^1_1\text{-}\mathsf{CA}_0$ forms sets defined by one quantifier over all sets.
It is the strength needed to split a closed set into its perfect part and its countable part.
For example, it forms the set of all programs that compute a well-ordering.

### L2 human

A proof in $\Pi^1_1\text{-}\mathsf{CA}_0$ usually forms the set of nodes of a tree above which there is no infinite path, or the hyperjump of a parameter.
A reversal to $\Pi^1_1\text{-}\mathsf{CA}_0$ usually shows that the theorem gives $\mathrm{HJ}(X)$, or the set of nodes of a tree with an infinite path above them.
Over $\mathsf{ACA}_0$ it suffices to get, for every sequence of trees $(T_k)_k$ on $\mathbb{N}$, the set of $k$ such that $T_k$ has a path.

### L3 human

$\Pi^1_1\text{-}\mathsf{CA}_0$ is impredicative: a set is defined by quantifying over a totality to which it belongs.
Its ordinal analysis uses notations built from symbols for uncountable cardinals, as in Buchholz's functions $\psi_\nu$.
The link with [[β-models|J0Z2GNJZ2W]] is one way to see its strength: from any set it builds a countable model containing that set that judges $\Pi^1_1$ statements about its own sets correctly.
