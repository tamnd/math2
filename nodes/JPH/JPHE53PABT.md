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

Circular reasoning proves a claim by assuming the claim, often without noticing.
Here is a short example from a calculus exam; decide whether it is a proof.

> Claim: $\lim_{x \to 0} \frac{\sin x}{x} = 1$.
> Both $\sin x$ and $x$ tend to $0$, so by L'Hôpital's rule the limit equals $\lim_{x \to 0} \frac{\cos x}{1} = 1$.

In a course that defines sine on the unit circle, this is not a proof.
L'Hôpital's rule needs the derivative $\sin' = \cos$, and that derivative was found with the very limit we want, so the argument runs in a circle.
The correct first proof squeezes $\frac{\sin x}{x}$ between $\cos x$ and $1$ with areas in the unit circle, as the [[worked example|XFD21N14W4]] shows.

In general, an argument is circular when its conclusion, or a statement whose proof needs the conclusion, appears among its premises.
In a [[proof|0B94TKFQJX]] the circle is direct when a step assumes the claim, and hidden when a step cites a result whose own proof depends on the claim.

## Motivation

A proof is a chain from accepted statements to a new one.
If the new statement is already among the accepted ones, the chain is short and valid, but it gives no reason to believe anything.
Nobody writes "$P$, therefore $P$".
In practice the circle passes through other results: a proof of $P$ cites $Q$, and the textbook proved $Q$ from $P$.
So to check a proof for circles, you must know where each cited result comes from.

This is also why every textbook orders its results, so that no proof uses a later one.
The [[sine limit|XFD21N14W4]] and the [[smallest prime factor|VVY4Y14P0H]] are the two standard cases where a careless order creates a circle.

## Notation

The error has formal names in logic and informal names in teaching.
Logic calls it *petitio principii*, Latin for "asking for the starting point", which English renders as "begging the question", and also *circulus in probando*, "a circle in the proving".
Teachers say "assuming what is to be proved" or "assuming the result".
Watch out for the daily English use of "begs the question" to mean "raises the question"; in logic the phrase means only the error.

## Remarks

### Where the circle hides

A student proves that every integer $n \ge 2$ has a prime factor by starting "let $p$ be the [[smallest prime factor|VVY4Y14P0H]] of $n$".
That first sentence already assumes that a prime factor exists.
A student proves an identity by starting from the identity and simplifying both sides until $0 = 0$ appears.
That shows only "claim implies true", and [[squaring both sides|FGS7ZJJYRK]] shows that the method can even "prove" a false identity.
An induction step that assumes $P(n + 1)$, or "$P(k)$ for every $k$", assumes what it should prove; this is one of the [[errors in induction proofs|V52HDTMPV5]].
Many attempts to prove the [[parallel postulate|2PC3XY0PYZ]] assumed a statement that cannot be proved without it, and Legendre's attempts are told in [[famous incorrect proofs|1CV4HTA6C8]].

### When it only looks circular

With [[sine defined by its power series|VEVN4JA38E]], the L'Hôpital argument of the Summary is correct, because $\sin' = \cos$ then comes from differentiating the series term by term.
A proof by [[strong induction|0KMVFSHFGZ]] that every $n \ge 2$ is a product of primes uses the claim for smaller numbers.
That is the induction hypothesis, a different statement from the claim for $n$, so the proof is not circular.
A [[proof by contradiction|0J0XBKG64S]] assumes the negation of the claim, not the claim, so it is not circular either.

### Circles depend on the book

An argument whose premises include its conclusion is valid in the sense of logic, since "$P$, so $P$" never leads from truth to falsehood.
So circularity is not a failure of logic; it is a failure to give a reason.
A development is free of circles exactly when its results can be listed so that each is proved only from earlier ones.
Whether a given proof is circular therefore depends on the order of definitions and results.
The same L'Hôpital argument is circular with the geometric definition of sine and correct with the series definition.
A circular proof of a true statement is still not a proof, and checking the conclusion will not reveal the error.

### Watch out

The most common circle in student work is "proof by working backward and stopping".
To prove $\frac{a + b}{2} \ge \sqrt{ab}$ for $a, b \ge 0$, a student writes $\frac{a + b}{2} \ge \sqrt{ab}$, so $a + b \ge 2\sqrt{ab}$, so $(\sqrt{a} - \sqrt{b})^2 \ge 0$, "true".
The chain starts from the claim, so as written it proves nothing.
The correct version runs the steps the other way, and each step must be reversible:
$$(\sqrt{a} - \sqrt{b})^2 \ge 0 \;\Longrightarrow\; a + b - 2\sqrt{ab} \ge 0 \;\Longrightarrow\; \frac{a + b}{2} \ge \sqrt{ab}.$$

### History

Aristotle described the error of asking for the original point in the *Sophistical Refutations* and the *Prior Analytics*, and the Latin *petitio principii* renders his Greek phrase.
The English phrase "begging the question" comes from a translation of the Latin in the 16th century.
For the parallel postulate, attempted proofs over many centuries assumed an equivalent statement, and these are the best-known circular arguments in mathematics.

### Try it

Is this a proof that $\sqrt{2}$ is irrational: "Suppose $\sqrt{2} = \frac{p}{q}$ in lowest terms; since $\sqrt{2}$ is irrational, this is impossible"?
No: the reason given is the claim itself, while the standard proof derives that $p$ and $q$ are both even.

A book defines $\ln x = \int_1^x \frac{dt}{t}$ and proves $\ln(ab) = \ln a + \ln b$ from that integral.
Is a proof of $\exp(a + b) = \exp(a)\exp(b)$ from this rule circular in that book?
No: the logarithm rule comes first and uses only the integral, so the chain has no cycle.

## Explanations

### L1 human

Circular reasoning means using the answer to prove the answer.
A friend says "this film is the best, because no film is better".
The reason only repeats the claim in other words.
In mathematics the circle is usually longer: fact A is proved with fact B, but fact B was proved with fact A.
To avoid it, you need to know where each fact that you use comes from.

### L2 human

We check whether a proof that $\frac{d}{dx} e^x = e^x$ is circular in a book that defines $\ln x = \int_1^x \frac{dt}{t}$ for $x > 0$, and $\exp$ as the inverse function of $\ln$.
By the [[fundamental theorem of calculus|0NHGY0N0JB]], $\ln'(x) = \frac{1}{x}$, and this uses only the definition of $\ln$.
The derivative is positive, so $\ln$ is strictly increasing and has a differentiable inverse $\exp$.
The rule for the derivative of an inverse function gives
$$\exp'(y) = \frac{1}{\ln'(\exp y)} = \frac{1}{1/\exp y} = \exp y.$$
Every result used here is proved before $\exp$ is defined, so the proof is not circular in this book.

Now picture a second book, which defines $\exp$ by its power series and $\ln$ as its inverse, and computes $\ln'$ from $\exp' = \exp$.
There the same steps, used to prove $\exp' = \exp$, would run in a circle.
The typical use of this check is to read a proof next to the order of the book, asking for each cited result where its proof is.
Watch out: a proof is not correct just because each cited result is true, since a true result can still depend on the claim.

### L3 human

The dependency structure of a theory is a directed graph whose vertices are definitions and results and whose edges are uses.
A correct development lists the vertices in a topological order, which exists exactly when the graph has no cycle.
Proof assistants exclude cycles by construction: a declaration may refer only to earlier declarations, and a recursive definition must pass a termination check.
Not every apparent circle is an error: [[strong induction|0KMVFSHFGZ]] and well-founded recursion use the claim for smaller cases, and the well-foundedness of the order breaks the circle.
A cycle of implications $P_1 \Rightarrow P_2 \Rightarrow \cdots \Rightarrow P_1$ is also fine, but it proves only that the statements are equivalent, and one of them must be proved on its own before any is true.
