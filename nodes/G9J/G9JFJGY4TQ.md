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

A proof method is a pattern for getting from the hypotheses of a statement to its conclusion, and the shape of the statement usually tells you which pattern to try.
"If $n$ is odd, then $n^2$ is odd" invites you to assume that $n$ is odd and compute, while "$\sqrt{2}$ is irrational" invites you to assume a fraction $p/q$ and look for trouble.
The basic methods of [[mathematical proof|0B94TKFQJX]] are direct proof, the contrapositive, contradiction, cases, existence and uniqueness proofs, counterexamples and proofs of impossibility.
Induction and the counting and invariant arguments of later topics complete the standard list.
A long proof combines several of them, one for each part of the goal.
Every proof node in the library names its methods with the `methods` edge, and each target of that edge is one of these method concepts, so the methods also index the proofs that use them.

## Remarks

### Read the form of the goal first

Before you choose a method, write the statement with its quantifiers and connectives, as in the topic [[the language of mathematical statements|WMY13MXY3W]].
The outermost symbol of the goal then suggests the first line of the proof.
"For every $x$" suggests that you let $x$ be arbitrary, and "if ... then" suggests that you assume the hypothesis.
"There is" suggests a search for a witness, "and" suggests two separate proofs, and "if and only if" suggests two directions.
"Not" suggests that you assume the positive statement and derive a contradiction, or that you look for a counterexample to the opposite claim.
The hypotheses suggest steps too: a hypothesis "$A$ or $B$" suggests a proof by cases, and a hypothesis "there is an $x$ with $P(x)$" suggests that you name such an $x$.

### Implications and universal statements

An implication "if $P$, then $Q$" has three standard proofs.
A [[direct proof|0NTF6DMVAP]] assumes $P$ and derives $Q$.
A [[proof by contrapositive|0BB5TPGQ1N]] assumes not $Q$ and derives not $P$, which is equivalent.
A [[proof by contradiction|0J0XBKG64S]] assumes $P$ and not $Q$ together and derives an absurdity.
A universal statement "for every $x$, $P(x)$" starts with an arbitrary element, as in [[proving universal statements|CX38X989TB]].
The work can then split by [[proof by cases|0WCP0PVET6]], shrink by a symmetry with [[without loss of generality|Y7NE0E6PCV]], or, over the natural numbers, run by [[mathematical induction|0ASJVEFA9J]].
An equivalence is two implications, or a cycle of them for a longer list, as in [[proving biconditionals and equivalences|TFQ1845T84]].

### Existence, uniqueness and negative statements

To prove "there is an $x$ with $P(x)$", a [[constructive proof|01XM7JEKHY]] names the object and checks it, while a [[non-constructive existence proof|JZQVJ9XT63]] shows that the object must exist without naming it.
"Exactly one" adds a [[proof of uniqueness|GQHHNV79PA]], which shows that any two such objects are equal.
On the negative side, a [[counterexample|0ED72CTBNP]] refutes a universal claim with one instance, and a [[proof of impossibility|6F55216R53]] shows that no object or method of a given kind exists.
The [[forward-backward method|V8ZB838JY5]] stands apart: it is a way to find a proof, not a form for writing one.

### Contradiction is not one thing

Many books call every proof that starts with "suppose not" a proof by contradiction, but two different arguments hide under the name.
To prove a negation $\neg P$, you may assume $P$ and derive an absurdity; that is a refutation, and the irrationality of $\sqrt{2}$ is proved this way.
To prove a positive statement $P$, you may assume $\neg P$, derive an absurdity, and conclude $P$; only this second form needs the law of excluded middle.
A proof by contradiction that never uses its assumption is a direct proof in disguise, and it reads better when rewritten, as [[a direct proof in disguise|K686ZGPR17]] shows.

### Methods in later topics

Induction and its variants, strong induction, well-ordering and infinite descent, are in the topic [[induction and well-ordering as proof methods|EEH2F76CYQ]].
Counting arguments, invariants, the pigeonhole principle, double counting and extremal arguments are in the topic [[counting, invariant and extremal arguments|GB14W4SYPK]].
Patterns for common goals, such as two inclusions for an equality of sets, are in the topic [[proof patterns for common goals|MEKKHHQTKB]].
The writing of proofs and the errors in them are in the topics [[writing and reading proofs|STSM6PR7TX]] and [[fallacies and errors in proofs|T6QQ749DM5]].
