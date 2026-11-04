---
tag: DKB53Y4GD2
kind: statement
role: proposition
name: Von Neumann's 1929 axiom system
sources:
  - wikipedia: en:528491@r1330985339
    locator: Von Neumann–Bernays–Gödel set theory, section History > Von Neumann's 1929 axiom system
    note: adopted
    mention: wikipedia://en/528491#8B3P
    sections: [Statement]
inventory: [ZFRWWEN075]
---

## Statement

In 1929, von Neumann published an article containing the axioms that would lead to NBG. This article was motivated by his concern about the consistency of the axiom of limitation of size. He stated that this axiom "does a lot, actually too much." Besides implying the axioms of separation and replacement, and the [[well-ordering theorem|0N109NG5ZX]], it also implies that any class whose [[cardinality|0G0ASKNA6Z]] is less than that of *V* is a set. Von Neumann thought that this last implication went beyond Cantorian set theory and concluded: "We must therefore discuss whether its \[the axiom's\] consistency is not even more problematic than an axiomatization of set theory that does not go beyond the necessary Cantorian framework."

Von Neumann started his consistency investigation by introducing his 1929 axiom system, which contains all the axioms of his 1925 axiom system except the axiom of limitation of size. He replaced this axiom with two of its consequences, the axiom of replacement and a choice axiom. Von Neumann's choice axiom states: "Every relation *R* has a subclass that is a function with the same domain as *R*."

Let *S* be von Neumann's 1929 axiom system. Von Neumann introduced the axiom system *S* + Regularity (which consists of *S* and the axiom of regularity) to demonstrate that his 1925 system is consistent relative to *S*. He proved:

1. If *S* is consistent, then *S* + Regularity is consistent.
1. *S* + Regularity implies the axiom of limitation of size. Since this is the only axiom of his 1925 axiom system that *S* + Regularity does not have, *S* + Regularity implies all the axioms of his 1925 system.

These results imply: If *S* is consistent, then von Neumann's 1925 axiom system is consistent. Proof: If *S* is consistent, then *S* + Regularity is consistent (result 1). Using proof by contradiction, assume that the 1925 axiom system is inconsistent, or equivalently: the 1925 axiom system implies a contradiction. Since *S* + Regularity implies the axioms of the 1925 system (result 2), *S* + Regularity also implies a contradiction. However, this contradicts the consistency of *S* + Regularity. Therefore, if *S* is consistent, then von Neumann's 1925 axiom system is consistent.

Since *S* is his 1929 axiom system, von Neumann's 1925 axiom system is consistent relative to his 1929 axiom system, which is closer to Cantorian set theory. The major differences between Cantorian set theory and the 1929 axiom system are classes and von Neumann's choice axiom. The axiom system *S* + Regularity was modified by Bernays and Gödel to produce the equivalent NBG axiom system.
