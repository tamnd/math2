---
tag: DC60FYCSPM
kind: concept
name: Second-order arithmetic
msc: ["03F35", "03B30"]
topics: [BY8AAFN7C5]
audience: grad
uses: [D8SD54M5PN, 3K1AKGXF8A, 1QD0KDDGYJ, 5GS6DRJ5SY, G6X7SZSNC5, P0H5NYX8Z0, HACXBCM7SS]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: Models
same_as:
  wikidata: Q7442973
  wikipedia: Second-order arithmetic
---

## Summary

The number $\sqrt{2}$ is not a natural number, but it can be stored as a set of natural numbers: the set of codes of the fractions $1, 1, 5/4, 11/8, 22/16, \dots$ that approach it.
Second-order arithmetic is the theory that talks about natural numbers and about sets of natural numbers, and with such codes it can talk about most of analysis and countable algebra.

Second-order arithmetic $\mathsf{Z}_2$ is a first-order theory with two sorts of variables.
Number variables range over natural numbers, and set variables range over sets of natural numbers.
The language has $0$, $1$, $+$, $\cdot$ and $<$ on numbers, and the membership relation $n \in X$.
The axioms are the basic axioms for $0$, $1$, $+$, $\cdot$ and $<$ in the style of [[Robinson arithmetic|3K1AKGXF8A]], the induction axiom for sets, and the [[comprehension schema|5GS6DRJ5SY]] for every formula $\varphi(n)$ in which $X$ is not free.
The schema reads:
$$\exists X \, \forall n \, \big( n \in X \leftrightarrow \varphi(n) \big).$$
The [[definition of second-order arithmetic|Y92NXGEQBD]] states the axioms in full.
A model is a pair $(M, \mathcal{S})$ of a structure for the numbers and a family of subsets of its domain, and an $\omega$-model is a model whose numbers are the standard natural numbers.

## Motivation

[[Peano arithmetic|HACXBCM7SS]] speaks only about single numbers, but a real number is an infinite object.
To speak about reals, continuous functions and countable groups, a theory must quantify over infinite sets of numbers.
Set theory can do this, but it assumes far more than analysis uses.
Hilbert and Bernays saw that most of analysis needs only sets of natural numbers.
A real is a sequence of rationals, a sequence is a set of pairs, and a continuous function is fixed by countably many rational data.

So $\mathsf{Z}_2$ is the natural frame for the question "how much set existence does this theorem need?"
Its subsystems restrict comprehension and induction to smaller classes of formulas.
Each subsystem allows a different stock of sets, and [[reverse mathematics|7SQS69T17R]] measures a theorem by the weakest subsystem that proves it.
The base system [[RCA0|XQENB067R3]] and the four stronger systems after it are all subsystems of this one theory.

## Notation

The language is written $L_2$.
Lower-case letters $i, j, k, m, n$ are number variables, and upper-case letters $X, Y, Z$ are set variables.
A formula is arithmetical when it has no set quantifiers, and free set variables are allowed in it as parameters.
The classes $\Sigma^0_n$ and $\Pi^0_n$ are the [[arithmetical classes|GE43CSZTS9]], counted by number quantifiers, now with the extra atomic formulas $t \in X$.
The classes $\Sigma^1_n$ and $\Pi^1_n$ count alternations of set quantifiers in front of an arithmetical formula.
An $\omega$-model is written $(\mathbb{N}, \mathcal{S})$, or only $\mathcal{S}$, with $\mathcal{S} \subseteq \mathcal{P}(\mathbb{N})$.
Older books write $\mathsf{Z}_2$ as $\mathsf{PA}_2$ or call it "analysis".
A subscript $0$, as in $\mathsf{ACA}_0$, means that the system has restricted induction, not the induction scheme for all formulas.

## Remarks

### From real numbers to sets

The fractions for $\sqrt{2}$ come from one rule.
For each $k$, let $m_k$ be the largest natural number with $m_k^2 \le 2 \cdot 4^k$, and put $q_k = m_k / 2^k$.
For $k = 3$ this gives $m_3 = 11$, because of the two inequalities
$$11^2 = 121 \le 128 = 2 \cdot 4^3 < 144 = 12^2.$$
So $q_3 = 11/8 = 1.375$, and $\sqrt{2} \approx 1.4142$ lies in $[q_3, q_3 + 2^{-3})$.
A pair $(k, q_k)$ becomes one number by a pairing map, and the whole list becomes one set of numbers.
The [[coding of the square root of two|QY29R8PF9Z]] checks every step.
In the same way a sequence is a set of pairs, a countable group is a set with its operation coded as a set of triples, and a continuous function is a set of rational data.

### The full model and smaller models

The intended model is $(\mathbb{N}, \mathcal{P}(\mathbb{N}))$, where every subset of $\mathbb{N}$ is a set of the model.
There every comprehension instance holds, since the set that $\varphi$ defines is a subset of $\mathbb{N}$; the [[full model|CAA7K3VF59]] checks all axioms.
Smaller families of sets can fail comprehension.
The [[computable sets|W4J2H41PB7]] are not a model of $\mathsf{Z}_2$, because the halting set is defined by a $\Sigma^0_1$ formula and is not computable.
They are a model of the much weaker system $\mathsf{RCA}_0$, and this is the first hint of how the subsystems match levels of computability.

### What is not second-order arithmetic

Peano arithmetic is not second-order arithmetic: it has no set variables, so it cannot even state comprehension.
Its theorems are the arithmetical theorems of $\mathsf{ACA}_0$, by the [[conservativity of ACA0 over PA|HPA6HX3114]].
Full [[second-order logic|G6X7SZSNC5]] with the second-order Peano axioms is not $\mathsf{Z}_2$ either.
That theory forces the set variables to range over all subsets, and it then has only one model up to isomorphism.
$\mathsf{Z}_2$ is read with [[Henkin semantics|P0H5NYX8Z0]], so it has models $(M, \mathcal{S})$ with $\mathcal{S} \ne \mathcal{P}(M)$.
The [[Heaviside function|5W961M41F5]] shows a limit of the language itself: no code of $L_2$ represents a function from $\mathbb{R}$ to $\mathbb{R}$ with a jump.

### The first properties

With comprehension, the single induction axiom gives the induction scheme for every $L_2$ formula: form the set that the formula defines, then apply the axiom to it.
So every axiom of Peano arithmetic is a theorem of $\mathsf{Z}_2$.
$\mathsf{Z}_2$ has a computable set of axioms and contains Peano arithmetic, so the [[first incompleteness theorem|X9WYNYE29C]] applies, and some arithmetical sentence is undecided if $\mathsf{Z}_2$ is consistent.
$\mathsf{Z}_2$ is a first-order theory, so the [[compactness theorem|1NR3HAWG9D]] gives models with non-standard numbers.
The downward Löwenheim-Skolem theorem gives countable $\omega$-models, whose families $\mathcal{S}$ are countable.

### Watch out

The name suggests second-order logic, but $\mathsf{Z}_2$ is a two-sorted first-order theory, and the completeness theorem holds for it.
Next, an $\omega$-model fixes the numbers and not the sets.
The structure of computable sets is an $\omega$-model of $\mathsf{RCA}_0$, although it misses most subsets of $\mathbb{N}$.
Last, a subsystem with subscript $0$ proves induction only for the formulas whose sets it can form or for the class it names.
For example, $\mathsf{RCA}_0$ proves induction for $\Sigma^0_1$ formulas, and not in general for $\Sigma^0_2$ formulas.

### History

Hilbert and Bernays developed a large part of analysis in a system of this kind in the second volume of *Grundlagen der Mathematik* (1939).
Harvey Friedman began the study of its subsystems with restricted comprehension and induction, in his address at the International Congress of Mathematicians in Vancouver in 1974.
Stephen Simpson's book *Subsystems of Second Order Arithmetic* (1999, second edition 2009) became the standard reference.

### Try it

First, which set does comprehension give for the formula $\exists k \le n \, (k + k = n)$?
It gives the set of even numbers $\{0, 2, 4, \dots\}$, because $n$ satisfies the formula exactly when $n = 2k$ for some $k$.

Second, is $(\mathbb{N}, \{\emptyset, \mathbb{N}\})$ an $\omega$-model of $\mathsf{Z}_2$?
No: the formula $n = 0$ defines the set $\{0\}$, and that set is not in the family.

## Explanations

### L1 human

Ordinary arithmetic talks about whole numbers, such as $3$ and $17$.
Second-order arithmetic also talks about sets of whole numbers, such as the set of even numbers.
A real number such as $\sqrt{2}$ can be stored as a set of whole numbers that lists better and better fractions for it.
In this way the theory can talk about real numbers, sequences and functions.
Its main axiom says that the numbers with a property that the language can state form a set.
Most of calculus can be done inside this theory.

### L2 human

We prove with comprehension and induction that every nonempty set $X$ has a least element.
Suppose that $X$ has no least element.
Comprehension gives the set of numbers below which $X$ has no member:
$$Y = \{ n : \forall m \le n \, (m \notin X) \}.$$
Then $0 \in Y$, since $0 \in X$ would make $0$ the least element of $X$.
If $n \in Y$ and $n + 1 \notin Y$, then $n + 1 \in X$ and all smaller numbers are outside $X$, so $n + 1$ is least, which is impossible.
So $Y$ is closed under $n \mapsto n + 1$, the induction axiom gives $Y = \mathbb{N}$, and $X$ is empty.

The formula that defines $Y$ has only a bounded number quantifier, so the same proof works in the weak base system $\mathsf{RCA}_0$.
This is the typical use of $\mathsf{Z}_2$: fix a subsystem, and check which comprehension instances a proof uses.
The trap is to use a formula with set quantifiers, or with unbounded number quantifiers, inside a subsystem that does not allow it.

### L3 human

Second-order arithmetic sits between first-order arithmetic and set theory.
The sets definable in the full model form the [[analytical hierarchy|M6JGF4TPM6]], the lightface version of the projective sets of descriptive set theory.
The subsystems of $\mathsf{Z}_2$ are the scale of [[reverse mathematics|7SQS69T17R]].
Their $\omega$-models are families of sets with closure properties from computability theory, such as Turing ideals for $\mathsf{RCA}_0$ and jump ideals for $\mathsf{ACA}_0$.
The [[proof-theoretic ordinals|C72RBH0CDR]] of the five main subsystems are known, and they reach $\psi(\Omega_\omega)$ for $\Pi^1_1\text{-}\mathsf{CA}_0$.
An ordinal analysis of full $\mathsf{Z}_2$ is an open problem.
Higher-order arithmetic adds variables for sets of sets, and the sub-area on [[higher-order reverse mathematics|NPDRXTBW5W]] uses it for discontinuous functions.
