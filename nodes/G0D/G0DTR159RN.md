---
tag: G0DTR159RN
kind: statement
role: theorem
name: Model existence theorem
sources:
  - wikipedia: en:12450@r1371782634
    locator: Gödel's completeness theorem, section Statement > Model existence theorem
    note: adopted
    mention: wikipedia://en/12450#2V6I
    sections: [Statement]
inventory: [WCMCVZR0SC]
---

## Statement

The completeness theorem can also be understood in terms of consistency, as a consequence of Henkin's model existence theorem. We say that a theory *T* is *syntactically consistent* if there is no sentence *s* such that both *s* and its negation ¬*s* are provable from *T* in our deductive system. The model existence theorem says that for any first-order theory *T* with a well-orderable language,

if $T$ is syntactically consistent, then $T$ has a model.

Another version, with connections to the Löwenheim–Skolem theorem, says:

Every syntactically consistent, countable first-order theory has a finite or countable model.

Given Henkin's theorem, the completeness theorem can be proved as follows: If $T \models s$, then $T\cup\lnot s$ does not have models. By the contrapositive of Henkin's theorem, then $T\cup\lnot s$ is syntactically inconsistent. So a contradiction ($\bot$) is provable from $T\cup\lnot s$ in the deductive system. Hence $(T\cup\lnot s) \vdash \bot$, and then by the properties of the deductive system, $T\vdash s$.
