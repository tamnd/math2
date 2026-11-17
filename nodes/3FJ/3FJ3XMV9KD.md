---
tag: 3FJ3XMV9KD
kind: concept
name: Methodology of mathematics
aliases: [mathematical-method, mathematical-practice]
msc: ["00A35"]
topics: [N4P3E53HM0]
audience: research
uses: [0B94TKFQJX, 5V35SGEN1T, GD2JBXJV5Z, WMEMMHZ3BH, ENY0GKRJS8]
sources:
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Proofs_and_Refutations
    locator: lead section
  - book: isbn:9780691164076
---

## Summary

The methodology of mathematics is the study of how mathematicians actually work.
It asks how they form concepts, how they choose problems, how they find results, and how they test and accept them.
It describes practice: the use of examples, analogies, special cases, generalization, conjectures, counterexamples and proofs.
It does not ask what mathematical objects are or why mathematical knowledge is certain; those questions belong to the [[philosophy of mathematics|NTJ5XW0PVD]].
The subject matters because a finished theorem hides the path that led to it, and the path is what a student or a researcher needs to learn.
In the Mathematics Subject Classification it is the class 00A35.

## Motivation

A textbook presents a theory in the order of logic: [[axioms|GD2JBXJV5Z]], definitions, lemmas and theorems.
Research almost never proceeds in this order.
A mathematician meets a problem, tries cases, makes a [[conjecture|WMEMMHZ3BH]], finds a counterexample, changes a definition, and only at the end writes a [[proof|0B94TKFQJX]].
A reader who sees only the final proof cannot see why the definitions have their form, or how anyone found the result.
The methodology of mathematics studies this hidden part, so that it can be described, taught and improved.

## Remarks

### Examples

- Pólya's four phases of solving a problem: understand the problem, devise a plan, carry out the plan, and look back. He described them in *How to Solve It* (1945), with heuristics such as "solve a simpler related problem" and "work backward".
- Plausible reasoning, which Pólya studied in *Mathematics and Plausible Reasoning* (1954): induction from cases, analogy and the weighing of evidence for a conjecture. The topic [[plausible reasoning and experimental mathematics|DME0TPC348]] treats it in detail.
- Lakatos's method of proofs and refutations: a conjecture, a proof, a counterexample, and then a better conjecture or a better definition. *Proofs and Refutations* (1976) develops it with [[Euler's polyhedron formula|09HT3P35YP]].
- The use of [[examples in mathematical practice|F3NNR77WKP]] to test conjectures and to shape definitions.
- [[Abstraction and generalization|976RZZCT1H]], and the search for [[classifications and invariants|9HQ3TADPA8]], as common ways to organize results.
- The balance between solving single problems and building theories, discussed in [[problem solvers and theory builders|Z29HM45R29]].

### Non-examples

- The question whether numbers exist independently of minds is not methodology. It is a question of the ontology of mathematics, in the philosophy of mathematics.
- A formal proof system, with its rules of inference, is not methodology. It is an object of [[mathematical logic|DYJ0KGTPMR]], although methodology studies how proofs are found and judged.
- A list of contest tricks for one type of problem is not methodology by itself. It becomes methodology when it describes general strategies and their limits, as in the topic [[heuristics of discovery|X1NSTVGDNQ]].

### Basic properties

- Discovery and justification follow different orders. A result is often found by [[inductive or abductive reasoning|5V35SGEN1T]] and then justified by deduction.
- Definitions are results of the method, not only starting points. Lakatos showed how a definition such as "polyhedron" changes under pressure from counterexamples.
- Proof has [[several functions|ENY0GKRJS8]] in practice: verification, explanation, communication, discovery and systematization.
- Experiment and computation are part of the method. They suggest conjectures and test them, but they do not replace proof.

### History

René Descartes wrote rules for the direction of the mind, with mathematics as the model of method.
Henri Poincaré described his own discovery of results on Fuchsian functions in an essay on mathematical creation, published in *Science et méthode* in 1908.
Jacques Hadamard collected such accounts in *The Psychology of Invention in the Mathematical Field* (1945).
George Pólya published *How to Solve It* in 1945 and *Mathematics and Plausible Reasoning* in 1954.
Imre Lakatos developed his method of proofs and refutations in articles of the 1960s, and the book *Proofs and Refutations* appeared in 1976, after his death in 1974.

### Common errors

- To think that mathematics is discovered in the order in which it is written. The order of a paper is chosen for checking, not for finding.
- To think that a heuristic is a proof method. "Try a special case" helps to find a result, but a special case proves nothing about the general case.
- To mix methodology with epistemology. "How did they find it?" and "why is it certain?" are different questions.

## Explanations

### L1 human

A finished proof in a book looks neat, as if the author knew the way from the start.
In reality the author tried small cases, made guesses, made mistakes and changed the question several times.
The methodology of mathematics studies this real process.
For example, before proving that the angles of a triangle sum to $180°$, someone may have measured the angles of many triangles and noticed the pattern.
The pattern suggested the result, and only a proof made it certain.

### L2 human

We follow Lakatos's method on Euler's formula $V - E + F = 2$ for polyhedra, where $V$, $E$ and $F$ count vertices, edges and faces.

1. Test: a cube has $V = 8$, $E = 12$ and $F = 6$, and $8 - 12 + 6 = 2$.
2. Test: a tetrahedron has $V = 4$, $E = 6$ and $F = 4$, and $4 - 6 + 4 = 2$.
3. Conjecture: $V - E + F = 2$ for each polyhedron.
4. Counterexample: a picture frame, a square ring with a square hole, made of $16$ quadrilateral faces. It has $V = 16$, $E = 32$ and $F = 16$, so $V - E + F = 0$.
5. Response: we can reject the frame as "not a polyhedron", or we can add the hypothesis "without holes" to the conjecture. Lakatos called these responses monster-barring and lemma-incorporation.
6. The second response leads to a correct theorem: for each convex polyhedron, $V - E + F = 2$.

The typical use of this method is in research: each counterexample shows which hypothesis or which definition must change.
A trap is to bar the counterexample by a new definition without asking what it teaches.
The frame led to the Euler characteristic of surfaces, which takes the value $0$ on the torus.

### L3 human

The methodology of mathematics sits between the philosophy of mathematics, the history of mathematics, mathematics education and the practice of research.
Its main texts are descriptive: Pólya and Hadamard wrote from their own experience, and Lakatos wrote a rational reconstruction of a historical episode.
Later work studies practice with the tools of cognitive science, sociology and the analysis of proofs written for proof assistants.
The questions are concrete: which proofs mathematicians find explanatory, how definitions are chosen, how a community decides that a long proof is correct, and how computers change the search for results.
Within this site, the sub-areas on [[heuristics of discovery|X1NSTVGDNQ]], [[plausible reasoning and experimental mathematics|DME0TPC348]] and [[rigour and the acceptance of proofs|1BTHSHST4M]] continue these themes.
The epistemological questions, such as whether mathematical knowledge is a priori, belong to the [[philosophy of mathematics|NTJ5XW0PVD]].
