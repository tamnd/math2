---
tag: XZHACQ74C0
kind: concept
name: Structure of a mathematical paper
aliases: [structure-of-a-mathematical-paper]
msc: ["00A35"]
topics: [STSM6PR7TX]
audience: grad
uses: [KK5F0F03ZW, D5YPYTQ88G, 8JQHJK94RZ]
sources:
  - url: https://en.wikipedia.org/wiki/Theorem
    locator: Layout
  - url: https://en.wikipedia.org/wiki/Abstract_(summary)
    locator: Structure
  - url: https://en.wikipedia.org/wiki/IMRAD
    locator: Overview
  - url: https://en.wikipedia.org/wiki/Mathematics_Subject_Classification
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Academic_publishing
    locator: lead section
---

## Summary

A mathematical paper is built so that a reader can stop early and still learn the main result.
Compare two abstracts for the same short note.

> We prove Theorem 1 using Lemma 3 and the method of [7].

> We give a short proof that for every integer $n \ge 1$ there is a prime $p$ with $n < p \le 2n$.
> The proof compares upper and lower bounds for the binomial coefficient $\binom{2n}{n}$.

The first abstract makes no sense alone, since its reader sees neither Theorem 1 nor Lemma 3 nor reference [7].
The second states the result in full and names the method, so a reader learns in ten seconds whether to read on.

The same idea shapes the whole paper.
After the title and the abstract come the subject codes and keywords, an introduction that states the main results, a section of preliminaries, the sections with the proofs, and the references.
Inside, the results are labeled as theorems, lemmas, propositions, corollaries and definitions, and they are numbered so that a later proof can cite an earlier result.
The structure is a convention, not a rule, and it varies with the field, the journal and the author.

## Motivation

A paper serves readers with different aims.
A reader in a search wants to know in one minute whether the paper is relevant.
A reader in the field wants the exact main results and their relation to earlier work.
A reader who needs one lemma wants to find it and its hypotheses without reading the rest.
A referee wants to check each proof, as in [[checking a proof|4M98ZZNK0E]].
The parts of a paper answer these needs in order: the title and the abstract serve the first reader, the introduction the second, and the numbered results and proofs the last two.
Readers of papers seldom read from the first page to the last, and the structure lets them skip safely.

## Notation

A result is cited by its label and number, for example "Lemma 3.2", and a numbered display by its number, as in "by (2.5)".
With numbering within sections, "Theorem 2.3" is the third numbered item of Section 2.
Some authors label the main results of the introduction with letters, "Theorem A" and "Theorem B", to separate them from the numbered results of the body.

Subject codes come from the Mathematics Subject Classification, whose current version is MSC2020.
A code such as 11A41 has two digits for the area, here number theory, a letter for the subarea, and two digits for the topic, here primes.

## Remarks

### The parts of a paper

The parts of a typical paper, in order, are these.

- The title names the main object or result in words that a reader would search for, and many authors avoid symbols in it, since symbols are hard to search.
- The abstract states the main results in a few sentences.
  It must make sense alone, because databases show it without the paper, and many journals advise against citations and undefined notation in it.
- Many mathematics journals ask for subject codes and a few keywords, which databases use to index the paper.
- The introduction gives the background, states the main theorems in full, compares them with earlier results, and often ends with an outline.
- The preliminaries fix the notation, recall definitions, and state known results with references, often without proof.
- The body proves the main results, usually through a sequence of lemmas and propositions, and a long technical proof can move to an appendix.
- The acknowledgments thank colleagues, referees and funding bodies.
- The references give each cited work in full, with numbered citations such as [12] or with author and year.

### Numbering of results

With a shared counter, all theorems, lemmas, propositions, corollaries and definitions use one sequence: Lemma 2.1, Definition 2.2, Theorem 2.3.
A reader can then find "2.3" by its number alone.
With separate counters, each label has its own sequence, such as Lemma 1, Lemma 2 and Theorem 1, and a reader must search for the label and the number together.
Authors differ here, but in a long paper the shared counter is easier to navigate.

Many authors number within sections, so that a number also says where the result is, while a short note often numbers from $1$ on without sections.
Only the results and displays that are cited later need numbers.
A typesetting system such as LaTeX, described in [[mathematical typesetting|Y65B4RR53C]], assigns the numbers and the cross-references automatically.
The labels themselves signal the role of each result, as [[theorems, lemmas, corollaries and propositions|KK5F0F03ZW]] explains.

### Mathematics papers and IMRAD

Papers in the experimental sciences often follow the IMRAD pattern: introduction, methods, results, and discussion.
Mathematics papers usually do not use these headings.
A result and its proof form one unit, so the proof is not a separate "methods" section, and the results are stated in the introduction and proved in the body.
Some papers in applied mathematics and statistics, with numerical experiments, use a structure closer to IMRAD.

### Some typical shapes

A paper in combinatorics may state "Theorem A" and "Theorem B" in its introduction and prove them as Theorem 4.1 and Theorem 5.3, and then the introduction should say where each is proved.
A short note may have no sections, number its results Lemma 1, Lemma 2 and Theorem 3 with a shared counter, and end with a numbered list of references.
A paper with a long computation may state its main theorem in Section 3 and move the computation to an appendix, citing it as "Lemma A.2".

Two shapes fail.
An introduction that says "we prove a result on primes" without stating it forces the reader through the whole paper to learn the claim.
A paper that gives the proofs in the order the author found them, with false starts, is a research notebook, because the order of presentation differs from the order of discovery, as [[scratch work and the final proof|E97XXFW9MV]] explains.

### Basic properties

The main results appear at least twice: as statements in the introduction, and with proofs in the body.
The two statements must agree exactly.
Each result is cited only after it is stated, or with a forward reference that says where it is proved, and a forward reference must not hide a circular argument.
Each piece of notation is fixed once, usually in the preliminaries, and used the same way throughout, as [[mathematical writing style|D5YPYTQ88G]] advises.
The length and detail of the proofs depend on the readers of the journal, as discussed in [[level of detail in proofs|VYGBV5D8Y4]].

### Watch out

A common trap is a main theorem stated only in the body, after twenty pages of lemmas, so that no reader can judge the paper from its introduction.
Another is a statement in the introduction that drops a hypothesis of the version proved later, often because the writer simplified it for readability.

Numbering every display, or using separate counters for lemmas, theorems and definitions in a long paper, makes cross-references hard to follow.
New results do not belong in the preliminaries, and known results there need references, not long proofs.

### History

The pattern of definitions, statements and proofs goes back to [[Euclid's Elements|83WHDAV68J]].
The Mathematics Subject Classification is maintained by the two main reviewing databases, Mathematical Reviews and zbMATH, and its current version is MSC2020.
Many journals today publish LaTeX style files that fix the layout and the numbering of results.

### Try it

Rewrite the abstract "In this paper we prove Theorem 2 by the method of Section 4" so that it makes sense alone, for a paper that proves that every finite group of prime order is cyclic.
One answer is "We show that every finite group of prime order is cyclic, using Lagrange's theorem".

A paper numbers Lemma 1, Lemma 2, Definition 1, Theorem 1 and Lemma 3 with separate counters.
Renumber them with one counter in Section 2.
The answer is 2.1, 2.2, 2.3, 2.4 and 2.5.

## Explanations

### L1 human

A research paper in mathematics is a report of new results with their proofs.
It starts with a title and a short summary, called the abstract.
Then the introduction says what the new results are and why they are interesting.
After that come the proofs, broken into small numbered steps called lemmas.
At the end is a list of the other papers that the authors used.
Numbers such as "Lemma 2.3" work like house numbers: they let a reader find each result quickly.

### L2 human

We plan a short paper that proves one new theorem with two lemmas.

1. The title names the result in searchable words.
2. The abstract states the theorem in words in two to four sentences, with no citations.
3. Section 1 states the theorem as Theorem 1.1, compares it with the best earlier result, and gives an outline.
4. Section 2 fixes the notation and recalls known results with references.
5. Section 3 proves Lemma 3.1 and Lemma 3.2, and Section 4 proves Theorem 1.1, citing both lemmas by number.
6. The paper ends with the acknowledgments and the references.

This plan suits a first paper or a thesis chapter, where the order of sections is decided before the writing starts.
Watch out: Theorem 1.1 in Section 1 and its proved form in Section 4 must be compared word for word, since a dropped hypothesis in the introduction makes the stated theorem false.

### L3 human

The structure of a paper is the large-scale form of the advice on [[writing proofs|8JQHJK94RZ]]: state the goal first, give each step with its reason, and guide the reader through the structure.
A paper is a hierarchy of claims, as in a [[structured proof|H2W8D7BMSW]].
The main theorem is the root, the lemmas are its children, and each proof cites only results earlier in the order.
A monograph and a thesis extend the pattern with chapters, and a survey replaces most proofs by references.
A library of formal proofs for a proof assistant takes the hierarchy literally: each result is a named declaration, and its proof cites earlier declarations by name instead of by number.
The conventions of journals, peer review and preprints belong to [[publishing and peer review|A6ZGR8NM3S]].
