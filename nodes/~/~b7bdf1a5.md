---
tag: ~b7bdf1a5
kind: example
name: A Lambek parse of the cat sees a dog
msc: ["03B47", "03B65"]
topics: [98QF5J4W16]
audience: research
instance_of: [5FAC9KX4H0]
uses: [~19f422b8]
sources:
  - url: https://en.wikipedia.org/wiki/Categorial_grammar
    locator: Lambek calculus
  - url: https://plato.stanford.edu/entries/logic-substructural/
    locator: 2.3 The Lambek Calculus
    note: Restall, Substructural Logics, Stanford Encyclopedia of Philosophy, revision of 2024-08-15
---

## Example

Take the atoms $s$, $n$ and $np$, and the lexicon: "the" and "a" have type $np / n$, "cat" and "dog" have type $n$, and "sees" has type $(np \backslash s) / np$.
The sequent
$$np / n, \; n, \; (np \backslash s) / np, \; np / n, \; n \Rightarrow s$$
is derivable in the [[Lambek calculus|~19f422b8]], so "the cat sees a dog" is a sentence of this grammar.

1. $np \Rightarrow np$ and $s \Rightarrow s$ are axioms.
   ${\backslash}\mathrm{L}$ with $\Gamma = np$ gives $np, np \backslash s \Rightarrow s$.
2. $n \Rightarrow n$ is an axiom.
   ${/}\mathrm{L}$ on the axioms $n \Rightarrow n$ and $np \Rightarrow np$ gives $np / n, n \Rightarrow np$.
   This is "a dog".
3. ${/}\mathrm{L}$ with $\Gamma = np / n, n$ from step 2, and with the premise $np, np \backslash s \Rightarrow s$ from step 1, gives $np, (np \backslash s) / np, np / n, n \Rightarrow s$.
4. ${/}\mathrm{L}$ with $\Gamma = n$ and the premise of step 3, where $B = np$ is the first formula, gives $np / n, n, (np \backslash s) / np, np / n, n \Rightarrow s$.

## Remarks

The derivation uses no cut and no structural rule, so it is a derivation of $\mathsf{L}$ in the strict sense.
Step 3 combines the verb with its object, and step 4 combines the subject with the verb phrase.
The count check of [[the definition|~19f422b8]] agrees with the derivation, as the explanations compute.
A change of the word order changes the sequent, and [[the non-example|~088bc11a]] shows a word order for which no derivation exists.

## Explanations

### L1 human

The words of "the cat sees a dog" get types.
"The" needs a noun on its right, and "cat" is a noun, so "the cat" is a noun phrase.
"Sees" needs a noun phrase on its right and then one on its left.
"A dog" is a noun phrase on its right, and "the cat" is a noun phrase on its left, so the whole string is a sentence.

### L2 human

We check the count condition for each atom, with $\#_p(B / A) = \#_p(A \backslash B) = \#_p(B) - \#_p(A)$.

1. The types are $np / n$, $n$, $(np \backslash s) / np$, $np / n$, $n$.
2. For $n$: $-1 + 1 + 0 - 1 + 1 = 0$, and $\#_n(s) = 0$.
3. For $np$: $1 + 0 + (-1 - 1) + 1 + 0 = 0$, and $\#_{np}(s) = 0$.
   Here $\#_{np}((np \backslash s) / np) = (0 - 1) - 1 = -2$.
4. For $s$: $0 + 0 + 1 + 0 + 0 = 1$, and $\#_s(s) = 1$.

The typical use of a parse is to show that a string is a sentence, and the derivation is its syntactic structure.
A trap: the count check is necessary but not sufficient, so a parse needs a derivation.
