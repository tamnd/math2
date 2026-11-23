---
tag: Z742YPHPNS
kind: concept
name: Provably total function
aliases: [provably-recursive-function]
msc: ["03F30", "03D20"]
topics: [T6FK1E7GJ1]
audience: grad
uses: [MPSCREYC3M, KZSB5E471K, CV2E6JZHVP, 5NVA2JRHPV, 1QD0KDDGYJ, R6ZC4BJGXV]
sources:
  - url: https://en.wikipedia.org/wiki/Fast-growing_hierarchy
    locator: Points of interest
  - url: https://en.wikipedia.org/wiki/Primitive_recursive_function
    locator: Relationship to recursive functions
---

## Summary

A theory proves a function total when it proves that a program for the function halts on every input.
The functions that a theory can prove total measure its strength in the language of growth rates, and they are the main tool for natural independence results.

Precisely, let $T$ be a theory that contains basic arithmetic.
A function $f : \mathbb{N} \to \mathbb{N}$ is *provably total* in $T$ if there is a $\Sigma_1$ formula $\varphi(x, y)$ that defines the graph of $f$ in $\mathbb{N}$ and
$$T \vdash \forall x\, \exists y\, \varphi(x, y).$$
For [[Peano arithmetic|MPSCREYC3M]] these are the functions below the level $\varepsilon_0$ of the [[fast-growing hierarchy|R6ZC4BJGXV]], and for $\mathrm{I}\Sigma_1$ they are the [[primitive recursive functions|5NVA2JRHPV]].

## Motivation

Many true statements of number theory have the form $\forall x\, \exists y\, \varphi(x, y)$ with $\varphi$ decidable.
Such a statement says that the function "least $y$ with $\varphi(x, y)$" is defined everywhere.
So a theory proves the statement exactly when it proves this witness function total.

This turns unprovability into a question about speed.
If the witness function grows faster than every provably total function of $T$, then $T$ cannot prove the statement.
This is how [[Goodstein's theorem|XQMNJF241J]], the [[Kirby-Paris hydra|C028FF4TWM]] and the [[Paris-Harrington theorem|509ZWA0R26]] escape $\mathsf{PA}$.
The [[fast-growing hierarchy|R6ZC4BJGXV]] and the [[Hardy hierarchy|X8RKXQASR9]] give the scale on which the speeds are compared.

## Notation

A formula is $\Sigma_1$ if it has the form $\exists z\, \theta$ where $\theta$ has only bounded quantifiers, as in the [[arithmetical hierarchy|CV2E6JZHVP]].
$\mathrm{I}\Sigma_n$ is the theory of the basic axioms for $0$, successor, $+$, $\cdot$ and $<$, with the [[induction schema|1QD0KDDGYJ]] for $\Sigma_n$ formulas only.
We say that $g$ *eventually dominates* $f$ if $f(x) < g(x)$ for all large enough $x$.
Many books say *provably recursive* in place of provably total, and some require the formula $\varphi$ to describe a Turing machine computation.
For theories that contain $\mathrm{I}\Sigma_1$ the two versions give the same class of functions.

## Remarks

### A first example

Take the function $x \mapsto 2^x$.
A $\Sigma_1$ definition of its graph says: there is a coded list $s = \langle 1, 2, 4, \dots, y \rangle$ of length $x + 1$ in which each entry is twice the one before.
To prove totality, we show by induction on $x$ that such a list exists.
For $x = 0$ the list $\langle 1 \rangle$ works, and a list for $x$ extends to a list for $x + 1$ by adding twice its last entry.
The induction is on a $\Sigma_1$ formula, so $\mathrm{I}\Sigma_1$ can carry it out, and [[exponentiation is provably total in IΣ1|PCXE6QYCDR]].

The [[Ackermann function|SXAKCZYGVE]] needs more.
Its totality proof is a double induction, and the outer induction is on a $\Pi_2$ formula.
$\mathsf{PA}$ allows this, but $\mathrm{I}\Sigma_1$ does not, and in fact the Ackermann function is provably total in $\mathsf{PA}$ but not in $\mathrm{I}\Sigma_1$.

### Examples and non-examples

Every $f_\alpha$ of the fast-growing hierarchy with $\alpha < \varepsilon_0$ is provably total in $\mathsf{PA}$, by induction up to $\alpha$, which $\mathsf{PA}$ proves for each such $\alpha$.
The function [[$f_{\varepsilon_0}$ is not|Z2JK9QHKWF]], although it is total and computable.
The length function $L$ of Goodstein sequences is another total computable function that $\mathsf{PA}$ does not prove total.
A function that is not computable, such as the busy beaver function, is provably total in no theory at all.
The reason is that a total function with a $\Sigma_1$ graph is computable: search for the least witness, so the busy beaver function has no $\Sigma_1$ definition of its graph.

### The characterization theorems

Three theorems describe the provably total functions of the standard theories.

1. Kreisel: the provably total functions of $\mathsf{PA}$ are the functions defined by recursion along well-orders of type below $\varepsilon_0$.
2. Wainer and Schwichtenberg: a function is provably total in $\mathsf{PA}$ exactly when it is computable with a running time bounded by some $f_\alpha$ with $\alpha < \varepsilon_0$.
   In particular each provably total function of $\mathsf{PA}$ is eventually dominated by some such $f_\alpha$.
3. Parsons, and independently Mints: the provably total functions of $\mathrm{I}\Sigma_1$ are the primitive recursive functions.

From theorem 2, a function that eventually dominates every $f_\alpha$ with $\alpha < \varepsilon_0$ is not provably total in $\mathsf{PA}$.
That is the step behind every unprovability proof by growth rate.

### No theory gets them all

If $T$ is sound for $\Sigma_1$ sentences, every provably total function of $T$ is total and computable.
But if $T$ has a computable set of axioms, its provably total functions are not all the total computable functions.
List them as $h_0, h_1, h_2, \dots$ by running through the proofs of $T$.
Then $x \mapsto h_x(x) + 1$ is total and computable, but it differs from each $h_i$ at the input $i$.

### Watch out

Provable totality is a property of a function together with a definition.
Two $\Sigma_1$ formulas can define the same graph in $\mathbb{N}$, while $T$ proves totality for one and not for the other.
For example, let $\varphi$ define $x \mapsto 0$ and let $\varphi'$ say "$y = 0$ and the Goodstein sequence of $x$ reaches $0$".
Both define the zero function in $\mathbb{N}$, but $\mathsf{PA}$ proves $\forall x\, \exists y\, \varphi'(x, y)$ only if it proves Goodstein's theorem, which it does not.
By the definition, a function counts as provably total when at least one defining formula works.

A second slip: "not provably total" does not mean "not total".
The non-examples above are total, and stronger theories prove it.

### History

Georg Kreisel characterized the provably recursive functions of $\mathsf{PA}$ through recursion along ordinals below $\varepsilon_0$, with the methods of [[Gentzen's consistency proof|QPV0HNP22S]] of 1936.
Stanley Wainer and Helmut Schwichtenberg described them through the fast-growing hierarchy.
Charles Parsons, and independently Grigori Mints, showed that $\mathrm{I}\Sigma_1$ proves total exactly the primitive recursive functions.

### Try it

First, is $x \mapsto x^2$ provably total in $\mathrm{I}\Sigma_1$?
Yes, since it is primitive recursive, and $\mathrm{I}\Sigma_1$ proves every primitive recursive function total.

Second, why is $f_\omega$ not provably total in $\mathrm{I}\Sigma_1$?
Because $f_\omega$ is not primitive recursive, as it eventually dominates each $f_n$, and $\mathrm{I}\Sigma_1$ proves only primitive recursive functions total.

## Explanations

### L1 human

A computer program computes a function when it stops on every input.
A system of axioms may or may not be able to prove that a given program always stops.
The functions whose programs a theory can prove to stop are its provably total functions.
For example, a program that doubles $1$ again and again $x$ times computes $2^x$, and weak axioms already prove that it stops.
Stronger theories can prove that faster-growing functions are total.

### L2 human

Here is how the notion gives unprovability, worked for Goodstein's theorem.
The statement is "for every $m$ there is $k$ with $G_k = 0$", and the test $G_k = 0$ is decidable.
Let $L(m)$ be the least such $k$, so $L(3) = 6$ and $L(2) = 4$.
If $\mathsf{PA}$ proved the statement, $L$ would be provably total in $\mathsf{PA}$.
Then theorem 2 would give some $\alpha < \varepsilon_0$ with $L(m) < f_\alpha(m)$ for all large $m$.
But $L(m) = H_{o_2(m)}(3) - 2$, and this escapes every such bound for infinitely many $m$.
So $\mathsf{PA}$ does not prove the statement.
The example shows the typical use: find the witness function, then compare it with the fast-growing hierarchy.

### L3 human

The provably total functions are a coarse invariant: theories with the same $\Pi_2$ consequences have the same provably total functions.
For theories with an [[ordinal analysis|C5E5TG8PGP]], they are usually the functions dominated by $f_\alpha$ with $\alpha$ below the [[proof-theoretic ordinal|C72RBH0CDR]], for a suitable choice of fundamental sequences.
The [[indicators|JWTZ8NVVGK]] of Paris and Kirby give the same information from the side of models.
The [[Hardy hierarchy|X8RKXQASR9]] gives the length functions of Goodstein sequences and hydra battles on the same scale.
