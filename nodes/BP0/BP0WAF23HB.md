---
tag: BP0WAF23HB
kind: topic
name: Definitions in mathematics
msc: ["00A35"]
topics: [SGSVYFDSYK]
---

## Summary

Every proof in mathematics rests on definitions, and this part of [[reasoning and proof|SGSVYFDSYK]] asks how a definition works and what it must satisfy before we may use it.
It starts from definitions you already know, such as the prime numbers and the even integers, and reads them closely: what the new word is, what condition gives its meaning, and why the "if" of a definition means "if and only if".
It then shows that many definitions hide a claim.
A definition through representatives, such as addition of residues or of fractions, must be shown well defined.
A definition with "the", such as the greatest common divisor, needs existence and uniqueness first, and a phrase such as "unique up to isomorphism" must name its equivalence relation.
Next come the definitions that are not explicit at all: recursions, classes, axioms and universal properties, and at the bottom the primitive notions that are never defined.
Along the way, one notion turns out to have several equivalent definitions, and the last page asks why we choose the ones we do, for example why $1$ is not a prime.

## Remarks

### Reading order

1. [[Mathematical definition|8ZCZ3HW91Z]]: how to read a definition, why its "if" means "if and only if", and how proofs unfold and fold definitions.
2. [[Kinds of definitions|B60DBNF77S]]: explicit, recursive, inductive, by abstraction, axiomatic, implicit and by universal property, with the proof that each kind owes.
3. [[Well-defined|HNGZEBKVY2]]: how to tell a rule on fractions or residues that works from one that fails, and the test that `Quotient.lift` asks for in Lean.
4. [[Equivalent definitions|NZ42PS2P1A]]: how to prove that two definitions of primes, continuity or compactness agree, and why they can stop agreeing in a larger setting.
5. [[Definite descriptions in definitions|5P955TVSS2]]: why "the identity element" or "the greatest common divisor" needs a proof of existence and uniqueness first.
6. [[Up to|CBC72TX3NQ]]: what "unique up to order", "up to a constant" and "up to isomorphism" mean, each with its equivalence relation.
7. [[Primitive notion|QMQEJKFEYZ]]: why definitions must stop somewhere, and how axioms fix the meaning of point, line, set and membership.
8. [[Choosing good definitions|S1R1VD31BS]]: why $1$ is not prime, why books disagree about $0$, and how theorems shape the definitions we keep.

### Prerequisites

1. [[The language of mathematical statements|WMY13MXY3W]]: quantifiers, connectives and the biconditional, which every definition uses.
2. [[Mathematical proof|0B94TKFQJX]]: what a proof is, because each hidden claim of a definition needs one.
3. [[Proof methods|G9JFJGY4TQ]]: direct proof, contradiction and contrapositive, which the uniqueness and well-definedness proofs use.
