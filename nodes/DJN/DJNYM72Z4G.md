---
tag: DJNYM72Z4G
kind: problem
name: Entscheidungsproblem
aliases: [decision-problem-for-first-order-logic, hilberts-entscheidungsproblem]
msc: ["03B25", "03D35"]
topics: [E4AVTNWE9E]
audience: ug2
about: [086QKPF0A6, 5SDS9T8E7J]
uses: [086QKPF0A6, 5SDS9T8E7J, 9DMSG5HAQX, WQ1ZE255SF, RWRNBS3Z7B]
history:
  first_stated: "1928"
  posed_by: David Hilbert and Wilhelm Ackermann
  notes: Posed in the book Grundzüge der theoretischen Logik (1928); answered in the negative by Alonzo Church and by Alan Turing in 1936.
sources:
  - url: https://en.wikipedia.org/wiki/Entscheidungsproblem
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Undecidability
  - book: isbn:9780521701464
---

## Problem

The Entscheidungsproblem asks for one mechanical test that tells, for every sentence of first-order logic, whether the sentence is true in all structures.
Here are two sentences to keep in mind, with a binary relation symbol $R$:
$$\sigma_1 = \exists y \, \forall x \, R(x, y) \to \forall x \, \exists y \, R(x, y), \qquad \sigma_2 = \forall x \, \exists y \, R(x, y) \to \exists y \, \forall x \, R(x, y).$$
The first is valid, because one $y$ that works for every $x$ works for each $x$.
The second is not valid, because $(\mathbb{N}, <)$ makes its hypothesis true and its conclusion false.
The problem asks for a method that settles every such case without human insight.

Formally, the problem is to find an [[algorithm|9DMSG5HAQX]] with the following property.
It takes as input an arbitrary sentence $\sigma$ of [[first-order logic|086QKPF0A6]] over any finite signature of relation, function and constant symbols.
It always stops, and it outputs "yes" if $\sigma$ is [[valid|5SDS9T8E7J]] and "no" otherwise.

Three forms of the problem are equivalent.

1. Validity: decide whether $\models \sigma$.
2. Satisfiability: decide whether $\sigma$ has a model.
   This is equivalent to form 1, because $\sigma$ is satisfiable if and only if $\neg \sigma$ is not valid.
3. Provability: decide whether $\vdash \sigma$ in a standard proof calculus.
   This is equivalent to form 1 by soundness and [[Gödel's completeness theorem|WQ1ZE255SF]].

The answer is negative: no such algorithm exists.
This is [[Church's theorem|VA6BNNY2YC]], proved independently by Church and by Turing in 1936.

## Remarks

### Half of the problem is easy

By the completeness theorem, a sentence is valid exactly when it has a proof.
Proofs are finite strings, so a computer can list them one by one and check each one.
Run that search on $\sigma_1$, and it stops after it reaches a proof of $\sigma_1$.
Run it on $\sigma_2$, and it never stops, because no proof of $\sigma_2$ exists.
So the search confirms every valid sentence but never rejects an invalid one.
In the language of computability, the set of valid sentences is [[computably enumerable|TN9G24VABN]], or semi-decidable.

The hard half is the "no" answer.
You can sometimes find a countermodel by hand, as $(\mathbb{N}, <)$ for $\sigma_2$, but countermodels may need to be infinite, and no search through finite objects finds all of them.
Church's theorem says that the gap cannot be closed: the set of valid sentences is not [[computable|PPGD5KW8JC]].

### Why the problem needed a definition of algorithm

A positive answer needs only one algorithm, and everyone recognizes an algorithm when it is written down.
A negative answer is a claim about all possible algorithms.
To prove it, you need an exact mathematical class that contains every algorithm.
In 1936 Church proposed the functions definable in the [[lambda calculus|BD756KR8FM]], and Turing proposed the functions computed by [[Turing machines|758EYCN27B]].
The two classes turned out to be the same.
The claim that they contain every intuitive algorithm is the [[Church-Turing thesis|RWRNBS3Z7B]].
With the thesis, "no Turing machine decides validity" becomes "no algorithm decides validity".

### How the negative answer goes

Turing first proved that the [[halting problem|Z7TN2B35B0]] is undecidable.
He then turned each machine $M$ into a first-order sentence that is valid exactly when $M$ halts.
A test for validity would therefore decide the halting problem, which is impossible.
Church reached the same result from an unsolvable problem of his own about the lambda calculus.
The proofs are written out with [[Church's theorem|VA6BNNY2YC]].

### Where the answer is yes

The problem has positive answers for many fragments of first-order logic, and the topic [[decidability of logics and theories|E4AVTNWE9E]] collects them.
In the [[monadic predicate calculus|SERN6CRVWW]] all relation symbols are unary, and validity is decidable.
Several classes of prenex sentences, sorted by their quantifier prefix, are decidable, as [[decidable prefix classes|ZF79MZRQ8V]] explains.
Some theories also have a decidable set of consequences, for example [[Presburger arithmetic|4W0E9G7PPV]], the theory of the natural numbers with addition.

### Watch out

Do not read "undecidable" as "some sentences can never be settled".
Each single sentence is valid or not, and for $\sigma_1$ and $\sigma_2$ we settled the question in two lines.
Undecidability says only that no single algorithm settles all sentences.

Do not mix up validity with validity in finite structures.
Truth in every finite structure is a different and harder question: by [[Trakhtenbrot's theorem|XP6FW2WDWT]], its set is not even computably enumerable.

### Related decision problems

[[Hilbert's tenth problem|X8TVJSVTD4]] asks for an algorithm that decides whether a polynomial equation with integer coefficients has a solution in integers.
It also has a negative answer, and its proof reduces the halting problem to it in the same spirit.

### Try it

What does the proof search do on $\exists x \, P(x) \to \forall x \, P(x)$?
It runs forever, because the sentence is not valid: the domain $\{0, 1\}$ with $P = \{0\}$ is a countermodel.

Which of the three forms do you use to show that $\sigma_2$ is not valid?
The satisfiability form: $\neg \sigma_2$ has the model $(\mathbb{N}, <)$, so $\sigma_2$ is not valid.

## History

Hilbert and Ackermann stated the problem in 1928 in their book Grundzüge der theoretischen Logik, and they called it the main problem of mathematical logic.
The problem belonged to the wider [[program of Hilbert|P1RW6JWX73]].
Before 1936 several special cases were solved in the positive.
Löwenheim treated the monadic case in 1915.
Bernays and Schönfinkel, and Ackermann, solved prefix classes in 1928.
Gödel proved the completeness theorem in 1929, so validity and provability became the same question.
In 1936 Church published "A note on the Entscheidungsproblem", and Turing published "On computable numbers, with an application to the Entscheidungsproblem".

## Explanations

### L1 human

Hilbert hoped for a machine-like method that could judge every statement of logic as "always true" or "not always true".
Such a method would settle many questions of mathematics by calculation alone.
In 1936 Church and Turing showed that no such method can exist.
Turing first described exactly what a mechanical method is, with his machines.
Then he showed that a method for logic would also predict whether any machine stops, and that this prediction is impossible.
For small parts of logic a method does exist, for example when every property talks about one object at a time.

### L2 human

We decide one sentence by hand, with the method for the monadic fragment.
Let $\sigma$ be $\forall x \, P(x) \to \exists x \, P(x)$, with one unary symbol $P$.
The sentence $\sigma$ is valid if and only if $\neg \sigma$ has no model, and $\neg \sigma$ is equivalent to $\forall x \, P(x) \wedge \neg \exists x \, P(x)$.

The sentence $\neg \sigma$ is monadic with $k = 1$ predicate and quantifier rank $q = 1$.
By the [[finite model property of the monadic predicate calculus|AS0NHQMAKA]], if it has a model, then it has one with at most $q \cdot 2^k = 2$ elements.
So we check the structures with one or two elements.
In each of them, either $P$ is the whole domain, and then $\neg \exists x \, P(x)$ fails, or $P$ misses an element, and then $\forall x \, P(x)$ fails.
So $\neg \sigma$ has no model, and $\sigma$ is valid.

The typical use of the Entscheidungsproblem today is as the model of a negative result: to show that a question has no algorithm, reduce the halting problem to it.
The positive side shows the other typical move: find a bound on the size of a model, and then search a finite list.

### L3 human

In a signature with a binary relation symbol, the set of valid sentences is a complete computably enumerable set.
It is computably enumerable, and the halting set reduces to it by a computable map, so the Entscheidungsproblem has exactly the difficulty of the halting problem.
The finite version is hard in the other direction: finite satisfiability is computably enumerable and undecidable, so finite validity is co-c.e. and not c.e.

The classical decision problem, in the sense of Börger, Grädel and Gurevich, is the program of sorting the fragments of first-order logic into decidable and undecidable ones.
The fragments are cut out by quantifier prefix, by number of variables or by guards, as in [[two-variable logic|S7C3C7DJRF]] and the [[guarded fragment|Y7YS1C3GAE]].
The same question for theories, rather than for pure logic, leads to the decidable theories of Presburger, Tarski and Rabin, and to the [[essentially undecidable|9JDDFN8PT7]] theories of Tarski, Mostowski and Robinson.
