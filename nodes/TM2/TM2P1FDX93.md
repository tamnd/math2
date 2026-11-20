---
tag: TM2P1FDX93
kind: example
name: Classical consequence is monotonic
msc: ["03B05", "03B60"]
topics: [NJB94B39QK]
audience: ug1
not_instance_of:
  - target: BKDFH4PKRP
    note: classical consequence keeps every conclusion when premises are added
uses: [BKDFH4PKRP, 1HK0VYWTV7, H31CS3HK5P]
sources:
  - url: https://plato.stanford.edu/entries/logic-nonmonotonic/
    locator: Non-monotonic Logic (SEP entry), section 1
---

## Example

Classical propositional [[logical consequence|1HK0VYWTV7]] is monotonic, so it is not a [[nonmonotonic logic|BKDFH4PKRP]].
Recall that $\Sigma \vDash \varphi$ means: every [[truth valuation|H31CS3HK5P]] that makes all of $\Sigma$ true makes $\varphi$ true.

1. Let $\Sigma \vDash \varphi$ and $\Sigma \subseteq \Sigma'$.
2. Let $v$ be a valuation that makes all of $\Sigma'$ true.
3. Since $\Sigma \subseteq \Sigma'$, the valuation $v$ makes all of $\Sigma$ true.
4. By step 1, $v$ makes $\varphi$ true.
5. So $\Sigma' \vDash \varphi$.

For instance, $\set{b, b \to f} \vDash f$, and so $\set{b, b \to f, p, p \to \neg f} \vDash f$.
The larger set is unsatisfiable, so it implies every formula, in particular $f$ and $\neg f$.

## Remarks

The argument works for every consequence relation defined by "truth in all models of the premises".
Nonmonotonic logics replace "all models" by "selected models", or they add rules with consistency conditions.
Then a larger premise set can select different models, and step 3 fails.

## Explanations

### L1 human

In ordinary logic, a valid argument stays valid when we add premises.
Every situation where all the new premises are true is one where the old premises are true.
So the old conclusion is still true there.

### L2 human

Monotonicity follows from one fact: more premises allow fewer models.
In the Tweety example, classical logic does not withdraw "Tweety flies"; it derives a contradiction instead.
A trap is to think that a contradiction removes conclusions; in classical logic it adds all of them.
