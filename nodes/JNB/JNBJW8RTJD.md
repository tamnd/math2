---
tag: JNBJW8RTJD
kind: concept
name: History of model theory
msc: ["03C98", "01A60"]
topics: [AY09KYSW81]
audience: grad
uses: [HFTBG5PMXC, 1NR3HAWG9D, 484M0TZ1S7, WQ1ZE255SF]
sources:
  - url: https://en.wikipedia.org/wiki/Model_theory
    locator: History
  - url: https://en.wikipedia.org/wiki/L%C3%B6wenheim%E2%80%93Skolem_theorem
    locator: lead section
  - book: isbn:9780521587136
    locator: Chapter 1
---

## Summary

The *history of model theory* is the development of the study of structures through the first-order sentences that are true in them.
It has four stages.
From 1915 to the 1930s, Löwenheim, Skolem, Gödel, Tarski and Mal'cev proved the first theorems on models: the [[Löwenheim-Skolem theorem|484M0TZ1S7]], the [[completeness|WQ1ZE255SF]] and [[compactness|1NR3HAWG9D]] theorems, and the definition of truth.
In the 1950s Tarski and Abraham Robinson made [[model theory|HFTBG5PMXC]] a branch of mathematics with its own methods and applications to algebra.
From 1965 Morley and Shelah built the classification theory of complete theories.
From the 1980s, the geometric stage of Zilber, Hrushovski, Pillay, van den Dries, Wilkie and others joined model theory with algebraic geometry and number theory.
The history explains why the basic notions of the subject have their present form.

## Motivation

The definitions of [[substructure|676H7EGTKJ]], [[elementary equivalence|P3B1V182N4]] and [[complete theory|655K8Y7VS8]] look abstract when a student first meets them.
Each one was introduced to solve a problem: to count the models of a theory, to decide the truth of sentences about numbers, or to transfer a theorem from one field to another.
A short history shows these problems, and it shows which later results used the basic notions.

## Remarks

### The first theorems

Leopold Löwenheim proved in 1915 that a first-order sentence with an infinite model has a countable model.
Thoralf Skolem extended the result to countable sets of sentences in 1920, and in 1922 he gave a proof without the axiom of choice.
Kurt Gödel proved the completeness theorem for first-order logic in his thesis of 1929, published in 1930, and the compactness theorem for countable languages follows from it.
Anatoly Mal'cev proved the compactness theorem for languages of any size in 1936, and in 1941 he used it to prove local theorems in group theory.
Alfred Tarski gave an exact definition of truth in a formal language in 1933.
This definition is the relation $\mathcal{M} \models \sigma$ on which all of model theory rests.

### A branch of mathematics

Tarski proved that the theory of the real field admits quantifier elimination, and he published the decision method in 1948.
Tarski and Robert Vaught introduced elementary extensions and the [[Tarski-Vaught test|60SA99BER7]] in a paper of 1957.
Abraham Robinson developed the use of model theory in algebra from 1951, with model completeness and the method of diagrams.
Jerzy Łoś proved his theorem on [[ultraproducts|AX9Q86GB8M]] in 1955.
Robinson created [[nonstandard analysis|WM62GKCBWN]] in 1961, with a book in 1966.
James Ax and Simon Kochen, and independently Yuri Ershov, proved the [[transfer theorem for p-adic fields|PHT3TJCS90]] in 1965.

### Classification theory

Michael Morley proved in 1965 that a countable theory that is categorical in one uncountable cardinal is categorical in all uncountable cardinals; see [[Morley's theorem|V7N84P60SJ]].
Saharon Shelah then developed stability theory and the classification of complete theories by the number and the structure of their models.
His book *Classification Theory and the Number of Non-isomorphic Models* appeared in 1978.

### The geometric stage

Boris Zilber studied [[strongly minimal|PNGY60EBDJ]] sets and conjectured a description of their geometries.
Ehud Hrushovski refuted this conjecture in 1993 with a [[new strongly minimal set|B3XW32T6EH]].
Hrushovski and Zilber proved a positive version for Zariski geometries in 1996.
In 1996 Hrushovski also proved the Mordell-Lang conjecture for function fields with methods of geometric stability theory.
Lou van den Dries proposed the study of [[o-minimal|DTWHAW1N0V]] structures in 1984, and Anand Pillay and Charles Steinhorn developed it in 1986, partly with Julia Knight.
Alex Wilkie proved in 1996 that the real exponential field is model complete and o-minimal.
Jonathan Pila and Wilkie proved a counting theorem for rational points on o-minimal sets in 2006, and Pila used it in 2011 to prove the André-Oort conjecture for products of modular curves.
Michael Chris Laskowski showed in 1992 that the [[NIP theories|74VCDYQDGP]] of Shelah are those in which definable families have finite Vapnik-Chervonenkis dimension.

### Textbooks

Chang and Keisler's *Model Theory* (1973) was the standard text for two decades.
Wilfrid Hodges' *Model Theory* (1993) and David Marker's *Model Theory: An Introduction* (2002) present the subject after the geometric turn.

### Common errors

- To date model theory from Tarski only. The Löwenheim-Skolem theorem of 1915 and the completeness theorem of 1929 are theorems of model theory, although the name came later.
- To think that the classification theory of Shelah is only about counting models. It also gave the tools, such as forking, that the geometric stage used.

## Explanations

### L1 human

Model theory began about a hundred years ago with a strange result.
Löwenheim showed that a sentence about an infinite structure is already true in a structure whose elements can be listed $1, 2, 3, \dots$.
So the sentences of logic cannot fix the size of an infinite structure.
In the 1930s and 1950s, Gödel, Tarski and Robinson made these ideas exact and used them in algebra.
Later, Morley and Shelah sorted the theories into kinds by how their models behave.
Today model theory is also used to prove theorems about equations and numbers.

### L2 human

We follow one idea, compactness, through the history.

1. Gödel (1929 to 1930): a countable set of sentences has a model if each finite subset has a model, as a corollary of completeness.
2. Mal'cev (1936): the same for sets of sentences of any size.
3. Mal'cev (1941): applications to groups, where a property of a group follows from the property of its finitely generated subgroups.
4. Robinson (1960s): a model of all finite parts of the theory of $\R$ with a new positive element below every $1/n$ is a field with infinitesimals, the start of nonstandard analysis.

The typical use of compactness is to build a model with a new element that satisfies infinitely many conditions.
A trap is to credit compactness to one person: the countable case and the general case have different authors.

### L3 human

The history shows a steady move from logic to geometry.
The first theorems concerned all structures at once, and they gave tools: compactness, [[Löwenheim-Skolem|484M0TZ1S7]], ultraproducts, back-and-forth.
Robinson's work turned these tools on special theories, such as [[algebraically closed fields|MT8TDVPBXB]] and real closed fields.
Morley's theorem led Shelah to ask which complete theories have a structure theory for their models, and the answer is the dividing lines of [[stability|T7JW5QY6KR]], superstability and [[NIP|74VCDYQDGP]].
The geometric stage then used these dividing lines inside algebraic structures, where forking independence becomes algebraic independence and definable groups become algebraic groups.
The later sub-areas of [[model theory|F3AXVABC35]] follow this order, and the [[history of mathematical logic|WP3602P9EH]] places it in the wider history of logic.
