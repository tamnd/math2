---
tag: E1XCM5TEFD
kind: counterexample
name: Grelling-Nelson paradox
aliases: [grelling-paradox, heterological-paradox]
msc: ["03A05"]
topics: [6Q4JJ2MMV8]
audience: ug2
uses: [B20TDZV9WW, VFHBYVXPCB]
refutes:
  - target: B20TDZV9WW
    via: Z9KYS2C3D9
sources:
  - url: https://en.wikipedia.org/wiki/Grelling%E2%80%93Nelson_paradox
    locator: Paradox
  - url: https://en.wikipedia.org/wiki/Grelling%E2%80%93Nelson_paradox
    locator: Similarities with Russell's paradox
  - url: https://plato.stanford.edu/entries/self-reference/
    locator: "Self-Reference and Paradox, 1.1 Semantic Paradoxes"
---

## Counterexample

The claim refuted is the [[naive satisfaction schema|B20TDZV9WW]].
It says that every adjective is true of exactly the things that have the property it expresses, words included.

*Definitions.*
An adjective is [[autological|VFHBYVXPCB]] if it describes itself.
For example, "English" is an English word, and "pentasyllabic" has five syllables.
An adjective is *heterological* if it does not describe itself.
For example, "long" is not a long word, and "monosyllabic" has more than one syllable.

*Derivation.* Ask whether "heterological" is heterological.

1. By the definition, for every adjective $A$: $A$ is heterological if and only if $A$ does not describe itself.
2. The naive principle says: "heterological" describes $A$ if and only if $A$ is heterological.
3. Put $A :=$ "heterological" in step 1: "heterological" is heterological if and only if "heterological" does not describe itself.
4. Put $A :=$ "heterological" in step 2: "heterological" describes itself if and only if "heterological" is heterological.
5. Steps 3 and 4 give: "heterological" describes itself if and only if it does not describe itself.
6. If "heterological" describes itself, step 5 says it does not. So it does not describe itself.
7. Then step 5, from right to left, says that it describes itself. Steps 6 and 7 contradict each other.

*Formal form.* Read "$A$ describes $x$" as $\mathrm{Sat}(\ulcorner A \urcorner, x)$, and "heterological" as the formula $\neg \mathrm{Sat}(v, v)$.
Then steps 1 to 7 are the [[proof that the naive satisfaction schema is inconsistent|Z9KYS2C3D9]].

## Remarks

### Autological is not paradoxical

Ask whether "autological" is autological.
The naive principle gives: "autological" is autological if and only if "autological" is autological.
This is a tautology, so both answers are consistent.
The situation is like the [[truth-teller|XADBJH4872]], while "heterological" behaves like the [[liar|KBYY281V8T]].

### Relation to Russell's paradox

Wikipedia describes a translation into [[Russell's paradox|0HESMMSYEG]]: identify each adjective with the set of things it applies to.
Then "heterological" corresponds to the set of all sets that are not members of themselves.
The difference is the domain: Grelling-Nelson uses satisfaction of words, and Russell uses membership of sets.
So the first is a semantic paradox, and the second is a set-theoretic paradox.

### Self-reference

The SEP entry on self-reference states that the definition of "heterological" refers to all predicates, including itself.
It calls such definitions impredicative.
The formal version needs no [[diagonal lemma|3PRW76471J]]: a formula can be applied to its own code because codes are numbers.

### Ambiguous adjectives

Some adjectives depend on the occasion of use, for example "loud".
Wikipedia notes that this problem is avoided by taking the paradox to be about word types and not word tokens.

## Explanations

### L1 human

Some words describe themselves: "short" is a short word, and "English" is English.
Other words do not: "long" is not long, and "German" is not German.
Call the second kind of words heterological.
Now ask whether the word "heterological" is heterological.
If it is, then it describes itself, so it is not heterological.
If it is not, then it does not describe itself, so it is heterological.

### L2 human

1. Write $H(A)$ for "$A$ does not describe $A$".
2. The word "heterological" describes exactly the words $A$ with $H(A)$.
3. So "heterological" describes "heterological" if and only if $H$("heterological").
4. By step 1, $H$("heterological") means "heterological" does not describe "heterological".
5. Steps 3 and 4 give a statement of the form $p \leftrightarrow \neg p$.

The typical use is as the simplest semantic paradox: it needs only predicates and self-application, and no sentence that names itself.
The trap is to confuse it with Russell's paradox.
The two have the same diagonal form, but the relation is "describes", not "is a member of".

### L3 human

Both this paradox and Russell's paradox are instances of one diagonal pattern.
A relation $R$ on a set $X$ cannot have a "row" $R(a, \cdot)$ equal to the diagonal complement $\{x : \neg R(x, x)\}$.
[[Lawvere's fixed-point theorem|N84M16W19X]] gives the categorical form of this pattern.
