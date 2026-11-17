---
tag: ZWK8Q2N6YQ
kind: concept
name: History of group theory
msc: ["20-03"]
topics: [BAZT8JJ70S]
audience: ug1
uses: [G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/History_of_group_theory
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Group_(mathematics)
    locator: History
  - url: https://en.wikipedia.org/wiki/Classification_of_finite_simple_groups
    locator: lead section
---

## Summary

The history of group theory is the story of how the idea of a [[group|G5S1M9]] grew from three separate sources into one abstract theory.
The first source is the theory of [[polynomial|N2EY1EVPRB]] equations, where Lagrange and Galois studied the [[permutations|05RWFKVTJ7]] of the roots.
The second source is number theory, where Gauss and Kronecker worked with structures that are [[abelian groups|082GHNPJ53]] in modern language.
The third source is geometry, where Klein and Lie described a geometry by its group of transformations.
Between 1854 and 1900 these sources met in the abstract definition of a group by axioms.
In the twentieth century, the theory of finite groups led to the [[classification of finite simple groups|06J6P03MG7]], one of the longest proofs in mathematics.
The history shows why the group axioms have their present form: each axiom records a property that all the early examples share.

## Motivation

A student meets the group axioms first and the examples later.
The historical order was the opposite.
Mathematicians worked with permutations of roots, with residues modulo $n$ and with rigid motions for many decades before anybody wrote the axioms.
The history explains why a short list of axioms covers so many different examples.
It also explains the names of many theorems: Lagrange, Cauchy, Cayley, Sylow and Jordan-Hölder.
Several of these theorems were first proved for permutations, and only later for abstract groups.

## Remarks

### Roots of equations (1770 to 1832)

In 1770 and 1771 Joseph-Louis Lagrange published a long study of the methods that solve the equations of degree $2$, $3$ and $4$.
He looked at expressions in the [[roots|019MA1VTR2]] of a polynomial and counted the values that each expression takes when the roots are permuted.
He found that this number of values always divides $n!$, where $n$ is the degree.
In modern language, this is a special case of [[Lagrange's theorem|3C53TD]] for subgroups of the [[symmetric group|0515A6D2Y1]] $S_n$.
Lagrange also saw why his method did not work for degree $5$, but he did not prove that no formula exists.
Paolo Ruffini gave an incomplete proof of this fact in 1799, and Niels Henrik Abel gave a complete proof in 1824.
This result is now the [[Abel-Ruffini theorem|163A2WQQJX]].
Évariste Galois went further, around 1830.
To each polynomial he attached a group of permutations of its roots, now its [[Galois group|0XTY86BZKY]].
He showed that the equation is [[solvable by radicals|J7YS0DA3HQ]] exactly when this group has a special structure, which is now called solvable.
Galois used the word "groupe" in this sense, and he saw the importance of the subgroups that are now called [[normal subgroups|0CB0DX5BVV]].
He died in 1832 at the age of 20.
Joseph Liouville published his papers in 1846, and this publication started [[Galois theory|WNQDKQYZ2R]].

### Permutations and the first theorems (1815 to 1872)

Augustin-Louis Cauchy wrote on permutations in 1815, and again in a long series of papers from 1844 to 1846.
He introduced much of the notation for permutations, and he proved that a group of permutations whose order is divisible by a prime $p$ has an element of order $p$.
This result is now [[Cauchy's theorem|0JM7PA288B]].
Camille Jordan collected the theory of permutation groups and of Galois theory in his book "Traité des substitutions et des équations algébriques" of 1870.
This book was the standard text on groups for the next 30 years.
Jordan also showed that two [[composition series|0XV2A49X6Q]] of a finite group give the same list of factor orders.
In 1872 Ludwig Sylow proved the theorems on subgroups of prime power order that are now the [[Sylow theorems|FESTJ0K9TX]].
Sylow stated them for groups of permutations.
Émile Mathieu found five permutation groups with unusual properties in 1861 and 1873.
These [[Mathieu groups|T1KR4KPX8P]] were later recognized as the first [[sporadic simple groups|PZ49Z4CBFZ]].

### The abstract group (1854 to 1900)

In 1854 Arthur Cayley published the first definition of an abstract finite group.
He described a group by a set of symbols, an associative product and a multiplication table, now called a [[Cayley table|0YB2NRP0T5]].
He listed the groups with $4$ and with $6$ elements, and he observed that each group can be seen as a group of permutations of its own elements.
This observation is now [[Cayley's theorem|0151VYVX27]].
Few mathematicians took up the abstract view at that time.
In 1801 Carl Friedrich Gauss studied the [[integers modulo n|03VFZ2WETT]] and the composition of binary quadratic forms.
Both are abelian groups in modern language, but Gauss did not use the word group.
In 1870 Leopold Kronecker studied finite abelian groups without a reference to permutations.
In 1882 Walther von Dyck gave an axiomatic definition of an abstract group, and he described groups by generators and relations.
This method is now called a [[presentation of a group|0JGEQXQ4AC]].
In 1889 Otto Hölder used [[quotient groups|0KYX2N69J0]] in an abstract form.
He proved that two composition series have the same factor groups, up to [[isomorphism|08MG7H8JW5]] and the order of the list.
This result is now the [[Jordan-Hölder theorem|0E088ZP533]].
The modern axioms ask for associativity, an identity element and inverses, and they include infinite groups.

### Geometry and continuous groups

In 1872 Felix Klein proposed the [[Erlangen program|9QW65PGEPW]].
In this program, a geometry is the study of the properties of a space that a fixed group of transformations does not change.
For example, Euclidean geometry studies the properties that all distance-preserving maps keep.
From the 1870s, Sophus Lie studied continuous groups of transformations, which are now called [[Lie groups|7JBRGCVJRB]].
In the 1880s Henri Poincaré used groups of transformations of the plane, now called [[Fuchsian groups|VNJWSCVP6V]], in the theory of complex functions.
In 1891 Evgraf Fedorov and Arthur Schoenflies, working independently, classified the $230$ symmetry groups of crystals in three dimensions.
These [[crystallographic groups|7KTJKFQT2N]] connect group theory with physics and chemistry.

### Characters, representations and the first textbooks

In 1896 Georg Frobenius began the theory of [[characters|RMWMYBY8TC]] of finite groups.
This theory studies a group through its actions on vector spaces, the [[group representations|WYGRXCG2RN]].
William Burnside published "Theory of Groups of Finite Order" in 1897, and a second edition in 1911.
In 1904 Burnside used characters to prove that a group of order $p^a q^b$, with $p$ and $q$ prime, is solvable.
This result is now [[Burnside's theorem|0FMAQSB1SC]].
In 1902 Burnside also asked a question about finitely generated groups whose elements have finite order, now the [[Burnside problem|XWEMJ7T2XV]].

### Infinite groups and presentations

The presentations of von Dyck led to the study of infinite groups given by generators and relations.
Max Dehn studied such groups with the help of geometry and topology, and in 1911 he posed the [[word problem for groups|PBGTTAVMMT]].
Jakob Nielsen in 1921 and Otto Schreier in 1927 proved that each subgroup of a [[free group|0KTW26C80J]] is free.
This result is now the [[Nielsen-Schreier theorem|W97X7WX5G8]].
This line of work became combinatorial group theory, and later [[geometric group theory|2T3218RXTD]].

### The classification of finite simple groups

A [[simple group|0YMYMNQ0QZ]] is a nontrivial group whose only normal subgroups are the trivial subgroup and the group itself.
By the Jordan-Hölder theorem, the simple groups are the building blocks of all finite groups.
In 1928 Philip Hall began the modern theory of [[solvable groups|0FXJ7YFMMX]], with the subgroups that are now called [[Hall subgroups|KPWW9X14V2]].
In the 1950s Richard Brauer proposed to classify the finite simple groups by the centralizers of their elements of order $2$.
In 1955 Claude Chevalley constructed many families of simple groups from Lie algebras over finite fields, the [[groups of Lie type|NPEBABQ49M]].
In 1963 Walter Feit and John Thompson proved that each finite group of odd order is solvable.
This [[Feit-Thompson theorem|6VK9RSG13Q]] has a proof of about 255 journal pages, and it opened the way to the classification.
In 1965 Zvonimir Janko found a new sporadic group, the first one since the Mathieu groups.
Robert Griess constructed the largest sporadic group, the [[Monster group|C9VY20TAPT]], in 1982.
The classification states that each finite simple group is cyclic of prime order, an [[alternating group|0Z5905Q73D]], a group of Lie type or one of $26$ sporadic groups.
Its proof is spread over several hundred journal articles by about 100 authors.
The last gap, the case of the quasithin groups, was closed by Michael Aschbacher and Stephen Smith in 2004.
In 2012 a team led by Georges Gonthier completed a computer-checked proof of the Feit-Thompson theorem.

### Timeline

| Year | Person | Event |
|---|---|---|
| 1770 to 1771 | Lagrange | Studies the permutations of the roots of an equation. |
| 1799 | Ruffini | Gives an incomplete proof that the general quintic has no solution by radicals. |
| 1801 | Gauss | Integers modulo $n$ and composition of quadratic forms. |
| 1815 | Cauchy | First paper on permutations. |
| 1824 | Abel | Proves that the general quintic has no solution by radicals. |
| about 1830 | Galois | Attaches a group to an equation and uses the word "groupe". |
| 1844 to 1846 | Cauchy | Series of papers on permutation groups, with Cauchy's theorem. |
| 1846 | Liouville | Publishes the papers of Galois. |
| 1854 | Cayley | First definition of an abstract finite group. |
| 1861 and 1873 | Mathieu | Finds the Mathieu groups. |
| 1870 | Jordan | "Traité des substitutions". |
| 1870 | Kronecker | Studies finite abelian groups in abstract form. |
| 1872 | Sylow | Proves the Sylow theorems. |
| 1872 | Klein | Erlangen program. |
| 1882 | von Dyck | Axiomatic definition and presentations by generators and relations. |
| 1889 | Hölder | Quotient groups and the Jordan-Hölder theorem. |
| 1891 | Fedorov, Schoenflies | Classify the $230$ crystallographic groups in three dimensions. |
| 1896 | Frobenius | Begins character theory. |
| 1897 | Burnside | "Theory of Groups of Finite Order". |
| 1904 | Burnside | Proves the $p^a q^b$ theorem. |
| 1921 and 1927 | Nielsen, Schreier | Subgroups of free groups are free. |
| 1928 | P. Hall | Theory of solvable groups and Hall subgroups. |
| 1955 | Chevalley | Constructs the Chevalley groups. |
| 1963 | Feit, Thompson | Groups of odd order are solvable. |
| 1965 | Janko | Finds the first new sporadic group since Mathieu. |
| 1982 | Griess | Constructs the Monster group. |
| 2004 | Aschbacher, Smith | Close the quasithin case of the classification. |
| 2012 | Gonthier and others | Computer-checked proof of the Feit-Thompson theorem. |

### Common errors

1. Lagrange did not prove "the order of a subgroup divides the order of the group". He proved a statement about the values of expressions in the roots, and the abstract theorem came much later.
2. The early theorems were about groups of permutations. Cauchy and Sylow proved their theorems for permutation groups, and Frobenius gave an abstract proof of the Sylow theorem in 1887.
3. Cayley wrote the first abstract definition in 1854, but few mathematicians used it before the 1880s.

## Explanations

### L1 human

Group theory began with a puzzle about equations.
School algebra has a formula for the solutions of $x^2 + bx + c = 0$.
Similar formulas exist for equations with $x^3$ and with $x^4$, but not for equations with $x^5$.
In the years around 1800 to 1830, Ruffini, Abel and Galois found the reason.
Galois looked at the ways to shuffle the solutions of an equation, and these shuffles form a group.
Later, mathematicians saw the same kind of structure in numbers, in geometry and in crystals.
So they wrote down the few rules that all these examples share, and these rules are the group axioms.

### L2 human

We follow one calculation of Lagrange, with the four roots $x_1, x_2, x_3, x_4$ of an equation of degree $4$.
Take the expression $y = x_1 x_2 + x_3 x_4$, and permute the four roots in all $4! = 24$ ways.

1. The expression $y$ splits the four roots into two pairs: $\{x_1, x_2\}$ and $\{x_3, x_4\}$.
2. A permutation of the roots sends this splitting to another splitting into two pairs.
3. There are exactly $3$ splittings of four roots into two pairs, so $y$ takes at most $3$ values.
4. The $3$ values are $x_1 x_2 + x_3 x_4$, $x_1 x_3 + x_2 x_4$ and $x_1 x_4 + x_2 x_3$, and suitable permutations give each of them.
5. The permutations that fix $y$ form a subgroup of $S_4$ with $8$ elements: $24 / 3 = 8$.
6. The number of values, $3$, divides $24$, as Lagrange observed.

In the language of this area, the $8$ permutations form a subgroup $H$ of $S_4$, and the $3$ values match the $3$ cosets of $H$.
So the observation of Lagrange is the equation $|S_4| = 3 \cdot |H|$, a case of Lagrange's theorem.
Lagrange used the $3$ values as the roots of a cubic equation, and so he reduced degree $4$ to degree $3$.
The same idea fails for degree $5$, and Galois explained why with the structure of the group $S_5$.
A trap is to read modern theorems into old texts.
Lagrange counted values of expressions, and he had no word for a group or a subgroup.

### L3 human

The history of group theory is a model for the axiomatic method of modern algebra.
A structure appears first in many concrete cases: permutations, residues, quadratic forms and motions.
The axioms then isolate what the cases share, and theorems proved from the axioms apply to all cases at once.
The same development happened for vector spaces, rings and fields, and later for topological spaces and categories.
In the language of category theory, a group is a category with one object in which each morphism is invertible.
The two main lines of the twentieth century go on today.
For finite groups, the classification of finite simple groups is complete, and a second-generation proof by Gorenstein, Lyons and Solomon is in progress.
For infinite groups, geometric group theory studies a finitely generated group through the geometry of its [[Cayley graph|0GYQK9NDJF]].
The later sub-areas of this area follow a similar order: subgroups and cosets, homomorphisms and quotients, [[group actions|0WCY42EV9V]], Sylow theory, composition series and simple groups.
