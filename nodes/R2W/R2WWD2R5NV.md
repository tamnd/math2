---
tag: R2WWD2R5NV
kind: example
name: The formula p → □p is not a theorem of K
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
not_instance_of:
  - target: G989VP2NGP
    note: necessitation applies only to theorems, and p is not a theorem, so p → □p is not an instance
uses: [G989VP2NGP, NGHWZ9Y7ZV, JS8W7PA6JK, E87G6ZTMTN, TVE4F04KME, 5PZCVXYXDD]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

The [[necessitation rule|G989VP2NGP]] passes from the theorem $\varphi$ to the theorem $\square\varphi$.
The formula $p \to \square p$ looks like the same step written inside the language, but it is not a theorem of $\mathsf{K}$.

1. Take $W = \{ 1, 2 \}$, $R = \{ (1, 2) \}$ and $V(p) = \{ 1 \}$.
2. At $1$, $p$ is true, and the only successor $2$ lacks $p$, so $\square p$ is false.
3. So $p \to \square p$ is false at $1$, and by [[soundness|E87G6ZTMTN]], $\mathsf{K} \nvdash p \to \square p$.

Next we find the frames on which $p \to \square p$ is valid: they are the frames with $R[w] \subseteq \{ w \}$ for every $w$.

4. Let $R[w] \subseteq \{ w \}$ and let $p$ be true at $w$. Every successor of $w$ is $w$ itself, so $\square p$ is true at $w$.
5. Let some $w$ have a successor $v \neq w$, and put $V(p) = \{ w \}$. Then $p$ is true at $w$, and $\square p$ is false at $w$ because of $v$.
6. The frame of step 1 fails the condition at $1$, which matches step 3.

## Remarks

A rule about theorems and the matching formula say different things.
The rule is about theorems, which are true at every world of every model.
The formula is about truth at a single world, and truth at one world does not pass to its successors.

The logic $\mathsf{K} + (p \to \square p)$ is the logic of the frames with $R[w] \subseteq \{ w \}$ for all $w$.
Its [[canonical model|TVE4F04KME]] has this property.
If $\Gamma R \Delta$ and $\varphi \in \Gamma$, then $\square\varphi \in \Gamma$ by the axiom, so $\varphi \in \Delta$, and $\Gamma = \Delta$ by maximality.
If we also add the axiom $\mathrm{T}$, the frames become those with $R[w] = \{ w \}$, and we get the [[trivial logic|5PZCVXYXDD]], which proves $\square p \leftrightarrow p$.

## Explanations

### L1 human

The rule says that what logic proves is necessary.
The formula $p \to \square p$ says something stronger: whatever is true is necessary.
That is false, since it may rain today without being necessary that it rains.
In a picture with two worlds, it rains in world 1 and not in world 2, and world 1 sees world 2.
Then in world 1 rain is true but not necessary.

### L2 human

Take the frame with $W = \{ a, b \}$ and $R = \{ (a, a), (b, b) \}$.
Each $R[w]$ is $\{ w \}$, so $p \to \square p$ is valid on it, by step 4.
Now take $W = \{ a, b \}$ with $R = \{ (a, b), (b, a) \}$ instead.
This frame fails the condition, and $V(p) = \{ a \}$ makes $p \to \square p$ false at $a$.
Both frames are symmetric, so symmetry is not the property that matters here.
The typical use of the example is to check that a proof does not apply necessitation to a hypothesis.
Watch out: $\top \to \square\top$ is a theorem, because $\top$ is a theorem, but this does not make $p \to \square p$ a theorem, since $p$ is not one.
