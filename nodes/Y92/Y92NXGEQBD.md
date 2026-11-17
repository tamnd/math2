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

The language $L_2$ of second-order arithmetic has two sorts of variables.
Number variables $i, j, k, m, n, \ldots$ range over numbers, and set variables $X, Y, Z, \ldots$ range over sets of numbers.
The number terms are built from number variables, the constants $0$ and $1$, and the binary operations $+$ and $\cdot$.
The atomic formulas are $s = t$, $s < t$ and $t \in X$, for number terms $s, t$ and a set variable $X$.
[[Formulas|HYJ10AF6RT]] are built from atomic formulas with the connectives, number quantifiers $\forall n$, $\exists n$ and set quantifiers $\forall X$, $\exists X$.
Equality of sets is defined: $X = Y$ abbreviates $\forall n\, (n \in X \leftrightarrow n \in Y)$.

*Second-order arithmetic* $\mathsf{Z}_2$ is the [[theory|92SWXST1ZM]] in $L_2$, with the usual first-order logic for both sorts, whose axioms are the following.

1. The basic axioms, for all numbers $m, n$:
   - $n + 1 \ne 0$, and $m + 1 = n + 1 \to m = n$;
   - $m + 0 = m$, and $m + (n + 1) = (m + n) + 1$;
   - $m \cdot 0 = 0$, and $m \cdot (n + 1) = (m \cdot n) + m$;
   - $\neg (m < 0)$, and $m < n + 1 \leftrightarrow (m < n \vee m = n)$.
2. The induction axiom:
$$\forall X\, \big( (0 \in X \wedge \forall n\, (n \in X \to n + 1 \in X)) \to \forall n\, (n \in X) \big).$$
3. The comprehension scheme: for every formula $\varphi(n)$ of $L_2$ in which $X$ is not free, the universal closure of
$$\exists X\, \forall n\, \big( n \in X \leftrightarrow \varphi(n) \big).$$

The formula $\varphi$ may have other free number variables and set variables; they are the parameters of the instance.

A *subsystem* of $\mathsf{Z}_2$ is a theory in $L_2$ all of whose axioms are theorems of $\mathsf{Z}_2$.
The usual subsystems keep the basic axioms and restrict comprehension and induction to classes of formulas.

## Notation

The theory is also called *analysis* or $\mathsf{PA}_2$ in older books.
For a class $\Gamma$ of formulas, $\Gamma\text{-}\mathsf{CA}$ denotes comprehension for formulas in $\Gamma$, and $\Gamma\text{-}\mathsf{IND}$ or $\mathsf{I}\Gamma$ denotes the induction scheme
$$\big(\varphi(0) \wedge \forall n\, (\varphi(n) \to \varphi(n + 1))\big) \to \forall n\, \varphi(n)$$
for formulas $\varphi \in \Gamma$.
The arithmetical classes $\Sigma^0_k$, $\Pi^0_k$ are defined as in [[first-order arithmetic|GE43CSZTS9]], with $t \in X$ as an extra atomic formula and with bounded number quantifiers allowed in $\Sigma^0_0$.
A formula is $\Sigma^1_k$ when it has the form $\exists X_1 \forall X_2 \cdots \theta$ with $k$ alternating blocks of set quantifiers and $\theta$ arithmetical, and likewise for $\Pi^1_k$.

## Remarks

### Coding

Inside the weak subsystem $\mathsf{RCA}_0$ the following codes are available, and all later pages use them.

- Pairs. The pairing map $(i, j) = (i + j)^2 + i$ is one-to-one from $\N \times \N$ to $\N$, and $X \times Y$ is the set of codes $(i, j)$ with $i \in X$ and $j \in Y$.
- Finite sequences. A finite sequence of numbers is coded by one number, for example with [[Gödel's β-function|BM6P0C2AC2]]. The set of codes of finite sequences is written $\N^{<\N}$, and the set of codes of finite $0$-$1$ sequences is $2^{<\N}$.
- Functions. A function $f \colon X \to Y$ is a set $f \subseteq X \times Y$ such that each $i \in X$ has exactly one $j$ with $(i, j) \in f$.
- Rational numbers. Integers are coded by pairs of numbers, and rationals by pairs of integers, with the usual operations and order, which are defined by bounded formulas.
- Real numbers. A real number is a sequence $x = (q_k)_{k \in \N}$ of rationals with $\abs{q_k - q_l} \le 2^{-k}$ for all $k < l$. Two reals $x = (q_k)$ and $y = (r_k)$ are equal when $\abs{q_k - r_k} \le 2^{-k+1}$ for all $k$, and $x < y$ when $q_k + 2^{-k+1} < r_k$ for some $k$.
- Sequences of reals. A sequence of reals is a function from $\N \times \N$ to the rationals whose rows are reals.
- Countable structures. A countable group is a set $G \subseteq \N$ with the group operation coded as a set of triples, and the same works for rings, fields, vector spaces, graphs and orders.
- Separable spaces. A complete separable metric space is coded by a countable dense set with its rational distances, and its points are [[Cauchy sequences|0PWX18FM4G]] from the dense set with a fixed rate of convergence.
- Continuous functions. A continuous function between such spaces is coded by a set of quadruples of basic balls; the page on [[RCA0|XQENB067R3]] gives the details.

Every coded notion uses only sets of numbers, so second-order arithmetic can state theorems about these objects.
The statement $x < y$ is $\Sigma^0_1$, and $x = y$ is $\Pi^0_1$, so equality of reals is not decidable from the codes.

### Models

A *structure* for $L_2$ is a tuple $(M, \mathcal{S}) = (|M|, \mathcal{S}, +_M, \cdot_M, 0_M, 1_M, <_M)$, where $|M|$ is a nonempty set, $\mathcal{S}$ is a family of subsets of $|M|$, and the other entries interpret the symbols on $|M|$.
Number variables range over $|M|$, set variables range over $\mathcal{S}$, and $t \in X$ is interpreted by membership.
A *model* of a theory in $L_2$ is a structure in which every axiom is true.
An *$\omega$-model* is a model whose number part is the standard structure $(\N, +, \cdot, 0, 1, <)$; it is determined by its family $\mathcal{S} \subseteq \mathcal{P}(\N)$.

### Relation to second-order logic

The comprehension scheme is the [[comprehension schema|5GS6DRJ5SY]] of second-order logic for unary relations.
With the full semantics, where $\mathcal{S} = \mathcal{P}(|M|)$, the [[second-order Peano axioms|0QFT7Z76N5]] are categorical.
$\mathsf{Z}_2$ uses the Henkin semantics: its structures may have $\mathcal{S} \ne \mathcal{P}(|M|)$.

## Explanations

### L1 human

The theory has two kinds of objects: numbers and sets of numbers.
It has the usual rules for adding and multiplying numbers.
It has one rule of induction for sets: a set that contains $0$ and is closed under adding $1$ contains every number.
It has one rule for making sets: each property that the language can express gives a set.
For example, the property "$n$ is even" gives the set $\set{0, 2, 4, \ldots}$.

### L2 human

We check that the comprehension scheme gives the set of even numbers and the graph of the squaring function.

1. Take $\varphi(n) := \exists k \le n\, (k + k = n)$. Comprehension gives a set $E$ with $n \in E \leftrightarrow \varphi(n)$.
2. In the standard model, $E = \set{0, 2, 4, \ldots}$, since $4 = 2 + 2$ and no $k \le 3$ has $k + k = 3$.
3. Take $\psi(p) := \exists i \le p\, \exists j \le p\, (p = (i + j) \cdot (i + j) + i \wedge j = i \cdot i)$. Here $i \le p$ and $j \le p$ hold for each pair code $p = (i, j)$, since $p \ge (i + j)^2 \ge i + j$.
4. Comprehension gives a set $Q$ of the pairs $(i, i^2)$. The pair $(3, 9)$ has code $(3 + 9)^2 + 3 = 147$, so $147 \in Q$.
5. For each $i$ there is exactly one $j$ with $(i, j) \in Q$, so $Q$ codes a function $\N \to \N$.

The typical use is to turn an object of analysis into a set, and then to ask which comprehension axiom makes that set exist.
A trap is to treat the codes of reals as reals: two different codes can name the same real, so every definition must respect the equality of reals.

### L3 human

The two-sorted presentation is equivalent to a one-sorted presentation in a language with a function sort, and to the restriction of higher-order arithmetic to types $0$ and $1$.
The coding of complete separable metric spaces lets one state theorems of functional analysis, such as the Hahn-Banach theorem for separable Banach spaces, in $L_2$.
Uncountable objects that are not determined by countable data, such as arbitrary functions from $\mathbb{R}$ to $\mathbb{R}$, are outside $L_2$; higher-order reverse mathematics treats them.
The Henkin reading makes $\mathsf{Z}_2$ a first-order theory, so it has the completeness and compactness theorems, at the price of models with non-standard numbers or with few sets.
