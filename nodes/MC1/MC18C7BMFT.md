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

Some theorems come down to a finite problem far too large for any person, and a computer-assisted proof lets a program do that part.
The price is a new question of trust: a referee can read every line of a written proof, but not billions of steps of a computation.

Here is a problem that you can state in one line.
Color each of the numbers $1, 2, \dots, n$ red or blue.
Can you do it so that no [[Pythagorean triple|0M7ARED5Q7]] $a^2 + b^2 = c^2$ has all three numbers in one color?
In 2016 Marijn Heule, Oliver Kullmann and Victor Marek showed that the answer is yes for $n = 7824$ and no for $n = 7825$.
The "yes" is a coloring that a short program checks in a moment.
The "no" had to rule out every one of the $2^{7825}$ colorings, and the solvers wrote a record of about $200$ terabytes, which an independent checking program verified, as [[the Boolean Pythagorean triples problem|417PHKB4VC]] describes.

A computer-assisted proof is a [[mathematical proof|0B94TKFQJX]] in which a program carries out some steps, and these steps are too many or too long for a person to check by hand.
In the usual form, a written argument reduces the theorem to a finite list of claims, and the program checks each claim on the list.
The program may enumerate cases, solve a large logical problem, or compute with numbers under strict control of the errors.

## Motivation

A [[proof by cases|0WCP0PVET6]] with a thousand cases is still a proof, but nobody can write it out or read it.
The [[four color theorem|0M406JC8J1]] was the first famous case.
Its proof shows that a [[minimal counterexample|JGRCNPKNGG]] must contain one of a long list of configurations, and that none of them can occur in a minimal counterexample.
The second half needs a separate check for each configuration, and Kenneth Appel and Wolfgang Haken gave those checks to a computer in 1976.

Several famous theorems, among them the four color theorem and the [[Kepler conjecture|AFMBQT06ZV]], have no known proof without a computer.
So mathematicians had to decide when to trust such a proof.
The methods below are their answers: independent programs, certificates that a small checker verifies, and formal proofs in a proof assistant.

## Notation

The words "computer-assisted proof" and "computer-aided proof" mean the same thing.
A proof found by a program, such as an automated theorem prover, is a different case from a proof checked by a program, and authors often say which they mean.
A "certificate" is the output of a program that another, simpler program can verify, and DRAT is a common format of certificates for SAT solvers.

## Remarks

### Three famous cases

The four color theorem came first.
A written argument reduces the theorem to a list of more than a thousand configurations, and a program checks that each one is reducible.
[[The proof of the four color theorem|17BMQS5PTG]] follows how mathematicians came to accept it, from 1976 to Georges Gonthier's formal check in Coq in 2005.

Thomas Hales announced a proof of the Kepler conjecture in 1998.
He reduced the problem to a finite set of configurations of balls and checked bounds on them by computer with [[linear programming|VNMXB0J2KA]].
The *Annals of Mathematics* published the written part in 2005, and the Flyspeck project completed a formal proof in 2014, which appeared in 2017, as [[the Kepler example|40QATE3WJN]] tells.

The Boolean Pythagorean triples problem of 2016 is the third.
Its written reduction is half a page and its computation is enormous, so it is the extreme form of the idea.

### Other kinds of computer help

A program can also find a proof that a person then reads.
William McCune's prover EQP settled the [[Robbins conjecture|X74S395RZD]] in 1996, and the derivation it found is short enough for a person to check.

A program can compute with real numbers if it controls the rounding.
Warwick Tucker proved in 2002 that the Lorenz equations have a strange attractor, using [[interval arithmetic|QPKKTE1ZY0]], which encloses each real number between two machine numbers, so that rounding cannot make a computed bound false.

Heule announced in 2017 a computer proof that the fifth Schur number is $160$, with a proof file of about $2$ petabytes; the Schur numbers come from [[Schur's theorem|V6XJQXZ7E8]].

### What does not count

A check of [[Goldbach's conjecture|063JNBSMJ0]] for all even numbers up to $4 \cdot 10^{18}$ is not a proof of the conjecture, as [[the Goldbach check|VE6ACCC4F7]] explains.
The reduction fails: no written argument takes the infinitely many even numbers down to the checked range.

A floating-point computation of an integral to $15$ digits is not a proof of its value either.
The control of errors fails, because nothing bounds the rounding errors, so the computed digits can be wrong.

A short proof typed into a proof assistant, such as [[the Lean example|QF0Q7B5Q73]], is usually not called computer-assisted.
The computer checks each step, but a person could read every step, so it is a formal proof in the sense of [[formal and informal proofs|8VZ77R4R8S]].

### Where the trust comes from

Trust in a computer-assisted proof rests on three parts.
The reduction is a written proof, and referees check it in the usual way.
The program can contain errors, and so can the compiler, the operating system and the hardware.

Mathematicians reduce the second risk in three ways.
Another group writes an independent program and runs it on other machines, and agreement makes it unlikely that one error decides the result.
A solver prints a certificate, and a small checker, much simpler than the solver, verifies it.
Or a proof assistant such as Coq, HOL Light, Isabelle or Lean checks the whole proof, computation included, and then the reader must trust only the small kernel of the assistant and the formal statement.
[[Proof assistants and their design|YM6PRDE88V]] treats these systems.

### A check you can run by hand

Every coloring of the edges of the complete graph $K_6$ with two colors has a triangle in one color.
An exhaustive check is easy to set up.
The graph has $\binom{6}{2} = 15$ edges and $\binom{6}{3} = 20$ triangles, so the program tests
$$2^{15} \cdot 20 = 32768 \cdot 20 = 655360$$
pairs of a coloring and a triangle, and it finds a one-colored triangle in every coloring.
Since the $2^{15}$ colorings are all the colorings, the finite check is a complete proof.

A person can also prove it.
A vertex $v$ has $5$ edges, so by the [[pigeonhole principle|0HGVCWQGY3]] $3$ of them, say to $a$, $b$ and $c$, have one color, say red.
If one of $ab$, $bc$, $ca$ is red, it makes a red triangle with $v$, and if none is red, then $abc$ is a blue triangle.
Both proofs establish the same statement, and only the second says why it is true.

### Watch out

A computer-assisted proof is not numerical evidence.
It checks every case of a proved reduction, while evidence checks some cases of an unproved claim, as in [[plausible reasoning and experimental mathematics|DME0TPC348]].

The computer is not the only place where errors hide.
In 1981 Ulrich Schmidt found an error in the written discharging argument of the four color proof, not in the program.

A formal verification does not remove all doubt.
The proof assistant checks the formal statement, and a person must still check that the formal statement says what the theorem says.

### History

Appel and Haken announced their proof of the four color theorem in 1976, the first major theorem whose proof needed a computer.
In 1979 the philosopher Thomas Tymoczko argued that such a proof cannot be surveyed by a person, and [[long proofs and surveyability|RM0S65BHWH]] treats his argument.
Hales announced his proof of the Kepler conjecture in 1998, and the referees could not certify all of its computations.
Gonthier, with Benjamin Werner, checked a proof of the four color theorem in Coq in 2005, and Flyspeck completed a formal proof of the Kepler conjecture in 2014.
SAT solvers settled the Boolean Pythagorean triples problem in 2016.

### Try it

First, on $K_5$, color the $5$ edges of a pentagon red and the $5$ diagonals blue.
Is there a triangle in one color?
No: the red edges form a $5$-cycle and so do the blue edges, and a $5$-cycle contains no triangle, so $6$ is the smallest size that forces one.

Second, a program checks that a polynomial has no root in $[0, 1]$ by evaluating it at $10^6$ equally spaced points in floating point.
Is that a computer-assisted proof?
No: the points miss the values in between and the rounding is not controlled, so nothing is proved; interval arithmetic on small subintervals could give a proof.

## Explanations

### L1 human

Some theorems come down to a very long list of cases.
Each case is easy, but there are too many for a person to check in a lifetime.
In a computer-assisted proof, mathematicians first prove that the list contains every possible case.
Then a program checks each case on the list.
For example, the four color theorem says that four colors are enough to color any map so that neighboring countries get different colors.
Its proof reduces all maps to more than a thousand special patterns, and a computer checks each pattern.
People accepted the proof only after others checked the program and repeated the computation.

### L2 human

We test a solver's claim the way a referee would, on a small case of the Pythagorean coloring problem.
For $n = 13$ the only triples are $(3, 4, 5)$, $(6, 8, 10)$ and $(5, 12, 13)$.
Suppose a solver outputs the coloring "$5$ and $10$ blue, everything else red".
We check each triple:
$$\{3, 4, 5\} \ni 5 \text{ blue}, \qquad \{6, 8, 10\} \ni 10 \text{ blue}, \qquad \{5, 12, 13\} \ni 5 \text{ blue},$$
and each triple also has a red number, so no triple has one color.
The check took three lines and did not require us to trust the solver at all.
That is the typical use of a certificate: the hard search is done once, and the easy check can be repeated by anyone.
Watch out for the other direction: when a solver answers "no coloring exists", there is nothing this short to check, and only a certificate such as a DRAT proof, verified by an independent checker, turns the answer into a proof.

### L3 human

A computer-assisted proof hands part of the verification to a machine, and the general question is how much can be handed over without loss of trust.
Complexity theory frames one answer: for problems in NP a solution is a short certificate that a fast program checks, while a proof that no solution exists can be very long.
The SAT community answers with proof formats such as DRAT, which a small checker verifies, and that checker can itself be verified in a proof assistant.
Proof assistants give a second answer: a proof checked by a small kernel needs trust only in that kernel, and the formal proofs of the four color theorem and the Kepler conjecture removed most of the doubt in this way.

These questions connect with the acceptance of very long human proofs in [[long proofs and surveyability|RM0S65BHWH]] and with the social side of acceptance in [[acceptance of proofs|MJ3EHQJJHX]].
The tools belong to [[computer-assisted proof and verification|54HCSZ6NBT]], [[SAT and SMT solving|3BW08M1EX7]] and [[automated theorem proving|A51M1KK9DJ]].
