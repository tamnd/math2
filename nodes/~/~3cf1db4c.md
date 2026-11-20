---
tag: ~3cf1db4c
kind: example
name: A three-valued model shows that C1 is paraconsistent
msc: ["03B53"]
topics: [NJB94B39QK]
audience: grad
instance_of: [~3c6ff4aa, C7YWCR87QJ]
not_instance_of:
  - target: TTKZGJEEK7
    note: the model refutes p, not p, therefore q in C1
uses: [~b5c5d455, C7YWCR87QJ, TTKZGJEEK7]
sources:
  - url: https://plato.stanford.edu/entries/logic-paraconsistent/
    locator: Paraconsistent Logic (SEP entry), section 3.5
  - book: isbn:9783319332031
---

## Example

We define a three-valued matrix $M$ and show that every theorem of [[da Costa's system $C_1$|~b5c5d455]] is designated in it.
The values are $1$, $\tfrac12$, $0$, and the designated values are $1$ and $\tfrac12$.
Write $d(a)$ for "$a$ is designated".

- $a \land b = 1$ if $d(a)$ and $d(b)$, and $0$ otherwise.
- $a \lor b = 1$ if $d(a)$ or $d(b)$, and $0$ otherwise.
- $a \to b = 1$ if $a = 0$ or $d(b)$, and $0$ otherwise.
- $\neg 1 = 0$, $\neg\tfrac12 = \tfrac12$, $\neg 0 = 1$.

1. The binary connectives depend only on designation and return $0$ or $1$. So, for formulas built from atoms with $\land$, $\lor$, $\to$, designation behaves like classical truth. Axioms 1 to 7 are classical positive tautologies, so they get the value $1$.
2. Modus ponens preserves designation: if $d(a)$ and $a \to b = 1$, then $a \neq 0$, so $d(b)$.
3. Axiom 8, $A \lor \neg A$: if $A = 0$, then $\neg A = 1$; otherwise $A$ is designated. So the value is $1$.
4. Axiom 9, $\neg\neg A \to A$: for $A = 1$, $\tfrac12$, $0$, the value of $\neg\neg A$ is $1$, $\tfrac12$, $0$. So $\neg\neg A$ is designated only when $A$ is, and the value is $1$.
5. The formula $A^\circ = \neg(A \land \neg A)$. For $A = \tfrac12$: $A \land \neg A = 1$ and $A^\circ = 0$. For $A \in \set{0, 1}$: $A \land \neg A = 0$ and $A^\circ = 1$. So $A^\circ = 0$ exactly when $A = \tfrac12$.
6. Axiom 10, $B^\circ \to ((A \to B) \to ((A \to \neg B) \to \neg A))$: if $B = \tfrac12$, then $B^\circ = 0$ and the value is $1$. If $B \in \set{0, 1}$, then exactly one of $B$, $\neg B$ is designated. If $A \to B$ and $A \to \neg B$ are both $1$, then $A = 0$, so $\neg A = 1$. In every case the value is $1$.
7. Axiom 11: every formula $A \land B$, $A \lor B$, $A \to B$ has a value in $\set{0, 1}$, so by step 5 its $\circ$ is $1$, and the consequent is $1$.
8. By steps 1 to 7 and induction on derivations, every formula derivable from designated premises is designated.

Now let $v(p) = \tfrac12$ and $v(q) = 0$.
Then $v(p) = v(\neg p) = \tfrac12$ are designated and $v(q)$ is not.
By step 8, $p, \neg p \nvdash_{C_1} q$.
So $C_1$ is [[paraconsistent|C7YWCR87QJ]], and not [[explosive|TTKZGJEEK7]].

## Remarks

The same valuation shows that $p^\circ$ is not a theorem of $C_1$, since $v(p^\circ) = 0$.
So $\neg(A \land \neg A)$ fails in $C_1$, as da Costa intended.
The matrix is sound for $C_1$ but not complete; $C_1$ has no finite characteristic matrix.
Only atoms and negated formulas can take the value $\tfrac12$ here, which is why axiom 11 holds without effort.

## Explanations

### L1 human

We build a small three-valued "truth table" model in which all the axioms of $C_1$ are accepted.
In it, $p$ and "not $p$" are both accepted while $q$ is not.
Since the axioms and rule never lead from accepted to unaccepted, $C_1$ cannot prove $q$ from $p$ and "not $p$".

### L2 human

The key step is step 6.
Reductio is restricted to well-behaved $B$, and the middle value is exactly the value where $B$ is not well-behaved.
So the model can give $p$ the middle value without breaking reductio.
A trap is to check only the axioms and forget modus ponens; step 2 is needed for soundness.
