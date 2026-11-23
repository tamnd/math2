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

Proofs and refutations is Imre Lakatos's account of how a theorem and its concepts grow together.
A conjecture gets a proof, a counterexample breaks the conjecture, and the analysis of the proof shows which hidden assumption failed, so that the assumption becomes a new hypothesis and often a new concept.

Lakatos's own case is [[Euler's polyhedron formula|09HT3P35YP]].
Count the vertices, edges and faces of a cube, a tetrahedron and an octahedron:
$$8 - 12 + 6 = 2, \qquad 4 - 6 + 4 = 2, \qquad 6 - 12 + 8 = 2.$$
The first conjecture is that $V - E + F = 2$ for every polyhedron.
Cauchy's proof removes one face, stretches the rest of the surface flat on a plane, and counts on the flat network.
Then a counterexample appears: a picture frame, a square ring built from $16$ four-sided faces, has
$$V - E + F = 16 - 32 + 16 = 0.$$
One response is to say that the frame is not a real polyhedron, and another is to keep the formula only for convex solids.
Lakatos's response is to ask which step of the proof the frame breaks.
The answer is the first step: a ring-shaped surface with one face removed cannot be stretched flat.
So that step becomes a hypothesis, and the improved theorem says that $V - E + F = 2$ when the surface, with one face removed, can be stretched flat, that is, when the surface is a topological sphere.

In the method, a [[conjecture|WMEMMHZ3BH]] gets a [[proof|0B94TKFQJX]], read as a thought experiment that splits the conjecture into lemmas.
[[Counterexamples|0ED72CTBNP]] then refute the conjecture or a lemma, and the guilty lemma is added to the conjecture as a hypothesis.
Like every [[heuristic|6KCEWEP4WA]], the method gives no guarantee: it does not say when the process ends, and the final theorem still needs a correct proof.

## Motivation

A finished theorem states its hypotheses as if they had been clear from the start.
The history of a theorem often shows another order: a general claim, a proof, an object for which the claim fails, and then a repair.
Euler stated his formula for polyhedra in general, Cauchy gave a proof, and later authors found solids with $V - E + F$ equal to $0$, $4$ or $-6$.
Each failure raised the question of what a polyhedron is, and the answers led to the hypothesis "the surface is a topological sphere" and to the [[Euler characteristic|RNDDWDAFJ5]] of a surface.

The method helps in three situations.
When a counterexample to a proved statement appears, it asks which step the counterexample breaks.
When a hypothesis of a theorem seems arbitrary, it asks which step of the proof needs it.
When a definition seems arbitrary, it asks which proof produced it.
It works best in young areas where the concepts are not yet fixed, and least in areas with settled axioms.

## Notation

Lakatos named the responses to a counterexample, and books on his work keep his terms.
A *global counterexample* refutes the conjecture itself, and a *local counterexample* refutes a lemma of the proof.
*Monster-barring* rejects a global counterexample by a new definition that excludes it, as in "the frame is not a polyhedron".
*Exception-barring* restricts the conjecture to a safe domain, such as convex polyhedra, without looking at the proof.
*Monster-adjustment* reads the counterexample in a new way, so that it no longer refutes the conjecture.
*Lemma-incorporation* finds the lemma that the counterexample refutes and adds it to the conjecture as a hypothesis.
A *proof-generated concept* is a concept that arises as the content of such an incorporated lemma.

## Remarks

### The stages of the method

Lakatos describes the method in stages.
You state a primitive conjecture and give a rough proof that splits it into lemmas.
Then you look for counterexamples, both global and local.
For each global counterexample you find the guilty lemma, the one that the counterexample refutes, and you add it to the conjecture as a hypothesis.
The improved conjecture has a smaller domain and more content, because it says exactly what the proof proves.
Then you test the improved conjecture again, since a new hypothesis can meet new counterexamples.

The two kinds of counterexample do different jobs.
A global counterexample that is not local refutes the conjecture but no stated lemma, so the proof must use some lemma that it never stated; finding that hidden lemma is proof analysis.
A local counterexample that is not global refutes a step of the proof but not the conjecture, so the proof needs repair and the statement can stay.

### Euler's formula in full

[[Counterexamples to Euler's polyhedron formula|C1X8DP1SNE]] works through the whole story.
A hollow cube, a cube with a cube-shaped cavity, has two separate surfaces and gives
$$V - E + F = 16 - 24 + 12 = 4.$$
The picture frame gives $0$, and Kepler's small stellated dodecahedron, with its $12$ star faces, gives $12 - 30 + 12 = -6$.
Proof analysis explains each value.
Each sphere-like surface contributes $2$, and a connected surface with $g$ tunnels has $V - E + F = 2 - 2g$, so the frame, with one tunnel, gives $0$.

### Cauchy's sum theorem

In 1821 Cauchy stated that a convergent series of continuous functions has a continuous sum.
The series with terms $x(1 - x)^n$ on $[0, 1]$ is a global counterexample, since its sum is $0$ at $x = 0$ and $1$ for $0 < x \le 1$.
The guilty lemma is hidden in the proof: it assumes that one index $N$ makes the error small for all $x$ near a point at once.
Incorporating that lemma gives the hypothesis of [[uniform convergence|08VZ57PT26]].
[[Cauchy's sum theorem and the hidden lemma of uniform convergence|NDYRDNFXRR]] gives the details.

### When the method misleads

Monster-barring can go too far.
If each new solid is barred by a new clause, the defender can end with the definition "a polyhedron is a solid with $V - E + F = 2$".
Then the theorem is true by definition and says nothing, as [[defining a polyhedron as a solid with V − E + F = 2|T8TXB0PMJN]] shows.
The test of a new hypothesis is whether you can check it without computing the conclusion.

Exception-barring loses content in another way.
Restricting Euler's formula to convex solids makes it true, but it gives up nonconvex solids, such as an L-shaped block, for which the formula still holds.
Checking more and more cases is not the method either: the five [[Platonic solids|017E5PRS1Q]] all give $2$, and that evidence involves no proof and no analysis.

### Watch out

Do not treat every counterexample as a defeat.
A global counterexample often shows a missing hypothesis, and the repaired theorem says more, not less.

Do not treat every exclusion as monster-barring either.
The definition of a [[prime number|01826KMG2H]] excludes $1$ so that factorization into primes is unique, and that exclusion is good because a theorem explains it.

Finally, the method does not claim that mathematics has no certain results.
It describes how theorems are found and improved, and the final theorem with its full hypotheses is proved in the usual sense.

### History

Imre Lakatos (1922 to 1974) developed the method in his doctoral thesis of 1961, *Essays in the Logic of Mathematical Discovery*.
A version of its first chapter appeared as "Proofs and Refutations" in four parts in the *British Journal for the Philosophy of Science* in 1963 and 1964.
The book *Proofs and Refutations*, edited by John Worrall and Elie Zahar, appeared in 1976, after his death.
It is a dialogue in a classroom, with pupils named after Greek letters, about proofs of Euler's formula, and its footnotes give the real history.
An appendix applies the method to Cauchy's sum theorem and uniform convergence.
Lakatos translated Pólya's *How to Solve It* into Hungarian, and his account drew on Pólya's heuristics and on Karl Popper's philosophy of science.

### Try it

A square pyramid has a square base and four triangular sides; does it satisfy Euler's formula?
It has $5$ vertices, $8$ edges and $5$ faces, and $5 - 8 + 5 = 2$, so it does.

Two cubes that share one edge form a solid; is it a counterexample, and to which lemma?
It has $V = 14$, $E = 23$ and $F = 12$, so $V - E + F = 3$, and the first lemma fails, because after you remove a face of one cube, the surface of the other cube is still closed and cannot be laid flat.

## Explanations

### L1 human

A mathematician guesses a rule and writes an argument for it.
Then someone finds an object that breaks the rule.
Instead of throwing the rule away, we look at the argument and find the step where the object causes trouble.
That step tells us which condition the rule needs.
For example, "corners minus edges plus faces is $2$" holds for a box, but a picture frame with a hole gives $0$.
The step that fails flattens the surface, which needs a solid without holes.
So the corrected rule is that the count is $2$ for solids without holes.

### L2 human

Let us apply the method to the claim that a function with positive derivative is increasing.
The conjecture says that if $f$ is differentiable on a set $D$ with $f'(x) > 0$ for each $x \in D$, then $x < y$ in $D$ implies $f(x) < f(y)$.
The proof uses the [[mean value theorem|0BARQY52N5]], which gives a point $c$ between $x$ and $y$ with
$$f(y) - f(x) = f'(c)(y - x) > 0.$$
Now a global counterexample appears: $f(x) = -1/x$ on $D = \mathbb{R} \setminus \{0\}$.
Here $f'(x) = 1/x^2 > 0$, but $f(-1) = 1 > -1 = f(1)$.
Which step fails?
The mean value theorem needs $f$ to be differentiable on the whole interval $[x, y]$, and $[-1, 1]$ contains $0$, which is not in $D$.
So the guilty lemma is "$[x, y] \subseteq D$", and the improved theorem asks that $D$ be an interval.
The proof produced the concept of an interval, a connected subset of $\mathbb{R}$.
Exception-barring would have kept only $D = \mathbb{R}$ and lost the true cases $D = (0, 1)$ and $D = [2, 5]$.

### L3 human

Lakatos's account belongs to the philosophy of mathematical practice: it treats mathematics as a growing body of conjectures and proofs, in analogy with Popper's account of conjectures and refutations in the natural sciences.
Its main claim for working mathematicians is that many hypotheses and definitions are proof-generated, such as connectedness in the derivative example, the topological sphere and the Euler characteristic for polyhedra, and uniform convergence for series.
The same pattern shows in modern research, where a counterexample often leads to a new invariant, and in formal proof, where a proof assistant forces every hidden lemma to be stated.
[[Choosing good definitions|S1R1VD31BS]] collects more proof-generated concepts, and [[hypotheses and conclusion of a theorem|W48XN2MEM9]] asks what each hypothesis is for.
[[Rigor and the acceptance of proofs|1BTHSHST4M]] and [[plausible reasoning and experimental mathematics|DME0TPC348]] continue these themes, and [[mathematical intuition|4BT08RE4CR]] discusses why the first conjecture is often too general.
