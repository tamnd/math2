---
tag: D0S5PRXVZM
kind: example
name: Contraction fails in Łukasiewicz logic
msc: ["03B50", "03B52"]
topics: [WZP584JQ06]
audience: research
instance_of: [NFCEM44XYH]
uses: [JQ713VVD0G]
sources:
  - url: https://en.wikipedia.org/wiki/%C5%81ukasiewicz_logic
    locator: Real-valued semantics
---

## Example

In [[infinite-valued Łukasiewicz logic|JQ713VVD0G]], consider the contraction formula $p \to (p \odot p)$, where $x \odot y = \max(0, x + y - 1)$.
Let $v(p) = \tfrac12$.

1. Compute the strong conjunction: $v(p \odot p) = \max(0, \tfrac12 + \tfrac12 - 1) = 0$.
2. Compute the implication: $v(p \to (p \odot p)) = \min(1, 1 - \tfrac12 + 0) = \tfrac12$.
3. The value $\tfrac12$ is not the designated value $1$, so $p \to (p \odot p)$ is not a tautology.
4. In general the value is $\min(1, 1 - x + \max(0, 2x - 1))$.
   For $x \le \tfrac12$ it is $1 - x$, and for $x \ge \tfrac12$ it is $x$, so it equals $1$ only at $x = 0$ and $x = 1$.

So strong conjunction is not idempotent, and a premise $p$ cannot be used twice for free.

## Remarks

The rule form of contraction fails too.
The formula $(p \to (p \to q)) \to (p \to q)$ has the value $\tfrac12$ at $p = \tfrac12$ and $q = 0$.
Here $p \to q = \tfrac12$, then $p \to (p \to q) = \tfrac12 \to \tfrac12 = 1$, and finally $1 \to \tfrac12 = \tfrac12$.

The weak conjunction behaves differently.
It is $\min$, which is idempotent, so $p \to (p \land p)$ is a tautology.
The failure belongs to $\odot$ alone.

At $p = \tfrac12$ both $p \odot p$ and $\neg p \odot \neg p$ have the value $0$, while $p \oplus p$ and $\neg p \oplus \neg p$ have the value $1$.
So the middle value is the point where strong and weak connectives differ most.
On the classical values $0$ and $1$ the formula is always $1$, which is why two-valued tables never show the failure.

## Explanations

### L1 human

Two half-truths do not make a truth in Łukasiewicz logic.
"$p$ and also $p$", with the strong "and", is worth less than $p$ when $p$ is half true.
So you cannot use the same half-true premise twice and keep the same strength.

### L2 human

To refute a law, compute the inner connective first, then the implication with $\min(1, 1 - x + y)$, and look for a point where the value is below $1$.
Here the inner value at $\tfrac12$ is $0$, and the implication then gives $\tfrac12$.
This is the typical use of the example: it shows that Łukasiewicz logic is a logic without contraction, where premises behave like resources.
The [[substructural logics|98QF5J4W16]] study this feature in general.
Watch out: at $p = 0$ and $p = 1$ the formula has the value $1$, so a search over classical values alone finds nothing.
