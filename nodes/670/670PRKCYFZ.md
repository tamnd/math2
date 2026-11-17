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

In [[Japaridze's polymodal logic GLP|3EDRQJJHMT]] we show $\mathsf{GLP} \vdash \langle 1 \rangle \top \to \langle 0 \rangle^k \top$ for every $k \geq 0$, by [[induction|0ASJVEFA9J]] on $k$.

1. Monotonicity dual: the axiom $[0] \neg X \to [1] \neg X$ gives, by contraposition, $\vdash \langle 1 \rangle X \to \langle 0 \rangle X$ for every $X$.
2. Case $k = 0$: $\langle 0 \rangle^0 \top = \top$. Case $k = 1$: step 1 with $X = \top$.
3. Step from $k \geq 1$ to $k + 1$. By the induction hypothesis, $\vdash \langle 1 \rangle \top \to \langle 0 \rangle^k \top$.
4. Since $k \geq 1$, $\langle 0 \rangle^k \top = \langle 0 \rangle (\langle 0 \rangle^{k-1} \top)$, and the axiom $\langle 0 \rangle \varphi \to [1] \langle 0 \rangle \varphi$ gives $\vdash \langle 0 \rangle^k \top \to [1] \langle 0 \rangle^k \top$.
5. Steps 3 and 4 give $\vdash \langle 1 \rangle \top \to [1] \langle 0 \rangle^k \top$.
6. The normal box fact $[1] X \wedge \langle 1 \rangle \top \to \langle 1 \rangle X$, step 1 of [[the mixing lemma|ADJA5TD6PZ]], gives $\vdash \langle 1 \rangle \top \to \langle 1 \rangle \langle 0 \rangle^k \top$.
7. Step 1 with $X = \langle 0 \rangle^k \top$ gives $\vdash \langle 1 \rangle \top \to \langle 0 \rangle^{k+1} \top$.

## Remarks

Arithmetically, $\langle 0 \rangle^k \top$ realizes as the $k$-fold iterated [[consistency statement|4NBAX3VRQ7]]: $\mathrm{Con}(\mathsf{PA})$, then $\mathrm{Con}(\mathsf{PA} + \mathrm{Con}(\mathsf{PA}))$, and so on.
So 1-consistency of $\mathsf{PA}$ implies all finite iterations of consistency, provably in $\mathsf{PA}$.
In the worm order, $\langle 1 \rangle \top$ lies above every $\langle 0 \rangle^k \top$; it corresponds to the ordinal $\omega$, and $\langle 0 \rangle^k \top$ to $k$.
The converse fails for each $k$.
If $\mathsf{GLP} \vdash \langle 0 \rangle^k \top \to \langle 1 \rangle \top$, then the example gives $\mathsf{GLP} \vdash Y \to \langle 0 \rangle Y$ for $Y = \langle 0 \rangle^k \top$, that is, $\vdash [0] \neg Y \to \neg Y$.
Löb's rule for $[0]$ gives $\mathsf{GLP} \vdash \neg Y$, so $\mathsf{PA}$ would refute the true sentence $\mathrm{Con}^k(\mathsf{PA})$, which is impossible since $\mathsf{PA}$ is sound.

## Explanations

### L1 human

$\langle 1 \rangle \top$ says that a theory is consistent in a strong sense.
The example shows that this strong consistency implies ordinary consistency, consistency of "the theory plus its consistency", and so on, for any finite number of steps.

### L2 human

The typical use is the comparison of consistency statements by modal computation instead of arithmetic.
A trap: the induction step needs $k \geq 1$, because the axiom $\langle 0 \rangle \varphi \to [1] \langle 0 \rangle \varphi$ applies only to formulas that start with $\langle 0 \rangle$; the case $k = 1$ is handled separately by monotonicity.
