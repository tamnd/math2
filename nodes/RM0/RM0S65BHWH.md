---
tag: RM0S65BHWH
kind: concept
name: Long proofs and surveyability
aliases: [surveyability, surveyable-proof, long-mathematical-proofs]
msc: ["00A35", "00A30"]
topics: [1BTHSHST4M]
audience: research
uses: [0B94TKFQJX, MC18C7BMFT, 06J6P03MG7, WP3GDNWJJW]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_long_mathematical_proofs
    locator: Long proofs
  - url: https://en.wikipedia.org/wiki/List_of_long_mathematical_proofs
    locator: Long computer calculations
  - url: https://en.wikipedia.org/wiki/Computer-assisted_proof
    locator: Philosophical objections
  - url: https://en.wikipedia.org/wiki/Classification_of_finite_simple_groups
    locator: History of the proof
  - url: https://en.wikipedia.org/wiki/Classification_of_finite_simple_groups
    locator: Second-generation classification
  - url: https://en.wikipedia.org/wiki/Feit%E2%80%93Thompson_theorem
    locator: History
  - url: https://en.wikipedia.org/wiki/Robertson%E2%80%93Seymour_theorem
    locator: lead section
---

## Summary

A proof is surveyable when a competent mathematician can read it and check each of its steps in a reasonable time.
A long proof, in the sense of this page, is a proof that is too long for one reader to check in full.
The reason is either that the written text runs to thousands of pages or that a part of the proof is a large computation.
The term "surveyable" became a standard term of the philosophy of mathematics through Thomas Tymoczko's article of 1979 on the [[four colour theorem|0M406JC8J1]].
Long proofs are accepted through the division of the checking among many experts, through later and shorter versions of the proof, and in recent years through formal verification.
The subject matters because some central theorems, such as the [[classification of finite simple groups|06J6P03MG7]], have no known proof that one person can check alone.

## Motivation

The traditional picture of a [[proof|0B94TKFQJX]] has one reader who follows the argument from the hypotheses to the conclusion and checks each step.
This picture fits Euclid's proof that there are infinitely many primes, which takes a few lines.
It does not fit a proof that fills several hundred journal articles by about one hundred authors.
It also does not fit a [[computer-assisted proof|MC18C7BMFT]], whose computation has billions of steps.
In both cases the community accepts the theorem, although no single person has checked the whole proof.
So the question is what this acceptance rests on, and whether such a proof gives the same kind of knowledge as a short proof.

## Remarks

### Examples

- The Feit-Thompson theorem. Walter Feit and John Thompson proved in 1963 that each finite group of odd order is [[solvable|0FXJ7YFMMX]]. Their paper has $255$ pages and fills a whole issue of the Pacific Journal of Mathematics. Georges Gonthier and his colleagues announced a formal proof in the Coq proof assistant in September 2012. The theorem has its own page, the [[Feit-Thompson theorem|6VK9RSG13Q]].
- The classification of finite simple groups. The proof consists of tens of thousands of pages in several hundred journal articles, by about $100$ authors, published mostly between 1955 and 2004. Daniel Gorenstein announced in 1983 that the classification was complete, but the case of the quasithin groups was still open. Michael Aschbacher and Stephen Smith closed it in 2004 with a proof of $1221$ pages.
- The second-generation proof of the classification. Gorenstein, Richard Lyons and Ronald Solomon began a revised proof, published by the American Mathematical Society from 1994. As of 2023 ten volumes had appeared, eight by Gorenstein, Lyons and Solomon and two by Inna Capdeboscq. The aim is a single connected account that a reader can follow.
- The [[Robertson-Seymour theorem|WP3GDNWJJW]]. Neil Robertson and Paul Seymour proved that the finite graphs are well-quasi-ordered by the minor relation in a series of twenty papers, Graph Minors I to XX, published from 1983 to 2004. The series has more than $500$ pages.
- Computer-assisted proofs. The proofs of the four colour theorem and of the [[Kepler conjecture|AFMBQT06ZV]] are long because of their computations, as the pages on [[the four colour proof|17BMQS5PTG]] and [[the Kepler proof|40QATE3WJN]] describe. The proof of the [[Boolean Pythagorean triples problem|417PHKB4VC]] is a file of about $200$ terabytes.

### Non-examples

- [[Euclid's proof that there are infinitely many primes|0292EPPPT0]] is surveyable. It takes a few lines, and each reader can check each step.
- The first half of the [[Boolean Pythagorean triples problem|417PHKB4VC]] is surveyable in the relevant sense, although a long search found it. The proof that $\{1, \dots, 7824\}$ has a good colouring is the colouring itself, and a short program or a patient person can check it against each triple. The length of a search does not make the result long; only the length of the proof does.
- A textbook proof of one page that cites earlier theorems is not a long proof in this sense. Each cited theorem was checked on its own, and a reader can check each one in turn. The classification is different, because its parts are too many for one reader even in turn.

### Basic properties

- Length depends on the starting point. A proof that cites strong results can be short, while the same proof from the axioms can be very long.
- Long proofs are checked by a division of labour. Each expert checks a part, and the community accepts the whole when each part has been checked by someone. The acceptance then rests on trust between experts, as described in [[acceptance of proofs|MJ3EHQJJHX]].
- Length makes errors more likely, and errors in long proofs can stay hidden for years. The gap in the quasithin case of the classification is an example.
- Later proofs are often shorter or better organized. The second-generation proof of the classification and the proof of the four colour theorem by Robertson, Sanders, Seymour and Thomas are examples.
- Formal verification changes what must be surveyed. After a proof assistant has checked a proof, a reader must survey only the kernel of the assistant and the formal statement of the theorem, as described in [[formal and informal proofs|8VZ77R4R8S]].

### History

Thomas Tymoczko published "The four-color problem and its philosophical significance" in The Journal of Philosophy in 1979.
He named three features of a proof: it is convincing, it is surveyable, and it is formalizable.
He argued that the proof of Appel and Haken is convincing and formalizable in principle, but that no mathematician can survey it.
He concluded that our knowledge of the four colour theorem rests in part on an empirical premise, the reliability of computers, and so a new kind of experiment had entered mathematics.
In 1980 Michael Detlefsen and Mark Luker replied in the same journal, in "The four-color theorem and mathematical proof".
They argued that the computer proof raised no philosophical problem that was new in principle.

### Common errors

- To think that a long proof is a weaker proof. A correct proof proves its theorem whatever its length; length only makes the check harder and errors more likely.
- To think that a computer proof cannot be surveyed in any sense. The written reduction and the program can be read and checked, even when the run of the program cannot.
- To think that the classification of finite simple groups was complete in 1983. Gorenstein's announcement was premature, and the last gap was closed in 2004.

## Explanations

### L1 human

Most proofs in a textbook fit on one page, and a student can check each line.
Some proofs are so long that no person can read all of them.
The list of all finite simple groups, the basic building blocks of finite groups, was proved in hundreds of articles by about a hundred authors.
No single mathematician has checked all of those pages.
Mathematicians still accept the result, because each part was checked by experts and the parts fit together.
A proof that one person can check from start to end is called surveyable, and the long proofs on this page are not surveyable in that sense.

### L2 human

We estimate how long one reader would need to check two long proofs.
The rates in the steps are assumptions for the estimate, not measured facts.

1. Assume that a careful referee checks $10$ pages of a research proof in one working day.
2. A written proof of $10000$ pages then needs $10000 / 10 = 1000$ working days.
3. With $250$ working days in a year, this is $1000 / 250 = 4$ years of full-time work. The classification has more pages than this, so one reader would need many years.
4. Now take a proof file of $200$ terabytes, that is $2 \cdot 10^{14}$ characters.
5. Assume that a person reads $10$ characters each second, for $8$ hours each day. This is $10 \cdot 3600 \cdot 8 = 288000$ characters each day.
6. The file needs $2 \cdot 10^{14} / 288000 \approx 6.9 \cdot 10^{8}$ days, which is about $1.9$ million years.

The written proof of step 3 is long but within reach of a team, while the file of step 6 can be checked only by a program.
This is the reason why the two kinds of long proof are accepted in different ways: the first by experts who share the work, the second by independent checking programs.
A trap is to apply the estimate of step 6 to the written part of a computer-assisted proof, which is often short and is checked by referees in the usual way.

### L3 human

Proof theory gives a precise sense to the length of a proof.
Kurt Gödel observed that a stronger formal system can prove some theorems with far shorter proofs than a weaker system, and [[proof complexity|13JZKN6WKC]] studies lower bounds on the length of proofs in a fixed system.
These results show that some true statements have only very long proofs, so long proofs are not a defect of current methods alone.

In practice the question of surveyability became a question about trust and its distribution.
Tymoczko's argument assumed that a proof is accepted because an individual checks it.
The practice of the classification, of the Graph Minors series and of large formal libraries shows a different model, in which a community checks a proof through overlapping partial checks, later revisions and machine verification.
The pages on [[computer-assisted proof|MC18C7BMFT]] and [[acceptance of proofs|MJ3EHQJJHX]] continue this theme, and the epistemological questions belong to the [[philosophy of mathematics|NTJ5XW0PVD]].
