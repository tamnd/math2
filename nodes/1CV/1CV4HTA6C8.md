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

In 1847 Gabriel Lamé told the Paris Academy that he had proved [[Fermat's Last Theorem|0Y5X3SDBCZ]].
Here is the core of his argument for an odd prime $p$; look for the step that needs a reason.

> Let $\zeta$ be a primitive $p$-th root of unity, and suppose $x^p + y^p = z^p$ in positive integers.
> Factor the left side: $(x + y)(x + \zeta y)\cdots(x + \zeta^{p-1} y) = z^p$.
> The factors have no common factor, so each one is a $p$-th power in $\mathbb{Z}[\zeta]$, and a descent then gives a contradiction.

The step "so each one is a $p$-th power" is true in $\mathbb{Z}$, because integers factor uniquely into primes.
Joseph Liouville questioned it at once, since Lamé used it in $\mathbb{Z}[\zeta]$, where factorization into irreducible elements is unique for $p \le 19$ and fails for $p = 23$.
Kummer repaired the idea with ideal numbers, whose factorization is always unique, and proved the theorem for every regular prime.
The full theorem waited until Wiles.

A famous incorrect proof is a published or announced [[proof|0B94TKFQJX]] of a significant result that experts took seriously and that later turned out to have a gap or a false step.
It is almost never a [[mathematical fallacy|S2BW0FDHV8]] planted on purpose; the failing step is one that the author and the first readers found evident.

## Motivation

A proof counts as accepted when competent readers check it and find no error, and readers can miss a gap.
The famous cases show which steps are hard to check: a case that looks like a case already done, a property of a familiar number system carried into a new one, or a statement that seems geometrically evident.
They also show how errors come to light, through a reader who tries to extend the argument, a referee, or a counterexample to a lemma.
Very often the search for the missing step created new mathematics.
The broader question of when a proof counts as accepted is treated in [[rigor and the acceptance of proofs|1BTHSHST4M]].

## Notation

Historians separate two cases.
An incomplete proof has a gap: some step is not justified, the result may still be true, and the gap can sometimes be closed.
An incorrect proof has a false step that does not follow, and sometimes the claimed result itself is false.
Informally, mathematicians say a proof "has a hole" for the first case and "is wrong" for the second, and the two words should not be mixed.

## Remarks

### Kempe, Tait and four colors

Alfred Kempe published a proof of the [[four color theorem|0M406JC8J1]] in 1879, and it was accepted for 11 years.
In 1890 Percy Heawood showed that it fails for a vertex with five neighbors.
There Kempe made two Kempe chain swaps in turn, and Heawood drew a map in which the first swap breaks the chain that the second one needs.
Peter Guthrie Tait published a different proof in 1880, and Julius Petersen showed in 1891 that it was wrong.
Heawood used Kempe's method to prove the [[five color theorem|06C0JBE52D]], and that [[proof is correct|VSVWRHH2GN]], since the failing part of Kempe's argument is not needed for five colors.
Kenneth Appel and Wolfgang Haken proved the four color theorem in 1976, with the help of a computer.

### Legendre and the parallel postulate

Adrien-Marie Legendre gave several proofs of the [[parallel postulate|2PC3XY0PYZ]] over about forty years, in editions of his *Éléments de géométrie*, first published in 1794.
One proof assumed that through each point inside an angle there is a line meeting both sides of the angle.
That statement cannot be proved without the postulate, because it fails in [[hyperbolic geometry|GN4N94GQ0Z]], so the proof is [[circular|JPHE53PABT]].
Legendre did not find the error, and his correct result from the same work is the [[Saccheri-Legendre theorem|1Y2XK0QJDX]].

### Dulac, Wiles and Cauchy

In 1923 Henri Dulac published a proof that a polynomial vector field in the plane has only finitely many [[limit cycles|0AAQ73WRFB]].
Around 1980, Jean Écalle and Yulij Ilyashenko independently found a gap in it.
Ilyashenko in 1991 and Écalle in 1992 gave independent proofs of [[Dulac's theorem|NEYHC1XZ14]], which belongs to the history of [[Hilbert's sixteenth problem|C1XNMMKZ1J]].

Andrew Wiles announced a proof of Fermat's Last Theorem in June 1993.
By September 1993, questions from Nick Katz during the refereeing had exposed a gap in one step.
Wiles closed it on 19 September 1994 with an argument that uses joint work with Richard Taylor, and the two papers appeared in May 1995.

In his *Cours d'analyse* of 1821, Augustin-Louis Cauchy stated that a convergent series of continuous functions has a continuous sum, and in 1826 Niels Henrik Abel gave a series that seems to contradict it.
Historians still disagree about what Cauchy meant by convergence, so the status of this case is unclear.

### What the cases share

An incorrect proof does not make its result false: Kempe, Lamé, Dulac and the first version of Wiles all claimed results that were later proved.
The failing step is usually one taken as evident, such as a case like one already done, or a property of $\mathbb{Z}$ used in a larger ring.
The repairs produced new tools, among them Kempe chains, Kummer's ideal numbers and the [[ideal class group|WQ46BD3ARY]], and the study of hyperbolic geometry.
Errors surfaced through an expert reader (Heawood, Liouville), a referee (Katz), or a later author who studied the proof closely (Écalle and Ilyashenko).

### Watch out

A false proof built on purpose, such as a "proof" that $1 = 2$, is not in this class, since its author knows the error and nobody accepts the result.
An open [[conjecture|WMEMMHZ3BH]] that nobody claims to have proved is not an incorrect proof either.
Also, a wrong first proof says nothing against the theorem, and a published proof is not checked in every step just because it was refereed.

### Try it

Kempe's argument also handles a vertex with at most four neighbors.
Does Heawood's map show that this part is wrong too?
No: the counterexample needs five neighbors, and the cases with at most four neighbors are correct.

In which ring does Lamé's key step first fail?
In $\mathbb{Z}[\zeta_{23}]$, the first case where factorization into irreducible elements is not unique.

## Explanations

### L1 human

Sometimes a great mathematician publishes a proof, other experts read it and agree, and years later someone finds a mistake.
In 1879 Kempe "proved" that four colors are enough to color any map so that neighboring countries have different colors.
In 1890 Heawood found a map where one step of Kempe's argument does not work.
The statement was still true, but a correct proof came only in 1976, with the help of a computer.
So every step of a proof needs a reason, even a step that seems evident to everyone.

### L2 human

We test the assumption that broke Lamé's argument in a simpler ring, $R = \{a + b\sqrt{-5} : a, b \in \mathbb{Z}\}$.
The [[field norm|KRNFEZWPY0]] $N(a + b\sqrt{-5}) = a^2 + 5b^2$ is multiplicative.
In $R$, $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$, and the norms of the four factors are $4$, $9$, $6$ and $6$.
No element has norm $2$ or $3$, since $a^2 + 5b^2 \in \{2, 3\}$ forces $b = 0$ and then $a^2 \in \{2, 3\}$.
So a proper factor of any of the four elements is impossible, and all four are [[irreducible|0YMT0D2442]].
The units are the elements of norm $1$, namely $\pm 1$, so $2$ is not a unit times $1 \pm \sqrt{-5}$.
So $6$ has two essentially different factorizations, and $R$ is not a [[unique factorization domain|0W4X9G6263]].

The same example, seen through prime elements, appears in [[irreducible and prime elements in this ring|5BM35ES8WK]].
The typical use of this check is to test a ring for unique factorization before an argument relies on it.
Watch out for carrying a property of $\mathbb{Z}$ into a larger ring without proof, which is exactly Lamé's step.

### L3 human

The famous errors share a structure: a lemma true in a familiar case is used in a wider case where it fails, or a case analysis misses a configuration.
For Lamé the familiar case is $\mathbb{Z}$, and the failure in $\mathbb{Z}[\zeta_p]$ is measured by the class group of the [[cyclotomic field|NN77VYSGXR]]; Kummer's condition that $p$ does not divide the class number defines [[regular primes|B4VK33PCXZ]].
For Kempe the missed configuration is the interaction of two Kempe chains, and Appel and Haken replaced his single configuration by a large unavoidable set of reducible ones.
Legendre's assumption is one of many statements equivalent to the parallel postulate over the other axioms, and the consistency of hyperbolic geometry shows that none of them follows from those axioms.
Some long or delicate proofs are now checked in proof assistants, which removes the class of errors that come from steps taken as evident.
