---
tag: ZV2MWBRN04
kind: example
name: Prefixing a double negation fails in predicate logic
msc: ["03F25", "03F55", "03B20"]
topics: [8XY7JYZKFW]
audience: grad
not_instance_of:
  - target: HGJVM49PA4
    note: "The map from A to not-not-A fails the second condition: classical logic proves the formula for all x, P(x) or not P(x), but intuitionistic logic does not prove its double negation."
uses: [Q11N8X99FK, NGHWZ9Y7ZV, QEZR7PZ2DD]
sources:
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
    locator: First-order logic
  - url: https://en.wikipedia.org/wiki/Glivenko%27s_theorem
    locator: lead section
  - book: isbn:9781447145578
---

## Example

Let $D$ be the map $A \mapsto \neg \neg A$ on formulas of first-order logic, and let $A = \forall x\, (P(x) \vee \neg P(x))$.
We show that $A$ is classically provable but $D(A) = \neg \neg A$ is not intuitionistically provable.
So $D$ is not a [[double-negation translation|HGJVM49PA4]] for predicate logic.

We use a [[Kripke model|NGHWZ9Y7ZV]] for first-order [[intuitionistic logic|Q11N8X99FK]].
Its nodes are $w_0 \le w_1 \le w_2 \le \cdots$, and the domain of $w_n$ is $\{ 0, 1, \dots, n \}$.
The node $w_m$ forces $P(k)$ if and only if $k < m$.
Forcing follows the usual clauses: $w \Vdash \neg B$ if no $v \ge w$ forces $B$, and $w \Vdash B \vee C$ if $w$ forces $B$ or forces $C$.
Also $w \Vdash \forall x\, B$ if every $v \ge w$ forces $B(d)$ for every $d$ in the domain of $v$.

1. The model is monotone.
   Domains grow along $\le$, and if $w_m$ forces $P(k)$, then $k < m \le m'$, so $w_{m'}$ forces $P(k)$.
2. Classical logic proves $A$: the excluded middle gives $P(x) \vee \neg P(x)$, and ${\forall}\mathrm{I}$ gives $A$.
3. Fix $m$.
   The element $m$ is in the domain of $w_m$, and $w_m$ does not force $P(m)$, since $m < m$ is false.
4. The node $w_{m+1} \ge w_m$ forces $P(m)$, so $w_m$ does not force $\neg P(m)$.
5. By steps 3 and 4, $w_m$ does not force $P(m) \vee \neg P(m)$, so $w_m$ does not force $A$.
6. Step 5 holds for every $m$, so no node forces $A$.
   Hence $w_0$ forces $\neg A$.
7. Then $w_0$ does not force $\neg \neg A$, because $w_0 \ge w_0$ forces $\neg A$.
8. Intuitionistic logic is sound for Kripke models: every provable formula is forced at every node.
   So $\nvdash_i \neg \neg A$.

So $D$ fails the condition "$\vdash_c B$ implies $\vdash_i D(B)$" at $B = A$.

## Remarks

For propositional formulas the map $D$ does work, by Glivenko's theorem.
What breaks it is the universal quantifier: the model keeps adding new objects, and each new object is undecided when it appears.

The same model forces $\forall x\, \neg \neg (P(x) \vee \neg P(x))$ at every node, since that formula is intuitionistically provable.
So the model refutes the double negation shift
$$\forall x\, \neg \neg B(x) \to \neg \neg \forall x\, B(x).$$
This is the reason why the Kuroda translation puts $\neg \neg$ after each $\forall$, and it is the principle that [[bar recursion|8CCG6F2FAT]] later interprets.

What changes with a finite chain $w_0 \le \cdots \le w_n$?
The last node then forces $\neg P(n)$, since no later node forces $P(n)$, so $w_n$ forces $A$ and every node forces $\neg \neg A$.
The infinite chain is essential.

## Explanations

### L1 human

For statements without "for all", putting "it is impossible that not" in front of a classical truth makes it acceptable to intuitionistic logic.
This example shows that the trick breaks with "for all".
Picture a collection of objects $0, 1, 2, \dots$ that grows over time, while our knowledge grows too.
At each time, the newest object is not yet known to have $P$, but it will be known to have $P$ later.
So at no time is every object decided, and "it is impossible that not every object is decided" fails at the start.

### L2 human

We check steps 3 to 7 at the node $w_2$, with domain $\{ 0, 1, 2 \}$.
The node $w_2$ forces $P(0)$ and $P(1)$, since $0 < 2$ and $1 < 2$.
It does not force $P(2)$, since $2 < 2$ is false.
The later node $w_3$ forces $P(2)$, so $w_2$ does not force $\neg P(2)$ either.
So $w_2$ does not force $P(2) \vee \neg P(2)$, and it does not force $A$.

The typical use of such a model is to show that a principle is not intuitionistically provable.
Watch out for finite chains: their last node decides everything, and then the model forces $\neg \neg A$.
