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

A strong box can carry a weak consistency fact inside it.
In [[Japaridze's polymodal logic GLP|3EDRQJJHMT]], let $m < n$ and let $A$, $B$ be formulas.
We show the mixing lemma:

$$\mathsf{GLP} \vdash \langle n \rangle A \wedge \langle m \rangle B \to \langle n \rangle (A \wedge \langle m \rangle B).$$

We use rule (RM) from [[the proof of the properties of Löb's axiom|17C5DRFAW7]] for the box $[n]$.
It holds because necessitation holds for every box of $\mathsf{GLP}$.

1. First a fact about any normal box: $\vdash [n] X \wedge \langle n \rangle Y \to \langle n \rangle (Y \wedge X)$.
   The tautology $X \to (\neg(Y \wedge X) \to \neg Y)$, rule (RM) and axiom $\mathrm{K}$ give $[n] X \to ([n] \neg(Y \wedge X) \to [n] \neg Y)$.
   This is the contrapositive form of the fact.
2. The axiom of $\mathsf{GLP}$ for $m < n$ gives $\vdash \langle m \rangle B \to [n] \langle m \rangle B$.
3. Step 1 with $X = \langle m \rangle B$ and $Y = A$ gives $\vdash [n] \langle m \rangle B \wedge \langle n \rangle A \to \langle n \rangle (A \wedge \langle m \rangle B)$.
4. Steps 2 and 3 give the mixing lemma.

## Remarks

The lemma is the main tool for computing with worms, because it moves a weaker consistency statement inside a stronger one.
For example, with $n = 1$, $m = 0$ and $A = B = \top$, it gives $\langle 1 \rangle \top \wedge \langle 0 \rangle \top \to \langle 1 \rangle \langle 0 \rangle \top$.

The lemma fails for $m = n$, already in $\mathsf{GL}$.
Take the frame with $1 R 2$ and $1 R 3$, with $p$ true only at $2$ and $q$ true only at $3$.
At $1$, both $\lozenge p$ and $\lozenge q$ hold.
But $2$ has no successors, so $2 \not\models \lozenge q$, and $3 \not\models p$.
So $\lozenge(p \wedge \lozenge q)$ fails at $1$.

The lemma also fails for $m > n$.
With $n = 0$, $m = 1$ and $A = B = \top$, it would give $\langle 1 \rangle \top \to \langle 0 \rangle \langle 1 \rangle \top$, since $\langle 1 \rangle \top$ implies $\langle 0 \rangle \top$.
Contraposed, this is $[0] \neg \langle 1 \rangle \top \to \neg \langle 1 \rangle \top$.
Löb's rule for $[0]$ then gives $\mathsf{GLP} \vdash [1] \bot$, which is false by arithmetical soundness.

## Explanations

### L1 human

Suppose a strong theory sees that $A$ is possible, and a weaker one sees that $B$ is possible.
Then the strong theory sees that "$A$, and $B$ is possible for the weak one" is possible.
The reason is that the strong theory can check the weak consistency fact $\langle m \rangle B$ itself.

### L2 human

The typical use is to rewrite a conjunction of consistency statements as one worm.
For example, $\langle 1 \rangle \top \wedge \langle 0 \rangle \langle 0 \rangle \top$ becomes $\langle 1 \rangle \langle 0 \rangle \langle 0 \rangle \top$ with $A = \top$ and $B = \langle 0 \rangle \top$.
Watch out for the order of indices.
The axiom $\langle m \rangle B \to [n] \langle m \rangle B$ needs $m < n$, and the remarks show that the lemma is false for $m = n$ and for $m > n$.

### L3 human

The mixing lemma is the modal form of a reflection argument.
A stronger theory proves that the weaker consistency facts it can see remain true inside its own possibilities.
In Beklemishev's calculus of worms, the lemma is one of the basic rules for comparing worms, whose order type is $\varepsilon_0$.
