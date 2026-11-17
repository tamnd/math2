---
tag: ADJA5TD6PZ
kind: example
name: The mixing lemma of GLP
msc: ["03F45", "03B45"]
topics: [3E7M66WW6Q]
audience: research
instance_of: [3EDRQJJHMT]
uses: [3EDRQJJHMT, 17C5DRFAW7]
sources:
  - url: https://en.wikipedia.org/wiki/Japaridze%27s_polymodal_logic
    locator: Language and axiomatization
---

## Example

In [[Japaridze's polymodal logic GLP|3EDRQJJHMT]], let $m < n$ and let $A$, $B$ be formulas.
We show $\mathsf{GLP} \vdash \langle n \rangle A \wedge \langle m \rangle B \to \langle n \rangle (A \wedge \langle m \rangle B)$.

1. A normal box fact: $\vdash [n] X \wedge \langle n \rangle Y \to \langle n \rangle (Y \wedge X)$. The tautology $X \to (\neg(Y \wedge X) \to \neg Y)$ and rule (RM) of [[the proof of the properties of Löb's axiom|17C5DRFAW7]], with axiom $\mathrm{K}$, give $[n] X \to ([n] \neg(Y \wedge X) \to [n] \neg Y)$, which is the contrapositive form of the claim.
2. The axiom of $\mathsf{GLP}$ for $m < n$ gives $\vdash \langle m \rangle B \to [n] \langle m \rangle B$.
3. Step 1 with $X = \langle m \rangle B$ and $Y = A$ gives $\vdash [n] \langle m \rangle B \wedge \langle n \rangle A \to \langle n \rangle (A \wedge \langle m \rangle B)$.
4. Steps 2 and 3 give the claim.

## Remarks

The lemma fails for $m = n$ in $\mathsf{GL}$: $\lozenge p \wedge \lozenge q \to \lozenge(p \wedge \lozenge q)$ fails at the root of the frame $1 R 2$, $1 R 3$ with $p$ true only at $2$ and $q$ true only at $3$.
There $2$ has no successors, so $2 \not\models \lozenge q$, and $3 \not\models p$.
It is the main tool for computing with worms: it moves a weaker consistency statement inside a stronger one.
For example, with $n = 1$, $m = 0$ and $A = B = \top$, it gives $\langle 1 \rangle \top \wedge \langle 0 \rangle \top \to \langle 1 \rangle \langle 0 \rangle \top$.

## Explanations

### L1 human

If a strong theory sees that $A$ is possible, and a weaker one sees that $B$ is possible, then the strong theory sees that "$A$, and $B$ is possible for the weak one" is possible.
The reason is that the strong theory can check the weak consistency fact $\langle m \rangle B$ itself.

### L2 human

The typical use is to rewrite products of consistency statements as one worm.
A trap: the order of indices matters; the axiom $\langle m \rangle B \to [n] \langle m \rangle B$ needs $m < n$, and with $m > n$ the lemma is not available.
