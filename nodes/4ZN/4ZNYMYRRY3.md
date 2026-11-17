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

A mathematical abbreviation is a short written form of a word or a phrase that occurs often in mathematical text, such as `iff` for "if and only if" or `wlog` for "without loss of generality".
Some abbreviations come from English, and some come from Latin phrases that English writing kept.
Each abbreviation has one fixed expansion, and a reader must replace it by that expansion to read the sentence correctly.
Abbreviations matter because they appear in almost every lecture, proof and paper, and a misread abbreviation changes the logic of a sentence.

## Motivation

Mathematical writing repeats a small set of phrases many times: "if and only if", "such that", "the left-hand side", "the following are equivalent".
On a blackboard or in a note, writers shorten these phrases to save time and space.
The short forms became a common code among mathematicians.
A student who does not know the code cannot follow a proof, and a student who uses it wrongly writes false sentences.
So this page lists the common abbreviations, gives the full form of each, and shows how each one changes the logic of a sentence.

## Notation

The table gives each abbreviation, its full form, and its use.

| Abbreviation | Full form | Use |
|---|---|---|
| `iff` | if and only if | joins two statements that are equivalent: the [[biconditional|0S6GMNJ62Y]] |
| `wlog`, `WLOG` | without loss of generality | adds an assumption that covers all cases by a symmetry or a relabelling |
| `TFAE` | the following are equivalent | starts a list of statements that are all equivalent to each other |
| `s.t.` | such that | introduces the condition on an object |
| `resp.` | respectively | pairs two lists in order: "$A$ (resp. $B$)" |
| `i.e.` | that is (Latin "id est") | restates the same thing in other words |
| `e.g.` | for example (Latin "exempli gratia") | gives one instance among others |
| `cf.` | compare (Latin "confer") | sends the reader to a related source |
| `viz.` | namely (Latin "videlicet") | gives the complete list or the exact item |
| `et al.` | and others (Latin "et alii") | shortens a list of authors |
| `LHS`, `RHS` | left-hand side, right-hand side | the two sides of an equation or an inequality |
| `NTS`, `WTS` | need to show, want to show | states the goal of a proof or a step |
| `a.e.` | almost everywhere | true outside a set of measure zero |
| `a.s.` | almost surely | true with probability $1$ |
| `w.r.t.` | with respect to | names the variable or the structure that is used |
| `Q.E.D.` | which was to be shown (Latin "quod erat demonstrandum") | marks the end of a proof |

The site spells out the full phrase in its own pages.
It keeps `iff` only in the names of statements, where space is short.

## Remarks

### Examples

1. [[A sentence with the abbreviations s.t., wlog and iff|K35RJ9YHC0]] expands to a correct argument when each abbreviation is replaced by its full form.
2. [[The abbreviations LHS, RHS and NTS in the proof of an identity|Z2HAC8J58R]] organise a proof of $(a + b)^2 - (a - b)^2 = 4ab$.
3. "TFAE for a finite group $G$: (a) $G$ is cyclic; (b) $G$ has an element of order $\lvert G \rvert$." This states (a) $\Rightarrow$ (b) and (b) $\Rightarrow$ (a), and both directions need a proof.
4. "The functions $\sin$ and $\cos$ are odd and even, resp." This means that $\sin$ is odd and $\cos$ is even.
5. "Let $f$ be continuous, e.g. $f(x) = x^2$." The function $x^2$ is one continuous function among many.

### Non-examples

1. [[The sentence "n is even, i.e. n = 4" misuses i.e.|PQ28MSV5XQ]]. The abbreviation `i.e.` claims that the two parts say the same thing, but $6$ is even and $6 \neq 4$.
2. "Let $x \geq 0$, `wlog`." This is not a valid use when the claim to be proved is not symmetric under $x \mapsto -x$. For example, the claim $x^3 \geq 0$ is true for $x \geq 0$ and false for $x = -1$.
3. The symbol $\Leftrightarrow$ is not an abbreviation of a word. It is a logical symbol with the same meaning as `iff`, and it belongs in formulas, not in prose.

### Basic properties

1. Each abbreviation has one expansion. A sentence with an abbreviation is true exactly when the sentence with the full form is true.
2. `iff` gives two implications. To prove "$P$ iff $Q$" we prove $P \Rightarrow Q$ and $Q \Rightarrow P$.
3. `TFAE` with $k$ statements needs a cycle of implications. For three statements, the cycle (a) $\Rightarrow$ (b) $\Rightarrow$ (c) $\Rightarrow$ (a) is enough, because implication is transitive.
4. `wlog` needs a reason. The writer must check that the other cases follow from the chosen case, for example by a symmetry of the hypotheses and the conclusion.
5. `i.e.` and `e.g.` differ in logic. After `i.e.` comes an equivalent restatement, and after `e.g.` comes one instance.
6. `a.e.` and `a.s.` depend on a measure: [[almost everywhere|RARTMA0ZEC]] means outside a set of measure zero. The page on [[almost all and generic|N1XSAXCQY3]] compares this with other meanings of "almost all".

### History

The abbreviations `i.e.`, `e.g.`, `cf.` and `viz.` come from Latin, which was the common language of scholars in Europe for centuries.
The abbreviation `Q.E.D.` translates the Greek phrase that Euclid used at the end of his proofs; see [[Q.E.D. and end of proof marks|ET9J6R9T5C]].
Paul Halmos is credited with the abbreviation `iff`.

### Common errors

1. A student writes `i.e.` where `e.g.` is meant. "Primes, i.e. 2, 3 and 5" says that 2, 3 and 5 are all the primes, which is false.
2. A student uses `iff` in a definition and then proves only one direction of a theorem that is stated with `iff`. Both directions are needed in a theorem.
3. A student writes `wlog` without a symmetry that justifies it. The proof then covers only one case.

## Explanations

### L1 human

Mathematicians write some phrases so often that they shorten them.
For example, `iff` means "if and only if", and `s.t.` means "such that".
To read a sentence with an abbreviation, replace the short form by the full phrase.
The sentence "a whole number is even iff its last digit is even" means "a whole number is even if and only if its last digit is even".
So $34$ is even because its last digit $4$ is even, and $37$ is not even because $7$ is not even.

### L2 human

We expand and check a short proof written with abbreviations.
It has three parts: "Let $n \in \mathbb{Z}$ `s.t.` $n^2$ is odd", then "`NTS`: $n$ is odd", then "Suppose not, `i.e.` $n$ is even".

1. `s.t.` becomes "such that": we take an integer $n$ such that $n^2$ is odd.
2. `NTS` becomes "we need to show": the goal is that $n$ is odd.
3. "Suppose not, `i.e.` $n$ is even" becomes "suppose that $n$ is not odd, that is, $n$ is even". This is correct, because an integer that is not odd is even, so the two phrases say the same thing.
4. Then $n = 2k$ for an integer $k$, so $n^2 = 4k^2 = 2(2k^2)$ is even.
5. This contradicts the hypothesis that $n^2$ is odd, so $n$ is odd.

The typical use of abbreviations is in notes, on the board, and in quick written arguments.
A trap: `i.e.` must join two statements that are equivalent.
If the writer had written "suppose not, `i.e.` $n = 2$", the proof would cover only one even number.

### L3 human

Abbreviations are a small, fixed part of the controlled language of mathematics.
Each one stands for a logical connective or a discourse marker: `iff` is the biconditional, `TFAE` is a family of biconditionals, `s.t.` introduces a bounded quantifier, and `wlog` records a reduction by a symmetry group acting on the cases.
In formal systems, `wlog` corresponds to a tactic that proves a goal from one case and a symmetry lemma; Lean's Mathlib has such a tactic, `wlog`.
The measure-theoretic `a.e.` and the probabilistic `a.s.` are filter quantifiers: they say that a property holds on a set whose complement is in the null ideal.
The pages on [[mathematical jargon|4M1FGQ0HNZ]] and on [[trivial, obvious and clearly|Y0HXCJRB9B]] treat the informal words that are not abbreviations but play a similar role.
