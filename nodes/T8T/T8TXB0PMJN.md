---
tag: T8TXB0PMJN
kind: example
name: Defining a polyhedron as a solid with V − E + F = 2
msc: ["00A35", "52B10"]
topics: [X1NSTVGDNQ]
audience: research
not_instance_of:
  - target: 79P9CTRN0V
    note: the counterexamples are removed by a definition that repeats the conclusion, so no lemma of the proof is found and the theorem becomes true by definition and says nothing
uses: [79P9CTRN0V, 09HT3P35YP, C1X8DP1SNE]
sources:
  - url: https://en.wikipedia.org/wiki/Proofs_and_Refutations
    locator: Method
---

## Example

We start from the conjecture $V - E + F = 2$ for polyhedra, after the hollow cube, with $V - E + F = 4$, and the picture frame, with $V - E + F = 0$, have appeared, as in [[the counterexamples to Euler's formula|C1X8DP1SNE]].
A defender of the conjecture answers each counterexample by monster-barring, and pushes this answer to its end.

1. The defender bars the hollow cube with the clause "a polyhedron has one connected surface".
2. The defender bars the picture frame with the clause "a polyhedron has no tunnel".
3. The defender bars Kepler's star polyhedron, with $V - E + F = -6$, with the clause "the faces of a polyhedron do not cross each other".
4. Each new strange solid brings a new clause, so the list of clauses keeps growing.
5. The defender ends the process with one clause: "a polyhedron is a solid whose surface has $V - E + F = 2$".
6. With this definition, the theorem "every polyhedron has $V - E + F = 2$" is true for every object, because it repeats the definition.

Now we check the condition of the [[method of proofs and refutations|79P9CTRN0V]] that fails.

1. The method asks that each counterexample be tested against the lemmas of the proof.
2. Here no lemma is examined, because the definition in step 5 is chosen to make the conclusion true, not to make a step of the proof valid.
3. The resulting theorem has no content: it gives no way to know, for a given solid, whether $V - E + F = 2$ without counting.
4. Lemma-incorporation gives a testable hypothesis instead, "the surface becomes a flat network after one face is removed", which we can check without computing $V - E + F$, and which leads to the Euler characteristic.

So this defense is not an instance of the method.

## Remarks

Monster-barring is not always wrong.
Steps 1 to 3 each give a reasonable definition, and the class of solids they describe is close to the right one.
The defense fails when the definition is chosen only to save the theorem, with no link to the proof.
The test is whether the new definition can be checked without the conclusion, and whether it explains why the proof works.
The same pattern appears outside mathematics: a claim protected by a new definition after each failure stops making predictions.

## Explanations

### L1 human

Someone says that every bird can fly.
Shown a penguin, the person says that a penguin is not a real bird, and shown an ostrich, the person says the same.
In the end, the person defines a bird as an animal with feathers that can fly, and the claim can no longer be wrong.
But it no longer tells us anything either.
The same can happen with the rule "corners minus edges plus faces is $2$".

### L2 human

Compare two answers to the picture frame, which has $V = 16$, $E = 32$ and $F = 16$.
The answer by definition, "a polyhedron has $V - E + F = 2$", turns the theorem into
$$V - E + F = 2 \implies V - E + F = 2,$$
which is true and empty.
The answer by lemma-incorporation says that if the surface, with one face removed, can be stretched flat, then $V - E + F = 2$.
To use it on a solid we test the flattening, and that test does not need the count.
It also predicts that the frame fails, since a ring-shaped surface with one face removed cannot be stretched flat.
So ask of each new hypothesis whether you can check it without the conclusion.
Watch out: a hypothesis can sound geometric and still be circular, if the only way to check it is to compute $V - E + F$.
