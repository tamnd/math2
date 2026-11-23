---
tag: BAKPBE2677
kind: example
name: A deduction of "for all implies there exists" in the Hilbert-style calculus
msc: ["03B10"]
topics: [TTCRX3NFNY]
audience: ug2
instance_of: [N95HV0VWSM]
uses: [2B00FE6K5W, 05006AJ7DZ, 0Y0MQYST0M]
sources:
  - book: isbn:9780122384523
    locator: Section 2.4
  - url: https://en.wikipedia.org/wiki/Hilbert_system
    locator: Predicate logic (example system)
---

## Example

We work in the [[Hilbert-style predicate calculus|2B00FE6K5W]] $\mathsf{H}$ of Enderton, for a language with a unary relation symbol $P$.
In this calculus $\exists x\, P(x)$ abbreviates $\neg \forall x\, \neg P(x)$.
We show that $\vdash_{\mathsf{H}} \forall x\, P(x) \to \exists x\, P(x)$ by checking the following deduction line by line.
To keep the lines short, write $A$ for $\forall x\, P(x)$, $B$ for $P(x)$ and $C$ for $\forall x\, \neg P(x)$.

1. $A \to B$, that is, $\forall x\, P(x) \to P(x)$.
   This is an axiom of group 2 with $\varphi = P(x)$ and $t = x$, since $x$ is substitutable for itself and $P(x)[x/x] = P(x)$.
2. $C \to \neg B$, that is, $\forall x\, \neg P(x) \to \neg P(x)$.
   This is an axiom of group 2 with $\varphi = \neg P(x)$ and $t = x$.
3. $(A \to B) \to ((C \to \neg B) \to (A \to \neg C))$.
   This is an axiom of group 1, a [[tautology|05006AJ7DZ]], as the check below shows.
4. $(C \to \neg B) \to (A \to \neg C)$, by [[modus ponens|0Y0MQYST0M]] from lines 1 and 3.
5. $A \to \neg C$, by modus ponens from lines 2 and 4.

Line 5 is $\forall x\, P(x) \to \neg \forall x\, \neg P(x)$, which is $\forall x\, P(x) \to \exists x\, P(x)$.

It remains to check that line 3 is a tautology.
Its prime formulas are $A$, $B$ and $C$, and we look for a truth assignment that makes it false.
Such an assignment makes $A \to B$ and $C \to \neg B$ true and $A \to \neg C$ false.
Since $A \to \neg C$ is false, $A$ is true and $C$ is true.
Then $A \to B$ gives $B$ true, and $C \to \neg B$ gives $B$ false.
This is impossible, so no assignment makes line 3 false.
Check: the truth table of line 3 has 8 rows, and the argument shows that the only candidate rows, those with $A$ and $C$ true, are not counterexamples.

## Remarks

### What the example shows

The calculus splits the work in two.
The quantifier axioms of group 2 remove the quantifiers, and a single tautology does all the propositional reasoning.
The same five lines work with any formula $\varphi$ in place of $P(x)$, because $x$ is always substitutable for itself.

### Where the empty domain enters

The formula is valid because the domain of a structure is never empty: if $P$ holds of every element, it holds of some element.
The calculus builds this assumption into group 2, which allows the instance at the variable $x$ even when the language has no constant.
In a logic that allows an empty domain, the formula is false in the empty structure, and the instantiation axiom has to be restricted.

### The converse

The converse $\exists x\, P(x) \to \forall x\, P(x)$ has no deduction.
It is false in a structure with two elements where $P$ holds of one of them, and the calculus is [[sound|4A84VHDTHV]].

## Explanations

### L1 human

The formula says: "if every object has the property $P$, then some object has the property $P$".
This is true as long as there is at least one object, and logic assumes that there is one.
The deduction first removes "every" twice, once for "$P$" and once for "not $P$".
Then a rule of pure propositional logic joins the two pieces.
For example, if every student in a class passed, then some student passed, because the class has at least one student.

### L2 human

How would you find this deduction?
Work backward from the goal $A \to \neg C$.
The two instantiation axioms give $A \to B$ and $C \to \neg B$ with the same $B$, so ask which propositional law turns these two into $A \to \neg C$.
That law is line 3, and two steps of modus ponens finish.
Watch out: do not look for a rule for $\exists$, since the calculus has none and $\exists$ is only an abbreviation.
