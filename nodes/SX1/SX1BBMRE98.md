---
tag: SX1BBMRE98
kind: example
name: Von Wright's preference principles
msc: ["03B45", "03A05"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [4BRXSBXXWG]
uses: [4BRXSBXXWG, 0VABYWJWH9]
sources:
  - url: https://en.wikipedia.org/wiki/Value_theory
    locator: Absolute and relative
  - url: https://en.wikipedia.org/wiki/Glossary_of_logic
    locator: Glossary of logic, section A
---

## Example

Fix a set $W$ of worlds with a total [[preorder|0VABYWJWH9]] and the all-all lifting of [[axiological logic|4BRXSBXXWG]].
So $p \succ q$ holds when $|p \wedge \neg q|$ and $|\neg p \wedge q|$ are nonempty and each world of the first set is strictly better than each world of the second.
We check three principles of von Wright.

1. Conjunctive expansion says that $p \succ q$ holds exactly when $(p \wedge \neg q) \succ (\neg p \wedge q)$.
   Put $p' = p \wedge \neg q$ and $q' = \neg p \wedge q$.
   These are incompatible, so $p' \wedge \neg q' \equiv p'$ and $\neg p' \wedge q' \equiv q'$, and both sides compare $|p'|$ with $|q'|$.
2. Contraposition says that $p \succ q$ holds exactly when $\neg q \succ \neg p$.
   Here $\neg q \wedge \neg\neg p \equiv p \wedge \neg q$ and $\neg\neg q \wedge \neg p \equiv \neg p \wedge q$, so both sides make the same comparison.
3. Asymmetry says that $p \succ q$ and $q \succ p$ never hold together.
   Otherwise a world $w$ in the nonempty set $|p \wedge \neg q|$ and a world $v$ in $|\neg p \wedge q|$ would satisfy $w > v$ and $v > w$, which is impossible.

For a concrete check, take the worlds $11 > 10 > 01 > 00$ over atoms $p, q$.
The formula $p \succ q$ holds by $10 > 01$.
Contraposition gives $\neg q \succ \neg p$, which compares the same two worlds.

## Remarks

Contraposition yields the link between good and bad.
The comparison $p \succ \neg p$ is the comparison $\neg\neg p \succ \neg p$, so $\mathrm{G}p$ holds exactly when $\mathrm{B}\neg p$ does.
The principle that $p \succ q$ implies $(p \wedge r) \succ (q \wedge r)$ is not valid.
On the ranking above it fails with $r = \neg p \wedge q$, since $p \wedge r$ is contradictory, so $(p \wedge r) \succ (q \wedge r)$ has an empty comparison set and does not hold.

## Explanations

### L1 human

To say that tea is better than coffee is to say that tea without coffee is better than coffee without tea.
It is also to say that having no coffee is better than having no tea.
Von Wright found these rules for the word "better".

### L2 human

1. Rewrite each comparison as a comparison of the two sets where exactly one proposition holds.
2. Check that both sides of a principle produce the same two sets.
3. A principle that changes the sets, such as adding a conjunct $r$, can fail.

The typical use is to derive value laws without fixing a particular ranking.
Watch out: the principles hold for the all-all lifting, and other liftings validate different principles.
