---
tag: JZQVJ9XT63
kind: concept
name: Non-constructive existence proof
aliases: [non-constructive-proof, pure-existence-proof]
msc: ["00A35", "03F65"]
topics: [G9JFJGY4TQ, 958EF46EYJ]
audience: ug1
specializes: [0B94TKFQJX]
uses: [0JW2FHW7G3, 01XM7JEKHY, 0J0XBKG64S, 0RYYK8PG4S]
sources:
  - url: https://en.wikipedia.org/wiki/Constructive_proof
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_basis_theorem
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.3
---

## Summary

Sometimes you can prove that an object must exist and still not know which object it is.
A non-constructive existence proof does this: it shows that the object exists, but it does not name it and gives no method to find it.

Here is the classic case: there are irrational numbers $a$ and $b$ such that $a^b$ is rational.
Look at the number $c = \sqrt{2}^{\sqrt{2}}$; it is either rational or irrational.
If $c$ is rational, take $a = b = \sqrt{2}$, which are irrational, and $a^b = c$ is rational.
If $c$ is irrational, take $a = c$ and $b = \sqrt{2}$; then
$$a^b = \left(\sqrt{2}^{\sqrt{2}}\right)^{\sqrt{2}} = \sqrt{2}^{\sqrt{2} \cdot \sqrt{2}} = \sqrt{2}^{2} = 2,$$
which is rational.
In both cases a pair exists, so the statement is proved, and yet the proof does not tell you which case holds.

In general, a *non-constructive existence proof* of $\exists x \, P(x)$ is a proof that gives no witness.
There are three usual forms.
The first is a [[proof by contradiction|0J0XBKG64S]] that assumes no such object exists.
The second is a [[proof by cases|0WCP0PVET6]] with a different witness in each case and no way to decide the case.
The third is an appeal to a general theorem such as the [[intermediate value theorem|00KAFBR32E]], the [[pigeonhole principle|0HGVCWQGY3]] or the [[axiom of choice|0HTGB13FE2]].
Such proofs are valid in classical mathematics, which accepts the [[law of excluded middle|0RYYK8PG4S]], and they are rejected in constructive mathematics, which accepts only a [[constructive proof|01XM7JEKHY]] of existence.

## Motivation

A witness is sometimes hard to find and sometimes impossible to write down in finite terms.
The real root of $x^5 - x - 1$ has no formula in radicals, but the intermediate value theorem shows at once that it exists.
For a general theory, existence is often all you need: a theorem about a root, a maximum or a basis can be applied as soon as the object is known to exist.

Non-constructive proofs are often much shorter than constructive ones.
The price is information.
The proof does not say what the object is, and it may give no way to compute it.

## Notation

There is no special notation, since the statement is an ordinary [[existential statement|0JW2FHW7G3]] $\exists x \, P(x)$.
A proof by contradiction of it starts "Suppose that no $x$ satisfies $P(x)$", that is, $\forall x \, \neg P(x)$; see [[negation of an existential statement|05SZQKH75K]].
In Lean, `by_contra h` followed by `push_neg at h` produces this form, `by_cases h : P` splits on a proposition by `Classical.em`, and definitions that rely on `Classical.choice` must be marked `noncomputable`.

## Remarks

### Why the method is valid

Each form has one step that classical logic allows and constructive logic does not.
In the proof by cases, the step is "$c$ is rational or $c$ is irrational", an instance of the law of excluded middle for a question that the proof does not answer.
In the proof by contradiction, the step goes from "it is impossible that every $x$ fails $P$", which is $\neg \forall x \, \neg P(x)$, to "some $x$ satisfies $P$".
That step uses the [[double negation law|0NFAGWH84K]].

Watch the difference from a refutation.
To prove that $\sqrt{2}$ is irrational, you assume that it is rational and derive a contradiction.
That proves the negative statement $\neg P$ directly from "$P$ leads to absurdity", and it is valid even in intuitionistic logic.
Only the step from absurdity back to a positive existence claim needs excluded middle.

### Three common shapes

The first shape is a case split, as in the summary.
The second is a proof by contradiction with a count.
If $n$ real numbers have average $A$ and every one of them were less than $A$, their sum would be less than $nA$, which is false; so at least one of them is at least $A$.
The third shape quotes a theorem that is itself non-constructive.
For [[a real root of x^5 - x - 1|2W5SMZWGYF]], the polynomial is $-1$ at $1$ and $29$ at $2$, so the intermediate value theorem gives a root in between.
Transcendental numbers exist because the algebraic numbers form a countable set and the real numbers do not; the counting argument in this form names no [[transcendental number|0VTQXTCR2G]].
[[Hilbert's basis theorem|0YKA9J3XEE]], that every ideal of a polynomial ring in finitely many variables over a field is finitely generated, was proved in a form that shows a finite set of generators exists without computing one.

### When to choose it

Choose a non-constructive proof when the witness is hard to describe and you only need to know that it exists.
It is also a good first step: once you know that an object exists, a search for it is worth the effort.
Prefer a construction when the object will be used in a computation, or when the construction costs only a few more lines.
In the averaging example the largest of the numbers is a witness, so a constructive proof is just as short there.

### What is not a non-constructive proof

[[Irrational a and b with a to the power b rational, by construction|H7X4FMAHC8]] names the pair $\sqrt{2}$ and $\log_2 9$ and checks it.
[[There are n consecutive composite numbers|SJ5MYHND5D]] gives the numbers by a formula.
Liouville's proof that transcendental numbers exist is constructive too: it exhibits explicit numbers, such as $\sum_{k \ge 1} 10^{-k!}$, and proves that they are transcendental.

### Making it constructive

A non-constructive proof can often be upgraded with more work.
Bisection turns the root of $x^5 - x - 1$ into a sequence of nested intervals that you can compute; see the [[bisection method|7VMYC7MB3Q]].
For the irrational powers, the [[Gelfond-Schneider theorem|RN58Z2NWAC]] shows that $\sqrt{2}^{\sqrt{2}}$ is transcendental, so it is irrational and the second case of the summary is the true one.
That theorem is far deeper than the statement it settles.

Some existence results cannot be made constructive at all.
A subset of the real line that is not Lebesgue measurable is proved to exist with the axiom of choice.
Robert Solovay showed in 1970 that some form of choice is needed for this, if an inaccessible cardinal is consistent.

### Watch out

The first trap is to read a witness into the proof.
The summary proof does not show that $\sqrt{2}^{\sqrt{2}}$ is rational, nor that it is irrational, and quoting it for either fact is a mistake.

The second trap is to negate the goal wrongly at the start.
The negation of "some $x$ satisfies $P$" is "every $x$ fails $P$", not "some $x$ fails $P$".

The third trap is to treat a non-constructive proof as weaker in truth.
In classical mathematics it proves existence completely; it only gives less information.

### Writing it up

Say at the start what the proof will not do ("We do not identify the pair.").
In a proof by cases, state the case split as one sentence and give the witness of each case in its own paragraph.
In a proof by contradiction, write the negated assumption in full, with the quantifier turned, before you use it.
End with the existence statement itself.

### History

Paul Gordan proved in 1868, by explicit computation, that the invariants of binary forms are generated by finitely many of them.
In 1890 David Hilbert published the basis theorem and used it to prove finite generation for forms in any number of variables, without a method to find the generators.
Gordan is reported to have called the proof "not mathematics" but "theology".
Luitzen Egbertus Jan Brouwer's intuitionism, from the early twentieth century, rejected such proofs in principle; see [[constructivism|G958EQ8CWW]].

### Try it

First, prove that among any $5$ integers, two have a difference divisible by $4$.
There are only $4$ remainders on division by $4$, so two of the $5$ integers share a remainder, and their difference is divisible by $4$; the proof does not say which two.

Second, prove that some digit from $0$ to $9$ appears infinitely often in the decimal expansion of $\pi$.
If each of the $10$ digits appeared only finitely often, the expansion would have only finitely many places, which is false; the proof does not say which digit.

## Explanations

### L1 human

Thirteen people are in a room.
There are only twelve months, so two of them must have a birthday in the same month.
This argument proves that such a pair exists.
It does not say who the two people are.
To find them, you would have to ask everybody.
A proof that shows "something must exist" without pointing to it is a non-constructive proof.

### L2 human

Let us prove that if $a_1, \dots, a_n$ are real numbers with average
$$A = \frac{a_1 + \dots + a_n}{n},$$
then $a_i \ge A$ for some $i$.
Suppose, for a contradiction, that $a_i < A$ for every $i$.
Adding the $n$ inequalities gives $a_1 + \dots + a_n < nA$.
But the definition of $A$ says $a_1 + \dots + a_n = nA$, so we have a contradiction, and some $a_i$ satisfies $a_i \ge A$.
Check with numbers: $2, 7, 3$ have average $4$, and $7 \ge 4$.
The typical use: assume that every candidate fails, then add up or count the failures to reach a contradiction.
The proof does not tell which $a_i$ works; here the largest one always does, but in harder problems no such choice is known.

### L3 human

In intuitionistic logic a proof of $\exists x \, P(x)$ must contain a witness, so the classical step from $\neg \forall x \, \neg P(x)$ to $\exists x \, P(x)$ is not valid.
The Gödel-Gentzen negative translation still embeds classical arithmetic into intuitionistic arithmetic, with $\exists$ read as $\neg \forall \neg$.
Markov's principle is the special case of this step for decidable properties of natural numbers, and some constructive schools accept it while others do not.
Reverse mathematics measures how non-constructive a theorem is by the set existence axioms it needs; for example, the theorem that a continuous function on $[0, 1]$ attains a maximum is equivalent to weak König's lemma over the base system.
In Lean, non-constructive proofs of propositions are accepted, but definitions that depend on them cannot be compiled to code.
The wider theory is in the topic [[type theory and constructive mathematics|K6P3NSQEZ3]].
