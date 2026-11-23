---
tag: K9KMSBSAKK
kind: example
name: Replacing only falsity is not an A-translation for intuitionistic logic
msc: ["03F25", "03F55"]
topics: [8XY7JYZKFW]
audience: grad
not_instance_of:
  - target: 6CCK0TT69P
    note: "Replacing only falsity by A does not preserve provability in HA: HA proves (falsity implies 0 = 1), but not (0 = 0 implies 0 = 1)."
uses: [6CCK0TT69P, PAQ4ZX2TX1, RXHJPVMPJH]
sources:
  - url: https://en.wikipedia.org/wiki/Friedman_translation
    locator: Definition
---

## Example

For a formula $A$, let $B \mapsto B[A/\bot]$ replace each occurrence of $\bot$ in $B$ by $A$ and keep all other atomic formulas.
We show that this map lacks the main property of the [[A-translation|6CCK0TT69P]]: it does not preserve provability in [[Heyting arithmetic|RXHJPVMPJH]].

1. Let $B = \bot \to 0 = 1$.
   HA proves $B$ by the rule ${\bot}\mathrm{E}$ of [[natural deduction|PAQ4ZX2TX1]], followed by ${\to}\mathrm{I}$.
2. Let $A = (0 = 0)$.
   Then $B[A/\bot] = (0 = 0 \to 0 = 1)$.
3. HA proves $0 = 0$, so if HA proved $B[A/\bot]$, it would prove $0 = 1$.
4. HA does not prove $0 = 1$, since every theorem of HA is true in $\mathbb{N}$.
5. So HA proves $B$ but not $B[A/\bot]$.

The A-translation instead gives $B^A = (\bot \vee A) \to (0 = 1 \vee A)$, and HA proves it by cases: either disjunct of the premise gives $A$, and $A$ gives $0 = 1 \vee A$.

## Remarks

The example shows why the A-translation adds $A$ to every atomic formula and not only to $\bot$.
After the translation every atom follows from $A$, and that is exactly what the rule of ex falso needs.

In minimal logic there is no rule ${\bot}\mathrm{E}$, and there the map $B \mapsto B[A/\bot]$ does preserve provability, because $\bot$ is then an ordinary propositional symbol.
The negative translation of a classical proof can be carried out in minimal logic, and this gives the refined A-translation used in program extraction.

## Explanations

### L1 human

A proof may use the rule "from a contradiction, anything follows".
If we replace "contradiction" by some statement $A$ that is not a contradiction, this rule becomes "from $A$, anything follows", which is false.
For example, from "$0 = 0$" we cannot conclude "$0 = 1$".
Friedman's translation avoids the problem by also weakening every basic statement $P$ to "$P$ or $A$".

### L2 human

We compare the two maps on derivations that do not use ex falso.
The formula $\neg \neg (0 = 0)$, that is, $(0 = 0 \to \bot) \to \bot$, is provable: from $0 = 0 \to \bot$ and $0 = 0$ we get $\bot$.
With $A = (0 = 1)$, replacing only $\bot$ gives
$$(0 = 0 \to 0 = 1) \to 0 = 1,$$
and HA proves this by the same modus ponens.
So on this derivation the naive map works, and the failure appears only when ex falso produces an atom that does not follow from $A$.

Watch out: a map that you test only on formulas proved without ex falso can look correct and still be wrong.
