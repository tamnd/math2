---
tag: V8JVWE87TE
kind: statement
role: theorem
name: Brauer's theorem on induced characters
msc: [20C15]
uses: [G5S1M9, 0X1JXT47GA, RMWMYBY8TC, JJP4JFH3C6, 0KVGH0J5B3, 06QYRTX9KQ, 00HF4RJ5QN]
about: [RMWMYBY8TC, JJP4JFH3C6]
sources:
  - url: https://en.wikipedia.org/wiki/Brauer%27s_theorem_on_induced_characters
same_as:
  wikidata: Q4958218
  wikipedia: Brauer's theorem on induced characters
---

## Statement

Let $G$ be a finite [[group|G5S1M9]].
Let $p$ be a prime.
A subgroup $E$ of $G$ is $p$-elementary if it is a [[direct product|00HF4RJ5QN]] $E = C \times P$ of two subgroups.
Here $C$ is a [[cyclic group|0KVGH0J5B3]] of order prime to $p$ and $P$ is a [[$p$-group|06QYRTX9KQ]].
A subgroup is elementary if it is $p$-elementary for some prime $p$.
Then every complex [[character|RMWMYBY8TC]] of $G$ is an integer linear combination of [[induced|JJP4JFH3C6]] characters $\operatorname{Ind}_E^G \lambda$.
Here $E$ runs over the elementary subgroups of $G$ and $\lambda$ over the degree $1$ characters of $E$.

## Remarks

The proof shows that the trivial character $1_G$ lies in the subgroup $I$ of the ring of virtual characters spanned by characters induced from elementary subgroups.
Since $I$ is an ideal, by the formula $\operatorname{Ind}(\theta) \cdot \psi = \operatorname{Ind}(\theta \cdot \psi|_E)$, it then contains every character.
The passage from all characters of elementary subgroups to degree $1$ characters uses that elementary groups are nilpotent, so their irreducible characters are induced from degree $1$ characters.
The coefficients cannot in general be taken nonnegative.
If $G$ is not elementary, every elementary subgroup $E$ is proper, so each $\operatorname{Ind}_E^G \lambda$ has degree $[G : E] \ge 2$.
Then no combination with nonnegative integer coefficients equals the trivial character, of degree $1$.
Compared with [[Artin's induction theorem|2CABBY4EEB]], which uses cyclic subgroups and rational coefficients, Brauer's theorem uses larger subgroups and gains integer coefficients.

## Explanations

### L1 human

Every character of a finite group can be assembled from very simple pieces: one-dimensional characters of small, almost abelian subgroups, pushed up to the whole group by induction.
The price is that one must allow subtraction as well as addition.

### L2 human

A main use is in number theory: Brauer deduced that Artin L-functions extend to meromorphic functions on the whole complex plane, since this holds for Hecke L-functions of one-dimensional characters.
The theorem also gives Brauer's characterisation of characters: a class function is a virtual character if and only if its restriction to every elementary subgroup is a virtual character.
From this one obtains that every complex representation of $G$ can be realised over the field $\Q(\zeta_m)$, where $m$ is the exponent of $G$.
