---
tag: NPDRXTBW5W
kind: concept
name: Higher-order reverse mathematics
aliases: [higher-order-reverse-mathematics]
msc: ["03B30", "03F35", "03D65"]
topics: [BY8AAFN7C5]
audience: research
uses: [DC60FYCSPM, XQENB067R3, NAASTN80QN, 330YAP9Y4Q, 0X3WGX95FE, 0ZH5AJ2ED7]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Use of higher-order arithmetic
---

## Summary

Second-order arithmetic cannot name a function with a jump, so it cannot even state many theorems about arbitrary functions on the reals.
*Higher-order reverse mathematics* asks the reverse-mathematics question in a language with objects of all finite types: numbers, functions, functionals on functions, and so on.
Ulrich Kohlenbach set up the modern framework in 2005, with the base system $\mathsf{RCA}_0^\omega$.
This base system proves the same sentences of [[second-order arithmetic|DC60FYCSPM]] as [[RCA0|XQENB067R3]], so the classification of the usual theorems carries over.
What the framework adds is the ability to state theorems about discontinuous functions and uncountable families directly, without codes.

## Motivation

In $\mathsf{RCA}_0$ a real number is a sequence of rationals.
A [[continuous function|0X3WGX95FE]] $f \colon \mathbb{R} \to \mathbb{R}$ is coded by a set of numbers that lists rational approximations, and only continuous functions have such codes.
A discontinuous function such as the Heaviside function, a functional on [[Baire space|0ZH5AJ2ED7]], or a covering of $[0, 1]$ indexed by all reals cannot be named by a set of numbers.
So second-order arithmetic cannot state many theorems of analysis in their usual form.
Higher types give names to these objects: a function from reals to reals is an object of type $1 \to 1$.
Then one can ask which axioms prove such theorems too.

## Notation

The finite types are built from type $0$, the natural numbers, by the rule that $\sigma \to \tau$ is a type when $\sigma$ and $\tau$ are.
Type $1 = 0 \to 0$ is the type of functions $\mathbb{N} \to \mathbb{N}$, and type $2 = 1 \to 0$ is the type of functionals on Baire space.
The base system $\mathsf{RCA}_0^\omega$ is Kohlenbach's $\mathsf{E}\text{-}\mathsf{PRA}^\omega + \mathsf{QF}\text{-}\mathsf{AC}^{1,0}$.
It is [[primitive recursive arithmetic|330YAP9Y4Q]] in all finite types with extensionality and quantifier-free induction, plus the axiom of choice from type $1$ to type $0$ for quantifier-free formulas.
Kleene's quantifier $(\exists^2)$ is the following axiom.
$$\exists \varphi^{2}\, \forall f^{1}\, \big(\varphi(f) = 0 \leftrightarrow \exists n\, f(n) = 0\big)$$
$\mathsf{ACA}_0^\omega$ denotes $\mathsf{RCA}_0^\omega + (\exists^2)$.
Kleene's $(\exists^3)$ is the same axiom one type higher: a functional of type $3$ that decides $\exists f^1\, Y(f) = 0$ for each $Y$ of type $2$.

## Remarks

### Worked examples

Over $\mathsf{RCA}_0^\omega$, $(\exists^2)$ gives a discontinuous function $\mathbb{R} \to \mathbb{R}$, and the [[example on the Heaviside function|KC1TH9ETSW]] builds it.
Over $\mathsf{RCA}_0^\omega$, $(\exists^2)$ also proves arithmetical comprehension, and the [[example on arithmetical comprehension|PSACC4KCBN]] gives the induction on formulas.
A third example is the statement NIN: for every $Y \colon [0, 1] \to \mathbb{N}$ there are $x \ne y$ with $Y(x) = Y(y)$.
It is a form of the uncountability of $\mathbb{R}$, and Normann and Sanders studied its strength.

### Non-examples

The Heaviside function cannot be coded in second-order arithmetic, so the classical framework cannot even state that it exists, and the [[non-example|5W961M41F5]] proves this.
A theorem about continuous functions on $[0, 1]$, such as the intermediate value theorem, needs no higher types.
The conservation result below gives it the same strength in both frameworks.

### Basic properties

1. $\mathsf{RCA}_0^\omega$ is conservative over $\mathsf{RCA}_0$ for sentences of second-order arithmetic, by Kohlenbach.
   The proof interprets the higher types by the extensional continuous functionals, so that every object of higher type becomes a code that is a set of numbers.
2. Over $\mathsf{RCA}_0^\omega$, $(\exists^2)$ is equivalent to the existence of a discontinuous function $F \colon \mathbb{R} \to \mathbb{R}$, by Kohlenbach.
   One direction is the Heaviside example, and the other uses Grilliot's trick, which recovers $(\exists^2)$ from any point of discontinuity.
3. $\mathsf{RCA}_0^\omega$ does not prove that a discontinuous function exists, so by property 2 it does not prove $(\exists^2)$.
   The interpretation of property 1 gives a model in which every function $\mathbb{R} \to \mathbb{R}$ is continuous.
4. $\mathsf{ACA}_0^\omega$ proves every axiom of [[ACA0|NAASTN80QN]].
5. Normann and Sanders showed that NIN is not provable in $\mathsf{Z}_2^\omega$, the union of the systems that add to $\mathsf{RCA}_0^\omega$ the comprehension functionals for $\Pi^1_k$ formulas.
   NIN is provable in $\mathsf{Z}_2^\Omega = \mathsf{RCA}_0^\omega + (\exists^3)$.
6. Normann and Sanders also showed that the Heine-Borel theorem for coverings of $[0, 1]$ indexed by all reals is not provable in $\mathsf{Z}_2^\omega$.

### Watch out

Do not read $(\exists^2)$ as the same axiom as arithmetical comprehension.
$\mathsf{ACA}_0$ asserts one set for each formula, while $(\exists^2)$ is a single functional that answers all $\Sigma^0_1$ questions about all functions at once.
Do not treat a code of a continuous function as the function itself.
A code exists only for continuous functions, so "every function $\mathbb{R} \to \mathbb{R}$" in second-order arithmetic means "every coded continuous function".

### History

Kohlenbach introduced the framework in "Higher order reverse mathematics" (2005), as part of his work on the proof theory of analysis.
Kleene's quantifier $\exists^2$ and Feferman's non-constructive $\mu$-operator, which is equivalent to it over the base system, come from the older study of computation in higher types.
Normann and Sanders later used the framework to classify theorems about uncountable objects, and they proved NIN unprovable in $\mathsf{Z}_2^\omega$ in "On the uncountability of $\mathbb{R}$" (Journal of Symbolic Logic, 2022).

### Try it

Show that $(\exists^2)$ decides whether a real $x$ equals $0$.
Answer: the Heaviside example gives a test for $x > 0$, and the same test applied to $-x$ decides $x < 0$.
So $x = 0$ holds exactly when both tests fail, and two calls to $\varphi$ decide it.

## Explanations

### L1 human

Classical reverse mathematics talks only about whole numbers and sets of whole numbers.
It describes a real number or a continuous function by an infinite list of approximations.
A function with a jump, like the switch that is $0$ up to a point and $1$ after it, has no such description.
Higher-order reverse mathematics allows functions of functions as basic objects.
So it can ask which axioms are needed to prove theorems about jumps, about all functions on the reals, and about uncountable families.

### L2 human

Here is how $(\exists^2)$ turns a real number into a yes or no answer, the core of the Heaviside example.

1. Let $x$ be given by rationals $q_n$ with $\lvert q_n - x \rvert \le 2^{-n}$.
2. Then $x > 0$ if and only if $q_n > 2^{-n+1}$ for some $n$.
3. The function with $g(n) = 0$ if $q_n > 2^{-n+1}$ and $g(n) = 1$ otherwise is computable from the $q_n$.
4. The functional $\varphi$ of $(\exists^2)$ answers whether $g$ has a zero, so it decides whether $x > 0$.

The typical use: one shows that a theorem about arbitrary functions implies $(\exists^2)$ by building a discontinuous function from it, and then applies Grilliot's trick.
The trap: a function of type $1 \to 1$ on representations must give equal outputs on equal reals, and this extensionality has to be checked at each step.

### L3 human

The framework separates two kinds of strength that second-order arithmetic merges: comprehension for sets and the existence of functionals.
The results on NIN show how far apart they can be: a statement that is easy to state and true can lie beyond every comprehension functional of $\mathsf{Z}_2^\omega$.
Systems of finite type are also the setting of proof mining, a field Kohlenbach developed.
There [[the Dialectica interpretation|HZ17ES9PDY]] and related functional interpretations extract bounds from proofs.
The study of the functionals themselves, such as $\exists^2$, $\exists^3$ and the Suslin functional, belongs to higher-type computability theory.
