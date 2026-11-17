---
tag: MC18C7BMFT
kind: concept
name: Computer-assisted proof
aliases: [computer-aided-proof, computer-proof]
msc: ["00A35", "68V05"]
topics: [1BTHSHST4M]
audience: research
uses: [0B94TKFQJX, 0WCP0PVET6, JGRCNPKNGG]
sources:
  - url: https://en.wikipedia.org/wiki/Computer-assisted_proof
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Computer-assisted_proof
    locator: Methods
  - url: https://en.wikipedia.org/wiki/Computer-assisted_proof
    locator: Philosophical objections
  - url: https://en.wikipedia.org/wiki/Computer-assisted_proof
    locator: Theorems proved with the help of computer programs
---

## Summary

A computer-assisted proof is a [[mathematical proof|0B94TKFQJX]] in which a computer program carries out some of the steps, and these steps are too many or too long for a person to check by hand.
In the usual form, a human argument reduces the theorem to a finite list of claims, and the program checks each claim on the list.
The program can enumerate cases, solve a large system of logical constraints, or compute with numbers under strict control of the errors.
A computer-assisted proof is accepted when the readers trust three things: the reduction, the program and the machine that ran it.
The idea matters because several famous theorems, such as the [[four colour theorem|0M406JC8J1]] and the [[Kepler conjecture|AFMBQT06ZV]], have no known proof without a computer.

## Motivation

Some theorems reduce to a finite problem that is very large.
A [[proof by cases|0WCP0PVET6]] with a thousand cases is still a proof, but no person can write it out or read it.
The four colour theorem is the first famous case.
Its proof shows that a [[minimal counterexample|JGRCNPKNGG]] must contain one of a long list of configurations, and that no configuration on the list can occur in a minimal counterexample.
The second half of this argument needs a separate check for each configuration, and Appel and Haken gave these checks to a computer.

The use of a computer raises a question that a written proof does not raise.
A referee can read each line of a written proof.
A referee cannot read billions of steps of a computation, so the referee must trust a program and a machine.
The concept of a computer-assisted proof names this situation, and the methods of this page are the ways in which mathematicians gain that trust.

## Remarks

### Examples

- The [[four colour theorem|0M406JC8J1]]: a human argument reduces the theorem to a list of configurations, and a program checks that each configuration is reducible. The page on [[the computer-assisted proof of the four colour theorem|17BMQS5PTG]] describes how mathematicians came to accept it.
- The [[Kepler conjecture|AFMBQT06ZV]]: Thomas Hales reduced the problem to a finite set of configurations of balls and checked bounds on them by computer with [[linear programming|VNMXB0J2KA]]. The page on [[the proof of the Kepler conjecture and its formal verification|40QATE3WJN]] gives the history.
- The [[Boolean Pythagorean triples problem|417PHKB4VC]]: a SAT solver showed in 2016 that the numbers $1$ to $7825$ cannot be coloured with two colours without a one-coloured Pythagorean triple. The solver produced a proof file that an independent program checked.
- The [[Robbins conjecture|X74S395RZD]] in algebra: William McCune settled it in 1996 with the automated theorem prover EQP. Here the computer found a derivation, and the derivation is short enough for a person to check.
- The Lorenz attractor: Warwick Tucker proved in 2002 that the Lorenz equations have a strange attractor. His proof uses [[interval arithmetic|QPKKTE1ZY0]], which encloses each real number between two machine numbers, so that rounding errors cannot make a computed bound false.
- The fifth Schur number: Marijn Heule announced in 2017 a computer proof that the fifth Schur number is $160$. The proof file has a size of about $2$ petabytes. The Schur numbers come from [[Schur's theorem|V6XJQXZ7E8]].

### Non-examples

- A check of [[Goldbach's conjecture|063JNBSMJ0]] for all even numbers up to a bound is not a proof of the conjecture, as [[this non-example|VE6ACCC4F7]] explains. The condition that fails is the reduction: no human argument reduces the infinitely many cases to the checked ones.
- A floating-point computation of an integral to $15$ digits is not a proof that the integral has a given value. The condition that fails is the control of errors: rounding errors are not bounded, so the computed digits can be wrong.
- A short proof that a person writes in a proof assistant, such as [[this proof in Lean|QF0Q7B5Q73]], is usually not called computer-assisted. The computer checks each step, but a person could read every step. Such a proof is a formal proof in the sense of [[formal and informal proofs|8VZ77R4R8S]].

### Basic properties

- A computer check of finitely many cases proves a statement only about those cases. A statement about infinitely many objects needs a human argument, or a formal argument, that reduces it to the finite list.
- The trust in a computer-assisted proof is the trust in three parts. The reduction is a written proof, and referees check it in the usual way. The program can contain errors. The compiler, the operating system and the hardware can also fail.
- A computation can be repeated. Another group can write an independent program and run it on other machines. Agreement of independent programs reduces the chance that one error decides the result.
- Checking is often much easier than finding. A SAT solver that finds a colouring can print it, and a short program checks it. A solver that finds that no colouring exists can print a proof certificate, for example in the DRAT format, and a small checker verifies the certificate.
- Formal verification gives the strongest trust. When a proof assistant such as Coq, HOL Light, Isabelle or Lean checks the whole proof, including the computation, the reader must trust only the small kernel of the assistant and the statement of the theorem. The topic [[proof assistants and their design|YM6PRDE88V]] treats these systems.

### History

Kenneth Appel and Wolfgang Haken announced their proof of the four colour theorem in 1976, and it was the first major theorem whose proof needed a computer.
In 1979 the philosopher Thomas Tymoczko argued that such a proof cannot be surveyed by a person, and the page [[long proofs and surveyability|RM0S65BHWH]] treats his argument.
Thomas Hales announced a proof of the Kepler conjecture in 1998, and the referees could not certify all of the computer calculations.
Georges Gonthier and Benjamin Werner checked a proof of the four colour theorem in the Coq proof assistant in 2005, and the Flyspeck project completed a formal proof of the Kepler conjecture in 2014.
SAT solvers produced the proof of the Boolean Pythagorean triples problem in 2016, with a proof file of about $200$ terabytes.

### Common errors

- To treat a computer-assisted proof as numerical evidence. A computer-assisted proof checks every case of a proved reduction, while numerical evidence checks some cases of an unproved claim. The topic [[plausible reasoning and experimental mathematics|DME0TPC348]] treats evidence.
- To think that a computer-assisted proof cannot be checked at all. It can be checked: the reduction by reading, and the computation by independent programs, certificates and proof assistants.
- To think that a formal verification removes all doubt. The proof assistant checks the formal statement, and a person must still check that the formal statement says what the theorem says.

## Explanations

### L1 human

Some theorems come down to a very long list of cases.
Each case is easy, but there are too many cases for a person to check in a lifetime.
In a computer-assisted proof, mathematicians first prove that the list contains every possible case.
Then a program checks each case on the list.
For example, the four colour theorem says that four colours are enough to colour any map so that neighbouring countries get different colours.
Its proof reduces all maps to more than a thousand special patterns, and a computer checks each pattern.
People accepted the proof only after other people checked the program and repeated the computation.

### L2 human

We prove by an exhaustive check that each colouring of the edges of the complete graph $K_6$ with two colours has a triangle with all three edges of one colour.

1. The graph $K_6$ has $6$ vertices and $\binom{6}{2} = 15$ edges.
2. Each edge gets one of two colours, so there are $2^{15} = 32768$ colourings.
3. The graph has $\binom{6}{3} = 20$ triangles.
4. A program takes each colouring and tests each of the $20$ triangles. This is $32768 \cdot 20 = 655360$ tests.
5. The program reports that each colouring has at least one triangle of one colour. This finite check is the whole proof, because step 2 lists every colouring.
6. The bound is sharp: on $K_5$, colour the $5$ edges of a pentagon red and the $5$ diagonals blue. The red edges form a $5$-cycle and the blue edges form a $5$-cycle, so no triangle has one colour.

A person can also prove step 5 by hand.
A vertex $v$ has $5$ edges, so by the [[pigeonhole principle|0HGVCWQGY3]] $3$ of them have one colour, say red, and go to vertices $a$, $b$ and $c$.
If one of the edges $ab$, $bc$, $ca$ is red, it forms a red triangle with $v$.
If none of them is red, then $a$, $b$ and $c$ form a blue triangle.
The computer proof and the human proof prove the same statement, but only the human proof explains why it is true.
The typical use of the method is a statement that reduces to a finite but very large set of cases, where no short human argument is known.
A trap is a program that misses some cases, for example by a wrong loop bound.
Then the program reports success, but the proof is not complete, and only a check of the program can find the error.

### L3 human

A computer-assisted proof is a proof in which the verification of some steps is delegated, and the general question is how much of the verification can be delegated without loss of trust.
Complexity theory gives one answer: for problems in NP, a solution is a short certificate that a fast program checks, while a proof that no solution exists can be very long.
The SAT community answers this with proof formats such as DRAT, which a small checker can verify, and the checker itself can be verified in a proof assistant.
Proof assistants give a second answer: a proof that is checked by a small kernel needs trust only in that kernel.
In this way the formal proofs of the four colour theorem and the Kepler conjecture removed most of the doubt.

The questions of this page connect to the acceptance of very long human proofs, treated in [[long proofs and surveyability|RM0S65BHWH]], and to the social side of acceptance, treated in [[acceptance of proofs|MJ3EHQJJHX]].
The tools themselves belong to the topics [[computer-assisted proof and verification|54HCSZ6NBT]], [[SAT and SMT solving|3BW08M1EX7]] and [[automated theorem proving|A51M1KK9DJ]].
The use of computers to find conjectures, as opposed to proving them, belongs to [[plausible reasoning and experimental mathematics|DME0TPC348]].
