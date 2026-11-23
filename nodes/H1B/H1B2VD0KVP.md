---
tag: H1B2VD0KVP
kind: concept
name: Feasibly constructive proof
aliases: [feasible-proof, pv-proof]
msc: ["03F30", "03F20"]
topics: [RA380RWEC0]
audience: research
uses: [01XM7JEKHY, GVT2NKN37K, 1AKKDC17M2, FMM44KFZQT]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: Cook's equational theory
  - url: https://en.wikipedia.org/wiki/Cobham%27s_thesis
    locator: lead section
---

## Summary

Here are two proofs that the product $x \cdot y$ exists.
One adds $x$ to itself $y$ times, and the other follows the binary digits of $y$, as in long multiplication.
Both proofs are constructive, but for a $y$ with $100$ digits the first describes about $2^{100}$ additions and the second about $100$.
A feasibly constructive proof is a proof of the second kind: every function it uses is a [[polynomial-time|GVT2NKN37K]] algorithm, and every induction runs over the digits of a number.

Cook made the notion exact: a feasibly constructive proof is a derivation in his equational theory [[PV|FMM44KFZQT]].
By Buss's witnessing theorem and conservation, proofs of $\forall \Sigma^b_1$ sentences in $\mathsf{PV}_1$ or in $S^1_2$ count as well.
From such a proof of $\forall x \, \exists y \, A(x, y)$ you can read off a polynomial-time algorithm that finds $y$ from $x$.
The notion is the feasible analogue of a [[constructive proof|01XM7JEKHY]], with polynomial time in place of computability.

## Motivation

A constructive proof of an existence statement gives an algorithm, but the algorithm can be far too slow to run.
A proof by ordinary induction on $x$ describes a computation with $x$ steps, and $x$ is exponential in the number of digits of $x$.
Cook asked which proofs give algorithms that are feasible in the sense of Cobham and Edmonds, that is, polynomial-time.
His answer restricts the functions to those built by limited recursion on notation, and the induction to induction on notation.

A second motivation comes from propositional logic.
An equation with a feasibly constructive proof has short proofs of its propositional translations in the extended Frege system.
So the notion connects bounded arithmetic with [[proof complexity|1Q046J0AW2]], and it returns in [[Buss's witnessing theorem|RH4R7GTTAX]] and in the Krajicek-Pudlak-Takeuti theorem.

## Notation

We write $\mathsf{PV} \vdash t = u$ when the equation $t = u$ has a feasibly constructive proof in Cook's sense.
$\mathsf{PV}_1$ is the first-order version of $\mathsf{PV}$, and $S^1_2$ is Buss's first-order theory with polynomial induction for $\Sigma^b_1$ formulas.
"Polynomial time" always refers to the length $\lvert x \rvert$ of the input $x$, not to its value.

## Remarks

### Three small proofs

The successor in dyadic notation is defined by recursion on notation, with one step per digit.
The number $10$ is $s_2(4)$ and $4$ is $s_2(1)$, so the equation $\mathrm{succ}(s_2(y)) = s_1(\mathrm{succ}(y))$ carries twice:
$$\mathrm{succ}(10) = s_1(s_1(\mathrm{succ}(1))) = s_1(s_1(2)) = s_1(5) = 11.$$
The [[successor example|GMVXG3TBP6]] checks the bounding condition and the correctness.

The copying function $c$, with $c(0) = 0$ and $c(s_i(y)) = s_i(c(y))$, equals the identity.
The identity satisfies the same recursion, so the uniqueness rule of $\mathsf{PV}$ gives $c(y) = y$ in one step, as the [[copying example|6AFGGTHR4Y]] shows.

In $S^1_2$ every number has an integer square root.
The [[square root example|2HXW17RBWP]] proves it by polynomial induction on a $\Sigma^b_1$ formula, which halves the input at each step.
Cook also proved in $\mathsf{PV}$ that the extended Frege system is sound.

### What is not feasibly constructive

No proof that $x \mapsto 2^x$ is total is feasibly constructive.
The value $2^x$ has $x + 1$ binary digits, and $x = 1024$ has only $11$, so even writing the answer down takes exponential time.
The [[exponentiation non-example|62ZNJ2YXY0]] gives the count.

Recursion on notation without the bounding condition is not allowed either.
The equations $f(0) = 2$ and $f(s_i(y)) = f(y) \cdot f(y)$ give $f(y) = 2^{2^{d}}$ for a $y$ with $d$ digits, a value with about $2^d$ digits.

### What a feasible proof gives

Every function symbol of $\mathsf{PV}$ is polynomial-time, by induction on its definition, and every polynomial-time function has a symbol, by Cobham's theorem.
A feasibly constructive proof of $\forall x \, \exists y \, A(x, y)$, with $A$ in $\Sigma^b_1$, gives a polynomial-time $f$ with $A(x, f(x))$ for all $x$.
For $S^1_2$ this is [[Buss's witnessing theorem|RH4R7GTTAX]].
An equation proved in $\mathsf{PV}$ has propositional translations with polynomial-size extended Frege proofs, by Cook's theorem.

### Watch out

A true statement about a polynomial-time function need not have a feasibly constructive proof.
The multiplication function is polynomial-time, but the proof of its totality by adding $x$ to itself $y$ times is not feasible, because its induction runs over the value of $y$.
The correct move is to recurse on the digits of $y$.

Measure the cost in the length of the input, not in its value.
A loop with $x$ rounds looks small for $x = 1000$, but for an input with $100$ digits it has about $2^{100}$ rounds.

### History

Cobham characterized the polynomial-time functions by limited recursion on notation in 1965.
Cook introduced the term in the title of his paper *Feasibly constructive proofs and the propositional calculus*, at STOC 1975, and made it exact with $\mathsf{PV}$.
Buss's theory $S^1_2$, from his 1985 thesis published in 1986, gave a first-order setting.
Extended by the $\mathsf{PV}$ symbols, it proves the same $\forall \Sigma^b_1$ sentences as $\mathsf{PV}_1$.

### Try it

First, is the function $x \mapsto x \cdot x$ given by a $\mathsf{PV}$ symbol?
Yes: it is polynomial-time, so Cobham's theorem gives a symbol, and the value has at most $2 \lvert x \rvert$ binary digits.

Second, is $x \mapsto 2^{\lvert x \rvert}$ given by a $\mathsf{PV}$ symbol?
Yes: its value is $1$ followed by $\lvert x \rvert$ zeros in binary, so it is written down in polynomial time, and Cobham's theorem gives a symbol.

Third, why does a proof by ordinary induction on $x$ of $\forall x \, \exists y \, (y = x \cdot x)$ fail to be feasibly constructive, although the statement is true?
The induction runs $x$ times, which is exponential in $\lvert x \rvert$; the statement has a feasible proof, but this proof is not one.

## Explanations

### L1 human

A constructive proof that something exists shows how to find it.
A feasibly constructive proof shows how to find it fast.
Fast means that the work grows like a power of the number of digits of the input, for example the square of the number of digits.
Long multiplication of two numbers with $10$ digits takes about $100$ digit operations, so it is fast in this sense.
Counting up to a number with $10$ digits, one step at a time, takes billions of steps, so it is not fast.

### L2 human

Let us prove that the copying function is the identity, as a feasibly constructive proof.
The copying function $c$ has the equations $c(0) = 0$ and $c(s_i(y)) = s_i(c(y))$ for $i = 1, 2$.
The identity satisfies $\mathrm{id}(0) = 0$ and $\mathrm{id}(s_i(y)) = s_i(\mathrm{id}(y))$, so both follow the same recursion with $g = 0$ and $h_i(y, z) = s_i(z)$.
The uniqueness rule of $\mathsf{PV}$ then gives the equation below:
$$c(y) = \mathrm{id}(y) = y.$$
Unfolding $c(12) = s_2(s_1(s_2(0))) = 12$ only proves the case $y = 12$, and the rule is what covers every $y$ at once.
This is the typical use: prove an algorithm correct inside $\mathsf{PV}$, and get short propositional proofs of its correctness for each input length.

### L3 human

Feasibly constructive proofs relate to polynomial-time computation as intuitionistic proofs relate to computable functions.
The witnessing theorems of bounded arithmetic are the analogue of realizability and of the extraction of programs from proofs.
Stronger theories give larger classes: $S^i_2$ gives $\mathrm{FP}^{\Sigma^p_{i-1}}$.
The two-sorted theories of Cook and Nguyen also give classes below polynomial time, such as uniform $\mathrm{AC}^0$.

The link with [[proof complexity|1Q046J0AW2]] gives a second meaning.
Proofs in $\mathsf{PV}$ correspond to uniform families of extended Frege proofs.
So a superpolynomial lower bound for extended Frege proofs of the translations of a true equation would show that the equation has no feasibly constructive proof.
