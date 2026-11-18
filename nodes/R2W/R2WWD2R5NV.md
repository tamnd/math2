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
The formula $p \to \square p$ would say the same thing inside the language, at each world, and it is not a theorem of $\mathsf{K}$.

1. Take $W = \set{1, 2}$, $R = \set{(1, 2)}$ and $V(p) = \set{1}$.
2. At $1$, $p$ is true, and the only successor $2$ lacks $p$, so $\square p$ is false.
3. So $p \to \square p$ fails at $1$, and by [[soundness|E87G6ZTMTN]], $\mathsf{K} \nvdash p \to \square p$.
4. Frame condition: $p \to \square p$ is valid on a frame $(W, R)$ exactly when $R[w] \subseteq \set{w}$ for every $w$.
5. If $R[w] \subseteq \set{w}$ and $p$ is true at $w$, then every successor of $w$ is $w$ itself and has $p$. So $\square p$ is true at $w$.
6. If some $w$ has a successor $v \neq w$, put $V(p) = \set{w}$. Then $p$ is true at $w$, and $\square p$ is false at $w$ because of $v$.
7. So the frame of step 1 fails the condition at $1$, which matches step 3.

## Remarks

The example shows the difference between a rule and the corresponding formula.
The rule "from $\vdash \varphi$ infer $\vdash \square\varphi$" is about theorems, which are true at every world of every model.
The formula $p \to \square p$ is about truth at a single world, and truth at one world does not pass to the successors.
The logic $\mathsf{K} + (p \to \square p)$ is the logic of the frames with $R[w] \subseteq \set{w}$ for all $w$.
Its [[canonical model|TVE4F04KME]] satisfies the condition: if $\Gamma R \Delta$ and $\varphi \in \Gamma$, then $\square\varphi \in \Gamma$, so $\varphi \in \Delta$, and $\Gamma = \Delta$ by maximality.
If we add axiom $\mathrm{T}$, the frames become those with $R[w] = \set{w}$, and we get the [[trivial logic|5PZCVXYXDD]] with $\square p \leftrightarrow p$.
If we change the countermodel to $R = \set{(1, 1)}$ on $W = \set{1}$, then $p \to \square p$ holds, as step 5 predicts.

## Explanations

### L1 human

The rule says: what logic proves is necessary.
The formula $p \to \square p$ says something stronger: whatever is true is necessary.
That is false: it rains today, but it is not necessary that it rains.
In a picture with two worlds, it rains in world 1 and not in world 2, and world 1 sees world 2.
Then in world 1 rain is true, but not necessary.

### L2 human

1. Take the frame with $W = \set{a, b}$ and $R = \set{(a, a), (b, b)}$.
2. Each $R[w]$ is $\set{w}$, so $p \to \square p$ is valid on it, by step 5.
3. The frame with $W = \set{a, b}$ and $R = \set{(a, b), (b, a)}$ fails the condition, so $V(p) = \set{a}$ refutes $p \to \square p$ at $a$.
4. Both frames are symmetric, so symmetry is not the property that matters here.

The typical use of this example is to check that a proof does not apply necessitation to a hypothesis.
A trap: $\mathsf{K} \vdash \square\top$, and $\top \to \square\top$ is a theorem, but this does not make $p \to \square p$ a theorem, since $p$ is not a theorem.
