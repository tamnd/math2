---
tag: 166GE0RAPR
kind: example
name: The Russell set in naive set theory over LP
msc: ["03B53", "03E70"]
topics: [NJB94B39QK]
audience: ug2
instance_of: [3P0FM0AQF3]
uses: [3P0FM0AQF3, XGAMQBSE1G, 0HESMMSYEG, W28EY7C3FA]
sources:
  - url: https://plato.stanford.edu/entries/dialetheism/
    locator: Dialetheism (SEP entry), section 3.3
  - url: https://plato.stanford.edu/entries/logic-paraconsistent/
    locator: Paraconsistent Logic (SEP entry), section 2.3.2
---

## Example

[[Naive set theory|XGAMQBSE1G]] has the comprehension schema: for each condition $\varphi(x)$, there is a set $y$ with $\forall x\,(x \in y \leftrightarrow \varphi(x))$.
Take $\varphi(x) = x \notin x$, and let $R$ be the set it gives.
The instance at $x = R$ is $R \in R \leftrightarrow R \notin R$.

We read $A \leftrightarrow B$ as $(A \supset B) \land (B \supset A)$ with the material conditional of the [[logic of paradox|W28EY7C3FA]], and compute its value.
Let $a = v(R \in R)$, so $v(R \notin R) = 1 - a$.

1. $v(R \in R \supset R \notin R) = \max(1 - a, 1 - a) = 1 - a$.
2. $v(R \notin R \supset R \in R) = \max(a, a) = a$.
3. So $v(R \in R \leftrightarrow R \notin R) = \min(a, 1 - a)$.
4. This value is designated if and only if it is not $0$, that is, if and only if $a = \tfrac12$.

So every LP valuation that satisfies this instance of comprehension gives $R \in R$ the value $\mathsf{B}$.
Then $R \in R$ and $R \notin R$ are both designated: the Russell set is and is not a member of itself.
This is a [[dialetheia|3P0FM0AQF3]].

## Remarks

In classical logic, step 3 gives $\min(a, 1 - a) = 0$ for $a \in \set{0, 1}$, so the instance has no model; this is [[Russell's paradox|0HESMMSYEG]].
Over LP the contradiction is contained: the value $\tfrac12$ for $R \in R$ does not force a value for unrelated sentences.
The SEP entry on dialetheism reports that paraconsistent set theories with unrestricted comprehension avoid triviality in this way.
A theory with a detachable conditional must also avoid Curry's paradox, which the material conditional of LP does not raise, because modus ponens fails for it.

## Explanations

### L1 human

Russell's set contains exactly the sets that do not contain themselves.
Ask whether it contains itself, and each answer gives the other.
In LP, the statement "$R$ contains $R$" takes the value "both".
So the paradox becomes a true contradiction, not a collapse of the theory.

### L2 human

The computation reduces to $\min(a, 1 - a)$.
For $a = 1$ or $a = 0$ this is $0$; for $a = \tfrac12$ it is $\tfrac12$.
So only the middle value satisfies the comprehension instance.
A trap is to think that the theory is then trivial; triviality would need explosion, which LP lacks.
