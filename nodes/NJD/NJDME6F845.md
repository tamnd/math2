---
tag: NJDME6F845
kind: topic
name: Structures, satisfaction and truth
msc: ["03B10"]
topics: [DYJ0KGTPMR]
---

## Summary

This topic is a part of [[mathematical logic|DYJ0KGTPMR]], and it gives first-order formulas their meaning.
Take the sentence $\forall x \, \exists y \, (x < y)$, "every element has a larger one".
It is true in $(\mathbb{Z}, <)$ and in $(\mathbb{N}, <)$, and it is false in $(\{0, 1, 2\}, <)$, because nothing is larger than $2$.
The sentence $\exists x \, \forall y \, (x < y \vee x = y)$, "there is a least element", is true in $(\mathbb{N}, <)$ and false in $(\mathbb{Z}, <)$.
So the truth of a sentence depends on the structure in which we read it.

The story starts with structures: a nonempty domain, together with an interpretation of each symbol of the signature.
Tarski's clauses of 1933 then define when a structure satisfies a formula under an assignment of elements to the free variables, one connective and one quantifier at a time.
A sentence has no free variables, so it is simply true or false in a structure, and the true sentences form the theory of the structure.
A model of a set of axioms is a structure in which all the axioms are true, and a valid sentence is true in every structure.

A few lemmas make the definition usable.
Satisfaction depends only on the free variables, substitution of a term matches a change of the assignment, and isomorphic structures satisfy the same sentences.
The converse of the last fact fails: $(\mathbb{Q}, <)$ and $(\mathbb{R}, <)$ satisfy the same sentences, but they are not isomorphic, because one is countable and the other is not.

The topic ends with three other views of truth.
Herbrand structures are built from closed terms, games describe truth as a winning strategy for a verifier, and definable relations, such as the squares $\exists y \, (x = y \cdot y)$ in $(\mathbb{R}, +, \cdot)$, show what a structure can express.

## Remarks

### Reading order

1. [[Structure|983GZBQYT4]], to learn what a formula is read in: a domain with interpretations of the symbols of a signature.
2. [[Satisfaction|2RBQPV02AS]], to evaluate any formula by Tarski's recursive clauses for $\mathcal{M} \models \varphi[s]$.
3. [[Truth in a structure|K7XDVK5854]], to separate structures by sentences and to meet the theory $\operatorname{Th}(\mathcal{M})$ and elementary equivalence.
4. [[Model|MVCH6N9SNW]], to connect axioms with the structures in which they hold.
5. [[Validity|5SDS9T8E7J]], to recognize the sentences that are true in every structure.
6. [[Coincidence lemma|FM580NZ9W6]], to see why only the free variables and the symbols used matter.
7. [[Substitution lemma (semantic)|A7S460KHBM]], to trade a substitution of a term for a change of the assignment.
8. [[Isomorphism invariance of truth|NDTJ2E895C]], to know that isomorphic structures satisfy the same formulas.
9. [[Herbrand universe|NFW38QJ3A7]], to build a domain from the closed terms of a signature.
10. [[Herbrand structure|HKW429DSDK]], to find models of universal sentences among structures made of terms.
11. [[Game-theoretic semantics|D45Z7HETDA]], to read truth as a winning strategy for the verifier.
12. [[Definable relations|1DQ1M6ZWS4]], to define sets by formulas and to prove non-definability with automorphisms.
13. [[Drinker paradox|8BMQTZZEWB]], to test the definitions on a valid sentence that sounds false.

### Prerequisites

- [[First-order languages and syntax|PSRDJXRW53]]: signatures, terms, formulas, free variables and substitution.
- [[The propositional calculus|JDK63589SA]]: truth tables and tautologies, which the clauses for the connectives extend.
- [[Reasoning and proof|SGSVYFDSYK]]: proof by cases and proof by induction, used in the proofs of the lemmas.
