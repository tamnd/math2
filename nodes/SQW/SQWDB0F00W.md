---
tag: SQWDB0F00W
kind: example
name: Expansion is not an AGM revision
msc: ["03B42"]
topics: [CQM9SRN8PM]
audience: research
not_instance_of:
  - target: Y05YQN7HGQ
    note: expansion by a formula that contradicts the belief set gives an inconsistent set, which breaks the consistency postulate
uses: [Y05YQN7HGQ]
sources:
  - url: https://en.wikipedia.org/wiki/Belief_revision
    locator: The AGM postulates
---

## Example

Define the operator below for every formula $\varphi$.
$$K * \varphi := K + \varphi = \mathrm{Cn}(K \cup \{\varphi\})$$
We show that it is not an [[AGM revision|Y05YQN7HGQ]].

1. Take $K = \mathrm{Cn}(p)$ and $\varphi = \neg p$.
2. The set $K + \neg p = \mathrm{Cn}(\{p, \neg p\})$ contains $p \wedge \neg p$, so it is the inconsistent belief set $K_\bot$.
3. The formula $\neg p$ is consistent, since a valuation with $p$ false satisfies it.
4. Postulate 5 demands that $K * \neg p$ be consistent, because $\neg p$ is consistent.
   Step 2 shows that it is not.
5. So expansion breaks postulate 5, and it is not an AGM revision.

The other seven postulates do hold for expansion.
Closure, success, inclusion, vacuity and extensionality hold by the definition of $\mathrm{Cn}$.
Postulates 7 and 8 hold with equality, since $(K + \varphi) + \psi = K + (\varphi \wedge \psi)$.

## Remarks

Expansion and revision agree when $\varphi$ is consistent with $K$, by postulates 3 and 4.
They differ only when $\neg\varphi \in K$, and then expansion collapses to $K_\bot$.
So consistency is the postulate that forces an agent to give up old beliefs.
For the inconsistent belief set $K_\bot$ itself, every AGM revision by a consistent $\varphi$ must leave $K_\bot$, while expansion stays there.

## Explanations

### L1 human

You believe that the shop is open.
Someone tells you that it is closed.
If you simply add this to your beliefs, you believe both "open" and "closed", and your beliefs become useless.
A real revision drops "open" first.

### L2 human

To test an operator against postulate 5, compute $K * \varphi$ for a consistent $\varphi$ and check that it is consistent.
For expansion the test fails as soon as $\neg\varphi \in K$.
The typical use of the example is to explain why revision needs a contraction first, as in the Levi identity.
Watch out: expansion is the correct operation for consistent news, and the failure is only for news that contradicts $K$.
