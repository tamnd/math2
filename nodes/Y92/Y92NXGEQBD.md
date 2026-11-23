---
tag: Y92NXGEQBD
kind: definition
name: Second-order arithmetic
msc: ["03F35", "03B30"]
topics: [BY8AAFN7C5]
audience: grad
defines: DC60FYCSPM
uses: [0QFT7Z76N5, 3K1AKGXF8A, 92SWXST1ZM, HYJ10AF6RT, 1QD0KDDGYJ, 5GS6DRJ5SY, BM6P0C2AC2, 0PWX18FM4G, GE43CSZTS9]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: Coding mathematics
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Use of second-order arithmetic
---

## Definition

Second-order arithmetic is the theory of natural numbers and sets of natural numbers in which every formula defines a set.

The language $L_2$ has two sorts of variables.
Number variables $i, j, k, m, n, \ldots$ range over numbers, and set variables $X, Y, Z, \ldots$ range over sets of numbers.
The number terms are built from number variables, the constants $0$ and $1$, and the binary operations $+$ and $\cdot$.
The atomic formulas are $s = t$, $s < t$ and $t \in X$, for number terms $s, t$ and a set variable $X$.
[[Formulas|HYJ10AF6RT]] are built from atomic formulas with the connectives, the number quantifiers $\forall n$, $\exists n$ and the set quantifiers $\forall X$, $\exists X$.
Equality of sets is defined: $X = Y$ abbreviates $\forall n \, (n \in X \leftrightarrow n \in Y)$.

*Second-order arithmetic* $\mathsf{Z}_2$ is the [[theory|92SWXST1ZM]] in $L_2$, with first-order logic for both sorts, whose axioms are the following.

The first group is the basic axioms, the universal closures of these eight formulas:
$$\begin{gathered} n + 1 \ne 0, \qquad m + 1 = n + 1 \to m = n, \qquad m + 0 = m, \qquad m + (n + 1) = (m + n) + 1, \\ m \cdot 0 = 0, \qquad m \cdot (n + 1) = (m \cdot n) + m, \qquad \neg (m < 0), \qquad m < n + 1 \leftrightarrow (m < n \vee m = n). \end{gathered}$$
The second is the induction axiom, a single sentence:
$$\forall X \, \big( (0 \in X \wedge \forall n \, (n \in X \to n + 1 \in X)) \to \forall n \, (n \in X) \big).$$
The third is the comprehension scheme: for every formula $\varphi(n)$ of $L_2$ in which $X$ is not free, the universal closure of
$$\exists X \, \forall n \, \big( n \in X \leftrightarrow \varphi(n) \big).$$
The formula $\varphi$ may have other free number and set variables, and these are the parameters of the instance.

A *subsystem* of $\mathsf{Z}_2$ is a theory in $L_2$ all of whose axioms are theorems of $\mathsf{Z}_2$.

## Notation

Older books call the theory *analysis* or $\mathsf{PA}_2$.
For a class $\Gamma$ of formulas, $\Gamma\text{-}\mathsf{CA}$ is comprehension for the formulas in $\Gamma$.
The induction scheme for $\Gamma$ is written $\Gamma\text{-}\mathsf{IND}$ or $\mathsf{I}\Gamma$, and it consists of the formulas below for $\varphi \in \Gamma$.
$$\big(\varphi(0) \wedge \forall n \, (\varphi(n) \to \varphi(n + 1))\big) \to \forall n \, \varphi(n)$$
The classes $\Sigma^0_k$ and $\Pi^0_k$ are defined as in [[first-order arithmetic|GE43CSZTS9]], with $t \in X$ as an extra atomic formula and with bounded number quantifiers allowed in $\Sigma^0_0$.
A formula is $\Sigma^1_k$ when it has $k$ alternating blocks of set quantifiers, starting with $\exists$, in front of an arithmetical formula, and $\Pi^1_k$ is the same with $\forall$ first.

## Remarks

### Why each axiom is there

The basic axioms fix how $+$, $\cdot$ and $<$ behave, so that every number term has its usual value in the standard numbers.
They are the axioms of [[Robinson arithmetic|3K1AKGXF8A]] in a form adapted to $<$.
The induction axiom is one sentence, not a scheme, and it speaks only about sets.
So it gives induction for a formula only after comprehension has turned the formula into a set.
Comprehension is the axiom that makes sets exist, and it is the axiom that the subsystems cut down.
The usual subsystems keep the basic axioms and the induction axiom, and restrict comprehension, and sometimes add an induction scheme for a class of formulas.

### A small instance and a failing one

Take $\varphi(n)$ to be $\exists k \le n \, (k + k = n)$.
Comprehension gives a set $E$ with $n \in E$ exactly when $\varphi(n)$ holds, and in the standard numbers $E = \{0, 2, 4, \dots\}$.
Check: $4 \in E$ since $2 + 2 = 4$, and $3 \notin E$ since $0 + 0$, $1 + 1$, $2 + 2$ and $3 + 3$ are all different from $3$.

Now take the family of computable sets as the sets of an $\omega$-structure.
The comprehension instance for "program $e$ halts on input $e$" asks for the halting set, which is not computable.
So this structure fails comprehension, as the [[computable sets non-example|W4J2H41PB7]] shows in detail, and it is not a model of $\mathsf{Z}_2$.
The [[concept of second-order arithmetic|DC60FYCSPM]] collects more examples.

### Coding numbers, pairs and sequences

The weak subsystem $\mathsf{RCA}_0$ already proves that the following codes exist, and all later pages use them.
A pair is coded by the one-to-one map $(i, j) = (i + j)^2 + i$.
Check: the pair $(3, 9)$ has code $(3 + 9)^2 + 3 = 147$.
From $147$ we recover $i + j = 12$ as the largest number whose square is at most $147$, and then $i = 147 - 144 = 3$ and $j = 9$.
A finite sequence of numbers is coded by one number, for example with [[Gödel's β-function|BM6P0C2AC2]].
The set of codes of finite sequences is written $\mathbb{N}^{<\mathbb{N}}$, and the set of codes of finite $0$-$1$ sequences is $2^{<\mathbb{N}}$.
A function $f \colon X \to Y$ is a set $f \subseteq X \times Y$ such that each $i \in X$ has exactly one $j$ with $(i, j) \in f$.
Integers are coded by pairs of numbers and rationals by pairs of integers, and their operations and order are defined by bounded formulas.

### Coding reals and spaces

A real number is a sequence $x = (q_k)_{k \in \mathbb{N}}$ of rationals with $\lvert q_k - q_l \rvert \le 2^{-k}$ for all $k < l$.
Two reals $x = (q_k)$ and $y = (r_k)$ are equal when $\lvert q_k - r_k \rvert \le 2^{-k+1}$ for all $k$.
The order $x < y$ holds when $q_k + 2^{-k+1} < r_k$ for some $k$.
So $x < y$ is a $\Sigma^0_1$ statement and $x = y$ is a $\Pi^0_1$ statement, and equality of reals cannot be decided from the codes.
A sequence of reals is a function from $\mathbb{N} \times \mathbb{N}$ to the rationals whose rows are reals.
A countable group is a set $G \subseteq \mathbb{N}$ with its operation coded as a set of triples, and rings, fields, graphs and orders work the same way.
A complete separable metric space is coded by a countable dense set with its distances, and its points are [[Cauchy sequences|0PWX18FM4G]] from the dense set with the rate $2^{-k}$.
A continuous function is coded by a set of quadruples of rational data, and the page on [[RCA0|XQENB067R3]] gives the details.

### Models

A *structure* for $L_2$ is a tuple $(M, \mathcal{S}) = (\lvert M \rvert, \mathcal{S}, +_M, \cdot_M, 0_M, 1_M, <_M)$.
Here $\lvert M \rvert$ is a nonempty set, $\mathcal{S}$ is a family of subsets of $\lvert M \rvert$, and the other entries interpret the symbols on $\lvert M \rvert$.
Number variables range over $\lvert M \rvert$, set variables range over $\mathcal{S}$, and $t \in X$ is membership.
A *model* of a theory in $L_2$ is a structure in which every axiom is true.
An *$\omega$-model* is a model whose number part is the standard structure $(\mathbb{N}, +, \cdot, 0, 1, <)$, so it is determined by its family $\mathcal{S} \subseteq \mathcal{P}(\mathbb{N})$.
The comprehension scheme is the [[comprehension schema|5GS6DRJ5SY]] of second-order logic for unary relations.
With the full semantics, $\mathcal{S} = \mathcal{P}(\lvert M \rvert)$, and the [[second-order Peano axioms|0QFT7Z76N5]] are categorical.
$\mathsf{Z}_2$ uses Henkin semantics instead, so its structures may have $\mathcal{S} \ne \mathcal{P}(\lvert M \rvert)$.

## Explanations

### L1 human

The theory has two kinds of objects: numbers and sets of numbers.
It has the usual rules for adding and multiplying numbers.
It has one rule of induction: a set that contains $0$ and is closed under adding $1$ contains every number.
It has one rule for making sets: each property that the language can express gives a set.
For example, the property "$n$ is even" gives the set $\{0, 2, 4, \ldots\}$.

### L2 human

We use comprehension to get the graph of the squaring function as a set.
Take the formula below, in which the bounds come from $p \ge (i + j)^2 \ge i + j$ for each pair code $p = (i, j)$.
$$\psi(p) := \exists i \le p \, \exists j \le p \, \big( p = (i + j) \cdot (i + j) + i \wedge j = i \cdot i \big)$$
Comprehension gives a set $Q$ that contains exactly the codes of the pairs $(i, i^2)$.
For example, the pair $(3, 9)$ has code $147$, so $147 \in Q$.
For each $i$ there is exactly one $j$ with $(i, j) \in Q$, so $Q$ codes a function $\mathbb{N} \to \mathbb{N}$.
Since $\psi$ has only bounded quantifiers, even $\mathsf{RCA}_0$ proves that $Q$ exists.

The typical use is to turn an object of analysis into a set, and then to ask which comprehension instance makes that set exist.
The trap is to treat codes of reals as reals: two different codes can name the same real, so every definition must respect the coded equality.

### L3 human

The two-sorted presentation is equivalent to a presentation with a sort of functions from $\mathbb{N}$ to $\mathbb{N}$, and to the part of higher-order arithmetic with types $0$ and $1$.
The coding of complete separable metric spaces lets $L_2$ state theorems of functional analysis, such as the Hahn-Banach theorem for separable Banach spaces.
Objects that are not determined by countable data, such as arbitrary functions from $\mathbb{R}$ to $\mathbb{R}$, are outside $L_2$, and [[higher-order reverse mathematics|NPDRXTBW5W]] treats them.
The Henkin reading makes $\mathsf{Z}_2$ a first-order theory, so the completeness and compactness theorems hold for it, at the price of models with non-standard numbers or with few sets.
