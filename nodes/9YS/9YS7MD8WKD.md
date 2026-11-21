---
tag: 9YS7MD8WKD
kind: example
name: The three-element Nelson chain
msc: ["03G25"]
topics: [QYA4H5Y7VR]
audience: research
instance_of: [XRGDT262HQ]
uses: [GN34CR1AH1, NG943XNQWH]
sources:
  - book: isbn:9780444521415
---

## Example

Let $A = \set{0, u, 1}$ with $0 < u < 1$, $\sim 0 = 1$, $\sim u = u$ and $\sim 1 = 0$.
Put $1 \to y = y$, and $x \to y = 1$ for $x \in \set{0, u}$.
We check [[the definition|GN34CR1AH1]].

1. De Morgan algebra. $\sim$ reverses the chain and $\sim \sim x = x$.
2. Kleene condition. $x \land \sim x \le u$ and $y \lor \sim y \ge u$ for all $x, y$.
3. Clause 3 for $x = 1$: $z \le 0 \lor y = y$ iff $z \le 1 \to y$.
4. Clause 3 for $x = u$: $u \land z \le u \le u \lor y$ always, and $z \le 1 = u \to y$ always.
5. Clause 3 for $x = 0$: $0 \le 1 \lor y$ always, and $z \le 1$ always.
6. Clause 4. If $x \land y = 1$, both sides equal $z$. Otherwise $x \land y \in \set{0, u}$, the left side is $1$, and either $x \ne 1$ or $y \ne 1$, so the right side is $1$ too.

So $A$ is a [[Nelson algebra|XRGDT262HQ]].

## Remarks

1. $A$ is the twist structure over the two-element [[Heyting algebra|NG943XNQWH]], with $1 = (1, 0)$, $u = (0, 0)$, $0 = (0, 1)$.
2. $u \to 0 = 1$, but $u \not\le 0$. This is where the weak implication differs from the order.
3. The strong implication gives $u \Rightarrow 0 = (u \to 0) \land (1 \to u) = u \ne 1$, as it should.
4. The Heyting implication on the same chain gives $u \to 0 = 0$, so the two structures differ.

## Explanations

### L1 human

The three values are true, unknown and false.
Strong negation swaps true and false, and leaves unknown alone.
"If unknown, then $y$" is accepted for every $y$, in the weak sense.

### L2 human

1. Compute $u \to u = 1$ and $1 \to u = u$.
2. Compute the strong implication $1 \Rightarrow u = (1 \to u) \land (\sim u \to \sim 1) = u \land (u \to 0) = u \land 1 = u$.
3. Since $1 \not\le u$, the strong implication is not $1$, as expected.

The typical use: this algebra generates the variety of three-valued Nelson algebras.
The trap: $u \to 0 = 1$ looks like "$u$ is false", but it only says that $u$ is not verified.
