---
tag: S92WKWKZPE
kind: example
name: The box reading of premises gives classical consequence
msc: ["03B53", "03B45"]
topics: [NJB94B39QK]
audience: grad
not_instance_of:
  - target: 489SFB5NX2
    note: reading each premise as necessary, not possible, merges all participants into one view
  - target: C7YWCR87QJ
    note: the resulting consequence relation is classical and explosive
uses: [2YA3PJNVMS, VC3A2VWXND, 1HK0VYWTV7]
sources:
  - url: https://plato.stanford.edu/entries/logic-paraconsistent/
    locator: Paraconsistent Logic (SEP entry), section 3.1
---

## Example

Change the [[definition of discussive consequence|2YA3PJNVMS]] by reading each formula as $\Box A$ instead of $\Diamond A$.
So $A_1, \ldots, A_n \vDash_{\Box} B$ when $\Box A_1, \ldots, \Box A_n \vDash_{\mathrm{S5}} \Box B$.
We show that $\vDash_{\Box}$ is classical [[consequence|1HK0VYWTV7]].

1. Suppose $A_1, \ldots, A_n \vDash B$ classically. In an [[S5|VC3A2VWXND]] model where each $\Box A_i$ is true, every world makes all $A_i$ true, hence makes $B$ true. So $\Box B$ is true.
2. Suppose $A_1, \ldots, A_n \nvDash B$ classically, by a valuation $v$. The one-world model with valuation $v$ makes each $\Box A_i$ true and $\Box B$ false.
3. By steps 1 and 2, $\vDash_{\Box}$ is classical consequence.

In particular $p, \neg p \vDash_{\Box} q$, because no world makes $p$ and $\neg p$ both true, so $\Box p$ and $\Box\neg p$ have no common model.

## Remarks

The box reading requires every participant to hold every premise.
Then the participants form one consistent view, and the discussion behaves like one classical theory.
The diamond reading is what lets disagreement exist without explosion.

## Explanations

### L1 human

If every premise must be held by everyone, then nobody can hold "$p$" while somebody else holds "not $p$".
So a set of premises with $p$ and "not $p$" describes no possible discussion.
Then, as in classical logic, everything follows from it.

### L2 human

The two readings differ in one quantifier: "some world" for $\Diamond$, "all worlds" for $\Box$.
With "all worlds", the two-world counterexample to explosion fails, since $p$ is false at $w_2$, so $\Box p$ is false.
A trap is to think that any modal translation gives a paraconsistent logic; the choice of operator decides it.
