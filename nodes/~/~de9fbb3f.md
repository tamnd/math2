---
tag: ~de9fbb3f
kind: definition
name: Dyck word
msc: [68Q45]
defines: ~334b0f18
sources:
  - url: https://en.wikipedia.org/wiki/Dyck_language
    locator: Formal definition
---

## Definition

A Dyck word is a finite word $w$ over the two-letter alphabet $\{U, D\}$ with these two properties.
The word $w$ has as many letters $U$ as letters $D$.
Each prefix of $w$ has at least as many letters $U$ as letters $D$.

The semilength of a Dyck word is its number of letters $U$, which is half its length.

## Remarks

Other common alphabets are $\{(, )\}$ and $\{[, ]\}$. Then the Dyck words are the balanced strings of brackets.
The Dyck words of semilength $2$ are $UUDD$ and $UDUD$.
Read $U$ as a step $(1, 1)$ and $D$ as a step $(1, -1)$. A Dyck word is then a [[lattice path|~a1e7b571]] from $(0, 0)$ to $(2n, 0)$ that never goes below the horizontal axis.
The Dyck words of semilength $n$ are [[counted by the Catalan number|~5e982722]] $C_n$.

## Explanations

### L1 human

A Dyck word is a correct sequence of opening and closing brackets.
The sequence $(()())$ is a Dyck word, but $())($ is not, because after three symbols there are more closing than opening brackets.
