---
tag: ~25aedb3b
kind: concept
name: Provably total function
aliases: [provably-recursive-function]
msc: ["03F30", "03D20"]
topics: [T6FK1E7GJ1]
audience: grad
uses: [MPSCREYC3M, KZSB5E471K, CV2E6JZHVP, 5NVA2JRHPV, 1QD0KDDGYJ, ~24c8db71]
sources:
  - url: https://en.wikipedia.org/wiki/Fast-growing_hierarchy
    locator: Points of interest
  - url: https://en.wikipedia.org/wiki/Primitive_recursive_function
    locator: Relationship to recursive functions
---

## Summary

A [[computable function|KZSB5E471K]] $f$ is *provably total* in a theory $T$ if $T$ proves that the program for $f$ halts on every input.
The provably total functions of a theory measure its strength in the language of growth rates.
For [[Peano arithmetic|MPSCREYC3M]] they are the functions below the level $\varepsilon_0$ of the [[fast-growing hierarchy|~24c8db71]], and for $\mathrm{I}\Sigma_1$ they are the [[primitive recursive functions|5NVA2JRHPV]].

## Motivation

A $\Pi_2$ sentence $\forall x\, \exists y\, \varphi(x, y)$ with $\varphi$ decidable says that the function "least $y$ with $\varphi(x, y)$" is total.
So a $\Pi_2$ sentence is unprovable in $T$ when its witness function grows faster than every provably total function of $T$.
This is how the Goodstein, hydra and Paris-Harrington statements escape $\mathsf{PA}$.

## Notation

Let $T$ be a theory in the language of arithmetic, or a second-order theory that contains it.

- A formula is $\Sigma_1$ if it has the form $\exists z\, \theta$ with $\theta$ having only bounded quantifiers, as in the [[arithmetical hierarchy|CV2E6JZHVP]].
- A function $f : \N \to \N$ is *provably total in $T$* if some $\Sigma_1$ formula $\varphi(x, y)$ defines the graph of $f$ in $\N$, and $T \vdash \forall x\, \exists y\, \varphi(x, y)$.
- $\mathrm{I}\Sigma_n$ is the theory of the basic axioms for $0$, successor, $+$, $\cdot$ and $<$, with the [[induction schema|1QD0KDDGYJ]] for $\Sigma_n$ formulas only.
- $g$ *eventually dominates* $f$ if $f(x) < g(x)$ for all large enough $x$.

## Remarks

### Examples

- The [[exponential function|~8a46ddd1]] $x \mapsto 2^x$ is provably total in $\mathrm{I}\Sigma_1$.
- The [[Ackermann function|~47c3cf52]] is provably total in $\mathsf{PA}$, but not in $\mathrm{I}\Sigma_1$.
- Every function $f_\alpha$ of the fast-growing hierarchy with $\alpha < \varepsilon_0$ is provably total in $\mathsf{PA}$, as the Wikipedia article states.

### Non-examples

- The [[function $f_{\varepsilon_0}$|~4e374acd]] is total and computable, but not provably total in $\mathsf{PA}$.
- The Goodstein length function $L$ of [[Goodstein's theorem|XQMNJF241J]] is total and computable, but not provably total in $\mathsf{PA}$.
- A function that is not computable, such as the busy beaver function, is provably total in no theory, because its graph has no $\Sigma_1$ definition.

### Basic properties

- If $T$ is $\Sigma_1$-sound, every provably total function of $T$ is total and computable: search for the least witness $z$ of $\varphi(x, y)$.
- The provably total functions of a $\Sigma_1$-sound theory with a computable set of axioms do not include all total computable functions. The function $x \mapsto f_x(x) + 1$, over the list $f_0, f_1, \dots$ of the provably total functions, is total, computable and not in the list.
- **Theorem** (Kreisel). The provably total functions of $\mathsf{PA}$ are the functions defined by recursion along well-orders of type below $\varepsilon_0$.
- **Theorem** (Wainer). Each provably total function of $\mathsf{PA}$ is eventually dominated by some $f_\alpha$ with $\alpha < \varepsilon_0$.
- **Theorem** (Parsons; Mints). The provably total functions of $\mathrm{I}\Sigma_1$ are the primitive recursive functions.
- So a function that eventually dominates every $f_\alpha$ with $\alpha < \varepsilon_0$ is not provably total in $\mathsf{PA}$.

### History

Georg Kreisel characterized the provably recursive functions of $\mathsf{PA}$ through recursion along ordinals below $\varepsilon_0$, using the methods of Gentzen's [[consistency proof|QPV0HNP22S]].
Stanley Wainer described them through the fast-growing hierarchy.
Charles Parsons, and independently Grigori Mints, showed that $\mathrm{I}\Sigma_1$ proves total exactly the primitive recursive functions.

### Common errors

- Provable totality depends on the formula. The same function can be provably total through one definition and not through another, unless the definitions are provably equivalent.
- "Not provably total" does not mean "not total". The functions in the non-examples are total, and stronger theories prove it.

## Explanations

### L1 human

A computer program computes a function when it stops on every input.
A system of axioms may or may not be able to prove that a given program always stops.
The functions whose programs a theory can prove to stop are its provably total functions.
Stronger theories can prove that faster-growing functions are total.

### L2 human

How the notion gives unprovability, in steps.

1. Take a true statement "for every $x$ there is $y$ with $\varphi(x, y)$", where $\varphi$ is decidable.
2. Let $g(x)$ be the least such $y$. If the theory proves the statement, then $g$ is provably total.
3. Show that $g$ eventually dominates every provably total function of the theory.
4. Then $g$ is not provably total, so the theory does not prove the statement.

The typical use is with $\mathsf{PA}$ and step 3 checked against the functions $f_\alpha$ with $\alpha < \varepsilon_0$.
The trap: step 3 needs domination by $g$ itself, not by a function that is merely related to $g$.

### L3 human

The provably total functions of a theory are a coarse invariant: theories with the same $\Pi_2$ consequences have the same provably total functions.
For theories with an [[ordinal analysis|C5E5TG8PGP]], they are usually the functions eventually dominated by $f_\alpha$ with $\alpha$ below the [[proof-theoretic ordinal|C72RBH0CDR]], for a suitable choice of fundamental sequences.
Indicators give the same functions from the model-theoretic side, and the [[Hardy hierarchy|~ec594377]] gives the length functions of Goodstein sequences and hydra battles.
