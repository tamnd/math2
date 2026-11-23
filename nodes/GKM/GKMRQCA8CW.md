---
tag: GKMRQCA8CW
kind: concept
name: The language of proofs
aliases: [language-of-proofs]
msc: ["00A35"]
topics: [STSM6PR7TX]
audience: ug1
uses: [0B94TKFQJX, 8JQHJK94RZ, 661V0DH7V3, EGTZPA6QH3, FA6YZGR2SS]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Proof terminology
  - url: https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Mathematics
    locator: Writing style in mathematics
  - url: https://en.wikipedia.org/wiki/Q.E.D.
    locator: lead section
  - book: isbn:9781108439534
    locator: Chapter 3
---

## Summary

A formula on its own does not say whether it is assumed, chosen, still to be shown, or already proved.
The language of proofs is the small set of words, such as "let", "suppose", "hence" and "we claim", that gives each sentence of a [[proof|0B94TKFQJX]] its logical role.

Take the formula $x > 0$ in the middle of a proof.
It can be read in four ways, and four short phrases separate them:

> "Let $x > 0$": a new object enters, and $x > 0$ is all we know about it.
> "Suppose that $x > 0$": an assumption opens, and it must be closed later.
> "We must show that $x > 0$": a goal, not yet proved.
> "Hence $x > 0$": a conclusion from the lines before.

Each reading asks the reader for a different check.
In general, the words of a proof sort its sentences into new objects, assumptions, goals and conclusions, and a second group of phrases, the signposts, shows the plan: "there are two cases", "first", "conversely", "it remains to show".

## Motivation

A reader can check a line only after knowing its role.
A conclusion needs a reason, an assumption needs none but must be closed, and a new object needs a reason only when its existence is claimed.
Variables show the same problem.
In "$n = 2k$", the letter $k$ may be a number fixed earlier or a new integer that a definition provides.
The sentence "since $n$ is even, there is an integer $k$ with $n = 2k$" says which reading is meant, and it gives the reason for the existence of $k$.

Mathematical English has a fixed vocabulary for these roles, and the [[language of mathematics|661V0DH7V3]] uses it the same way in every field.
The same words return in every later method: [[writing proofs|8JQHJK94RZ]] uses them in every sentence, and [[structured proofs|H2W8D7BMSW]] turn the scope of each "let" and "suppose" into numbered levels.

## Notation

Some texts use symbols for the conclusion words: $\therefore$ for "therefore", $\because$ for "because", and $\Rightarrow$ for "hence".
Many style guides advise words in a final proof, because $\Rightarrow$ also means the [[conditional|FA6YZGR2SS]] "implies", and a reader cannot tell a deduction from an implication.
Short forms such as "iff", "WLOG" and "s.t." are on the page [[mathematical abbreviations|4ZNYMYRRY3]], and the end marks $\square$ and Q.E.D. are on the page [[end of proof marks|ET9J6R9T5C]].

## Remarks

### The words by role

| Role | Typical words | What the reader checks |
|---|---|---|
| arbitrary object | "let $x$ be a real number", "fix $\varepsilon > 0$" | nothing yet; later, that no special property of $x$ was used |
| name for a known object | "put $m = a + b$", "write $d$ for $\gcd(a, b)$" | nothing, since a name proves nothing |
| object known to exist | "choose $k$ with $n = 2k$", "there is an integer $k$ with" | the reason that such an object exists |
| assumption | "suppose that", "assume, for a contradiction, that" | that it is closed later |
| conclusion | "hence", "so", "thus", "it follows from (2) that" | that it follows from the lines named |
| reason first | "since $a \mid b$ and $b \mid c$, we get" | the reason, then the step |
| goal | "we claim that", "we show that", "it suffices to show that" | after "it suffices", that the new goal implies the old one |
| closing | "this proves the claim", "as required" | that the last line matches the announced goal |

"Fix" differs from "let" only in emphasis: it says that the object stays the same while other objects vary, as $\varepsilon$ does in an [[epsilon-delta proof|RXG5JTZ2PZ]].

### Two proofs read word by word

[[The language of a proof that the square of an odd integer is odd|7CFTMSRX3R]] tags every line of a short direct proof.
"Let" brings in $n$, "suppose" opens "$n$ is odd", "there is" produces $k$ with its reason, "put" names $m$, and "hence" closes the assumption.

[[A proof with "fix" and "we claim"|ZF4QJ8ATXX]] has a claim with its own proof inside the main proof.
The words "we claim" and "this proves the claim" mark the borders of the inner level, and "there are three cases" tells the reader to count to three.

### Signposts

Signposts describe the structure of the proof, not its mathematics: "the proof has two steps", "we consider two cases", "first we show uniqueness", "conversely".
A signpost costs one line and tells the reader where each part begins and ends.
They matter most in long proofs, in [[proofs by cases|0WCP0PVET6]], and in proofs of "if and only if", which have two directions.

### Tense, person and voice

Mathematical facts are stated in the present tense ("the sum is even"), because they do not change with time.
The future is for the plan ("we will show that $f$ is injective"), and the past is for earlier parts ("we proved in Lemma 2 that").

Most mathematical texts use "we", read as the writer and the reader following the argument together.
Here the authors of advice differ, so treat the choice as a matter of taste and of the custom of a journal, not of logic.
Some single authors write "I", some keep "we" in every text, and some prefer impersonal forms such as "it follows that".
Many guides prefer the active voice ("we prove") to the passive ("it is proved"), because the active voice says who does what.

### When the words are wrong

[[A column of formulas without proof words|T1R6KAM4CX]] is correct line by line, but the reader cannot tell which line is assumed and which is derived.
A column of the same shape "proves" the false claim that $a \mid bc$ implies $a \mid b$, so the shape alone cannot be trusted.

"Let $x$ be the largest prime" uses "let" for an object that does not exist, so the sentence names nothing.
A "let" with a description needs a proof that the object exists, as in [[existence and uniqueness statements|ACSC75R7R5]].
"$n^2$ is even, hence $n$ is even" uses "hence" for a step that needs its own argument, for example by the [[contrapositive|0BB5TPGQ1N]].

### Watch out

The most common slip is "let" where "there is" belongs.
Proving that $a \mid b$ and $b \mid c$ give $a \mid c$, a student writes "let $b = ak$".
That sentence defines $b$, but $b$ was already given, so the step changes the meaning of $b$ instead of using the hypothesis.
The correct sentence is "since $a \mid b$, there is an integer $k$ with $b = ak$".

A second slip is a "suppose" that is never closed.
The last line then holds only under that assumption, and the theorem is not proved.

### History

Greek geometric texts such as [[Euclid's Elements|83WHDAV68J]] used fixed phrases for the parts of a proposition.
The Latin "quod erat demonstrandum", shortened to Q.E.D., translates the Greek closing phrase "which was to be shown".
Halmos's essay of 1970 and the notes of Knuth, Larrabee and Roberts (1989) both give advice on the words of mathematical prose.

### Try it

Which word fits: "\_\_\_ $n$ be an integer, and \_\_\_ that $n^2$ is odd; we show that $n$ is odd"?
"Let" introduces the arbitrary $n$, and "suppose" opens the assumption.

What is wrong with "Choose $\varepsilon = 1$" as the first line of a proof that a limit holds?
The goal "for every $\varepsilon > 0$" needs an arbitrary $\varepsilon$, so the line should read "Let $\varepsilon > 0$".

## Explanations

### L1 human

A proof is like a set of instructions that a reader follows step by step.
Some small words tell the reader what each step does.
"Let" says that a new object enters, for example "let $n$ be any whole number".
"Suppose" says that something is assumed for the moment, for example "suppose $n$ is odd".
"So" or "hence" says that a new fact follows from the facts before it.
Without these words, a list such as "$n = 7$, $n^2 = 49$, $49$ is odd" does not show what was given and what was found.

### L2 human

We write a proof that if $a \mid b$ and $b \mid c$, then $a \mid c$, and we name the role of each word.
Here $a \mid b$ means that $b = ak$ for some integer $k$, by the definition of [[divisibility|0PG2H7WKGG]].

> Let $a$, $b$ and $c$ be integers.
> Suppose that $a \mid b$ and $b \mid c$.
> By the definition of divisibility, there are integers $k$ and $l$ with $b = ak$ and $c = bl$.
> Then $c = bl = (ak)l = a(kl)$.
> Since $kl$ is an integer, $a \mid c$.
> $\square$

"Let" makes $a$, $b$ and $c$ arbitrary, so the result holds for all integers.
"Suppose" opens the hypothesis, and "there are" produces $k$ and $l$ with the definition as the reason.
"Then" marks a calculation, and "since" gives the reason first and closes the assumption.

Check: $a = 2$, $b = 6$ and $c = 18$ give $k = 3$, $l = 3$ and $c = 2 \cdot 9$.
Each line is now a new object, an assumption, or a conclusion with its reason, and the reader never has to guess which.

### L3 human

The proof words are the surface form of a deduction system for first-order logic.
"Let" and "fix" open the scope of a universally quantified variable, "suppose" adds a hypothesis to the context, "choose" eliminates an existential quantifier, and "hence" applies a rule.
In the Fitch-style presentation of [[natural deduction|6KT3BJZ7D1]], an assumption opens an indented sub-proof, and the end of the sub-proof closes it.

The tactics of a proof assistant carry the same structure.
In Lean, `intro` plays the part of "let" or "suppose", `obtain` of "choose", `use` of "take", and `have` of "we claim".
[[Structured proofs|H2W8D7BMSW]] make the scope of each "let" and "suppose" visible with levels, and [[mathematical writing style|D5YPYTQ88G]] treats the sentences around the formulas.
