---
tag: ~0eedd6e6
kind: example
name: A Boolean algebra with conjunction as multiplication
msc: ["03G15", "06E25"]
topics: [QYA4H5Y7VR]
audience: research
instance_of: [KCG48CWY69]
uses: [~fbfe9e5e, 0XADJKM699]
sources:
  - url: https://en.wikipedia.org/wiki/Residuated_Boolean_algebra
    locator: Examples
---

## Example

Let $B$ be a [[Boolean algebra|0XADJKM699]].
Put $x \cdot y = x \land y$, $e = 1$, and $x \backslash z = z / x = \neg x \lor z$.
We check [[the definition|~fbfe9e5e]].

1. Boolean algebra. This is given.
2. Monoid. $\land$ is associative, and $x \land 1 = x = 1 \land x$.
3. Residuation. If $x \land y \le z$, then $y = (x \land y) \lor (\neg x \land y) \le z \lor \neg x$.
4. Conversely, if $y \le \neg x \lor z$, then $x \land y \le (x \land \neg x) \lor (x \land z) = x \land z \le z$.
5. By commutativity of $\land$, the right residual is the same.

So $B$ is a [[residuated Boolean algebra|KCG48CWY69]].

## Remarks

1. The conjugates are $x \rhd z = z \lhd x = x \land z$.
2. With converse $x^{\smile} = x$, this is a relation algebra; see [[this example|~391395a2]].
3. The multiplication $\land$ is the only binary Boolean term operation that is a residuated monoid multiplication. It must send $0$ in each argument to $0$, be monotone, and have a unit, and a check of the 16 binary operations of $\set{0, 1}$ leaves only $\land$.
4. Every Boolean algebra is therefore a Heyting algebra with $x \to z = \neg x \lor z$.

## Explanations

### L1 human

In ordinary logic, "$x$ and $y$ imply $z$" means the same as "$y$ implies (if $x$ then $z$)".
Here "if $x$ then $z$" is "not $x$, or $z$".
So the usual "and" is a residuated multiplication.

### L2 human

1. Take $B = \mathcal{P}(\set{1, 2, 3})$, $x = \set{1, 2}$ and $z = \set{2}$.
2. Then $x \backslash z = \set{3} \cup \set{2} = \set{2, 3}$.
3. Check: $x \cap \set{2, 3} = \set{2} \subseteq z$.
4. Adding $1$ to $y$ gives $x \cap y \ni 1$, which is not in $z$. So $\set{2, 3}$ is the largest.

The typical use: this is the smallest family of residuated Boolean algebras, and it links them with classical logic.
The trap: here the unit is the top; in most residuated Boolean algebras it is not.
