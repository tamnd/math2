---
tag: A2CFPP8JMN
kind: concept
name: Bounded arithmetic
aliases: [theories-of-bounded-arithmetic, buss-theories]
msc: ["03F30", "03F20", "68Q15"]
topics: [RA380RWEC0]
audience: research
uses: [T70PYM1F36, GE43CSZTS9, 1QD0KDDGYJ, 3K1AKGXF8A, Z742YPHPNS, GVT2NKN37K, TDQ7AXGM6P]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: Buss's first-order theories
  - url: https://en.wikipedia.org/wiki/Elementary_function_arithmetic
    locator: lead section
---

## Summary

Bounded arithmetic is arithmetic with a speed limit: its theories prove that a number exists only when a fast algorithm can find that number.
The typical formula of these theories looks like this one, which says "$x$ is a perfect square":
$$\exists y \le x \, (y \cdot y = x).$$
The quantifier $\exists y$ only ranges up to $x$, so a machine can decide the formula by trying the values $y = 0, 1, \dots, x$.
Formulas whose quantifiers all carry such bounds are the bounded formulas, and the theories of bounded arithmetic allow induction only for them.

The main theories are $\mathsf{I}\Delta_0$, which is [[Robinson arithmetic|3K1AKGXF8A]] plus induction for bounded ([[$\Delta_0$|GE43CSZTS9]]) formulas, the extension $\mathsf{I}\Delta_0 + \Omega_1$, and Buss's theories $S^i_2$ and $T^i_2$ for $i \ge 0$.
Buss's theories use the language below, where $\lvert x \rvert$ is the length of $x$ in binary and $x \# y = 2^{\lvert x \rvert \cdot \lvert y \rvert}$ is the smash function:
$$L_2 = \{ 0, S, +, \cdot, \lfloor x/2 \rfloor, \lvert x \rvert, \#, \le \}.$$
$T^i_2$ has ordinary induction for $\Sigma^b_i$ formulas, and $S^i_2$ has the weaker polynomial induction for $\Sigma^b_i$ formulas.
The aim is that the provably total functions of each theory, defined in the right way, form a complexity class.
For $S^1_2$ the class is the polynomial-time functions, so $S^1_2$ is a formal model of feasible reasoning, in the way that [[Peano arithmetic|HACXBCM7SS]] is a formal model of ordinary number theory.

## Motivation

A proof in Peano arithmetic that a number exists can promise a witness far too large to write down.
Induction on a formula $\exists y \, \mathrm{Exp}(x, y)$, which says that $2^x$ exists, proves that $2^x$ exists for every $x$, and $2^x$ has $x + 1$ binary digits, which is exponential in the length of $x$.
Parikh asked which proofs give witnesses of feasible size, and he showed by [[Parikh's theorem|YPQPC1WJMV]] that $\mathsf{I}\Delta_0$ gives witnesses below a polynomial in $x$.

A polynomial in $x$ is still exponential in the length $\lvert x \rvert$, so $\mathsf{I}\Delta_0$ does not yet match polynomial time.
Buss chose the language $L_2$ and the induction schemes so that the match becomes exact.
A proof of $\forall x \, \exists y \, A(x, y)$ in $S^1_2$, with $A$ in $\Sigma^b_1$, gives a [[polynomial-time|GVT2NKN37K]] algorithm that finds $y$ from $x$.
So questions of complexity theory become questions about provability, and back.
For example, the [[Krajíček-Pudlák-Takeuti theorem|YP7KE8E6DC]] shows that if the hierarchy of the theories $S^i_2$ collapses, then the [[polynomial hierarchy|TDQ7AXGM6P]] collapses.

## Notation

We write $\lvert x \rvert = \lceil \log_2(x + 1) \rceil$ for the binary length, so $\lvert 0 \rvert = 0$ and $\lvert 5 \rvert = 3$, and $x \# y$ for the smash function.
A bounded quantifier has the form $\forall x \le t$ or $\exists x \le t$, with $x$ not in the term $t$, and it is sharply bounded when $t$ has the form $\lvert s \rvert$.
The classes $\Sigma^b_i$ and $\Pi^b_i$ count the alternations of bounded quantifiers, and the sharply bounded quantifiers do not count.
The schemes $\Sigma^b_i$-$\mathsf{IND}$ and $\Sigma^b_i$-$\mathsf{PIND}$ are ordinary induction and polynomial induction for $\Sigma^b_i$ formulas, and $\mathsf{BASIC}$ is Buss's finite set of open axioms for the symbols of $L_2$.
Watch out: in this subject $\lvert x \rvert$ is never an absolute value, since every object is a natural number.
A second tradition, that of Cook and Nguyen, works with two sorts, numbers and binary strings, and names its theories $V^i$; the Remarks give a translation table.

## Remarks

### Lengths and the smash function

Why does Buss add the strange function $\#$?
Look at the lengths of numbers.
The number $5$ is $101$ in binary and $8$ is $1000$, so $\lvert 5 \rvert = 3$ and $\lvert 8 \rvert = 4$.
Then the smash of the two numbers is a power of two:
$$5 \# 8 = 2^{3 \cdot 4} = 2^{12} = 4096.$$
Check: $4096$ is $1$ followed by $12$ zeros in binary, so it has $13 = 3 \cdot 4 + 1$ digits.

In general $\lvert x \# y \rvert = \lvert x \rvert \cdot \lvert y \rvert + 1$, so smash multiplies lengths, just as $\cdot$ adds them roughly.
A term built from $+$, $\cdot$ and $\#$ therefore has a length that is a polynomial in the lengths of its inputs.
For example, $x \# x = 2^{\lvert x \rvert^2}$ and $(x \# x) \# x = 2^{(\lvert x \rvert^2 + 1) \lvert x \rvert}$.
So the terms of $L_2$ can bound every output of a polynomial-time machine, which writes at most polynomially many digits.
They can never bound $2^x$, which has $x + 1$ digits, exponentially many in $\lvert x \rvert$.

### The induction schemes

The schemes differ in how far each step moves.
For a formula $A$ in $\Sigma^b_i$, ordinary induction steps from $x$ to $x + 1$:
$$A(0) \land \forall x \, (A(x) \to A(x + 1)) \to \forall x \, A(x).$$
Polynomial induction steps from $\lfloor x/2 \rfloor$ to $x$, by adding one binary digit:
$$A(0) \land \forall x \, (A(\lfloor x/2 \rfloor) \to A(x)) \to \forall x \, A(x).$$
Then $T^i_2 = \mathsf{BASIC} + \Sigma^b_i$-$\mathsf{IND}$ and $S^i_2 = \mathsf{BASIC} + \Sigma^b_i$-$\mathsf{PIND}$, and $S_2$ and $T_2$ are the unions over $i$.

To reach $x$ by polynomial induction you need about $\lvert x \rvert$ steps, not $x$ steps.
This is why a proof in $S^1_2$ can run as a fast recursion on the digits of the input, as in [[the proof that integer square roots exist|2HXW17RBWP]].
The class $\Sigma^b_0$ is the class of formulas with only sharply bounded quantifiers.
The class $\Sigma^b_{i+1}$ is the closure of $\Pi^b_i$ under $\land$, $\lor$, sharply bounded quantifiers and bounded existential quantifiers, and $\Pi^b_{i+1}$ is defined dually.
For $i \ge 1$, the sets of natural numbers defined by $\Sigma^b_i$ formulas are exactly the sets in the class $\Sigma^p_i$ of the polynomial hierarchy, so $\Sigma^b_1$ matches [[NP|QQRA9GBW51]].

### A chain of theories

The weakest theory is $\mathsf{I}\Delta_0$, a [[fragment of Peano arithmetic|T70PYM1F36]].
By Parikh's theorem it cannot prove that $2^x$ is total, since $2^x$ is not bounded by any polynomial.
[[The theory $\mathsf{I}\Delta_0 + \Omega_1$|V8WD1F0NS2]] adds the axiom that $x^{\lvert x \rvert}$ exists, and that axiom gives exactly the growth rate of $x \# x$.
Buss's theories sit in one chain, in which the inclusions hold for $i \ge 1$:
$$S^1_2 \subseteq T^1_2 \subseteq S^2_2 \subseteq T^2_2 \subseteq \dots \subseteq S^i_2 \subseteq T^i_2 \subseteq S^{i+1}_2 \subseteq \dots$$
So $S_2 = T_2$, and $T_2$ proves the same theorems as $\mathsf{I}\Delta_0 + \Omega_1$, once the two languages are translated into each other.

Each theory has its own class of functions.
The $\Sigma^b_1$-definable functions of $S^1_2$ are the polynomial-time functions, by [[Buss's witnessing theorem|RH4R7GTTAX]], and more generally the $\Sigma^b_i$-definable functions of $S^i_2$ are the class $\mathrm{FP}^{\Sigma^p_{i-1}}$.
Buss and Krajíček showed that the $\Sigma^b_1$-definable functions of $T^1_2$ come from polynomial local search problems.
[[Cook's theory PV|FMM44KFZQT]] has a function symbol for each polynomial-time algorithm, and $S^1_2$, extended by these symbols, proves the same $\forall \Sigma^b_1$ sentences as $\mathsf{PV}_1$, the first-order version of $\mathsf{PV}$.
Whether the chain is strict is an [[open problem|PEJQDHHX8E]].

### What is not bounded arithmetic

[[Elementary function arithmetic|2JD80TE553]] has only bounded induction, but it adds an axiom saying that $2^x$ is total.
So its provably total functions outgrow every bound $2^{p(\lvert x \rvert)}$, and [[the non-example on EFA|S09CTN8JZ4]] works out the numbers.
The theory $\mathsf{I}\Sigma_1$ fails for another reason: its induction is for unbounded formulas, and induction on $\exists y \, \mathrm{Exp}(x, y)$ proves $2^x$ total.

Robinson arithmetic fails the other way.
Its witnesses are small, but it has no induction at all, so it does not even prove $x + y = y + x$.
It serves as a base theory, not as a model of feasible reasoning.

### Two naming traditions

Cook and Nguyen use two sorts, numbers and finite sets of numbers, which they read as binary strings.
The RSUV isomorphism reads a number $x$ of the one-sorted theory as the string of its binary digits, so the length $\lvert x \rvert$ becomes a number of the two-sorted theory.
The table matches the main theories.
The line $V^1$ and $S^1_2$ is the one used most: both capture polynomial time.

| Buss (one sort) | Cook and Nguyen (two sorts) | How they are related | Definable functions |
|---|---|---|---|
| $\mathsf{I}\Delta_0$ | $V^0$ | $V^0$ is conservative over $\mathsf{I}\Delta_0$ | $\mathrm{FAC}^0$, for $V^0$ |
| $S^i_2$, $i \ge 1$ | $V^i$ | RSUV isomorphic | $\mathrm{FP}^{\Sigma^p_{i-1}}$; for $i = 1$, $\mathrm{FP}$ |
| $T^i_2$, $i \ge 1$ | $TV^i$ | RSUV isomorphic | $\mathrm{FP}^{\Sigma^p_i}$, for $\Sigma^b_{i+1}$ definitions |
| $\mathsf{PV}$ | $\mathsf{VPV}$ | $\mathsf{VPV}$ is the two-sorted version of $\mathsf{PV}$ | $\mathrm{FP}$ |

The last column of the $T^i_2$ line uses a theorem of Buss: $S^{i+1}_2$ is conservative over $T^i_2$ for $\forall \exists \Sigma^b_{i+1}$ sentences.

### Watch out

Buss's theorem needs the right class of formulas.
It applies to $\forall x \, \exists y \, A$ with $A$ in $\Sigma^b_1$, and a formula in $\Pi^b_1$ does not count.
A formula that is $\Delta^b_1$ in the standard model counts only when $S^1_2$ proves it equivalent to a $\Sigma^b_1$ formula.

A second slip is to think that these theories prove only bounded sentences.
$\mathsf{I}\Delta_0$ proves $\forall x \, \exists y \, (y = x \cdot x)$, which has an unbounded $\exists y$.
Parikh's theorem only says that a bound for the witness exists, here $y \le x \cdot x$.

### History

Parikh studied $\mathsf{I}\Delta_0$ in 1971 and proved his bounding theorem.
Cook defined the equational theory $\mathsf{PV}$ in 1975.
Wrathall showed in 1978 that the sets defined by $\Delta_0$ formulas, the rudimentary sets, form the linear-time hierarchy.
Buss introduced $S^i_2$ and $T^i_2$ in his 1985 Princeton thesis, published as the book *Bounded Arithmetic* in 1986.
He took the smash function from Nelson's work on predicative arithmetic.
Krajíček, Pudlák and Takeuti linked the collapse of the hierarchy of theories to the polynomial hierarchy in 1991.

### Try it

First, compute $\lvert 12 \rvert$ and $12 \# 3$.
Since $12$ is $1100$ in binary and $3$ is $11$, the lengths are $4$ and $2$, so $12 \# 3 = 2^8 = 256$.

Second, classify $\forall y \le x \, \exists i \le \lvert x \rvert \, (y + i = x)$.
The $\exists i$ is sharply bounded and does not count, so the formula is $\Pi^b_1$.

Third, can a theory of bounded arithmetic prove $\forall x \, \exists y \, (y = x \# x)$?
Yes, $S^1_2$ proves it with the term $x \# x$ as witness.
But $\mathsf{I}\Delta_0$ cannot prove the totality of $x \mapsto x \# x$, written with a $\Delta_0$ formula for its graph, because $2^{\lvert x \rvert^2}$ is not bounded by a polynomial in $x$.

## Explanations

### L1 human

Ordinary proofs about numbers sometimes say "there is a number with this property" without a fast way to find it.
Bounded arithmetic is a set of rules for proofs in which every promised number can be found by a fast computer program.
Fast means that the running time grows like a polynomial in the number of digits of the input.
For example, a proof that every number has a square gives the program "multiply the number by itself".
For a number with $10$ binary digits, schoolbook multiplication takes about $10 \cdot 10 = 100$ digit steps.
A proof that $2^x$ exists for every $x$ is not allowed, because $2^x$ has $x + 1$ binary digits, far too many to write down.

### L2 human

Here is a typical small problem: show that $S^1_2$ proves that every number is even or odd, and read off an algorithm from the proof.
The sentence to prove is the following:
$$\forall x \, \exists y \le x \, (x = y + y \lor x = y + y + 1).$$
Its matrix is open and its one existential quantifier is bounded, so the part after $\forall x$ is a $\Sigma^b_1$ formula.
The axioms $\mathsf{BASIC}$ say that $x = \lfloor x/2 \rfloor + \lfloor x/2 \rfloor$ or $x = \lfloor x/2 \rfloor + \lfloor x/2 \rfloor + 1$, and from this $S^1_2$ proves $\lfloor x/2 \rfloor \le x$.
So the term $y = \lfloor x/2 \rfloor$ is a witness, and no induction is needed at all.
For $x = 13$ the witness is $6$, and $13 = 6 + 6 + 1$.
The algorithm is "drop the last binary digit", which takes time linear in $\lvert x \rvert$.

The problem shows the typical use in its simplest form: a proof of a $\forall \Sigma^b_1$ sentence carries an algorithm for the witness.
When the proof uses polynomial induction, the witness is no longer one term but a recursion on the binary digits, as in the [[integer square root|2HXW17RBWP]].

### L3 human

The theories $S^i_2$ and $T^i_2$ match the levels of the polynomial hierarchy, in the way that the theories $\mathsf{I}\Sigma_n$ match the levels of the [[arithmetical hierarchy|7CVJCQKY41]].
The [[provably total functions|Z742YPHPNS]] of $\mathsf{I}\Sigma_1$ are the primitive recursive functions, and the analogue for $S^1_2$ is the class of polynomial-time functions.
The two-sorted theories of Cook and Nguyen extend the picture below polynomial time: $V^0$ matches $\mathrm{AC}^0$, and other theories match logarithmic space and $\mathrm{NC}^1$.

Bounded arithmetic is also the uniform side of [[proof complexity|1Q046J0AW2]].
Proofs in a bounded theory translate into families of short proofs in a propositional proof system.
The [[Paris-Wilkie translation|ZVD982MVST]] does this for bounded-depth Frege systems, and Cook's translation of $\mathsf{PV}$ does it for extended Frege systems.
So the open problems about the theories, such as the [[pigeonhole principle|NJ18EZ5JBC]] and the separation of the hierarchy, are tied to $\mathrm{P} \ne \mathrm{NP}$ and to lower bounds for proof systems.
