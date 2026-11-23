---
tag: EJMQ2P9H5B
kind: example
name: Disjunction defined from implication
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
illustrates: [ZMVBAY7ZZD]
uses: [ZMVBAY7ZZD, 0NMG7W7Q11, 0F72FK8EKB, 05RSK4Q657, 0JMR2HM2N2]
sources:
  - url: https://en.wikipedia.org/wiki/Implicational_propositional_calculus
    locator: Functional (in)completeness
---

## Example

A language with only "if ... then" can still say "or".
Let $p$ and $q$ be propositional variables.
We show that the formula $(p \to q) \to q$ of the [[implicational propositional calculus|ZMVBAY7ZZD]] is [[logically equivalent|0JMR2HM2N2]] to the [[disjunction|0F72FK8EKB]] $p \lor q$.
We compare the two [[truth tables|05RSK4Q657]] row by row, with the rule that $a \to b$ is $0$ exactly when $a = 1$ and $b = 0$.

1. $p = 1$, $q = 1$: $p \to q = 1$, so $(p \to q) \to q = 1 \to 1 = 1$, and $p \lor q = 1$.
2. $p = 1$, $q = 0$: $p \to q = 0$, so $(p \to q) \to q = 0 \to 0 = 1$, and $p \lor q = 1$.
3. $p = 0$, $q = 1$: $p \to q = 1$, so $(p \to q) \to q = 1 \to 1 = 1$, and $p \lor q = 1$.
4. $p = 0$, $q = 0$: $p \to q = 1$, so $(p \to q) \to q = 1 \to 0 = 0$, and $p \lor q = 0$.

The two formulas agree in all four rows, so they are logically equivalent.

## Remarks

### What the example shows

The connective $\to$ alone can express disjunction, although it cannot express [[negation|PAG45X56GC]] or conjunction.
The definition is not symmetric in its form, but the values are symmetric: $(q \to p) \to p$ has the same table, by the same four rows with $p$ and $q$ exchanged.
That the two forms imply each other is a theorem of the implicational calculus, and its [[derivation|GEQWJPR0ZV]] needs Peirce's law.

### What changes with a constant

If $q$ is replaced by a formula that is always false, the formula becomes $(p \to \bot) \to \bot$, which is $\neg \neg p$.
This matches $p \lor \bot \equiv p$.
The other common definition, $\neg p \to q$ in the system L, needs negation, so it is not available here.

### Watch out

Do not write $p \to q$ for "$p$ or $q$".
At $p = 0$, $q = 0$ it has the value $1$, while $p \lor q$ has the value $0$.

## Explanations

### L1 human

The formula says: "if ($p$ implies $q$), then $q$".
It is false only when $p$ and $q$ are both false: then "$p$ implies $q$" is true, and $q$ is false.
In every other case it is true.
This is exactly the behavior of "$p$ or $q$".

### L2 human

We use the definition to write $p \lor q \lor r$ with $\to$ only.
First we write $p \lor q$ as $(p \to q) \to q$.
Then $(p \lor q) \lor r$ becomes
$$(((p \to q) \to q) \to r) \to r.$$
We check the row $p = q = r = 0$:
$$p \to q = 1, \qquad (p \to q) \to q = 0, \qquad 0 \to r = 1, \qquad 1 \to r = 0.$$
This is the value $0$ of $p \lor q \lor r$.
In every other row some variable is $1$, and the formula is $1$.
If $r = 1$, the last step gives $1$, and if $r = 0$, the formula has the value of $p \lor q$, which is $1$.
The typical use is to rewrite formulas with $\lor$ and $\to$ into the implicational language.
