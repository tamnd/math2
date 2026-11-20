---
tag: CWX983Y0DY
kind: example
name: Classical logic with the Sheffer stroke is not a non-classical logic
msc: ["03B60", "03B05"]
topics: [NJB94B39QK]
audience: grad
not_instance_of:
  - target: 3JK7T9D6X1
    note: the stroke language is a notational variant, since translations in both directions preserve classical consequence
uses: [3JK7T9D6X1, 1NNYWRN6B8, TDZVCWYJ9F, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Non-classical_logic
    locator: Classification of non-classical logics according to specific authors
  - url: https://en.wikipedia.org/wiki/Sheffer_stroke
    locator: Functional completeness
---

## Example

Let $\mathrm{L}_{|}$ be the propositional language with the single binary connective $\mid$, the [[Sheffer stroke|1NNYWRN6B8]], read by the truth table: $A \mid B$ is false exactly when $A$ and $B$ are both true.
Define $\Gamma \vDash_{|} B$ when every valuation that makes all of $\Gamma$ true makes $B$ true.
We show that $\mathrm{L}_{|}$ is a variant of classical logic, not a deviation or an extension.

1. Define a translation $t$ from classical formulas to stroke formulas: $t(p) = p$, $t(\neg A) = t(A) \mid t(A)$, and $t(A \land B) = (t(A) \mid t(B)) \mid (t(A) \mid t(B))$.
2. By the [[truth table|05RSK4Q657]] of $\mid$, $A \mid A$ has the value of $\neg A$, and $(A \mid B) \mid (A \mid B)$ has the value of $A \land B$. By induction on formulas, $v(t(A)) = v(A)$ for every valuation $v$.
3. Define a translation $s$ back by $s(p) = p$ and $s(A \mid B) = \neg(s(A) \land s(B))$. By the truth table again, $v(s(A)) = v(A)$ for every $v$.
4. By steps 2 and 3, $\Gamma \vDash A$ in classical logic if and only if $t(\Gamma) \vDash_{|} t(A)$, and $\Gamma \vDash_{|} B$ if and only if $s(\Gamma) \vDash s(B)$.

So the two systems have the same valid inferences up to a change of notation.
This is the definition of a variant.

## Remarks

The example shows that the classification of [[non-classical logics|3JK7T9D6X1]] concerns consequence, not symbols.
Step 2 uses the [[functional completeness|TDZVCWYJ9F]] of the stroke in an explicit form.
If we replace $\mid$ by a connective that is not functionally complete, such as $\lor$ alone, the translation $t$ does not exist; the result is a fragment of classical logic, still not a deviation.

## Explanations

### L1 human

The Sheffer stroke is one symbol that means "not both".
With it alone we can write "not $A$" as "not both $A$ and $A$".
We can also write "$A$ and $B$" in a longer way.
So every classical argument can be rewritten with the stroke, and the rewritten argument is valid exactly when the old one is.
Nothing about logic has changed; only the spelling changed.

### L2 human

We translate the inference from $p \land q$ to $p$.

1. $t(p \land q) = (p \mid q) \mid (p \mid q)$.
2. If this formula is true, then $p \mid q$ is false, by the table of $\mid$.
3. If $p \mid q$ is false, then $p$ and $q$ are both true.
4. So $(p \mid q) \mid (p \mid q) \vDash_{|} p$, as the classical inference predicts.

The typical use is to fix the meaning of "non-classical": the consequence relation must change.
A trap is to call every unusual notation a new logic.
