---
tag: 4HNAJQQ8Z0
kind: statement
role: theorem
name: Characterization of elementary classes by ultraproducts
aliases: [keisler-characterization-of-elementary-classes, ultraproduct-characterization-of-elementary-classes]
msc: ["03C20", "03C52"]
topics: [HZG1YP26AB]
audience: grad
about: [MEC3ZMC4F1]
uses: [MEC3ZMC4F1, AX9Q86GB8M, AGYBSTD7BG, P3B1V182N4, A37HPCKCE2, 1NR3HAWG9D]
history:
  first_stated: "H. Jerome Keisler, 1961"
  notes: "Keisler's paper Ultraproducts and elementary classes; the versions with ultraroots use the Keisler-Shelah theorem."
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_class
    locator: lead section
  - book: isbn:9780387987606
---

## Statement

Let $\mathcal{K}$ be a class of $L$-structures with nonempty domains.
An *ultraroot* of $\mathcal{M}$ is a structure $\mathcal{N}$ such that some ultrapower of $\mathcal{N}$ is isomorphic to $\mathcal{M}$.
$\mathcal{K}$ is an [[elementary class|MEC3ZMC4F1]] when $\mathcal{K} = \operatorname{Mod}(T)$ for a set $T$ of sentences, and a *basic elementary class* when $T$ can be one sentence.

1. $\mathcal{K}$ is an elementary class if and only if it is closed under [[elementary equivalence|P3B1V182N4]] and [[ultraproducts|AX9Q86GB8M]].
2. $\mathcal{K}$ is an elementary class if and only if it is closed under isomorphism, ultraproducts and ultraroots.
3. $\mathcal{K}$ is a basic elementary class if and only if $\mathcal{K}$ and its complement, among all $L$-structures, are closed under isomorphism and ultraproducts.

## Remarks

### Why each hypothesis is needed

- Ultraproducts in part 1: the class of finite sets is closed under elementary equivalence, but not under ultraproducts, and it is not elementary.
- Elementary equivalence in part 1, ultraroots in part 2: the class of uncountable sets is closed under isomorphism and ultraproducts, but not elementary; see [[this non-example|TWVY0QXN0K]].
- The complement in part 3: the class of infinite sets is elementary, by the sentences "at least $k$ elements", but its complement is not closed under ultraproducts, and it is not basic elementary.

### Consequences

- Elementary classes are determined by algebraic operations alone, with no reference to formulas.
- A class closed under isomorphism, ultraproducts and elementary substructures is elementary, by [[Frayne's theorem|QPX9HG9BH4]].
- To show that a class is not elementary, it suffices to find an ultraproduct of members outside it, or a nonmember with an ultrapower inside it.

### Converse

Each part is an equivalence.
The "only if" directions are the easy ones: they follow from [[Łoś's theorem|AGYBSTD7BG]].

### Generalizations

- Parts 2 and 3 use the [[Keisler-Shelah theorem|A37HPCKCE2]] to replace elementary equivalence by isomorphism and ultraroots. Without it, part 3 reads: $\mathcal{K}$ and its complement are closed under elementary equivalence and ultraproducts.
- For a class closed only under reduced products and isomorphism, the analogous results concern Horn sentences; see [[preservation of Horn formulas|8RRECJJM3G]].

## History

Keisler proved characterizations of this kind in his 1961 paper "Ultraproducts and elementary classes", using the generalized continuum hypothesis for the forms with isomorphism.
Shelah's proof of the isomorphism theorem in 1971 removed this hypothesis.
The [[proof|PP9Z1DJM5T]] of part 1 is the ultraproduct method applied to the theory of a structure.

## Explanations

### L1 human

A class of structures is elementary when some list of first-order rules describes exactly its members.
The theorem says how to recognize such classes without looking for the rules.
The class must be closed under gluing by ultraproducts.
Also, a structure must belong to the class when it is indistinguishable by first-order rules from a member.
The class of finite sets fails the first test, since gluing larger and larger finite sets gives an infinite set.

### L2 human

We use part 3 to show that the class $\mathcal{K}$ of fields of positive characteristic is not basic elementary.

1. $\mathcal{K}$ is closed under isomorphism.
2. Its complement contains the fields of characteristic $0$ and all structures that are not fields.
3. The ultraproduct of the fields $\F_p$ over a nonprincipal ultrafilter on the primes has characteristic $0$, by [[this example|145GABE79C]].
4. So $\mathcal{K}$ is not closed under ultraproducts, and part 3 fails.

The same argument shows that $\mathcal{K}$ is not elementary at all, by part 1.
In contrast, the class of fields of characteristic $0$ is elementary but not basic elementary, since its complement contains the $\F_p$ and not their ultraproduct.
The typical use is to prove that a class is not axiomatizable.
The trap is to check closure under ultraproducts with principal ultrafilters only; they give nothing new.

### L3 human

The theorem is a model-theoretic analogue of a closure characterization in topology: elementary classes are the closed sets of a topology on structures modulo elementary equivalence, and basic elementary classes are the clopen sets.
In this picture, ultraproducts play the role of limits, and the Stone space of complete theories is compact.
Similar characterizations hold for Horn classes with reduced products, for universal classes with substructures and ultraproducts, and for varieties in Birkhoff's theorem with products, substructures and quotients.
