---
tag: JPHE53PABT
kind: concept
name: Circular reasoning
aliases: [circular-reasoning-in-proofs, circular-argument, begging-the-question, petitio-principii, circulus-in-probando]
msc: ["00A35", "97E50"]
topics: [T6QQ749DM5]
audience: ug1
uses: [0B94TKFQJX, S2BW0FDHV8]
sources:
  - url: https://en.wikipedia.org/wiki/Circular_reasoning
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Begging_the_question
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Differentiation_of_trigonometric_functions
    locator: Limit of sin(θ)/θ as θ tends to 0
  - book: isbn:9781108439534
---

## Summary

Circular reasoning is an argument that uses its own conclusion, or a statement whose proof needs the conclusion, as one of its premises.
In a [[proof|0B94TKFQJX]] the circle can be direct, when a step assumes the claim, or hidden, when a step cites a lemma or a formula whose proof depends on the claim.
A circular argument is valid as a piece of logic, since "$P$, so $P$" is a valid inference, but it gives no reason to believe $P$.
Circularity is relative to a chosen order of definitions and results: the same argument can be circular in one book and correct in another.
The idea matters because hidden circles are among the hardest errors to see, and every textbook must order its results so that no proof uses a later one.

## Motivation

A proof is a chain of steps from accepted statements to a new one.
If the new statement appears among the accepted ones, the chain is short and correct, but it proves nothing.
In practice nobody writes "$P$, therefore $P$".
The circle passes through other results: a proof of $P$ cites $Q$, and the proof of $Q$ in the textbook uses $P$.
To check a proof for circularity, we must know where each cited result comes from.

## Notation

The idea has several names.

1. In logic and rhetoric: *petitio principii*, "assuming the original point", which English renders as "begging the question", and *circulus in probando*, "reasoning in a circle".
2. In teaching: "assuming what is to be proved" or "assuming the result".
3. In daily English, "begs the question" often means "raises the question". This page uses the phrase only in its logical sense.

## Remarks

### Examples

1. The computation of $\lim_{x \to 0} \frac{\sin x}{x}$ by [[L'Hôpital's rule|0JWT4PPQ7B]] is [[circular when sine is defined geometrically|XFD21N14W4]]. The rule needs $\sin' = \cos$, and the usual proof of $\sin'(0) = 1$ is this limit.
2. The "proof" that every integer $n \ge 2$ has a prime factor by "let $p$ be the [[smallest prime factor|VVY4Y14P0H]] of $n$" assumes the existence of a prime factor in its first step.
3. A "proof" of an identity that starts from the identity and reaches $0 = 0$ uses the claim as a premise. The page on [[squaring both sides|FGS7ZJJYRK]] shows a case where the conclusion is even false.
4. An induction step that assumes $P(n + 1)$, or "$P(k)$ for every $k$", is circular. This is one of the [[errors in induction proofs|V52HDTMPV5]].
5. Many attempts to prove the [[parallel postulate|2PC3XY0PYZ]] assumed a statement that is equivalent to it. Legendre's attempts are described in [[famous incorrect proofs|1CV4HTA6C8]].

### Non-examples

1. With [[sine defined by its power series|VEVN4JA38E]], the proof of $\frac{\sin x}{x} \to 1$ from $\sin'(0) = \cos 0 = 1$ is not circular, because $\sin' = \cos$ is proved by differentiating the series term by term.
2. A proof by [[strong induction|0KMVFSHFGZ]] that every $n \ge 2$ is a product of primes uses the claim for smaller numbers. This is the induction hypothesis, a different statement from the claim for $n$, so the proof is not circular.
3. A [[proof by contradiction|0J0XBKG64S]] assumes the negation of the claim, not the claim. It is not circular.

### Basic properties

1. An argument whose premises include its conclusion is valid in the logical sense. So circularity is not a failure of logic, but a failure of the argument to give a reason.
2. A proof is free of circles exactly when the results that it uses can be listed so that each result is proved from earlier ones only. The `uses` field of this site records such dependencies, and the graph of the field must have no cycle.
3. Whether a proof is circular depends on the definitions. A proof of $\frac{\sin x}{x} \to 1$ from $\sin' = \cos$ is circular with the geometric definition and correct with the series definition.
4. A circular proof of a true statement is still not a proof. Its conclusion can be true, so a check of the conclusion does not find the error.

### History

Aristotle described the error of asking for the original point, and the Latin name *petitio principii* translates his Greek phrase.
The English phrase "begging the question" is a translation of the Latin name from the 16th century.
For the [[parallel postulate|2PC3XY0PYZ]], many attempted proofs over about two thousand years assumed an equivalent statement, and these are the best-known circular arguments in mathematics.

### Common errors

1. A student proves an equation by starting from the equation and simplifying both sides until a true statement appears. The steps run from the claim to a true statement, and they prove nothing unless each step is reversible.
2. A student cites a formula from the end of the chapter in a proof that the chapter needs for that formula.
3. A student writes "by the definition of $p$" for an object $p$ whose existence is the claim.

## Explanations

### L1 human

Circular reasoning means using the answer to prove the answer.
Suppose a friend says "this film is the best, because no film is better".
The reason only repeats the claim in other words.
In mathematics the circle is often longer: we prove fact A with fact B, but fact B was proved with fact A.
To avoid it, we must know where each fact that we use comes from.

### L2 human

We check whether the following proof that $\frac{d}{dx} e^x = e^x$ is circular.
The book defines $\ln x = \int_1^x \frac{dt}{t}$ for $x > 0$, and $e^x$ as the inverse function of $\ln$.

1. The proof: $\ln$ is differentiable with $\ln'(x) = \frac{1}{x}$, by the [[fundamental theorem of calculus|0NHGY0N0JB]]. This step uses only the definition of $\ln$.
2. The function $\ln$ has a positive derivative, so it is strictly increasing and has a differentiable inverse $\exp$.
3. By the rule for the derivative of an inverse function, $\exp'(y) = \frac{1}{\ln'(\exp y)} = \exp y$.
4. Each step uses a result proved before $\exp$ is defined. So the proof is not circular in this book.
5. In a book that defines $\ln$ as the inverse of $\exp$ and computes $\ln'$ from $\exp' = \exp$, the same steps in the reverse order would be circular.

The typical use of this check is to read a proof together with the order of the book, and to ask for each cited result where its proof is.
A trap is to call a proof correct because each cited result is true; a true result can still depend on the claim.

### L3 human

The dependency structure of a theory is a directed graph whose vertices are definitions and results and whose edges are uses; a correct development is a topological order of an acyclic graph.
Circularity is a cycle in this graph, and hidden circularity is a cycle that passes through results of other chapters or other books.
Proof assistants exclude cycles by construction: a declaration can refer only to earlier declarations, and a recursive definition must pass a termination check.
Not every apparent circle is a fallacy: [[strong induction|0KMVFSHFGZ]] and well-founded recursion use the claim for smaller cases, and the well-foundedness of the order is what breaks the circle.
Equivalence proofs of the form $P_1 \Rightarrow P_2 \Rightarrow \cdots \Rightarrow P_1$ are cycles of implications, but they prove only that the statements are equivalent, and one of them must be proved independently to give the truth of all.
