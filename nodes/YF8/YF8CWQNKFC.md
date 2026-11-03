---
tag: YF8CWQNKFC
kind: definition
name: Social welfare function
msc: [91B14, 91B10, 91B15]
defines: KH8ACT22FR
uses: [JGP0Q56FRY, PW2NKAPXWA, 0FRXBVVR03]
sources:
  - url: https://en.wikipedia.org/wiki/Social_welfare_function
---

## Definition

Let $N = \set{1, \dots, n}$ be a finite set of individuals and let $A$ be a set of alternatives.
Let $\mathcal{R}(A)$ be the set of [[weak orderings|PW2NKAPXWA]] of $A$, that is, complete and transitive [[preference relations|JGP0Q56FRY]] on $A$.
A *profile* is a tuple $(R_1, \dots, R_n)$ with $R_i \in \mathcal{R}(A)$ the preference of individual $i$.
Let $\mathcal{D} \subseteq \mathcal{R}(A)^n$ be a set of admissible profiles.
A *social welfare function* (in the sense of Arrow) on $\mathcal{D}$ is a map $F \colon \mathcal{D} \to \mathcal{R}(A)$.
It assigns to each admissible profile a social preference $F(R_1, \dots, R_n)$, which is again a weak ordering of $A$.

## Remarks

Example: let $A = \set{x, y}$ and $\mathcal{D} = \mathcal{R}(A)^n$.
Majority rule ranks $x$ strictly above $y$ when more individuals strictly prefer $x$ to $y$ than $y$ to $x$, and declares indifference on a tie.
The result is complete and transitive on two alternatives, so majority rule is a social welfare function here.

Non-example: with $A = \set{x, y, z}$, three individuals and all profiles of [[linear orders|0FRXBVVR03]], pairwise majority rule is not a social welfare function.
For the profile $x \succ y \succ z$, $y \succ z \succ x$, $z \succ x \succ y$ it ranks $x$ above $y$, $y$ above $z$ and $z$ above $x$, which is not transitive.

Often $\mathcal{D}$ is taken to be all of $\mathcal{R}(A)^n$ (unrestricted domain), or the set of profiles of linear orders.
A *Bergson–Samuelson social welfare function* is a different notion: a function $W(u_1, \dots, u_n)$ of the individuals' utility levels, increasing in each argument.
