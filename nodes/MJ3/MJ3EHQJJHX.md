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

A proof is accepted when the mathematicians competent in its field agree that it is correct, and they then use its result as a theorem.
Acceptance is reached through reading, refereeing, seminars, independent checks and later use, and it usually takes months or years.
It is different from correctness: a correct proof can wait long for acceptance, and an accepted proof can later turn out to contain an error.
The process matters because it is how [[rigour|E1PE9R8DBB]] works in practice: no single reader certifies a long proof, and the community decides what counts as known.

## Motivation

The definition of a [[proof|0B94TKFQJX]] as a chain of justified steps says what a correct proof is.
It does not say how anyone comes to know that a given text is such a chain.
For a short proof, each reader can check each step.
For a proof of a hundred pages in a specialized field, only a few people can check it, and they need time.
So mathematics needs a process that turns a claimed proof into an accepted theorem, and the process has its own strengths and failures.

## Notation

Several words describe the stages.
A "claim" or "announcement" states that a proof exists, often in a lecture or a preprint.
A "preprint" is a paper made public before refereeing, today usually on the arXiv.
A "referee" is an expert whom a journal asks to judge a paper, often anonymously.
A "gap" is a step that the text does not justify, which may or may not be repairable; an "error" is a step that is false.

## Remarks

### Refereeing and its limits

A journal sends a submitted paper to one or more referees, who report on its correctness, novelty and interest.
Referees often check the main ideas and selected details, not every line, and their reports are not public.
So publication in a refereed journal is strong evidence of correctness, and not a guarantee.
The process is part of [[publishing and peer review|A6ZGR8NM3S]].

### Consensus and time

Acceptance grows as more people read and use a result.
Experts give lectures on the proof, write expositions, simplify the argument, and apply the result to new problems.
Each new use is a new test, because an error in the result tends to produce false consequences.
In 1979 Richard De Millo, Richard Lipton and Alan Perlis argued, in "Social processes and proofs of theorems and programs", that this social process is what makes a theorem reliable.
They concluded that formal verification of programs could not gain trust in the same way, since nobody reads and uses such verifications; their paper started a long debate.

### Errors in published proofs

- In 1879 Alfred Kempe published a proof of the [[four colour theorem|0M406JC8J1]]. In 1890 Percy Heawood found an error in it, after eleven years of acceptance.
- In 1821 Cauchy's textbook stated that a convergent sum of continuous functions is continuous, and Abel gave a counterexample in 1826; the page [[history of proof and rigour|20F7K9RVT6]] tells the story.
- The Appel-Haken proof of the four colour theorem, published in 1977, had errors that later work found and corrected; see [[the acceptance of the four colour proof|17BMQS5PTG]].

### Contested claims

Some claimed proofs are neither accepted nor refuted for a long time.
In August 2012 Shinichi Mochizuki released preprints of his inter-universal Teichmüller theory, with a claimed proof of the [[abc conjecture|G7JH2NXPC0]].
In March 2018 Peter Scholze and Jakob Stix visited Kyoto and reported a gap in the argument for one corollary, and Mochizuki replied that they had misunderstood it.
In 2020 the journal Publications of the Research Institute for Mathematical Sciences, whose chief editor is Mochizuki, accepted the papers; they were published in 2021.
Most experts in the field do not accept the proof, and the abc conjecture is generally treated as open.
The case shows that publication alone does not settle acceptance.

### Examples

- Andrew Wiles announced a proof of [[Fermat's Last Theorem|0Y5X3SDBCZ]] in lectures at Cambridge in June 1993. During refereeing a gap was found in September 1993. Wiles repaired it in September 1994, with a step proved jointly with Richard Taylor, and the papers appeared in 1995.
- Grigori Perelman posted three preprints on the arXiv in 2002 and 2003, with a proof of the [[Poincaré conjecture|3R064KFF68]] and of the geometrization conjecture. He did not submit them to a journal. In 2006 three teams completed detailed written checks, and the community accepted the proof; Perelman declined the Fields Medal in 2006 and the Clay prize in 2010.
- Thomas Hales announced a proof of the [[Kepler conjecture|AFMBQT06ZV]] in 1998. The head of the referee panel said that they were "99% certain" of it, but they could not check the computer part. A formal proof completed in 2014 removed the doubt; see [[Hales's proof|40QATE3WJN]].

### Non-examples

- An announcement in a lecture, with no written proof, is not an accepted proof. The condition that fails: no expert can yet check it.
- A proof checked only by its author is not accepted, however careful the author is. The condition that fails: no independent reader has checked it.
- The abc case above is not an accepted proof, although it is published. The condition that fails: the experts of the field have not reached agreement.

### Basic properties

- Acceptance is a matter of degree and of time. A new result moves from "claimed" to "believed" to "standard" as checks and uses accumulate.
- Acceptance depends on the reputation and the clarity of the author. A clear exposition by a known expert is read sooner, and this can delay the reading of work by outsiders.
- A formal proof checked by a proof assistant reduces the trust needed in human readers. It moves the trust to the checker and to the formal statement; see [[formal and informal proofs|8VZ77R4R8S]].
- A gap does not make a result false. Wiles's gap was repaired, and Kempe's error was not, although his method survived in later proofs.

### History

Refereeing of journal papers became a standard practice in the 20th century.
The arXiv, started in 1991, made preprints public at once, and the Perelman case showed that acceptance can happen without a journal.
Since 1976, computer proofs and very long proofs have raised new questions of acceptance; see [[computer-assisted proof|MC18C7BMFT]] and [[long proofs and surveyability|RM0S65BHWH]].

### Common errors

- To think that publication in a journal proves correctness. Referees can miss errors, as Kempe's case shows.
- To think that acceptance is a vote that can make a false result true. Acceptance is the community's best judgement, and it is revised when an error is found.
- To think that a contested claim must be either fraud or a hidden success. The usual case is an honest disagreement about whether a step is justified.

## Explanations

### L1 human

When a mathematician claims to have proved something new, other mathematicians must check the argument.
For a short proof this takes minutes, but some proofs have hundreds of pages and use ideas that few people know.
Experts read the proof, ask the author questions, and try to use the result.
If a step is wrong, someone usually finds it, as happened with a famous first proof of Fermat's Last Theorem in 1993.
In that case the author fixed the gap a year later, and the proof was accepted.
So a proof becomes part of mathematics when the experts agree that it is right.

### L2 human

We follow one claim through the stages of acceptance, Wiles's proof of Fermat's Last Theorem.

1. Announcement: in June 1993 Wiles lectured at the Isaac Newton Institute in Cambridge and announced the proof.
2. Refereeing: he submitted a long manuscript, and several referees checked it in detail.
3. A gap: in September 1993 a referee's question showed that one argument did not work as written.
4. Repair: in September 1994 Wiles found a way around the gap, with a step proved jointly with Richard Taylor.
5. Publication: the two papers appeared in the Annals of Mathematics in 1995.
6. Use: later work built on the methods of the proof and extended them, which tested them again.

The typical use of this case is to show that the process works: the referees found a gap that the lectures had not shown.
A trap is to say that the 1993 proof was "wrong" and the 1995 proof "right" in a simple sense; the main strategy survived, and one step was replaced.

### L3 human

The acceptance of proofs is studied in the philosophy of mathematical practice and in the sociology of mathematics.
One view, close to De Millo, Lipton and Perlis, holds that the social process is what gives a proof its authority.
Another view holds that the authority comes from the existence of a formal derivation, and that the social process only estimates whether one exists.
Proof assistants make the second view concrete: a formal proof of the full statement replaces the trust in readers by trust in a small checker, as in the Flyspeck project.
The question of how much speculation should come before acceptance was the subject of [[the Jaffe-Quinn and Thurston debate|K3M3TEX7SJ]], and the general questions belong to the [[philosophy of mathematics|NTJ5XW0PVD]].
