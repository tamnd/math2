---
tag: 1CV4HTA6C8
kind: concept
name: Famous incorrect proofs
aliases: [famous-incorrect-proofs, incomplete-proofs, famous-wrong-proofs]
msc: ["00A35", "01A55", "01A60"]
topics: [T6QQ749DM5]
audience: research
uses: [0B94TKFQJX, S2BW0FDHV8, 1BTHSHST4M]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_incomplete_proofs
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Four_color_theorem
    locator: Early proof attempts
  - url: https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem
    locator: Ernst Kummer and the theory of ideals
  - url: https://en.wikipedia.org/wiki/Wiles%27s_proof_of_Fermat%27s_Last_Theorem
    locator: Announcement and subsequent developments
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_sixteenth_problem
    locator: The second part of Hilbert's 16th problem
  - url: https://mathshistory.st-andrews.ac.uk/HistTopics/Non-Euclidean_geometry/
    locator: paragraphs on Legendre
---

## Summary

A famous incorrect proof is a published or announced [[proof|0B94TKFQJX]] of a significant result that experts accepted, or took seriously, and that later turned out to contain an invalid step or a gap.
The claimed result can be true, as for the four colour theorem and Fermat's Last Theorem, or false.
The error is almost never a [[mathematical fallacy|S2BW0FDHV8]] made on purpose: it is a step that the author and the first readers took as evident.
The cases matter because they show how proofs are checked in practice, and because the search for the missing step often created new mathematics.

## Motivation

A proof is accepted when competent readers check it and find no error.
This check is done by people, and people can miss a gap, so an accepted proof is not certain to be correct.
The history of such errors shows which steps are hard to check: a case that looks like an earlier case, a property of a familiar number system used in a new one, or a statement that is "geometrically evident".
It also shows how errors were found: by a reader who tried to extend the argument, by a referee, or by a counterexample to a lemma.
The topic on [[rigour and the acceptance of proofs|1BTHSHST4M]] treats the general question of when a proof counts as accepted.

## Notation

The literature separates two cases.

1. An incomplete proof has a gap: a step is not justified, but the result can still be true and the gap can sometimes be closed.
2. An incorrect proof has a false step: the step does not follow, and sometimes the claimed result is false.

The Wikipedia "List of incomplete proofs", as of 2026-11, sorts its entries into results later proved rigorously, incorrect results, theories proven inconsistent, and cases of unclear status.
The list changes as historians and mathematicians revise their judgments.

## Remarks

### Examples

1. Kempe and the [[four colour theorem|0M406JC8J1]]. Kempe published a proof in 1879, and it was accepted for 11 years. In 1890 Heawood showed that it fails in the case of a vertex with five neighbours.
2. Tait and the four colour theorem. Tait published a different proof in 1880, which also stood for 11 years, until Petersen showed in 1891 that it was wrong.
3. Lamé and [[Fermat's Last Theorem|0Y5X3SDBCZ]]. In 1847 Lamé announced a proof that assumed unique factorisation in rings of cyclotomic integers. Liouville at once questioned this assumption, and Kummer had shown that it fails for some exponents.
4. Legendre and the [[parallel postulate|2PC3XY0PYZ]]. Legendre gave several proofs over about forty years. One proof assumed that through each point inside an angle there is a line that meets both sides of the angle, a statement equivalent to the postulate.
5. Dulac and limit cycles. In 1923 Dulac published a proof that a polynomial vector field in the plane has only finitely many [[limit cycles|0AAQ73WRFB]]. In the early 1980s Ilyashenko found a gap in it.
6. Wiles and Fermat's Last Theorem. Wiles announced a proof in June 1993. In August 1993 Nick Katz found a gap in one step during the review of the manuscript.

### Non-examples

1. A deliberate false proof, such as a "proof" that $1 = 2$, is not in this class. Its author knows the error, and nobody accepts the result.
2. Heawood's proof of the [[five colour theorem|06C0JBE52D]] uses the method of Kempe, but [[it is correct|VSVWRHH2GN]]. The part of Kempe's argument that fails is not needed for five colours.
3. An open [[conjecture|WMEMMHZ3BH]] that nobody claims to have proved is not an incorrect proof. The condition "an announced proof" fails.

### Basic properties

1. An incorrect proof does not make its result false. Kempe, Lamé, Dulac and the first version of Wiles all claimed results that were later proved.
2. The failing step is usually a step that the author treated as evident: a case that seemed similar to a done case, or a property of the integers used in a larger ring.
3. The search for the missing step often produced new tools: Kempe chains, Kummer's ideal numbers and the [[ideal class group|WQ46BD3ARY]], and the analysis of hyperbolic geometry.
4. Errors were found in several ways: by an expert reader (Heawood, Liouville), by a referee (Katz), or by a later author who studied the proof in detail (Ilyashenko).

### History

Kempe's error was in the case of degree 5.
He made two Kempe chain interchanges in turn, and Heawood gave a map in which the first interchange changes the chain that the second one needs.
Heawood then used Kempe's method to prove the five colour theorem, and Appel and Haken proved the four colour theorem in 1976.
Kummer's work on factorisation in cyclotomic rings led to the proof of Fermat's Last Theorem for [[regular primes|B4VK33PCXZ]]; unique factorisation in $\mathbb{Z}[\zeta_p]$ holds for primes $p \le 19$ and fails first for $p = 23$.
Legendre published his attempts in editions of his *Éléments de géométrie*, first published in 1794, and he did not find his error; his correct result is the [[Saccheri-Legendre theorem|1Y2XK0QJDX]].
Ilyashenko and Écalle gave independent proofs of [[Dulac's theorem|NEYHC1XZ14]] in 1991 and 1992, and Dulac's claim is part of the history of [[Hilbert's sixteenth problem|C1XNMMKZ1J]].
Wiles closed his gap in September 1994, with an argument that uses joint work with Richard Taylor, and the two papers appeared in 1995.
Cauchy stated in 1821 that a convergent series of continuous functions has a continuous sum.
In 1826 Abel gave a series that seems to contradict this statement.
Historians disagree on what Cauchy meant by convergence, and the Wikipedia list places this case under "status unclear".

### Common errors

1. A student concludes that a theorem is false because its first proof was wrong. The examples above show true results with wrong first proofs.
2. A student assumes that a published proof has been checked in every step. Refereeing reduces errors, but it does not remove them.
3. A student uses the word "wrong" for a proof with a gap that was later closed. The two cases of the Notation section are different.

## Explanations

### L1 human

Sometimes a great mathematician publishes a proof, other experts read it and agree, and years later someone finds a mistake.
In 1879 Kempe "proved" that four colours are enough to colour any map so that neighbouring countries have different colours.
In 1890 Heawood found a map where one step of Kempe's argument does not work.
The statement was still true, but a correct proof came only in 1976, with the help of a computer.
Such stories show that every step of a proof needs a reason, even a step that seems evident to everyone.

### L2 human

We check the assumption that broke Lamé's argument in a simpler ring.
Let $R = \{a + b\sqrt{-5} : a, b \in \mathbb{Z}\}$, and let $N(a + b\sqrt{-5}) = a^2 + 5b^2$ be the [[field norm|KRNFEZWPY0]], which is multiplicative.

1. In $R$, $6 = 2 \cdot 3$ and $6 = (1 + \sqrt{-5})(1 - \sqrt{-5})$.
2. The norms are $N(2) = 4$, $N(3) = 9$ and $N(1 \pm \sqrt{-5}) = 6$.
3. No element has norm $2$ or $3$, because $a^2 + 5b^2 \in \{2, 3\}$ forces $b = 0$, and then $a^2 \in \{2, 3\}$ has no integer solution.
4. A proper factorisation of an element of norm $4$, $9$ or $6$ would need a factor of norm $2$ or $3$. So $2$, $3$ and $1 \pm \sqrt{-5}$ are [[irreducible|0YMT0D2442]].
5. The only units of $R$ are $\pm 1$, because they are the elements of norm $1$. So $2$ is not a unit multiple of $1 \pm \sqrt{-5}$, since the norms differ.
6. So $6$ has two essentially different factorisations into irreducible elements, and $R$ is not a [[unique factorisation domain|0W4X9G6263]].

The page on [[irreducible and prime elements in this ring|5BM35ES8WK]] gives the same example from the point of view of prime elements.
The typical use of this check is to test whether a ring is a unique factorisation domain before an argument uses unique factorisation in it.
A trap is to carry a property of $\mathbb{Z}$, such as unique factorisation, into a larger ring without a proof, as Lamé did for $\mathbb{Z}[\zeta_p]$.

### L3 human

The famous errors share a structure: a lemma that holds in a familiar case is used in a wider case where it fails, or a case analysis misses one configuration.
In Lamé's proof the familiar case is $\mathbb{Z}$, and the measure of failure in $\mathbb{Z}[\zeta_p]$ is the [[ideal class group|WQ46BD3ARY]] of the [[cyclotomic field|NN77VYSGXR]]; Kummer's condition "$p$ does not divide the class number" defines regular primes.
In Kempe's proof the missed configuration is the interaction of two Kempe chains, and the later proof of Appel and Haken replaced the single reducible configuration by a large unavoidable set of reducible ones.
Legendre's assumption is one of many statements that are equivalent to the parallel postulate over the other axioms; the consistency of [[hyperbolic geometry|GN4N94GQ0Z]] shows that none of them follows from those axioms.
Today some long or delicate proofs are checked by computer in proof assistants, and formal verification removes the class of errors that comes from steps taken as evident.
The topic on [[rigour and the acceptance of proofs|1BTHSHST4M]] discusses the social process of checking, and the sub-area on mathematical software treats proof assistants.
