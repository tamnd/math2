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

A finished theorem hides the path that led to it, and the methodology of mathematics studies that path.
It asks how mathematicians form concepts, choose problems, find results, and test and accept them.
Its material is practice: examples, special cases, analogies, generalization, [[conjectures|WMEMMHZ3BH]], counterexamples and [[proofs|0B94TKFQJX]].
It does not ask what mathematical objects are or why mathematical knowledge is certain, since those questions belong to the [[philosophy of mathematics|NTJ5XW0PVD]].
In the Mathematics Subject Classification it is the class 00A35.

## Motivation

A textbook presents a theory in logical order: [[axioms|GD2JBXJV5Z]], definitions, lemmas, theorems.
Research almost never runs in that order.
A mathematician meets a problem, tries small cases, makes a conjecture, finds a counterexample, changes a definition, and only at the end writes a proof.
A reader who sees only the final proof cannot see why the definitions have their form, or how anyone found the result.

Here is a small case.
Compute the sums of the first odd numbers:
$$1 = 1, \quad 1 + 3 = 4, \quad 1 + 3 + 5 = 9, \quad 1 + 3 + 5 + 7 = 16.$$
The squares suggest the conjecture $1 + 3 + \cdots + (2n - 1) = n^2$, by [[inductive reasoning|5V35SGEN1T]], and only then does anyone look for a proof.
The order of finding was computation, pattern, conjecture, proof, while the textbook shows only the last step.
The methodology of mathematics describes the hidden steps so that they can be taught and improved.

## Notation

The field has no symbols of its own.
"Methodology" here means the study of methods, not a single method.
"Mathematical practice" is a near synonym used in recent work, and "heuristic" names a rule of thumb for finding a result, such as "try a special case", as opposed to a rule for proving it.

## Remarks

### Pólya's four phases on a small problem

George Pólya split problem solving into four phases: understand the problem, devise a plan, carry out the plan, and look back.
Try them on the question of how many diagonals a convex polygon with $n$ sides has.
To understand it, count small cases: a square has $2$ diagonals and a pentagon has $5$.
For a plan, notice that each vertex joins by a diagonal to every vertex except itself and its two neighbors, so to $n - 3$ others.
Carrying out the plan, $n$ vertices give $n(n - 3)$ ends of diagonals, and each diagonal has two ends:
$$\text{number of diagonals} = \frac{n(n - 3)}{2}.$$
Looking back, the formula gives $\frac{4 \cdot 1}{2} = 2$ and $\frac{5 \cdot 2}{2} = 5$, which match the counts, and it predicts $9$ for a hexagon.
The sub-area on [[heuristics of discovery|X1NSTVGDNQ]] treats such rules in detail.

### Definitions are results, not only starting points

In a finished theory a definition comes first, but in practice it is often the last thing to be settled.
The word "prime" is a short example.
If $1$ counted as prime, then $6 = 2 \cdot 3 = 1 \cdot 2 \cdot 3$ would have two factorizations into primes, and the uniqueness of prime factorization would fail.
So the definition was shaped by the theorem it had to serve, and [[why 1 is not a prime number|JSR7S5TZ9C]] tells this story in full.
Imre Lakatos made the same point at length with the word "polyhedron", which changed under pressure from counterexamples to Euler's formula, as the L2 explanation shows.

### Choosing problems

A good problem is one whose solution teaches something beyond itself.
David Hilbert presented a list of open problems at the International Congress of Mathematicians in Paris in 1900, and many of them shaped research for decades.
The tension between solving hard single problems and building general theories is the subject of [[problem solvers and theory builders|Z29HM45R29]].
[[Examples in mathematical practice|F3NNR77WKP]], [[abstraction and generalization|976RZZCT1H]] and the search for [[classifications and invariants|9HQ3TADPA8]] are other common ways in which problems are chosen and results organized.

### Experiment and computation

Computation suggests conjectures and tests them, but it does not replace proof.
The polynomial $n^2 + n + 41$ is prime for $n = 0$ to $39$, and at $n = 40$ it equals $41^2 = 1681$.
A good experimenter uses such data both ways: to form a guess and to try to break it.
Proof then has [[several functions|ENY0GKRJS8]], since it verifies the guess, explains it and often suggests the next one.
The sub-area on [[plausible reasoning and experimental mathematics|DME0TPC348]] continues this theme.

### What it is not

The question whether numbers exist independently of minds is not methodology.
It is a question of ontology, and it belongs to the philosophy of mathematics.
A formal proof system with its rules of inference is not methodology either, because it is an object of [[mathematical logic|DYJ0KGTPMR]], although methodology studies how proofs are found and judged.
A list of contest tricks for one type of problem becomes methodology only when it describes general strategies and their limits.

### Watch out

Mathematics is not discovered in the order in which it is written.
A paper chooses its order for checking, not for finding, so a student who tries to invent proofs in textbook order usually gets stuck.

A heuristic is not a proof method.
"Try a special case" helps you find a result, but a special case proves nothing about the general case, as $n^2 + n + 41$ shows.

### History

Henri Poincaré described how he found results on Fuchsian functions in his essay on mathematical creation, published in *Science et méthode* in 1908.
Jacques Hadamard collected such accounts in *The Psychology of Invention in the Mathematical Field* (1945).
George Pólya published *How to Solve It* in 1945 and *Mathematics and Plausible Reasoning* in 1954.
Imre Lakatos developed his method of [[proofs and refutations|79P9CTRN0V]] in articles of the 1960s, and the book *Proofs and Refutations* appeared in 1976, after his death in 1974.

### Try it

First, apply Pólya's "look back" to the diagonal formula: does it give a sensible answer for a triangle?
It gives $\frac{3 \cdot 0}{2} = 0$, which is right, since a triangle has no diagonals.

Second, compute $1$, $1 + 2 + 1$, $1 + 2 + 3 + 2 + 1$ and $1 + 2 + 3 + 4 + 3 + 2 + 1$, and state a conjecture.
The sums are $1, 4, 9, 16$, which suggests that $1 + 2 + \cdots + n + \cdots + 2 + 1 = n^2$; it is true, since the left side is $\frac{n(n + 1)}{2} + \frac{(n - 1)n}{2} = n^2$.

## Explanations

### L1 human

A finished proof in a book looks neat, as if the author knew the way from the start.
In reality the author tried small cases, made guesses, made mistakes and changed the question several times.
The methodology of mathematics studies this real process.
For example, someone who measures the angles of many paper triangles notices that they always add up to about $180°$.
The pattern suggests the result, and only a proof makes it certain.

### L2 human

Here is Lakatos's method run on [[Euler's polyhedron formula|09HT3P35YP]] $V - E + F = 2$, where $V$, $E$ and $F$ count the vertices, edges and faces.
Two tests support it:
$$\text{cube: } 8 - 12 + 6 = 2, \qquad \text{tetrahedron: } 4 - 6 + 4 = 2.$$
So we conjecture that $V - E + F = 2$ for every polyhedron.
Now take a picture frame: a square ring with a square hole, made of $16$ quadrilateral faces.
It has $4$ outer, $4$ inner, $4$ top and $4$ bottom faces, $16$ vertices, and $16 \cdot 4 / 2 = 32$ edges, so
$$V - E + F = 16 - 32 + 16 = 0.$$
There are two responses.
We can reject the frame as "not a real polyhedron", which Lakatos called monster-barring.
Or we can find the hidden assumption in the proof and add it as a hypothesis, which he called lemma-incorporation.
The second response leads to a correct theorem, for example $V - E + F = 2$ for every convex polyhedron.
Watch out: barring a counterexample by a new definition, without asking what it teaches, loses information.
The frame points to the [[Euler characteristic|RNDDWDAFJ5]] of surfaces, which is $0$ for the torus.

### L3 human

The methodology of mathematics sits between the philosophy of mathematics, the history of mathematics, mathematics education and research practice.
Its classic texts are descriptive.
Pólya and Hadamard wrote from their own experience, and Lakatos wrote a rational reconstruction of a historical episode in the form of a classroom dialogue.
Later work studies practice with the tools of cognitive science and sociology, and with the record of proofs written for proof assistants.
The questions are concrete: which proofs mathematicians find explanatory, how definitions are chosen, how a community decides that a long proof is correct, and how computers change the search for results.
The sub-areas on [[heuristics of discovery|X1NSTVGDNQ]] and [[rigor and the acceptance of proofs|1BTHSHST4M]] continue these themes, while questions such as whether mathematical knowledge is a priori go to the philosophy of mathematics.
