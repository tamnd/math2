---
tag: FMM44KFZQT
kind: definition
name: Cook's theory PV
aliases: [pv, cooks-equational-theory, pv1]
msc: ["03F30", "03F20", "68Q15"]
topics: [RA380RWEC0]
audience: research
defines: H1B2VD0KVP
uses: [1AKKDC17M2, GVT2NKN37K, A2CFPP8JMN, 1Q046J0AW2]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: Cook's equational theory
  - url: https://en.wikipedia.org/wiki/Cobham%27s_thesis
    locator: lead section
---

## Definition

$\mathsf{PV}$ is an [[equational theory|1AKKDC17M2]] with a function symbol for each polynomial-time algorithm.
We follow Cook and write numbers in dyadic notation.
Every $n \ge 1$ has exactly one form $s_1(m) = 2m + 1$ or $s_2(m) = 2m + 2$ with $m < n$, so $n$ is a string over the digits $1$ and $2$.
The function symbols and their defining equations are introduced together, in stages called ranks.

1. **Initial functions.** There is a fixed finite set of initial functions.
   Among them are the constant $0$, the successors $s_1$ and $s_2$, and $\mathrm{Tr}(x)$, which deletes the last dyadic digit of $x$.
2. **Composition.** If $f$ and $g_1, \dots, g_k$ are symbols, then there is a symbol $h$ with the defining equation $h(\bar x) = f(g_1(\bar x), \dots, g_k(\bar x))$.
3. **Limited recursion on notation.** Let $g$, $h_1$, $h_2$, $l_1$, $l_2$ be symbols of rank at most $k$.
   Assume that $\mathsf{PV}$ derives, at rank $k$, equations that bound $h_i(\bar x, y, z)$ by the concatenation of the dyadic strings $z$ and $l_i(\bar x, y)$, for $i = 1, 2$.
   Then there is a symbol $f$ of rank $k + 1$ with the defining equations below.

$$f(\bar x, 0) = g(\bar x), \qquad f(\bar x, s_i(y)) = h_i(\bar x, y, f(\bar x, y)) \quad (i = 1, 2).$$

The theorems of $\mathsf{PV}$ are the equations that follow from the defining equations by four kinds of rules.
The equality rules give $t = t$, give $u = t$ from $t = u$, and give $t = v$ from $t = u$ and $u = v$.
Substitution gives $t(r) = u(r)$ from $t(x) = u(x)$, for every term $r$.
Congruence gives $f(\dots, t, \dots) = f(\dots, u, \dots)$ from $t = u$.
The **uniqueness rule**, a form of induction on notation, applies when $f_1$ and $f_2$ provably satisfy the equations of item 3 for the same $g$, $h_1$ and $h_2$.
It then gives $f_1(\bar x, y) = f_2(\bar x, y)$.

A [[feasibly constructive proof|H1B2VD0KVP]], in Cook's sense, is a derivation in $\mathsf{PV}$.

## Notation

Later books write numbers in binary, with $s_0(x) = 2x$, $s_1(x) = 2x + 1$ and recursion on $\lfloor y/2 \rfloor$, and the resulting theory has the same strength.
The name $\mathsf{PV}$ also stands for the set of its function symbols, as in $\mathrm{dWPHP}(\mathsf{PV})$.
$\mathsf{PV}_1$ is the first-order theory in the language of $\mathsf{PV}$ whose axioms are universal sentences.
They include every equation that $\mathsf{PV}$ proves, and axioms that replace induction for open formulas.
$\mathsf{VPV}$ is the two-sorted theory of Cook and Nguyen built on $\mathsf{PV}$.

## Remarks

### A first computation

Here is the successor in dyadic notation, a legal $\mathsf{PV}$ symbol by limited recursion on notation.
Its equations are $\mathrm{succ}(0) = s_1(0)$, $\mathrm{succ}(s_1(y)) = s_2(y)$ and $\mathrm{succ}(s_2(y)) = s_1(\mathrm{succ}(y))$.
The number $6$ is $s_2(2)$ and $2$ is $s_2(0)$, so two carries happen:
$$\mathrm{succ}(6) = s_1(\mathrm{succ}(2)) = s_1(s_1(\mathrm{succ}(0))) = s_1(s_1(1)) = s_1(3) = 7.$$
Check: $6 + 1 = 7$.
The [[successor example|GMVXG3TBP6]] verifies the bound and the correctness for all $y$.

### Why each rule is there

Composition and recursion on notation are Cobham's rules for the [[polynomial-time|GVT2NKN37K]] functions, and Cobham's theorem says they give all of them.
Recursion on notation runs once per digit of $y$, not once per unit of $y$.
So a number with $100$ digits costs $100$ rounds, where ordinary recursion would cost about $2^{100}$.

The bounding condition keeps the values short.
Without it, the equations $f(0) = 2$ and $f(s_i(y)) = f(y) \cdot f(y)$ square the value once per digit.
Then $f(y) = 2^{2^{d}}$ for a $y$ with $d$ digits, and writing this value down takes about $2^d$ digits, which is not polynomial in $d$.

The uniqueness rule is the only form of induction in $\mathsf{PV}$.
Without it, $\mathsf{PV}$ can only unfold definitions on numerals, so it proves $c(12) = 12$ for the copying function $c$ but not $c(y) = y$ for a variable $y$.
The [[copying example|6AFGGTHR4Y]] gives the proof of $c(y) = y$ with the rule.

### What has no symbol

The function $x \mapsto 2^x$ has no $\mathsf{PV}$ symbol.
Every symbol has values whose length is polynomial in the length of the inputs, and $2^x$ has $x + 1$ binary digits.
The [[exponentiation non-example|62ZNJ2YXY0]] gives the count.

### Proofs and propositional logic

Cook proved that each equation of $\mathsf{PV}$ translates into a family of propositional tautologies, one for each input length.
These tautologies have polynomial-size proofs in the extended Frege system, and the proofs can be built in polynomial time.
This is the start of the link between bounded arithmetic and [[proof complexity|1Q046J0AW2]].

The first-order theory $\mathsf{PV}_1$ proves the same equations as $\mathsf{PV}$.
It is a universal theory, so [[Herbrand's theorem|VZ21F10WRS]] applies to it, and that is the first step of the [[Krajicek-Pudlak-Takeuti theorem|YP7KE8E6DC]].
Buss's theory $S^1_2$, extended by the $\mathsf{PV}$ symbols, proves the same $\forall \Sigma^b_1$ sentences as $\mathsf{PV}_1$, by [[Buss's witnessing theorem|RH4R7GTTAX]].

### Watch out

Do not confuse recursion on notation with ordinary recursion on $y$.
Defining $x \cdot y$ by adding $x$ to itself $y$ times gives a function that is polynomial-time, but the definition is not a $\mathsf{PV}$ definition.
For $y = 2^{100}$ it runs $2^{100}$ rounds, while recursion on the digits of $y$ runs about $100$.

Do not treat the bound in item 3 as a side remark.
It is a derivation inside $\mathsf{PV}$ at a lower rank, so the language and the theory grow together.

### History

Cobham characterized the polynomial-time functions by limited recursion on notation in 1965.
Cook defined $\mathsf{PV}$, in dyadic notation, in *Feasibly constructive proofs and the propositional calculus*, at STOC 1975, and he proved the translation into extended Frege proofs there.
Krajíček, Pudlák and Takeuti introduced $\mathsf{PV}_1$ in 1991.

## Explanations

### L1 human

$\mathsf{PV}$ is a set of rules for fast computer programs, together with rules for proving that two programs give the same answers.
Each program is built from simple pieces, for example "add a digit at the end of a number".
A program may repeat a step once for each digit of its input, but not once for each unit of its value.
For the number $1000$, which has $10$ binary digits, this means about $10$ repetitions, not $1000$.
To prove two programs equal, you show that both follow the same digit-by-digit recipe.

### L2 human

Let us compute $\mathrm{succ}(5)$ and then $\mathrm{succ}(6)$ from the defining equations, and see that each digit costs one step.
The number $5$ is $s_1(2)$, since $5 = 2 \cdot 2 + 1$, so the second equation applies at once:
$$\mathrm{succ}(5) = \mathrm{succ}(s_1(2)) = s_2(2) = 6.$$
The number $6$ is $s_2(2)$, so the third equation applies, and a carry moves to $2 = s_2(0)$:
$$\mathrm{succ}(6) = s_1(\mathrm{succ}(2)) = s_1(s_1(\mathrm{succ}(0))) = s_1(s_1(s_1(0))) = 7.$$
The last digit $1$ stops the carry after one step, and the digit $2$ passes it on.
So $\mathsf{PV}$ is a base theory in which a correctness proof follows the digits, and each such proof gives short extended Frege proofs of its propositional translations.

### L3 human

$\mathsf{PV}$ is to polynomial time what primitive recursive arithmetic is to the primitive recursive functions.
Both are quantifier-free theories with a symbol for each function of the class and induction as a rule.
Its first-order extension $\mathsf{PV}_1$ is the bottom of the hierarchy of theories used in the proof of the Krajicek-Pudlak-Takeuti theorem.
In the two-sorted setting of Cook and Nguyen the same theory reappears as $\mathsf{VPV}$.

The link with proof complexity is the main reason for the interest in $\mathsf{PV}$.
$\mathsf{PV}_1$ proves that extended Frege is sound, and extended Frege p-simulates every proof system that $\mathsf{PV}_1$ proves sound.
So the strength of $\mathsf{PV}_1$ and the strength of extended Frege are two views of one object.
Extensions such as $\mathsf{PV}_1 + \mathrm{dWPHP}(\mathsf{PV})$ give the [[approximate counting|65K2S22DGZ]] theories for randomized algorithms.
