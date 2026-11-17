---
tag: G9JFJGY4TQ
kind: topic
name: Proof methods
aliases: [methods]
msc: ["00A35"]
topics: [958EF46EYJ]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Methods of proof
---

## Summary

This topic collects the standard methods of [[mathematical proof|0B94TKFQJX]]: the general patterns, such as direct proof, proof by contradiction, proof by cases and induction, by which a proof gets from its hypotheses to its conclusion.
A method is chosen mainly by the logical form of the statement to be proved, and a long proof usually combines several methods, one for each part of the goal.
A proof node names its methods with the `methods` edge, and each target of that edge is a concept in this topic.
So the topic also lets a reader find all the proofs in the library that use one method.

## Remarks

### A map of the methods

1. Methods for an implication "if $P$, then $Q$": [[direct proof|0NTF6DMVAP]] assumes $P$ and derives $Q$; [[proof by contrapositive|0BB5TPGQ1N]] assumes not $Q$ and derives not $P$; [[proof by contradiction|0J0XBKG64S]] assumes $P$ and not $Q$ and derives a contradiction.
2. Methods for a universal statement "for every $x$, $P(x)$": [[proving universal statements|~ad3ff00f]] with an arbitrary element, [[proof by cases|0WCP0PVET6]], [[without loss of generality|~804de89a]], and, for the natural numbers, [[mathematical induction|0ASJVEFA9J]].
3. Methods for an existence statement "there is an $x$ with $P(x)$": [[constructive proof|01XM7JEKHY]] names the object, and a [[non-constructive existence proof|~796d0c7e]] shows that it must exist; uniqueness is a separate [[proof of uniqueness|~0d8083c0]].
4. Methods for an equivalence: [[proving biconditionals and equivalences|~afb23056]] by two directions, or by a cycle of implications for a list.
5. Methods for a negative statement: a [[counterexample|0ED72CTBNP]] refutes a universal claim, and a [[proof of impossibility|~36702f86]] shows that no object or method of a given kind exists.
6. A method for finding proofs, rather than for writing them: the [[forward-backward method|~f8b8bc06]].

### Choosing a method by the form of the goal

The first step is to write the statement in logical form, with its quantifiers and connectives; see the topic [[the language of mathematical statements|WMY13MXY3W]].
The outermost symbol of the goal then suggests the first step of the proof.
The words "for every" suggest an arbitrary element, and "if ... then" suggests assuming the hypothesis.
The words "there is" suggest a search for a witness, and "and" suggests two separate proofs.
The word "not" suggests a proof by contradiction, or a counterexample to the opposite claim.
The hypotheses suggest steps too: a hypothesis "$A$ or $B$" suggests a proof by cases, and a hypothesis "there is an $x$ with $P(x)$" suggests naming such an $x$.
When the conclusion is a statement about all natural numbers, induction is the first method to try.

### Direct proof and proof by contradiction

Many statements have both a direct proof and a proof by contradiction, and the two are often the same argument in two forms.
A proof by contradiction that never uses the assumed negation is a direct proof in disguise, and it is clearer when rewritten as a direct proof; see [[a direct proof in disguise as a proof by contradiction|~6305be77]].
A proof of a negative statement, such as the irrationality of $\sqrt{2}$, often assumes the positive statement and derives a contradiction.
Such a proof is a direct proof of a negation, and it is valid in intuitionistic logic as well.
The strict form, which proves a positive statement from the absurdity of its negation, needs the law of excluded middle.
A direct proof gives more information in general, and a proof by contradiction is often shorter to find.
The page on [[proof by contradiction|0J0XBKG64S]] treats the distinction in detail.

### The methods in the next sub-areas

1. Induction and its variants, strong induction, well-ordering and infinite descent, are treated in the topic [[induction and well-ordering as proof methods|EEH2F76CYQ]].
2. Counting arguments, invariants, the pigeonhole principle, double counting and extremal arguments are treated in the topic [[counting, invariant and extremal arguments|GB14W4SYPK]].
3. Patterns for common goals, such as two inclusions for a set equality and two inequalities for an equality of numbers, are treated in the topic [[proof patterns for common goals|MEKKHHQTKB]].
4. The writing of proofs and the errors in them are treated in the topics [[writing and reading proofs|STSM6PR7TX]] and [[fallacies and errors in proofs|T6QQ749DM5]].
