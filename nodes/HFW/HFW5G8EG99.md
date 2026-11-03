---
tag: HFW5G8EG99
kind: statement
role: theorem
name: Schaefer's dichotomy theorem
msc: [68Q17, 03B05]
uses: [5EHA6R2M6K, 3QKF32ZAKN, GVT2NKN37K, JGZWHWA8P8, 0B3D4C8YF2, 3GT13ACR68]
about: [5EHA6R2M6K]
sources:
  - url: https://en.wikipedia.org/wiki/Schaefer%27s_dichotomy_theorem
same_as:
  wikidata: Q7430892
  wikipedia: Schaefer's dichotomy theorem
---

## Statement

Let $\Gamma$ be a finite set of nonempty relations on $\set{0, 1}$.
Let $\mathrm{SAT}(\Gamma)$ be the [[constraint satisfaction problem|5EHA6R2M6K]] $\mathrm{CSP}(\Gamma)$ with domain $\set{0, 1}$.
Then $\mathrm{SAT}(\Gamma)$ lies in [[P|GVT2NKN37K]] if at least one of the following holds.

1. Every relation in $\Gamma$ contains the all-zero tuple.
2. Every relation in $\Gamma$ contains the all-one tuple.
3. Every relation in $\Gamma$ is the set of models of a [[conjunctive normal form|0B3D4C8YF2]] whose clauses each have at most one positive literal.
4. Every relation in $\Gamma$ is the set of models of a conjunctive normal form whose clauses each have at most one negative literal.
5. Every relation in $\Gamma$ is the set of models of a conjunctive normal form whose clauses each have at most two literals.
6. Every relation in $\Gamma$ is the set of solutions of a system of linear equations over the field $\F_2$.

Otherwise $\mathrm{SAT}(\Gamma)$ is [[NP-complete|JGZWHWA8P8]].

## Remarks

The classes are called $0$-valid, $1$-valid, Horn, dual Horn, bijunctive and affine.
In cases 1 and 2 the constant assignment works.
In cases 3 and 4 unit propagation decides the problem, in case 5 the method for 2-SAT does, and in case 6 Gaussian elimination does.
For the hardness, assume that none of the six conditions holds.
Schaefer showed that the relations of $\Gamma$ then express every Boolean relation by existentially quantified conjunctions, possibly with the help of constants.
So [[SAT|3QKF32ZAKN]] reduces to $\mathrm{SAT}(\Gamma)$.
Thomas Schaefer proved the theorem in 1978.

Example: 3-SAT is $\mathrm{SAT}(\Gamma)$ for the eight relations given by clauses of three literals.
The relation of the clause $x \lor y \lor z$ fails conditions 1, 3, 5 and 6, and the relation of $\neg x \lor \neg y \lor \neg z$ fails conditions 2 and 4.
So 3-SAT is NP-complete, in agreement with the Cook–Levin theorem.

## Explanations

### L1 human

Boolean constraint problems come in many forms, depending on which kinds of rules are allowed.
The theorem says that each such form is either easy or as hard as any problem in NP.
There are exactly six simple reasons for being easy, and if none applies, the problem is hard.

### L2 human

The theorem is the two-element case of the dichotomy for constraint satisfaction problems on finite domains.
That general dichotomy, conjectured by Feder and Vardi, was proved by Bulatov and by Zhuk in 2017.
By [[Ladner's theorem|3GT13ACR68]], NP contains intermediate problems if $\mathrm{P} \ne \mathrm{NP}$, so a dichotomy for a whole family is a strong structural fact.
The six tractable cases are described by closure under polymorphisms: constants, the binary minimum, the binary maximum, the majority operation, and the operation $x + y + z$ modulo $2$.
