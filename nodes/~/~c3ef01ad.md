---
tag: ~c3ef01ad
kind: example
name: Rational closure of the penguin base
msc: ["68T27", "03B60"]
topics: [NJB94B39QK]
audience: grad
instance_of: [~5ba6fe6b]
uses: [~5ba6fe6b, ~d45c3d4a, ~2b4be2dd]
sources:
  - url: https://plato.stanford.edu/entries/logic-nonmonotonic/
    locator: Non-monotonic Logic (SEP entry), section 3.6.3
---

## Example

Use the atoms $b$ (bird), $p$ (penguin), $f$ (flies) and $r$ (red), and the base
$$\mathbf{K} = \set{b \mathrel{|\!\sim} f,\ p \mathrel{|\!\sim} b,\ p \mathrel{|\!\sim} \neg f}.$$
We compute ranks as in the rational closure of Lehmann and Magidor, and compare with the [[preferential|~5ba6fe6b]] closure.

Ranks: for a set $\mathbf{K}'$, let $m(\mathbf{K}') = \set{\varphi \to \psi : \varphi \mathrel{|\!\sim} \psi \in \mathbf{K}'}$.
A formula has rank $0$ if it is consistent with $m(\mathbf{K}_0)$, where $\mathbf{K}_0 = \mathbf{K}$.
$\mathbf{K}_{i+1}$ is the set of assertions in $\mathbf{K}_i$ whose antecedent has no rank $\leq i$.
A formula has rank $i+1$ if it has no rank $\leq i$ and is consistent with $m(\mathbf{K}_{i+1})$.
The rational closure contains $\varphi \mathrel{|\!\sim} \psi$ if the rank of $\varphi \land \psi$ is less than the rank of $\varphi \land \neg\psi$, or if $\varphi \land \neg\psi$ has no rank.

1. $m(\mathbf{K}_0) = \set{b \to f, p \to b, p \to \neg f}$. It implies $\neg p$, since $p$ would give $b$, then $f$ and $\neg f$.
2. Rank $0$: $b \land r \land f$, $b \land \neg p$ (true at $b, f, r$ true and $p$ false). Not rank $0$: $p$, $b \land r \land \neg f$ (it violates $b \to f$), $b \land p$.
3. $\mathbf{K}_1 = \set{p \mathrel{|\!\sim} b,\ p \mathrel{|\!\sim} \neg f}$, since $b$ has rank $0$ and $p$ does not. So $m(\mathbf{K}_1) = \set{p \to b, p \to \neg f}$.
4. Rank $1$: $b \land r \land \neg f$, $p \land \neg f$ and $b \land p$, all true at $b, p, r$ true and $f$ false.
5. $\mathbf{K}_2 = \emptyset$, since $p$ has rank $1$. So $p \land f$, which contradicts $m(\mathbf{K}_1)$, has rank $2$.

Conclusions of the rational closure.

6. $b \mathrel{|\!\sim} f$ and $b \land r \mathrel{|\!\sim} f$, because rank $0$ is less than rank $1$ (steps 2 and 4).
7. $p \mathrel{|\!\sim} \neg f$, because $p \land \neg f$ has rank $1$ and $p \land f$ has rank $2$.
8. $b \mathrel{|\!\sim} \neg p$, because $b \land \neg p$ has rank $0$ and $b \land p$ has rank $1$.

The preferential closure does not contain $b \land r \mathrel{|\!\sim} f$.

9. Take three states: $s_1$ labeled $b, \neg p, f, \neg r$; $s_2$ labeled $b, \neg p, \neg f, r$; $s_3$ labeled $b, p, \neg f, \neg r$. Let $s_1 \prec s_2$ and $s_1 \prec s_3$.
10. This model is finite and ranked, with $s_1$ on the lowest level. By [[soundness of system P|~2b4be2dd]], its relation is preferential.
11. $\min \widehat{b} = \set{s_1}$, so $b \mathrel{|\!\sim} f$. $\min \widehat{p} = \set{s_3}$, so $p \mathrel{|\!\sim} b$ and $p \mathrel{|\!\sim} \neg f$. So the relation contains $\mathbf{K}$.
12. $\widehat{b \land r} = \set{s_2}$, and $s_2$ does not satisfy $f$. So $b \land r \mathrel{|\!\not\sim} f$.
13. The preferential closure is the intersection of all preferential relations that contain $\mathbf{K}$, so it does not contain $b \land r \mathrel{|\!\sim} f$.

## Remarks

The model in step 9 is ranked, so even the intersection of all rational relations that contain $\mathbf{K}$ misses $b \land r \mathrel{|\!\sim} f$.
Rational closure gets it by giving every formula the lowest rank that $\mathbf{K}$ allows.
Pearl's system Z gives the same conclusions.
The [[preferential model|~d45c3d4a]] in step 9 is one of many; the closure needs only one counterexample.

## Explanations

### L1 human

From "birds fly" we want to conclude "red birds fly", since color has nothing to do with flying.
Rational closure gives this conclusion.
It treats every situation as normal as the rules allow, and a red flying bird breaks no rule.

### L2 human

Ranks measure how exceptional a formula is with respect to the base: rank $0$ is normal, and penguins have rank $1$.
A conclusion holds if its normal cases have a lower rank than its exceptions.
A trap is to think that system $\mathbf{P}$ alone gives "red birds fly"; the model in step 9 shows that it does not.
