---
tag: 670PRKCYFZ
kind: example
name: 1-consistency implies iterated consistency in GLP
msc: ["03F45", "03B45"]
topics: [3E7M66WW6Q]
audience: research
instance_of: [3EDRQJJHMT]
uses: [3EDRQJJHMT, ADJA5TD6PZ, 4NBAX3VRQ7, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Japaridze%27s_polymodal_logic
    locator: Language and axiomatization
---

## Example

One strong consistency statement implies every finite tower of ordinary ones.
In [[Japaridze's polymodal logic GLP|3EDRQJJHMT]] we show, for every $k \geq 0$:

$$\mathsf{GLP} \vdash \langle 1 \rangle \top \to \langle 0 \rangle^k \top.$$

We use [[induction|0ASJVEFA9J]] on $k$.

1. The dual of monotonicity: the axiom $[0] \neg X \to [1] \neg X$ gives, by contraposition, $\vdash \langle 1 \rangle X \to \langle 0 \rangle X$ for every $X$.
2. Case $k = 0$: $\langle 0 \rangle^0 \top = \top$, so the claim is a tautology.
3. Step from $k$ to $k + 1$.
   By the induction hypothesis, $\vdash \langle 1 \rangle \top \to \langle 0 \rangle^k \top$.
4. Next, $\vdash \langle 0 \rangle^k \top \to [1] \langle 0 \rangle^k \top$.
   For $k \geq 1$, $\langle 0 \rangle^k \top$ starts with $\langle 0 \rangle$, and this is the axiom $\langle 0 \rangle \varphi \to [1] \langle 0 \rangle \varphi$.
   For $k = 0$, it is $\top \to [1] \top$, which holds by necessitation for $[1]$.
5. Steps 3 and 4 give $\vdash \langle 1 \rangle \top \to [1] \langle 0 \rangle^k \top$.
6. The normal box fact $[1] X \wedge \langle 1 \rangle \top \to \langle 1 \rangle X$ is step 1 of [[the mixing lemma|ADJA5TD6PZ]] with $Y = \top$.
   With step 5 it gives $\vdash \langle 1 \rangle \top \to \langle 1 \rangle \langle 0 \rangle^k \top$.
7. Step 1 with $X = \langle 0 \rangle^k \top$ gives $\vdash \langle 1 \rangle \top \to \langle 0 \rangle^{k+1} \top$.

Check on the step from $k = 0$: step 6 gives $\langle 1 \rangle \top \to \langle 1 \rangle \top$, and step 7 gives $\langle 1 \rangle \top \to \langle 0 \rangle \top$, which is step 1 with $X = \top$.

## Remarks

Arithmetically, $\langle 0 \rangle^k \top$ realizes as the $k$-fold iterated [[consistency statement|4NBAX3VRQ7]].
For $k = 1$ it is $\mathrm{Con}(\mathsf{PA})$, for $k = 2$ it is $\mathrm{Con}(\mathsf{PA} + \mathrm{Con}(\mathsf{PA}))$, and so on.
So 1-consistency of $\mathsf{PA}$ implies all finite iterations of consistency, and $\mathsf{PA}$ proves this.
In the worm order, $\langle 1 \rangle \top$ lies above every $\langle 0 \rangle^k \top$.
It has the place $\omega$, while $\langle 0 \rangle^k \top$ has the place $k$.

The converse fails for each $k$.
Write $Y = \langle 0 \rangle^k \top$, and suppose $\mathsf{GLP} \vdash Y \to \langle 1 \rangle \top$.
With the example this gives $\mathsf{GLP} \vdash Y \to \langle 0 \rangle Y$, that is, $\vdash [0] \neg Y \to \neg Y$.
Löb's rule for $[0]$ gives $\mathsf{GLP} \vdash \neg Y$.
For $k = 0$ this is $\vdash \bot$.
For $k \geq 1$, $\mathsf{PA}$ would refute the true sentence $\mathrm{Con}^k(\mathsf{PA})$, which is impossible because $\mathsf{PA}$ is sound.

## Explanations

### L1 human

$\langle 1 \rangle \top$ says that a theory is consistent in a strong sense.
The example shows that this strong consistency implies ordinary consistency.
It also implies the consistency of "the theory plus its consistency", and so on, for any finite number of steps.

### L2 human

The typical use is to compare consistency statements by a modal computation instead of by arithmetic.
Each step of the induction does the same three things.
It pushes $\langle 0 \rangle^k \top$ under $[1]$, combines it with $\langle 1 \rangle \top$, and then weakens $\langle 1 \rangle$ to $\langle 0 \rangle$.
Watch out in step 4: the axiom $\langle 0 \rangle \varphi \to [1] \langle 0 \rangle \varphi$ applies only to formulas that start with $\langle 0 \rangle$.
For $k = 0$ the formula is $\top$, and necessitation does the job instead.

### L3 human

The example is the first step of Beklemishev's ordinal analysis with worms.
Each $\langle 0 \rangle^k \top$ stands for a finite ordinal, and $\langle 1 \rangle \top$ stands for $\omega$, their limit.
In the same way, $\langle n + 1 \rangle \top$ implies every finite tower of $\langle n \rangle$, and the worms climb to $\varepsilon_0$.
