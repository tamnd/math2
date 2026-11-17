---
tag: 79P9CTRN0V
kind: concept
name: Proofs and refutations
msc: ["00A35"]
topics: [X1NSTVGDNQ]
audience: research
specializes: [6KCEWEP4WA]
uses: [WMEMMHZ3BH, 0B94TKFQJX, 0ED72CTBNP, 09HT3P35YP]
sources:
  - url: https://en.wikipedia.org/wiki/Proofs_and_Refutations
    locator: Method
  - url: https://en.wikipedia.org/wiki/Imre_Lakatos
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Euler_characteristic
    locator: Polyhedra
---

## Summary

The method of proofs and refutations is Imre Lakatos's description of how a mathematical theorem and its concepts grow together.
It starts with a [[conjecture|WMEMMHZ3BH]] and a [[proof|0B94TKFQJX]] of it, read as a thought experiment that splits the conjecture into lemmas.
[[Counterexamples|0ED72CTBNP]] then appear: a global counterexample refutes the conjecture, and a local counterexample refutes a lemma of the proof.
Proof analysis finds the lemma that a global counterexample refutes, and the lemma is added to the conjecture as a hypothesis; the new hypothesis often defines a new concept.
The method matters because it explains why theorems have the hypotheses they have, and why many definitions were made only after a proof failed.
It is a [[heuristic|6KCEWEP4WA]] for research and for reading: it does not tell when the process ends, and it does not replace a correct final proof.

## Motivation

A finished theorem states its hypotheses as if they were obvious from the start.
The history of a theorem often shows a different order: a general claim, a proof, an object for which the claim fails, and then a repair.
[[Euler's polyhedron formula|09HT3P35YP]] $V - E + F = 2$ is the standard case.
Euler stated it for polyhedra in general, Cauchy gave a proof, and later authors found solids for which $V - E + F$ is $0$, $4$ or $-6$.
Each failure raised the question of what a polyhedron is, and the answers led to the hypothesis "the surface is a topological sphere" and to the [[Euler characteristic|RNDDWDAFJ5]] of a surface.
Lakatos turned this history into a general pattern of discovery, and the pattern applies to many other theorems.

## Notation

Lakatos's terms, used on this site with his meanings:

- A *global counterexample* is an object that refutes the conjecture itself.
- A *local counterexample* is an object that refutes a lemma of the proof; it may or may not refute the conjecture.
- *Monster-barring* rejects a global counterexample by a new definition that excludes it ("this is not a polyhedron").
- *Exception-barring* restricts the conjecture to a safe domain that excludes the known counterexamples, such as convex polyhedra, without analyzing the proof.
- *Monster-adjustment* reinterprets a counterexample so that it is no longer one, for example by counting the faces of a star polyhedron in a different way.
- *Lemma-incorporation* finds the lemma of the proof that the counterexample refutes, and adds it to the conjecture as a hypothesis.
- A *proof-generated concept* is a concept that arises as the content of an incorporated lemma.

## Remarks

### The steps

Lakatos describes the method in stages.

1. State a primitive conjecture.
2. Give a proof: a rough thought experiment that splits the conjecture into lemmas.
3. Look for counterexamples, both to the conjecture (global) and to the lemmas (local).
4. Analyze the proof against each global counterexample: find the "guilty" lemma, the one that the counterexample refutes.
5. Incorporate the guilty lemma into the conjecture as a hypothesis. This gives an improved conjecture, often with a new concept.
6. Test the improved conjecture and the improved proof again, and look at other proofs that use the same concept.

### When it applies

- A proof is known, but a counterexample to the statement has appeared: the method asks which step the counterexample breaks.
- A theorem has a hypothesis whose role is unclear: the method asks which step of the proof needs it.
- A definition seems arbitrary: the method asks which proof produced it.
- The method applies best to young areas where concepts are not yet fixed, and least to areas with settled axioms.

### Examples

1. [[Counterexamples to Euler's polyhedron formula and the responses to them|C1X8DP1SNE]]: the hollow cube and the picture frame, Cauchy's proof, and the hypothesis that each step of the proof needs.
2. [[Cauchy's sum theorem and the hidden lemma of uniform convergence|NDYRDNFXRR]]: the claim that a convergent series of continuous functions has a continuous sum, its counterexample, and the concept that the analysis of its proof produced.
3. The definition of a [[prime number|01826KMG2H]] excludes $1$ so that factorization into primes is unique; the theorem shaped the definition.
4. In Lakatos's account, the dialogue on Euler's formula also treats a local counterexample: when the triangles of a flattened polyhedron are removed in a bad order, a step of Cauchy's proof fails, but the formula holds, and the proof is repaired by an order of removal.

### Non-examples

1. [[Defining a polyhedron as a solid with V − E + F = 2|T8TXB0PMJN]]: monster-barring pushed to its end makes the theorem true by definition and empty.
2. Checking a conjecture on more and more cases. Testing $V - E + F = 2$ on the five [[Platonic solids|017E5PRS1Q]] gives evidence, but it involves no proof and no analysis, so it is not the method.
3. A proof of a settled theorem in an axiomatic theory, such as a proof in group theory from the group axioms. No concept changes, and the method has nothing to act on.

### Basic properties

1. A global counterexample that is not local refutes the conjecture but not the proof: some lemma that the proof uses without stating it is false for the object. Finding this hidden lemma is proof analysis.
2. A local counterexample that is not global refutes the proof but not the conjecture: the proof needs repair, and the statement can stay.
3. Lemma-incorporation always gives a true statement when the analysis is complete: the conjecture is restricted to the objects for which each lemma of the proof holds.
4. The improved theorem has a smaller domain but more content: it says exactly what the proof proves.
5. The process can repeat. Each new hypothesis can meet new counterexamples, and the concepts get sharper each time.

### Related methods

- [[Counterexample|0ED72CTBNP]] and [[conjecture|WMEMMHZ3BH]]: the two basic moves of the method.
- [[Choosing good definitions|S1R1VD31BS]]: how definitions change under counterexamples, with more examples of proof-generated concepts.
- [[Methodology of mathematics|3FJ3XMV9KD]]: the general study of how mathematics is done, where Lakatos's method is one of several descriptions.
- [[Variation of the problem|KT5SASGTQ5]]: dropping or adding a condition is the move of exception-barring and of lemma-incorporation.
- [[Hypotheses and conclusion of a theorem|W48XN2MEM9]]: the method explains where each hypothesis comes from.

### History

Imre Lakatos (1922 to 1974) developed the method in his doctoral thesis of 1961, Essays in the Logic of Mathematical Discovery.
A version of its first chapter appeared as "Proofs and Refutations" in four parts in the British Journal for the Philosophy of Science in 1963 and 1964.
The book Proofs and Refutations, edited by John Worrall and Elie Zahar, appeared in 1976, after his death; it is based on the first three chapters of the thesis.
The book is a dialogue in a classroom, with pupils named after Greek letters, about proofs of Euler's polyhedron formula; footnotes give the real history.
An appendix applies the method to Cauchy's theorem on the continuity of the sum of a series and to uniform convergence.
Lakatos had translated Pólya's How to Solve It into Hungarian, and his philosophy of mathematics drew on Pólya's work on heuristics and on Karl Popper's theory of knowledge.

### Common errors

1. Treating every counterexample as a defeat of the theorem. A global counterexample often shows a missing hypothesis, and the repaired theorem is stronger in content.
2. Treating monster-barring as always wrong. Some exclusions are good definitions, such as excluding $1$ from the primes; the question is whether the exclusion is explained by a proof.
3. Reading the method as a claim that mathematics has no certain results. Lakatos describes how theorems are found and improved; the final theorem with its full hypotheses is proved in the usual sense.

## Explanations

### L1 human

A mathematician guesses a rule and writes an argument for it.
Then someone finds an object that breaks the rule.
Instead of throwing the rule away, we look at the argument and find the step where the object causes trouble.
That step tells us what extra condition the rule needs.
For example, "corners minus edges plus faces is $2$" holds for a cube, but fails for a picture frame with a hole, where the count is $0$.
The step that fails is the flattening of the surface, which needs a solid without holes.
So the corrected rule is: for solids without holes, the count is $2$.

### L2 human

We apply the method to the claim that a function with a positive derivative is increasing.

1. Conjecture: if $f$ is differentiable on a set $D$ with $f'(x) > 0$ for each $x \in D$, then $x < y$ in $D$ implies $f(x) < f(y)$.
2. Proof: for $x < y$, the [[mean value theorem|0BARQY52N5]] gives $c$ between $x$ and $y$ with $f(y) - f(x) = f'(c)(y - x) > 0$.
3. Global counterexample: $f(x) = -\frac{1}{x}$ on $D = \mathbb{R} \setminus \{0\}$. Here $f'(x) = \frac{1}{x^2} > 0$, but $f(-1) = 1 > -1 = f(1)$.
4. Proof analysis: the mean value theorem needs $f$ to be differentiable on the whole interval $[x, y]$. For $x = -1$, $y = 1$ the interval contains $0 \notin D$. This is the guilty lemma: "$[x, y] \subseteq D$".
5. Lemma-incorporation: the improved theorem asks that $D$ be an interval. The concept that the proof generates is "interval", that is, a connected subset of $\mathbb{R}$.

The typical use: the counterexample tells which hidden assumption of the proof must become a hypothesis.

A trap: exception-barring would restrict the claim to $D = \mathbb{R}$ and lose the cases $D = (0, 1)$ or $D = [2, 5]$, where the claim is still true.

### L3 human

Lakatos's account belongs to the philosophy of mathematical practice: it treats mathematics as a growing body of conjectures and proofs, in analogy with Karl Popper's account of conjectures and refutations in the natural sciences.
Its main claim for working mathematicians is that hypotheses and definitions are often proof-generated: connectedness in the mean value example, simple connectivity and the Euler characteristic in the polyhedron example, uniform convergence in the series example.
The same pattern appears in modern research, where a counterexample often leads to a new invariant, and in formal proof, where a proof assistant forces each hidden lemma of a proof to be stated.
The topics [[rigour and the acceptance of proofs|1BTHSHST4M]] and [[plausible reasoning and experimental mathematics|DME0TPC348]] continue these themes, and [[mathematical intuition|4BT08RE4CR]] discusses why the first conjecture is often too general.
