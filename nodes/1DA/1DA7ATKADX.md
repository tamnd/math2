---
tag: 1DA7ATKADX
kind: example
name: The full Lambek calculus with exchange is algebraizable but not implicative
msc: ["03G27", "03B47"]
topics: [QYA4H5Y7VR]
audience: research
instance_of: [CESWST3NWA]
uses: [6JT3CMJT8F, XADWEW9TNP, E337A6WVH3, 26PHE1PQ3H]
sources:
  - book: isbn:9780444521415
  - book: isbn:9781848902077
---

## Example

Let $\mathrm{FL}_e$ be the full Lambek calculus with exchange, in $\land, \lor, \cdot, \to, 1, 0$, as a consequence relation.
It is finitely [[algebraizable|XADWEW9TNP]] with $K$ the commutative [[residuated lattices|E337A6WVH3]] with an extra constant, $E(x) = \set{x \wedge 1 \approx 1}$ and $\Delta(x, y) = \set{x \to y, y \to x}$.
So a formula is designated in an algebra iff its value is at least the unit $1$.
We show that $\mathrm{FL}_e$ is not implicative for any binary term $\Rightarrow$; see [[the Leibniz hierarchy|6JT3CMJT8F]].

1. Suppose $\Rightarrow$ makes $\mathrm{FL}_e$ implicative. Replacement and $\vdash z \Rightarrow z$ give $x \Rightarrow y, y \Rightarrow x \vdash \varphi(x) \Rightarrow \varphi(y)$ for every formula $\varphi(x)$, by induction on $\varphi$.
2. With $x \vdash y \Rightarrow x$ and $y \vdash x \Rightarrow y$ this gives $x, y \vdash \varphi(x) \Rightarrow \varphi(y)$, and modus ponens gives $x, y, \varphi(x) \vdash \varphi(y)$.
3. Take $\varphi(x) = x \to 1$. Interpret in [[the integers as a residuated lattice|26PHE1PQ3H]], with the unit $1$ as the integer $0$, $x \to y$ as $y - x$ and the constant $0$ as the integer $0$.
4. Send $x$ to the integer $0$ and $y$ to the integer $1$. Then $x$, $y$ and $x \to 1 = 0$ are all at least the unit, while $y \to 1 = -1$ is not.
5. By soundness, $x, y, x \to 1 \nvdash y \to 1$, against step 2.

## Remarks

1. The same model shows that $x \nvdash y \to x$ in $\mathrm{FL}_e$: with $x = 0$ and $y = 1$, $y \to x = -1$. The rule fails because $\mathrm{FL}_e$ has no weakening.
2. Implicative logics are regularly algebraizable: each algebra of the equivalent algebraic semantics has only one designated element. In the integers, both $0$ and $1$ are designated.
3. Adding weakening, that is, the integrality $x \le 1$ and $0 \le x$, gives intuitionistic logic without contraction, and with contraction too one gets intuitionistic logic, which is implicative.

## Explanations

### L1 human

In the Lambek calculus, a true premise cannot be added for free, so "if anything, then $x$" does not follow from $x$.
This blocks the classical way to express "equals", even though the logic has a good class of algebras.

### L2 human

1. In the integers, a value counts as true when it is at least $0$.
2. Both $0$ and $1$ are true, but they are different.
3. So "true" does not mean "equal to the top", and the logic is not implicative.

The typical use: the example separates the top two levels of the Leibniz hierarchy.
The trap: algebraizable does not mean that $E(x)$ is $x \approx 1$ with $1$ the top; here the designated set is an up-set with many elements.
