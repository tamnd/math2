---
tag: MJ3EHQJJHX
kind: concept
name: Acceptance of proofs
aliases: [acceptance-of-a-proof, proof-as-social-process]
msc: ["00A35", "01A80"]
topics: [1BTHSHST4M]
audience: research
uses: [0B94TKFQJX, E1PE9R8DBB, 8VZ77R4R8S]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Nature and purpose
  - url: https://en.wikipedia.org/wiki/Abc_conjecture
    locator: Claimed proofs
  - url: https://en.wikipedia.org/wiki/Wiles%27s_proof_of_Fermat%27s_Last_Theorem
    locator: Announcement and subsequent developments
  - url: https://en.wikipedia.org/wiki/Four_color_theorem
    locator: Early proof attempts
  - url: https://en.wikipedia.org/wiki/Grigori_Perelman
    locator: Verification
---

## Summary

In June 1993 Andrew Wiles ended a series of lectures in Cambridge with a proof of [[Fermat's Last Theorem|0Y5X3SDBCZ]], and the news spread around the world within days.
The referees then read the manuscript line by line, and by September 1993 they had found a gap in one step.
Wiles closed the gap in September 1994, partly in joint work with Richard Taylor, and the two papers appeared in 1995.
Only then did mathematicians treat the theorem as proved.

A proof is accepted when the mathematicians competent in its field agree that it is correct and start to use its result as a theorem.
Acceptance comes through reading, refereeing, seminars, independent checks and later use, and it usually takes months or years.
It is not the same as correctness: a correct proof can wait a long time for acceptance, and an accepted proof can later turn out to contain an error.
Acceptance is how [[rigor|E1PE9R8DBB]] works in practice, since for a long proof no single reader can certify every step.

## Motivation

The definition of a [[proof|0B94TKFQJX]] as a chain of justified steps says what a correct proof is.
It does not say how anyone comes to know that a given text is such a chain.
For a short proof, each reader checks each step.
For a proof of a hundred pages in a specialized field, only a few people can check it, and they need time.
So mathematics needs a process that turns a claimed proof into an accepted theorem, and that process has its own strengths and its own failures.

## Notation

A few words name the stages.
A claim or announcement says that a proof exists, often in a lecture or a preprint.
A preprint is a paper made public before refereeing, today usually on the arXiv.
A referee is an expert whom a journal asks to judge a paper, usually without the author knowing who.
A gap is a step that the text does not justify and that may or may not be repairable, while an error is a step that is false.

## Remarks

### Refereeing and its limits

A journal sends a submitted paper to one or more referees, who report on its correctness, novelty and interest.
Referees often check the main ideas and selected details rather than every line, and their reports are not public.
So publication in a refereed journal is strong evidence of correctness, but not a guarantee.
The wider system is described in [[publishing and peer review|A6ZGR8NM3S]].

### Consensus and time

Acceptance grows as more people read and use a result.
Experts lecture on the proof, write expositions, simplify the argument and apply the result to new problems.
Each new use is a new test, because an error in a result tends to produce false consequences.

In 1979 Richard De Millo, Richard Lipton and Alan Perlis argued, in "Social processes and proofs of theorems and programs" in Communications of the ACM, that this social process is what makes a theorem reliable.
They concluded that formal verifications of programs could not earn trust in the same way, because nobody reads, discusses or reuses them.
Their paper started a long debate between mathematicians and computer scientists about what formal verification can give.

### Errors that survived acceptance

Alfred Kempe published a proof of the [[four color theorem|0M406JC8J1]] in 1879, and it was accepted until Percy Heawood found an error in 1890.
Cauchy's textbook of 1821 stated that a convergent series of continuous functions has a continuous sum, and Abel gave a series in 1826 that seems to contradict it; [[history of proof and rigor|20F7K9RVT6]] tells the story.
The proof of the four color theorem by Appel and Haken, published in 1977, contained errors that later readers found and the authors corrected, as [[the four color proof|17BMQS5PTG]] describes.
None of these errors made the theorem false, but each shows that acceptance can run ahead of correctness.

### A contested claim

Some claims are neither accepted nor refuted for a long time.
In August 2012 Shinichi Mochizuki released four preprints on his inter-universal Teichmüller theory, with a claimed proof of the [[abc conjecture|G7JH2NXPC0]].
In March 2018 Peter Scholze and Jakob Stix visited Kyoto for several days of discussion with Mochizuki and Yuichiro Hoshi.
In their report of 2018 they stated that the argument for Corollary 3.12 of the third paper has a serious gap.
Mochizuki replied in writing that their objection rested on a misunderstanding of his theory.
In 2020 the journal Publications of the Research Institute for Mathematical Sciences, of which Mochizuki is chief editor, accepted the papers, and they were published there in 2021.
Mochizuki and some colleagues hold that the proof is complete, while Scholze, Stix and many other number theorists do not regard the conjecture as proved.
The case shows that publication alone does not settle acceptance.

### Two claims that were accepted

Grigori Perelman posted three preprints on the arXiv in 2002 and 2003, with a proof of the [[Poincaré conjecture|3R064KFF68]] and of the geometrization conjecture.
He never submitted them to a journal.
In 2006 three teams of authors published detailed expositions that checked the argument, and the community accepted the proof; Perelman declined the Fields Medal in 2006 and the Clay prize in 2010.

Thomas Hales announced a proof of the [[Kepler conjecture|AFMBQT06ZV]] in 1998.
The referees of the Annals of Mathematics reported that they were nearly certain of it but could not check every computer calculation, and the paper appeared in 2005.
The Flyspeck project completed a formal proof in 2014, which removed the remaining doubt, as [[Hales's proof|40QATE3WJN]] describes.

### What does not count as acceptance

An announcement in a lecture with no written proof is not accepted, because no expert can yet check it.
A proof checked only by its author is not accepted, however careful the author is, because no independent reader has checked it.
A published proof that the experts of its field do not agree on, as in the abc case, is not accepted either.

### Watch out

Do not think that publication proves correctness: referees can miss errors, as Kempe's case shows.
Do not think that acceptance is a vote that can make a false result true.
Acceptance is the community's best judgment at a time, and it is revised when an error is found.
And do not assume that a contested claim must be either fraud or a hidden success.
The usual case is an honest disagreement about whether a step is justified.

### Try it

First, in Wiles's case, which stage found the gap: the lectures, the refereeing, or later use?
The refereeing did, in the months after the lectures of June 1993, which had not shown it.

Second, why does each new use of a theorem count as a test of its proof?
If the theorem were false, some of its consequences would sooner or later conflict with known results or with examples.

## Explanations

### L1 human

When a mathematician claims to have proved something new, other mathematicians must check the argument.
For a short proof this takes minutes, but some proofs have hundreds of pages and use ideas that few people know.
Experts read the proof, ask the author questions and try to use the result.
If a step is wrong, someone usually finds it, as happened with the first version of the proof of Fermat's Last Theorem in 1993.
The author fixed that gap a year later, and the proof was accepted.
So a proof becomes part of mathematics when the experts agree that it is right.

### L2 human

We follow Wiles's proof through the stages of acceptance.
The announcement came in June 1993, in lectures at the Isaac Newton Institute in Cambridge.
Wiles then submitted a long manuscript, and several referees checked it in detail.
In September 1993 it was clear that one argument did not work as written.
In September 1994 Wiles found a way around the gap, with a step proved jointly with Richard Taylor.
The two papers appeared in the Annals of Mathematics in 1995, and later work built on their methods and tested them again.
The typical use of the case is to show that the process works: the referees found a gap that the lectures had not revealed.
Watch out for a simple reading in which the 1993 proof was "wrong" and the 1995 proof "right".
The main strategy survived, and one step was replaced.

### L3 human

Acceptance is studied in the philosophy of mathematical practice and in the sociology of mathematics.
One view, close to De Millo, Lipton and Perlis, holds that the social process is what gives a proof its authority.
Another holds that the authority comes from the existence of a formal derivation, and that the social process only estimates whether one exists.
Proof assistants make the second view concrete: a [[formal proof|8VZ77R4R8S]] of the full statement replaces trust in readers by trust in a small checker, as in the Flyspeck project.
Very long proofs strain the first view, as [[long proofs and surveyability|RM0S65BHWH]] and [[computer-assisted proof|MC18C7BMFT]] discuss.
How much speculation should come before acceptance was the subject of [[the debate of Jaffe and Quinn with Thurston|K3M3TEX7SJ]], and the general questions belong to the [[philosophy of mathematics|NTJ5XW0PVD]].
