---
tag: ZA3R1MSMFY
kind: statement
role: proposition
name: Axioms used in the book
sources:
  - wikipedia: en:21986@r1361834325
    locator: Naive Set Theory (book), section Axioms used in the book
    note: adopted
    mention: wikipedia://en/21986#ZRMJ
    sections: [Statement]
inventory: [30WKAA83NJ]
---

## Statement

The statements of the axioms given below are as they appear in the book, with section references, and with explanatory commentary on each one. The "principal primitive (undefined) concept of *belonging*" (that is, set membership) is the starting point, where "$x$ belongs to $A$" is written in the usual notation as $x\in A$. Here $x$ and $A$ are both sets, with the notational distinction of upper/lower case a purely stylistic choice. The axioms govern the properties of this relation between sets.

\1. **[[Axiom of Extension|0TB16T2C97]]** (Section 1): two sets are equal if and only if they have the same elements.

This guarantees that the membership and (logical) [[equality|086QKPF0A6]] relations interact appropriately.

\2. **Axiom of Specification** (Section 2): To every set $A$ and every condition $S(x)$ there corresponds a set $B$ whose elements are precisely those elements of $A$ for which $S(x)$ holds.

This is more properly an axiom schema (that is, each condition $S(x)$ gives rise to an axiom). "Condition" here means a "sentence" in which the variable $x$ (ranging over all sets) is a free variable. "Sentences" are defined as being built up from smaller sentences using [[first order logical|086QKPF0A6]] operations ([[and|025YZN3VJW]], [[or|0F72FK8EKB]], [[not|029JBBF693]]), including [[quantifiers|0FYQMKFE77]] ("[[there exists|0MSRQHCNN9]]", "[[for all|0GHS47PDAQ]]"), and with atomic (i.e. basic starting) sentences $x\in A$ and $A=B$.

This schema is used in 4.-7. below to cut down the set that is stated to exist to the set containing precisely the intended elements, rather than some larger set with extraneous elements. For example, the axiom of pairing applied to the sets $A$ and $B$ only guarantees there is *some* set $X$ such that $A\in X$ and $B\in X$. Specification can be used to then construct the set $\{A,B\}$ with *just* those elements.

\3. **Set existence** (Section 3): There exists a set.

Not specified as an named axiom, but instead stated to be "officially assumed". This assumption is not necessary once the axiom of infinity is adopted later, which also specifies the existence of a set (with a certain property). The existence of any set at all is used to show the [[empty set|0ECVK59Y03]] exists using the axiom of specification.

\4. **Axiom of pairing** (Section 3): For any two sets there exists a set that they both belong to.

This is used to show that the singleton $\{A\}$ containing a given set $A$ exists.

\5. **Axiom of unions** (Section 4): For every collection of sets there exists a set that contains all the elements that belong to at least one set of the given collection.

In Section 1 Halmos writes that "to avoid terminological monotony, we shall sometimes say *collection* instead of set." Hence this axiom is equivalent to the usual form of the axiom of unions (given the axiom of specification, as noted above).

From the axioms so far Halmos gives a construction of [[intersections of sets|0ZNMMA9TF5]], and the usual Boolean operations on sets are described and their properties proved.

\6. **Axiom of powers** (Section 5): For each set there exists a collection of sets that contains among its elements all the subsets of the given set.

Again (noting that "collection" means "set") using the axiom (schema) of specification we can cut down to get the [[power set|00E0YZCERH]] $P(A)$ of a set $A$, whose elements are precisely the subsets of $A$. The axioms so far are used to construct the [[cartesian product|09CEDJYBKP]] of sets.

\7. **Axiom of infinity** (Section 11): There exists a set containing 0 and containing the successor of each of its elements.

The set $0 := \emptyset$. The *successor* of a set $x$ is defined to be the set $x^+:=x \cup \{x\}$. For example: $\{a,b\}^+ = \{a,b,\{a,b\}\}$. This axiom ensures the existence of a set containing $0$ and hence $\{0\}$, and hence $\{0,\{0\}\}$ and so on. This implies that there is a set containing all the elements of the first infinite [[von Neumann ordinal|0RDJK7EQYY]] $\omega$. And another application of the axiom (schema) of specification means $\omega$ itself is a set.

\8. **[[Axiom of choice|0HTGB13FE2]]** (Section 15): The Cartesian product of a non-empty family of non-empty sets is non-empty.

This is one of many [[equivalents to the axiom of choice|0HTGB13FE2]]. Note here that "family" is defined to be a function $f\colon I\to X$, with the intuitive idea that the sets of the family are the sets $f(i)$ for $i$ ranging over the set $I$, and in usual notation this axiom says that there is at least one element in $\prod_{i\in I} f(i)$, as long as $f(i)\neq \emptyset$ for all $i\in I \neq \emptyset$.

\9. **Axiom of substitution** (Section 19): If $S(a,b)$ is a sentence such that for each $a$ in a set $A$ the set $\{b : S(a,b)\}$ can be formed, then there exists a function $F$ with domain $A$ such that $F(a) = \{b : S(a,b)\}$ for each $a$ in $A$.

A function $F\colon A\to X$ is defined to be a functional relation (i.e. a certain subset of $A\times X$), not as a certain type of set of [[ordered pairs|0JQWWFCS9R]], as in ZFC, for instance.

This 'axiom' is essentially the axiom schema of collection, which, given the other axioms, is equivalent to the axiom schema of replacement. It is the collection schema rather than replacement, because 1) $S(a,b)$ is a class *relation* instead of a class function and 2) the function $F$ is not specified to have [[codomain|0C5SR4FC74]] precisely the set $\{F(a) : a\in A\}$, but merely some set $X\supseteq \{F(a) : a\in A\}$.

This axiom is used in the book to a) construct limit [[von Neumann ordinals|0RDJK7EQYY]] after the first infinite ordinal $\omega$, and b) prove that every [[well-ordered set|01CGSJ0GNQ]] is order isomorphic to a unique von Neumann ordinal.
