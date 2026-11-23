---
tag: RVZCSFDB2Y
kind: concept
name: Toulmin model of argumentation
aliases: [toulmin-model, toulmin-scheme, toulmin-layout-of-arguments]
msc: ["97E50", "97C70"]
topics: [VHGA6J4NZK]
audience: research
uses: [0B94TKFQJX, W48XN2MEM9, 5V35SGEN1T]
sources:
  - url: https://en.wikipedia.org/wiki/Stephen_Toulmin
    locator: Toulmin model of argument
  - url: https://en.wikipedia.org/wiki/Argumentation_theory
    locator: "Stephen E. Toulmin's contributions"
  - url: https://doi.org/10.1007/s10649-006-9059-8
    locator: pages 3-21
  - url: https://doi.org/10.1007/s11858-008-0095-y
    locator: pages 427-441
---

## Summary

A student says that $3$ divides $123$, "because $1 + 2 + 3 = 6$".
The sentence contains a claim and a fact, but the rule that connects them, that a number is divisible by $3$ exactly when its digit sum is, is never spoken.
Whether the student knows that rule, half-remembers it, or has only seen it used, the sentence alone cannot tell.
The Toulmin model gives a teacher a way to write the missing rule down and ask about it.

The model describes one step of an argument by six parts.
The claim is the statement to be established, and the data are the facts offered for it.
The warrant is the general rule that licenses the step from data to claim, and the backing is what supports the warrant.
The qualifier states how strong the claim is, such as "certainly" or "probably", and the rebuttal states the conditions under which the claim would fail.
Stephen Toulmin proposed the model in *The Uses of Argument* (1958), and mathematics education uses it as a standard tool to analyze the arguments of students and of whole classes.

## Motivation

A classroom argument is rarely a [[proof|0B94TKFQJX]] in the logical sense.
Students say "it works for $1$, $2$ and $3$, so it always works", or "it is true because of the picture".
To study such talk, a researcher needs a way to describe arguments that are not deductive and that leave parts unsaid.
Formal logic records premises and conclusions, but it has no place for "probably" or for the reason why a rule applies.
The Toulmin model has places for both, so it can describe a weak argument without forcing it into a wrong form.

## Notation

Researchers draw the model as a diagram: data $D$ on the left, an arrow to the claim $C$ on the right, the warrant $W$ under the arrow, and the backing $B$ under the warrant.
The qualifier $Q$ stands next to the claim, and the rebuttal $R$ below it.
Some authors write "grounds" for data and "conclusion" for claim.
Götz Krummheuer used a reduced model with only data, claim, warrant and backing to analyze classroom talk.

## Remarks

### Laying out the opening argument

The claim $C$ is that $3$ divides $123$.
The data $D$ are that the digit sum of $123$ is $6$ and that $3$ divides $6$.
The warrant $W$, unspoken, is the divisibility test for $3$.
The backing $B$ is the reason the test works: $10 \equiv 1 \pmod 3$, so for digits $a$, $b$ and $c$,
$$100a + 10b + c \equiv a + b + c \pmod 3.$$
The qualifier is "certainly", because the warrant is a theorem, and there is no rebuttal.
Check: $123 = 3 \cdot 41$.

### Three more layouts

[[A proof that the sum of two odd numbers is even|PXJSRNZ5TS]] has the definition of "even" as its warrant and "certainly" as its qualifier.
[[A conjecture about a prime-generating polynomial|6KXTT705M2]] has computed cases as data, an inductive warrant, the qualifier "probably", and a rebuttal that a later value of $n$ triggers.
A geometry student who claims two triangles congruent uses two equal sides and the included angle as data, the side-angle-side criterion as warrant, and the axioms of the course as backing.

### What has no layout

[[A bare assertion|GF25NRYH94]] such as "$91$ is prime" has a claim but no data, so there is nothing for a warrant to link.
A table of $n^2$ for $n = 1$ to $10$ with no claim is not an argument either, since the claim is missing.
The model describes reasons, so it starts to work only when a student gives one.

### How steps combine

In a correct mathematical proof, every step has a deductive warrant and the qualifier "certainly", and the model reduces to a chain of deductions.
The model describes one step at a time, so a long argument is a chain or a tree in which the claim of one step becomes data for the next.
Warrants are often unsaid, and to reconstruct one the analyst asks which general rule would make the step valid.

### History

Toulmin published *The Uses of Argument* in 1958 as a criticism of formal logic as a model of everyday and legal reasoning.
Krummheuer brought a reduced form of the model into research on classroom argumentation in the 1990s.
Matthew Inglis, Juan Pablo Mejía-Ramos and Adrian Simpson (2007) argued that mathematics education should use the full model, qualifier included.
Studying graduate students in mathematics who explored conjectures in number theory, they found warrants of three types: inductive, structural-intuitive and deductive.
Christine Knipping (2008) used the model to reconstruct the global structure of a whole class's arguments.

### Watch out

An analyst may force every step into a deductive form.
A step with an inductive warrant and the qualifier "probably" is a correct use of the model, and it describes many good arguments in the exploring phase of mathematics.
An analyst may also drop the qualifier, and then "probably true" and "certainly true" look the same, so the difference between a conjecture and a theorem disappears.
A teacher may confuse data with warrant: the data are particular facts, and the warrant is a general rule.

### Try it

First, lay out "$x = 2$ solves $x^2 = 4$, because $2 \cdot 2 = 4$".
The claim is that $2$ is a solution, the data are $2 \cdot 2 = 4$, and the warrant is the definition of a solution.

Second, a student says "the angles of this triangle add to $180^\circ$, because I measured them".
The warrant is "measurement shows the exact value", which is inductive, so an honest qualifier is "approximately".

## Explanations

### L1 human

When people argue, they give a claim and some reasons.
Stephen Toulmin noticed that a reason usually has two parts: a fact and a rule that connects the fact to the claim.
For example, "$12$ ends in $2$" is the fact, "a number that ends in an even digit is even" is the rule, and "$12$ is even" is the claim.
People often leave the rule unsaid.
The Toulmin model writes all the parts down, and it adds a word for how sure the claim is and a note on when the claim might fail.

### L2 human

A student claims that $f(x) = x \sin(1/x)$, with $f(0) = 0$, is continuous at $0$, "because the graph has no jump there".
The claim is correct, and the data are a picture of the graph near $0$.
The warrant is "a graph with no jump is continuous", and its backing is the student's picture of continuity, not the [[definition of continuity|0W8YHHGCJG]].
The layout shows what the teacher must address: the claim is fine, but the warrant is not a theorem, since a picture cannot show every point.

A better warrant uses a bound.
For $x \ne 0$ we have $|\sin(1/x)| \le 1$, so
$$|f(x) - f(0)| = |x| \, |\sin(1/x)| \le |x|,$$
and the right side tends to $0$ as $x \to 0$.
The data are the same function, and the claim is the same, but the warrant is now deductive and the qualifier becomes "certainly".
Watch out: the analyst must not credit the student with the bound, because the student's own warrant was the picture.

### L3 human

The Toulmin model comes from argumentation theory, which studies reasoning in law, science and daily life.
In mathematics education it serves two purposes: analyzing single arguments, and reconstructing the argumentation of a class, as in Knipping's work.
It links the cognitive research on [[proof schemes|YVNRVXJR68]] with the social research on [[reasoning and proof in the classroom|E77B813MT4]].
The qualifier and the rebuttal give a place to [[plausible reasoning|DME0TPC348]], which a purely deductive model cannot describe.
The model also describes the step from a [[conjecture|WMEMMHZ3BH]] to a theorem: the claim stays the same, and the qualifier changes from "probably" to "certainly" when a deductive warrant is found.
