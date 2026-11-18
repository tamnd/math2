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

Define $K * \varphi := K + \varphi = \mathrm{Cn}(K \cup \set{\varphi})$ for every $\varphi$.
We show that this operator is not an [[AGM revision|Y05YQN7HGQ]].

1. Take $K = \mathrm{Cn}(p)$ and $\varphi = \neg p$.
2. $K + \neg p = \mathrm{Cn}(\set{p, \neg p})$ contains $p \wedge \neg p$, so it is the inconsistent belief set $K_\bot$.
3. The formula $\neg p$ is consistent.
4. Postulate 5 demands that $K * \neg p$ be consistent, since $\neg p$ is consistent. Step 2 shows that it is not.
5. So expansion breaks postulate 5, and it is not an AGM revision.
6. Expansion satisfies postulates 1, 2, 3, 4, 6, 7 and 8: each of them holds with equality or with $K_\bot$ on both sides.

## Remarks

Expansion and revision agree when $\varphi$ is consistent with $K$, by postulates 3 and 4.
They differ only when $\neg\varphi \in K$, and then expansion collapses to $K_\bot$.
The example shows that consistency is the postulate that forces an agent to give up old beliefs.
For the inconsistent belief set $K_\bot$ itself, every revision by a consistent $\varphi$ must leave $K_\bot$, while expansion stays there.

## Explanations

### L1 human

You believe that the shop is open.
Someone tells you that it is closed.
If you simply add this to your beliefs, you believe both "open" and "closed", and your beliefs become useless.
A real revision drops "open" first.

### L2 human

1. Compute $K + \varphi$.
2. Test whether it is consistent while $\varphi$ is consistent.
3. If not, postulate 5 fails.

The typical use is to explain why revision needs contraction first, as in the Levi identity.
A trap: expansion is a correct operation for consistent news; the failure is only for news that contradicts $K$.
