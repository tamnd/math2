---
tag: Y5C37JR9RR
kind: statement
role: proposition
name: Robinson's principle
sources:
  - wikipedia: en:152207@r1312261892
    locator: Compactness theorem, section Applications > Robinson's principle
    note: adopted
    mention: wikipedia://en/152207#91J0
    sections: [Statement]
inventory: [CKET7W4PJJ]
---

## Statement

The compactness theorem implies the following result, stated by Abraham Robinson in his 1949 dissertation.

Robinson's principle: If a first-order sentence holds in every [[field|04C5ZBG1WT]] of [[characteristic|0F6ES3BRYP]] zero, then there exists a constant $p$ such that the sentence holds for every field of characteristic larger than $p.$ This can be seen as follows: suppose $\varphi$ is a sentence that holds in every field of characteristic zero. Then its negation $\lnot \varphi,$ together with the field axioms and the infinite sequence of sentences

$$1 + 1 \neq 0, \;\; 1 + 1 + 1 \neq 0, \; \ldots$$

is not satisfiable (because there is no field of characteristic 0 in which $\lnot \varphi$ holds, and the infinite sequence of sentences ensures any model would be a field of characteristic 0). Therefore, there is a finite subset $A$ of these sentences that is not satisfiable. $A$ must contain $\lnot \varphi$ because otherwise it would be satisfiable. Because adding more sentences to $A$ does not change unsatisfiability, we can assume that $A$ contains the field axioms and, for some $k,$ the first $k$ sentences of the form $1 + 1 + \cdots + 1 \neq 0.$ Let $B$ contain all the sentences of $A$ except $\lnot \varphi.$ Then any field with a characteristic greater than $k$ is a model of $B,$ and $\lnot \varphi$ together with $B$ is not satisfiable. This means that $\varphi$ must hold in every model of $B,$ which means precisely that $\varphi$ holds in every field of characteristic greater than $k.$ This completes the proof.

The Lefschetz principle, one of the first examples of a transfer principle, extends this result. A first-order sentence $\varphi$ in the language of [[rings|0B1261B5ED]] is true in some (or equivalently, in every) algebraically closed field of characteristic 0 (such as the [[complex numbers|09FTAET5Z4]] for instance) if and only if there exist infinitely many primes $p$ for which $\varphi$ is true in some algebraically closed field of characteristic $p,$ in which case $\varphi$ is true in all algebraically closed fields of sufficiently large non-0 characteristic $p.$ One consequence is the following special case of the Ax–Grothendieck theorem: all injective [[complex|09FTAET5Z4]] polynomials $\mathbb{C}^n \to \mathbb{C}^n$ are surjective (indeed, it can even be shown that its inverse will also be a polynomial). In fact, the surjectivity conclusion remains true for any injective polynomial $F^n \to F^n$ where $F$ is a finite field or the algebraic closure of such a field.
