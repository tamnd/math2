---
tag: SB9HMACX5D
kind: example
name: Reflexivity at a point is not the translation of a modal formula
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
not_instance_of:
  - target: YW6YGBMVQY
    note: Rxx has one free variable but is not equivalent to the standard translation of any modal formula
uses: [YW6YGBMVQY, 1HQ1W36J4V, X27BR4YP2Y, 086QKPF0A6, NGHWZ9Y7ZV, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Standard_translation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Bisimulation
    locator: lead section
---

## Example

The [[first-order|086QKPF0A6]] formula $Rxx$ has one free variable, like every [[standard translation|YW6YGBMVQY]] $\mathrm{ST}_x(\varphi)$.
We show that no modal formula $\varphi$ has $\mathrm{ST}_x(\varphi)$ equivalent to $Rxx$ on all models.

### Two models that look alike

Let $\mathfrak{M}_1$ have one world $w$, the relation $\{ (w, w) \}$, and every variable false.
Let $\mathfrak{M}_2$ have $W = \mathbb{N}$, the relation $\{ (n, n + 1) : n \in \mathbb{N} \}$, and every variable false.
We claim that for every modal formula $\varphi$ and every $n \in \mathbb{N}$, $\mathfrak{M}_1, w \models \varphi$ holds if and only if $\mathfrak{M}_2, n \models \varphi$.

We use [[structural induction|12MQ2NJ29A]] on $\varphi$, for all $n$ at once.
For a variable and for $\bot$, both sides are false.
For $\alpha \to \beta$, both sides are computed from the values of $\alpha$ and $\beta$, which agree by the induction hypothesis.
For $\square\alpha$, the only successor of $w$ is $w$, so $\square\alpha$ holds at $w$ exactly when $\alpha$ holds at $w$.
The only successor of $n$ is $n + 1$, so $\square\alpha$ holds at $n$ exactly when $\alpha$ holds at $n + 1$.
By the induction hypothesis at $n + 1$, these two conditions agree, which proves the claim.

### The contradiction

Now suppose $\mathrm{ST}_x(\varphi)$ is equivalent to $Rxx$.
$Rww$ holds in $\mathfrak{M}_1$, so $\mathfrak{M}_1, w \models \varphi$ by [[the correctness of the standard translation|1HQ1W36J4V]].
By the claim with $n = 0$, $\mathfrak{M}_2, 0 \models \varphi$, so $R00$ would hold in $\mathfrak{M}_2$.
But $(0, 0)$ is not in the relation of $\mathfrak{M}_2$, so no such $\varphi$ exists.

## Remarks

### The bisimulation behind it

The relation $Z = \{ (w, n) : n \in \mathbb{N} \}$ is a [[bisimulation|X27BR4YP2Y]] between the two models, and the claim is its [[invariance lemma|TKFFTAX30E]].
[[Van Benthem's theorem|Y89MGMWE4H]] says that the translations of modal formulas are, up to equivalence, exactly the first-order formulas invariant under bisimulation, and $Rxx$ is not invariant.

### Frame validity is different

Reflexivity of a whole frame is defined by the axiom $\square p \to p$, as in [[the second-order translation of T|KM2BKWZKW8]].
That is a statement about all worlds and all valuations, not about one point in one model, so it does not contradict this example.

### Watch out

The example shows that one first-order formula is not modal, and it does not show that reflexivity is invisible to modal logic.
Validity on a frame and truth at a point in a model are different questions, and modal formulas answer the first one for reflexivity.

## Explanations

### L1 human

A point with a loop and an endless chain look the same from the inside.
At each step you can move on, and you always see the same facts.
Modal formulas only describe what you see when you move along arrows.
So they cannot tell the loop from the chain.
But "this point sees itself" is true for the loop and false for the chain.

### L2 human

Match the loop point $w$ with every point $n$ of the chain.
Each move from $w$ is matched by the move from $n$ to $n + 1$, and each move from $n$ is matched by the move from $w$ to $w$.
So $w$ and $n$ satisfy the same modal formulas.
As $Rww$ holds and $R00$ fails, $Rxx$ is not modal.
The typical use is to prove that a property is not modally expressible by exhibiting two bisimilar points that differ on it.

### L3 human

The argument uses the easy half of van Benthem's theorem: the translations of modal formulas are invariant under bisimulation.
[[Hybrid logic|NVPQ9W9DED]] adds a nominal $i$ true at one world only, and then $i \to \lozenge i$ expresses $Rxx$ at the world named $i$.
