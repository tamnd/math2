---
tag: DP7RSJETHC
kind: example
name: An extended resolution refutation is not a resolution refutation
msc: ["03F20", "03B35"]
topics: [CBAF7J051K]
audience: research
not_instance_of:
  - target: 6JSH907W5R
    note: the extension clauses that define a new variable are neither clauses of F nor resolvents, so the sequence is not a resolution refutation of F
uses: [6JSH907W5R, 5YSE04SHFH, ZDW6N1PGJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: Resolution in propositional logic
  - url: https://en.wikipedia.org/wiki/Frege_system
    locator: Extended Frege system
---

## Example

*Extended resolution*, introduced by Tseitin, lets a proof name a formula by a new variable.
To name $a \land b$ by a variable $z$ that occurs nowhere before, it adds the three *extension clauses*
$$\{\neg z, a\}, \qquad \{\neg z, b\}, \qquad \{z, \neg a, \neg b\},$$
which together say $z \leftrightarrow (a \land b)$.

Let $F$ have the three clauses $\{a\}$, $\{b\}$ and $\{\neg a, \neg b\}$.
Here is an extended resolution refutation of $F$.

1. $\{\neg z, a\}$, $\{\neg z, b\}$ and $\{z, \neg a, \neg b\}$, the extension clauses for $z$.
2. $\{z, \neg b\}$, the resolvent of $\{z, \neg a, \neg b\}$ and $\{a\}$ on $a$.
3. $\{z\}$, the resolvent of the clause of step 2 and $\{b\}$ on $b$.
4. $\{\neg a, \neg z\}$, the resolvent of $\{\neg a, \neg b\}$ and $\{\neg z, b\}$ on $b$.
5. $\{\neg z\}$, the resolvent of the clause of step 4 and $\{a\}$ on $a$.
6. $\square$, the resolvent of $\{z\}$ and $\{\neg z\}$ on $z$.

Each step from 2 to 6 is a correct resolution step.
But the sequence is not a [[resolution refutation|6JSH907W5R]] of $F$, because the three clauses of step 1 are not clauses of $F$, and they are not resolvents of earlier clauses.

## Remarks

The extension clauses do not change satisfiability.
Every assignment that satisfies $F$ extends to one that also satisfies the extension clauses, by setting $z := a \land b$.
So extended resolution is sound, even though its proofs are not resolution proofs.
Here the new variable saves nothing.
Resolve $\{\neg a, \neg b\}$ with $\{a\}$ to get $\{\neg b\}$, and then $\{\neg b\}$ with $\{b\}$ to get $\square$, a plain refutation with $5$ clauses.
The extended refutation above has $11$ clauses: $3$ axioms, $3$ extension clauses and $5$ resolvents.

For other formulas the saving is exponential.
Cook gave polynomial-size extended resolution refutations of the [[pigeonhole formulas|RJ571F7FF0]] in 1976, while [[Haken's theorem|4PCEYEW3JG]] says that resolution refutations of them have exponential size.
The new variables let a proof talk about formulas, not only about clauses.
Extended resolution is p-equivalent to [[extended Frege|5YSE04SHFH]], so it sits at the top of the known hierarchy, far above resolution.

Watch out: the new variable must really be new.
If $z$ already occurs in $F$, say in the clause $\{\neg z\}$, then the "extension" clauses add the constraint $z \leftrightarrow (a \land b)$ to a formula that already speaks about $z$, and soundness can fail.
For example, $F = \{\{a\}, \{b\}, \{\neg z\}\}$ is satisfiable, but with the three clauses above it becomes unsatisfiable.

## Explanations

### L1 human

A resolution proof may only combine clauses it already has.
Extended resolution may also say "let $z$ mean $a$ and $b$", and add clauses that state this definition.
Those clauses do not follow from the given clauses, so the proof is not a plain resolution proof.
It is still a correct proof, because a definition of a new name cannot create a contradiction.

### L2 human

We check that the extension clauses define $z$ correctly.
The clause $\{\neg z, a\}$ says $z \to a$, and the clause $\{\neg z, b\}$ says $z \to b$.
The clause $\{z, \neg a, \neg b\}$ says $(a \land b) \to z$.
Together they say $z \leftrightarrow (a \land b)$.
Check on one row: with $a = 1$, $b = 0$ the clauses force $z = 0$ through $\{\neg z, b\}$, and indeed $a \land b = 0$.
The typical use of the example is to show the exact point where extended resolution leaves resolution: only the extension clauses break the definition.
