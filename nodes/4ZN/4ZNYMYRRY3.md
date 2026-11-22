---
tag: 4ZNYMYRRY3
kind: concept
name: Mathematical abbreviations
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: school
uses: [QKEX4PD029, 0S6GMNJ62Y]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_mathematical_abbreviations
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Proof terminology
---

## Summary

A lecture note about an integer $n$ may say: "$n^2$ is even `iff` $n$ is even, `i.e.` `iff` $2 \mid n$."
Two short forms carry the logic of that sentence.
`iff` stands for "if and only if", so the sentence claims two implications, and `i.e.` stands for "that is", so the last part only restates "even" in other words.
Mathematical writing is full of such short forms, and each one has a fixed expansion that changes what the sentence claims.

A *mathematical abbreviation* is a short written form of a word or a phrase that occurs often in mathematical text, such as `iff` for "if and only if" or `wlog` for "without loss of generality".
Some come from English and some from Latin phrases that scholarly writing kept.
To read a sentence that contains one, replace the abbreviation by its full form, and read the logic of the full sentence.

## Motivation

Proofs repeat a small set of phrases many times: "if and only if", "such that", "the left-hand side", "the following are equivalent".
On a blackboard or in quick notes, writers shorten them, and the short forms became a common code.
You will meet the code in your first lecture, usually without a definition.
If you misread it, you misread the proof: `i.e.` and `e.g.` look alike, but one claims an equivalence and the other gives a single case.
The abbreviations also connect to the methods of proof, because `iff` and `TFAE` tell you what you must prove, as [[proving biconditionals and equivalences|TFQ1845T84]] explains.

## Notation

The common abbreviations and their full forms are these.

| Abbreviation | Full form | Use |
|---|---|---|
| `iff` | if and only if | joins two equivalent statements: the [[biconditional|0S6GMNJ62Y]] |
| `wlog`, `WLOG` | without loss of generality | adds an assumption that a symmetry or a relabeling makes harmless |
| `TFAE` | the following are equivalent | starts a list of statements that are pairwise equivalent |
| `s.t.` | such that; in optimization, subject to | introduces a condition |
| `resp.` | respectively | pairs two lists in order: "$A$ (resp. $B$)" |
| `i.e.` | that is (Latin "id est") | restates the same thing in other words |
| `e.g.` | for example (Latin "exempli gratia") | gives one case among others |
| `cf.` | compare (Latin "confer") | sends the reader to a related source |
| `viz.` | namely (Latin "videlicet") | gives the exact item or the full list |
| `et al.` | and others (Latin "et alii") | shortens a list of authors |
| `LHS`, `RHS` | left-hand side, right-hand side | the two sides of an equation or inequality |
| `NTS`, `WTS` | need to show, want to show | states the goal of a proof or a step |
| `a.e.` | almost everywhere | true outside a set of measure zero |
| `a.s.` | almost surely | true with probability $1$ |
| `w.r.t.` | with respect to | names the variable or the structure in use |
| `Q.E.D.` | which was to be shown (Latin "quod erat demonstrandum") | marks the end of a proof |

The site writes the full phrases in its own text, and it keeps `iff` only in the names of statements, where space is short.

## Remarks

### Expanding the opening sentence

Replace each short form in "$n^2$ is even `iff` $n$ is even, `i.e.` `iff` $2 \mid n$" by its full form.
You get two implications and one restatement:
$$n \text{ even} \Rightarrow n^2 \text{ even}, \qquad n^2 \text{ even} \Rightarrow n \text{ even}, \qquad n \text{ even} \Leftrightarrow 2 \mid n.$$
The third part is the definition of "even", so `i.e.` is used correctly.
The first two parts each need a proof.
For the first, $n = 2k$ gives $n^2 = 2(2k^2)$.
For the second, prove the contrapositive: $n = 2k + 1$ gives $n^2 = 2(2k^2 + 2k) + 1$, which is odd.
[[A sentence with the abbreviations s.t., wlog and iff|K35RJ9YHC0]] expands a longer argument in the same way, and [[the abbreviations LHS, RHS and NTS in the proof of an identity|Z2HAC8J58R]] shows the names of the two sides at work.

### The abbreviations that carry logic

Some short forms are only shorthand, such as `et al.` and `w.r.t.`.
Others make a claim that you must check.
`iff` claims two implications, and a proof of "$P$ `iff` $Q$" proves $P \Rightarrow Q$ and $Q \Rightarrow P$.
`TFAE` with three statements (a), (b), (c) claims that each pair is equivalent, and the cycle (a) $\Rightarrow$ (b) $\Rightarrow$ (c) $\Rightarrow$ (a) proves all of it, because implication is transitive.
`wlog` claims that the omitted cases follow from the chosen one, usually by a symmetry, and [[without loss of generality|Y7NE0E6PCV]] gives the check.

For example, "the functions $\sin$ and $\cos$ are odd and even, `resp.`" means that $\sin$ is odd and $\cos$ is even.
Check: $\sin(-x) = -\sin x$ and $\cos(-x) = \cos x$.

### Two readings of one short form

A few abbreviations have two common expansions, and the field tells you which one the author uses.

The first is `s.t.`.
In a proof, "choose $N$ `s.t.` $1/N < \varepsilon$" reads "such that".
In optimization, "minimize $x^2 + y^2$ `s.t.` $x + y = 1$" reads "subject to", and the condition is a constraint on the search.
Both readings introduce a condition, so the logic is the same, but only the second sets up a problem to solve.

The second is "almost".
In measure theory, `a.e.` means outside a set of measure zero: "$f = 0$ `a.e.`" holds for the function that is $1$ on $\mathbb{Q}$ and $0$ elsewhere, because $\mathbb{Q}$ has measure zero.
In number theory, "almost all $n$" means all but finitely many $n$ in some texts and a set of density one in others.
[[Almost everywhere|RARTMA0ZEC]] gives the measure sense, and [[almost all, generic and in general|N1XSAXCQY3]] compares all three; a careful text says which one it uses.

### What is not an abbreviation

The sign $\Leftrightarrow$ is not an abbreviation of a word.
It is a logical symbol with the same meaning as `iff`, and it belongs in formulas, not in running prose.
A jargon word such as "nice" is not an abbreviation either, because it has no fixed expansion, as [[mathematical jargon|4M1FGQ0HNZ]] explains.

A short form used with the wrong expansion fails too.
[[The sentence "n is even, i.e. n = 4" misuses i.e.|PQ28MSV5XQ]] shows `i.e.` where `e.g.` was meant: $6$ is even and $6 \neq 4$.
In the same way, "let $x \geq 0$, `wlog`" is not a valid use when the claim is $x^3 \geq 0$, because the claim fails at $x = -1$ and no symmetry links the two signs.

### Watch out

`i.e.` and `e.g.` differ in logic, not in style.
"The primes below $6$, `i.e.` $2$, $3$ and $5$" is correct, because the list is complete.
"The primes, `i.e.` $2$, $3$ and $5$" is false, because $7$ is prime too; the writer meant `e.g.`.
After `i.e.` you may replace the first part by the second in every later step, and after `e.g.` you may not.

Second, `iff` in a theorem needs both directions.
A definition written with "if" is read as "if and only if", but a theorem stated with `iff` is false when only one direction holds.

### History

The short forms `i.e.`, `e.g.`, `cf.` and `viz.` come from Latin, the common written language of European scholars for centuries.
`Q.E.D.` is the Latin translation of the Greek phrase with which Euclid closed his proofs, as [[Q.E.D. and end of proof marks|ET9J6R9T5C]] explains.
Paul Halmos is credited with the abbreviation `iff`.

### Try it

First, expand "TFAE for a finite group $G$: (a) $G$ is cyclic; (b) $G$ has an element of order $\lvert G \rvert$" and say what a proof must show.
It means "the following are equivalent", so a proof must show (a) $\Rightarrow$ (b) and (b) $\Rightarrow$ (a).

Second, decide whether "$n$ is divisible by $4$, `i.e.` $n$ is even" is correct.
It is not, because $n = 2$ is even and not divisible by $4$; the second part is a consequence, not a restatement.

## Explanations

### L1 human

Mathematicians write some phrases so often that they shorten them.
`iff` means "if and only if", and `s.t.` means "such that".
To read a sentence with a short form, replace it by the full phrase.
"A whole number is even `iff` its last digit is even" means "a whole number is even if and only if its last digit is even".
So $34$ is even because its last digit $4$ is even, and $37$ is not even because $7$ is odd.

### L2 human

A proof in lecture shorthand starts with three short sentences.
The first is "let $n \in \mathbb{Z}$ `s.t.` $n^2$ is odd", the second is "`NTS` $n$ is odd", and the third is "suppose not, `i.e.` $n$ is even".
Expand them one short form at a time.
`s.t.` gives "let $n$ be an integer such that $n^2$ is odd", and `NTS` gives "we need to show that $n$ is odd".
"Suppose not, `i.e.` $n$ is even" gives "suppose $n$ is not odd, that is, $n$ is even", and this `i.e.` is correct, because an integer that is not odd is even.
Then $n = 2k$ for an integer $k$, and
$$n^2 = 4k^2 = 2(2k^2),$$
so $n^2$ is even, which contradicts the hypothesis.
So $n$ is odd.
If the writer had put "suppose not, `i.e.` $n = 2$", the proof would cover one even number only, and this is the usual way that a misused `i.e.` breaks a proof.

### L3 human

Abbreviations are a fixed, small part of the controlled language of mathematics.
Each one stands for a connective or a marker of discourse: `iff` is the biconditional, `TFAE` is a family of biconditionals, `s.t.` introduces a bounded quantifier, and `wlog` records a reduction by a symmetry that acts on the cases.
In Lean's Mathlib, the tactic `wlog` proves a goal from one case together with a proof that the other cases reduce to it.
The measure-theoretic `a.e.` and the probabilistic `a.s.` are filter quantifiers: a property holds when the set where it fails lies in the ideal of null sets, a pattern that [[sufficiently large, eventually and frequently|FEQ7WATMHF]] shows for the filter of large numbers.
[[Mathematical jargon|4M1FGQ0HNZ]] and [[trivial, obvious and clearly|Y0HXCJRB9B]] treat the informal words that play a similar role but have no fixed expansion.
