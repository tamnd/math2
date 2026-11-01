---
tag: 2CABBY4EEB
kind: statement
role: theorem
name: Artin's induction theorem
msc: [20C15]
uses: [G5S1M9, 0X1JXT47GA, RMWMYBY8TC, JJP4JFH3C6, 0KVGH0J5B3]
about: [RMWMYBY8TC, JJP4JFH3C6]
sources:
  - url: https://en.wikipedia.org/wiki/Artin%27s_theorem_on_induced_characters
same_as:
  wikidata: Q97359344
  wikipedia: Artin's theorem on induced characters
---

## Statement

Let $G$ be a finite [[group|G5S1M9]].
Then every complex [[character|RMWMYBY8TC]] of $G$ is a rational linear combination of [[induced|JJP4JFH3C6]] characters $\operatorname{Ind}_C^G \theta$.
Here $C$ runs over the [[cyclic|0KVGH0J5B3]] subgroups of $G$ and $\theta$ over the characters of $C$.

## Remarks

For the proof, let $\psi$ be a class function on $G$ orthogonal to all characters induced from cyclic subgroups.
By [[Frobenius reciprocity|PAP76H0ND9]], the restriction of $\psi$ to each cyclic subgroup is orthogonal to all its characters, so it is zero.
Every element of $G$ lies in a cyclic subgroup, so $\psi = 0$.
Hence the induced characters span the space of class functions over $\C$, and a rationality argument gives rational coefficients.
Rational coefficients are needed in general.
For example, let $V = \Z/2 \times \Z/2$ be the Klein four-group.
Its cyclic subgroups are proper, so every character induced from one of them has even degree, and so has every integer combination of such characters.
Hence the trivial character $1_V$, of degree $1$, is not an integer combination.
But $1_V = \frac{1}{2}\sum_{C} \operatorname{Ind}_C^V 1_C - \frac{1}{2}\operatorname{Ind}_{1}^{V} 1$, with $C$ running over the three subgroups of order $2$.
[[Brauer's theorem on induced characters|V8JVWE87TE]] reaches integer coefficients by using elementary subgroups instead of cyclic ones.

## Explanations

### L1 human

The theorem says that all characters of a finite group come from characters of its cyclic subgroups, the simplest subgroups there are, by induction and by taking rational combinations.
So, up to fractions, cyclic subgroups control the whole character theory.

### L2 human

Artin used this to show that a power of every Artin L-function is a quotient of products of abelian L-functions, so that some power of it is meromorphic.
Brauer's theorem later removed the power.
The theorem is a statement about the rational character ring: tensored with $\Q$, the induction maps from cyclic subgroups are jointly surjective.
