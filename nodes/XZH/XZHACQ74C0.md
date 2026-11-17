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

A research paper in mathematics usually starts with a title, an abstract, subject codes and keywords.
Then come an introduction that states the main results, a section of preliminaries, the sections with the proofs, and a list of references.
The results inside the paper are labelled as theorems, lemmas, propositions, corollaries and definitions.
They are numbered so that a later proof can cite an earlier result.
The structure is a convention, not a rule, and it varies with the field, the journal and the author.
It matters because readers of papers seldom read from the first page to the last.
They read the abstract, then the main theorems, and then only the proofs that they need, and the structure lets them do this.

## Motivation

A paper must serve readers with different aims.
A reader in a search wants to know in one minute if the paper is relevant.
A reader in the field wants the exact main results and their relation to earlier work.
A reader who uses one lemma wants to find it and its hypotheses without the rest of the paper.
A referee wants to check each proof, as on the page [[checking a proof|4M98ZZNK0E]].
The standard parts of a paper answer these needs in order.
The title and the abstract serve the first reader, the introduction the second, and the numbered results and proofs the last two.

## Notation

1. A result is cited by its label and number, for example "Lemma 3.2" or "by (2.5)" for a numbered display.
2. With numbering within sections, "Theorem 2.3" is the third numbered item of Section 2.
3. The main results of the introduction are sometimes labelled with letters, "Theorem A" and "Theorem B". This separates them from the numbered results of the body.
4. Subject codes come from the Mathematics Subject Classification, in its current version MSC2020. A code such as 11A41 has two digits for the area, a letter for the subarea, and two digits for the topic.

## Remarks

### The parts of a paper

1. Title. It names the main object or result, in words that a reader would search for. Symbols in a title are hard to search, so many authors avoid them.
2. Abstract. It states the main results in a few sentences, and it must make sense alone, because databases show it without the paper. Many journals advise against citations and undefined notation in the abstract.
3. Subject codes and keywords. Many mathematics journals ask authors to list codes from the Mathematics Subject Classification and a few keywords, which databases use to index the paper.
4. Introduction. It gives the background, states the main theorems in full, compares them with earlier results, and often ends with an outline of the paper.
5. Preliminaries. This section fixes the notation, recalls the definitions, and states known results with references, often without proof.
6. Body. The sections of the body prove the main results, usually through a sequence of lemmas and propositions. A long technical proof can move to an appendix.
7. Acknowledgements. They thank colleagues, referees and funding bodies.
8. References. The list gives each cited work in full. Journals use either numbered citations such as [12] or author and year citations.

### Numbering of results

1. With a shared counter, all theorems, lemmas, propositions, corollaries and definitions use one sequence: Lemma 2.1, Definition 2.2, Theorem 2.3. A reader can find "2.3" by its number alone.
2. With separate counters, each label has its own sequence: Lemma 1, Lemma 2, Theorem 1. A reader must then search for the label and the number together.
3. Many authors number within sections, so that a number also says where the result is. Short papers often number results from $1$ on without sections.
4. Only the results and displays that a later part of the paper cites need numbers. A typesetting system such as LaTeX, as described on the page [[mathematical typesetting|Y65B4RR53C]], assigns the numbers and the cross-references automatically.
5. The labels themselves signal the role of each result, as the page [[theorems, lemmas, corollaries and propositions|KK5F0F03ZW]] explains.

### Mathematics papers and IMRAD

Papers in the experimental sciences often follow the IMRAD pattern: introduction, methods, results, and discussion.
Mathematics papers usually do not use these headings.
A mathematical result and its proof form one unit, so the proof is not a separate "methods" section.
The "results" are stated in the introduction and proved in the body.
Some papers in applied mathematics and statistics, with numerical experiments, use a structure closer to IMRAD.

### Examples

1. A typical paper in number theory might have the title "Primes in short intervals" and an abstract of four sentences that states the main bound. Its subject code is 11N05, for the distribution of primes. Its introduction states Theorem 1.1, and Section 2 recalls the needed estimates.
2. A paper in combinatorics states "Theorem A" and "Theorem B" in its introduction, and proves them as Theorem 4.1 and Theorem 5.3. The introduction says where each main theorem is proved.
3. A short note has no sections, and numbers its results Lemma 1, Lemma 2 and Theorem 3 with a shared counter. It gives the references in a numbered list.
4. A paper with a long computation states the main theorem in Section 3 and moves the computation to an appendix. The proof cites the appendix result as "Lemma A.2".

### Non-examples

1. A paper whose introduction says "we prove a result on primes" but never states the result fails the role of the introduction. A reader must read the whole paper to learn the claim.
2. A paper that writes the proofs in the order in which the author found them, with false starts, is a research notebook, not a paper. The order of presentation differs from the order of discovery, as the page [[scratch work and the final proof|E97XXFW9MV]] explains.
3. An abstract that says "We prove Theorem 1 using Lemma 3" makes no sense alone. The reader of the abstract does not see the theorem or the lemma.

### Basic properties

1. The main results appear at least twice: in the introduction, as statements, and in the body, with proofs. The two statements must agree exactly.
2. Each result is cited only after it is stated, or with a forward reference that says where it is proved. A forward reference must not create a circular argument.
3. Each piece of notation is fixed once, usually in the preliminaries, and is used in the same way in the whole paper. The page [[mathematical writing style|D5YPYTQ88G]] gives this advice.
4. The length and the level of detail of the proofs depend on the intended readers of the journal. The page [[level of detail in proofs|VYGBV5D8Y4]] discusses this.

### History

The pattern of definitions, statements and proofs goes back to [[Euclid's Elements|83WHDAV68J]].
The Mathematics Subject Classification was produced by the staff of the two main reviewing databases, Mathematical Reviews and Zentralblatt MATH.
Its current version is MSC2020.
Many journals today publish house style files for LaTeX, which fix the layout and the numbering of results.

### Common errors

1. A student states the main theorem only in the body, after twenty pages of lemmas. The reader then cannot judge the paper from its introduction.
2. A student numbers every display, or numbers lemmas, theorems and definitions with separate counters in a long paper. Both make the cross-references hard to follow.
3. A student puts new results into the preliminaries, or proves known results at length. The preliminaries recall known material with references, and new results belong in the body.

## Explanations

### L1 human

A research paper in mathematics is a report of new results with their proofs.
It starts with a title and a short summary, called the abstract.
Then the introduction tells what the new results are and why they are interesting.
After that come the proofs, broken into small numbered steps called lemmas.
At the end is a list of the other papers that the authors used.
The numbers, such as "Lemma 2.3", work like the addresses of houses: they let a reader find each result quickly.

### L2 human

We plan the structure of a short paper that proves one new theorem with two lemmas.

1. The title names the result in searchable words.
2. The abstract states the theorem in words in two to four sentences, with no citations.
3. Section 1, the introduction, states the theorem as Theorem 1.1, compares it with the best earlier result, and gives the outline.
4. Section 2, the preliminaries, fixes the notation and recalls the known results, with references.
5. Section 3 proves Lemma 3.1 and Lemma 3.2, and Section 4 proves Theorem 1.1, citing both lemmas by number.
6. The paper ends with the acknowledgements and the references.

The typical use of this plan is a first paper, or a thesis chapter.
There the writer decides the order of the sections before the writing starts.
A trap is to state Theorem 1.1 in the introduction in a form that differs from the form proved in Section 4.
For example, the introduction may drop one hypothesis.
The two statements must be checked against each other.

### L3 human

The structure of a paper is the large-scale form of the advice on [[writing proofs|8JQHJK94RZ]].
State the goal first, then give each step with its reason, and guide the reader through the structure.
A paper is a hierarchy of claims, as in a [[structured proof|H2W8D7BMSW]].
The main theorem is the root, the lemmas are its children, and each proof cites only results earlier in the order.
A monograph, a thesis and a survey extend the same pattern with chapters, and a survey replaces the proofs by references.
Papers in a formal library, such as a library of a proof assistant, take the hierarchy literally.
Each result is a named declaration, and its proof cites earlier declarations by name instead of by number.
The conventions of journals and of the publishing process, including peer review and preprints, belong to the topic [[publishing and peer review|A6ZGR8NM3S]].
