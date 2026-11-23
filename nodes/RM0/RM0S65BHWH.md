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

Euclid's proof that there are infinitely many primes fits in five lines, and you can check every step in a minute.
The proof that every finite group of odd order is solvable, by Walter Feit and John Thompson in 1963, fills $255$ journal pages.
The proof of the [[classification of finite simple groups|06J6P03MG7]] fills tens of thousands of pages, and no single person has read all of them.
Somewhere between these cases, the ideal of one reader who checks every step stops working.

A proof is surveyable when a competent mathematician can read it and check each step in a reasonable time.
A long proof, in the sense used here, is one that is too long for a single reader to check in full.
Either the written text runs to thousands of pages, or part of the proof is a large computation.
Thomas Tymoczko made "surveyable" a standard term of the philosophy of mathematics in 1979, in an article on the [[four color theorem|0M406JC8J1]].
Long proofs come to be trusted in other ways: experts divide the checking, later authors write shorter versions, and in recent years proof assistants check the whole proof.

## Motivation

The usual picture of a [[proof|0B94TKFQJX]] has one reader who follows the argument from the hypotheses to the conclusion.
That picture fits Euclid, and it does not fit a proof spread over several hundred articles by about a hundred authors.
It also does not fit a [[computer-assisted proof|MC18C7BMFT]] whose computation has billions of steps.
In both cases mathematicians accept the theorem, although nobody has checked the whole proof alone.
So two questions arise: what does that acceptance rest on, and does such a proof give the same kind of knowledge as a short one?

## Notation

"Surveyable" translates Wittgenstein's German word *übersehbar*, which he used for a proof that can be taken in as a whole.
Tymoczko gave it the sense of "checkable by a human reader in a reasonable time", and that is the sense used today.
"Long proof" has no fixed threshold; in practice it means a proof that a referee cannot check in full in the usual time.

## Remarks

### Two written proofs of great length

Feit and Thompson published their odd order theorem in 1963, and the paper fills a whole issue of the Pacific Journal of Mathematics.
Georges Gonthier and his colleagues announced a complete formal proof in the Coq proof assistant in September 2012; the theorem itself is the [[Feit-Thompson theorem|6VK9RSG13Q]].

The classification of finite simple groups is longer by far.
Its proof is spread over several hundred articles by about $100$ authors, published mostly between 1955 and 2004.
Daniel Gorenstein announced in 1983 that the classification was complete, but the case of the quasithin groups was still open.
Michael Aschbacher and Stephen Smith closed it in 2004 with a proof of $1221$ pages in two volumes.
From 1994 Gorenstein, Richard Lyons and Ronald Solomon have published a revised "second generation" proof in a series of volumes of the American Mathematical Society, with Inna Capdeboscq joining for later volumes.
Its aim is a single connected account that a reader can follow.

### A long proof in graph theory

Neil Robertson and Paul Seymour proved the [[Robertson-Seymour theorem|WP3GDNWJJW]]: the finite graphs are well-quasi-ordered by the minor relation.
The proof is the series Graph Minors I to XX, published from 1983 to 2004, and it runs to more than $500$ pages.
Each paper was refereed on its own, and the whole was accepted as the parts were checked and used.

### Long because of a computation

The proofs of the four color theorem and of the [[Kepler conjecture|AFMBQT06ZV]] have a written part that a person can read and a computer part that nobody reads by hand, as [[the four color proof|17BMQS5PTG]] and [[the Kepler proof|40QATE3WJN]] describe.
The proof of the [[Boolean Pythagorean triples problem|417PHKB4VC]] is a certificate of about $200$ terabytes.
It shows that $\{1, \dots, 7825\}$ cannot be split into two classes with no class holding a triple $a^2 + b^2 = c^2$.

Watch the other half of that result, though.
That $\{1, \dots, 7824\}$ can be split in this way is proved by one explicit coloring, which a short program or a patient person can check triple by triple.
A long search found it, but the proof itself is short, so the length of a search does not make a proof long.

### What is not a long proof

Euclid's proof of [[the infinitude of primes|0292EPPPT0]] is surveyable, since each reader can check each step.
A one-page textbook proof that cites earlier theorems is not long either, because a reader can check each cited theorem in turn.
The classification differs in kind: its parts are too many for one reader even in turn.

### How long proofs are trusted

Length depends on the starting point: a proof that cites strong results can be short, and the same proof from the axioms can be very long.
Long written proofs are checked by a division of labor, in which each expert checks a part and the community accepts the whole when every part has a checker.
That acceptance rests on trust between experts, as described in [[acceptance of proofs|MJ3EHQJJHX]].
Length makes errors more likely and lets them stay hidden for years, as the quasithin gap shows.
Later proofs are often shorter or better organized, such as the second generation classification and the four color proof of Robertson, Sanders, Seymour and Thomas in 1997.
A proof assistant changes what must be surveyed: after it accepts a proof, a reader needs to check only its small kernel and the formal statement, as [[formal and informal proofs|8VZ77R4R8S]] explains.

### Tymoczko and his critics

Thomas Tymoczko published "The four-color problem and its philosophical significance" in The Journal of Philosophy in 1979.
He named three features of a proof: it convinces, it is surveyable, and it can be formalized.
He argued that the proof of Appel and Haken convinces and can be formalized in principle, but that no mathematician can survey it.
So, he concluded, our knowledge of the four color theorem rests in part on an empirical premise, the reliability of computers, and a kind of experiment had entered mathematics.
In 1980 Michael Detlefsen and Mark Luker replied in the same journal, in "The four-color theorem and mathematical proof", that the computer proof raised no philosophical problem that was new in principle.

### Watch out

A long proof is not a weaker proof.
A correct proof proves its theorem at any length, and length only makes the check harder and errors more likely.
A computer proof is not unsurveyable in every sense either, because its written reduction and its program can be read and checked even when the run cannot.
Finally, do not date the classification to 1983: Gorenstein's announcement came before the quasithin case was done, and that gap closed in 2004.

### Try it

First, a referee checks $10$ pages of research proof a day and works $250$ days a year: how long does a $5000$ page proof take?
It takes $5000 / 10 = 500$ days, which is two years of full-time work.

Second, why is the coloring of $\{1, \dots, 7824\}$ a short proof although finding it was hard?
Checking it needs only a pass over the Pythagorean triples up to $7824$, and the search that found it is not part of the proof.

## Explanations

### L1 human

Most proofs in a textbook fit on a page, and a student can check every line.
Some proofs are so long that no person can read all of them.
The list of all finite simple groups, the building blocks of finite groups, was proved in hundreds of articles by about a hundred authors.
No single mathematician has checked all of those pages.
Mathematicians still accept the result, because experts checked each part and the parts fit together.
A proof that one person can check from start to end is called surveyable, and these long proofs are not surveyable in that sense.

### L2 human

We estimate how long one reader would need for two long proofs, with rates that are assumptions and not measured facts.
Suppose a careful referee checks $10$ pages of research proof in a working day, with $250$ working days a year.
A written proof of $10000$ pages then takes
$$\frac{10000}{10} = 1000 \text{ days} = \frac{1000}{250} = 4 \text{ years},$$
and the classification is longer still.
Now take a certificate of $200$ terabytes, about $2 \cdot 10^{14}$ characters, and a reader who reads $10$ characters a second for $8$ hours a day, which is $10 \cdot 3600 \cdot 8 = 288000$ characters a day.
The certificate takes
$$\frac{2 \cdot 10^{14}}{288000} \approx 6.9 \cdot 10^{8} \text{ days},$$
which is about $1.9$ million years.
The written proof is within reach of a team, and the certificate can be checked only by a program.
That is why the two kinds of long proof are accepted in different ways: the first by experts who share the work, the second by independent checking programs.
Watch out: the written part of a computer-assisted proof is often short, and referees check it in the usual way.

### L3 human

Proof theory gives a precise sense to the length of a proof.
Kurt Gödel observed that a stronger formal system can prove some theorems with far shorter proofs than a weaker one, and [[proof complexity|13JZKN6WKC]] studies lower bounds on proof length in a fixed system.
These results show that some true statements have only very long proofs, so long proofs are not only a defect of present methods.

In practice the question of surveyability became a question about how trust is shared.
Tymoczko assumed that a proof is accepted because an individual checks it.
The classification, the Graph Minors series and the large formal libraries show another model, in which a community checks a proof through overlapping partial checks, later revisions and machine verification.
The epistemological side of the question belongs to the [[philosophy of mathematics|NTJ5XW0PVD]].
