---
tag: CC604TAP5T
kind: example
name: An AGM revision on two atoms
msc: ["03B42"]
topics: [CQM9SRN8PM]
audience: research
instance_of: [Y05YQN7HGQ]
uses: [Y05YQN7HGQ, KV8J5H7KF2]
sources:
  - url: https://en.wikipedia.org/wiki/Belief_revision
    locator: The AGM postulates
---

## Example

The atoms are $p$ ("Tweety is a bird") and $q$ ("Tweety flies").
Write a valuation as $ab$, with $a$ the value of $p$ and $b$ the value of $q$.
Let $K = \mathrm{Cn}(p \wedge q)$, and take the following total preorder, most plausible first.
$$11 \; < \; 10 \approx 01 \; < \; 00$$
Define $\mathrm{Mod}(K * \varphi) := \min(\mathrm{Mod}(\varphi), \le)$, as in [[the representation theorem|KV8J5H7KF2]].
We compute four revisions and check postulates of [[AGM belief revision|Y05YQN7HGQ]].

1. The preorder is faithful to $K$: $\mathrm{Mod}(K) = \{11\}$, and $11$ lies strictly below every other valuation.
2. Revision by $\neg p$: the models are $01$ and $00$, and $01 < 00$.
   So $K * \neg p = \mathrm{Cn}(\neg p \wedge q)$: Tweety is not a bird, and still flies.
3. Revision by $\neg q$: the models are $10$ and $00$, and $10 < 00$.
   So $K * \neg q = \mathrm{Cn}(p \wedge \neg q)$: Tweety is a bird that does not fly.
4. Revision by $\neg(p \wedge q)$: the models are $10$, $01$ and $00$, and the minimal ones are $10$ and $01$.
   So $K * \neg(p \wedge q) = \mathrm{Cn}(p \leftrightarrow \neg q)$.
5. Revision by $p \vee q$: this is consistent with $K$, and $11$ is its minimal model.
   So $K * (p \vee q) = K = K + (p \vee q)$, as postulates 3 and 4 demand.
6. Success in step 4: the formula $\neg(p \wedge q)$ holds at $10$ and at $01$.
7. Postulates 7 and 8 with $\varphi = \neg(p \wedge q)$ and $\psi = \neg q$: the formula $\varphi \wedge \psi$ has models $10$ and $00$, so $K * (\varphi \wedge \psi) = \mathrm{Cn}(p \wedge \neg q)$.
8. The set $(K * \varphi) + \psi$ has the models $\{10, 01\} \cap \{10, 00\} = \{10\}$.
   So both sides equal $\mathrm{Cn}(p \wedge \neg q)$, and postulates 7 and 8 hold for this pair.

## Remarks

The ranking says that giving up one belief is more plausible than giving up both, and that the two beliefs are equally firm.
In step 4 the agent learns only that not both beliefs hold, so she suspends judgment between them, because $10$ and $01$ are tied.
If we change the ranking to $11 < 10 < 01 < 00$, step 4 gives $\mathrm{Cn}(p \wedge \neg q)$ instead: the agent keeps "Tweety is a bird" and gives up "Tweety flies".
The postulates allow both rankings, since they do not say which belief is more entrenched.

## Explanations

### L1 human

You believe that Tweety is a bird and that Tweety flies.
Someone tells you: "That is not all true."
With the first ranking you cannot tell which belief is wrong, so you keep only "exactly one of them is true".
With the second ranking you trust "bird" more than "flies", so you drop "flies".

### L2 human

To revise by hand, list the models of the new information, keep the lowest ones in the ranking, and believe everything true in all the kept models.
In step 2 the list is $01, 00$, the lowest is $01$, and the beliefs are $\neg p$ and $q$.
This is the typical use: a revision in a small knowledge base, computed in three lines.
Watch out in step 4: the ranking ties $10$ and $01$, so the result is the biconditional $p \leftrightarrow \neg q$, not one of the two atoms.
