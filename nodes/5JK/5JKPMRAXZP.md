---
tag: 5JKPMRAXZP
kind: example
name: Peano arithmetic is ω-consistent
msc: ["03F40", "03F30"]
topics: [HXHHWY3328]
audience: grad
instance_of: [4S29X1GTV4]
uses: [4S29X1GTV4, MPSCREYC3M, WP27CABPA4, 4A84VHDTHV]
sources:
  - url: https://en.wikipedia.org/wiki/%CE%A9-consistent_theory
    locator: lead section
  - book: isbn:9780521857840
---

## Example

$\mathsf{PA}$ proves $\exists x \, (x \cdot x = \underline{4})$, and it refutes $\underline{n} \cdot \underline{n} = \underline{4}$ for every $n \ne 2$, but it cannot refute $\underline{2} \cdot \underline{2} = \underline{4}$, because that sentence is true.
The real witness $2$ blocks the last refutation, and this is the whole idea of the example.

Let $\mathsf{PA}$ be [[first-order Peano arithmetic|MPSCREYC3M]].
We show that $\mathsf{PA}$ is [[ω-consistent|4S29X1GTV4]]: no formula $\varphi(x)$ has $\mathsf{PA} \vdash \exists x \, \varphi(x)$ together with $\mathsf{PA} \vdash \neg \varphi(\underline{n})$ for all $n$.

1. The [[structure of the natural numbers|WP27CABPA4]] $\mathbb{N}$ satisfies the basic axioms of $\mathsf{PA}$, by the definitions of $+$ and $\cdot$.
2. $\mathbb{N}$ satisfies every induction axiom, because a set of numbers that contains $0$ and is closed under $n \mapsto n + 1$ contains every number.
3. So $\mathbb{N} \models \mathsf{PA}$, and by [[soundness|4A84VHDTHV]] every theorem of $\mathsf{PA}$ is true in $\mathbb{N}$.
4. Suppose $\mathsf{PA} \vdash \exists x \, \varphi(x)$.
   By step 3, $\mathbb{N} \models \exists x \, \varphi(x)$, so there is $m \in \mathbb{N}$ with $\mathbb{N} \models \varphi(\underline{m})$.
5. If also $\mathsf{PA} \vdash \neg \varphi(\underline{m})$, then step 3 gives $\mathbb{N} \models \neg \varphi(\underline{m})$, which contradicts step 4.
6. So $\mathsf{PA} \nvdash \neg \varphi(\underline{m})$ for this $m$, and no formula witnesses $\omega$-inconsistency.

## Remarks

The argument used only that $\mathbb{N}$ is a model, so it works for every theory that is true in $\mathbb{N}$.
That is why it applies at once to $\mathsf{Q}$, to [[PA + Con(PA)|RD3VPJH67B]] and to true arithmetic.

The argument is semantic, and it happens outside $\mathsf{PA}$.
$\mathsf{PA}$ cannot prove a formal statement of its own $\omega$-consistency, because such a statement implies $\mathrm{Con}(\mathsf{PA})$, which $\mathsf{PA}$ does not prove.

Add an axiom that is false in $\mathbb{N}$, and step 3 breaks.
The result can then be $\omega$-inconsistent, as for [[PA + ¬Con(PA)|FK06QR6A44]].
This example is what lets us apply Gödel's original form of the first incompleteness theorem to $\mathsf{PA}$.

## Explanations

### L1 human

Every axiom of Peano arithmetic is true of the ordinary numbers $0, 1, 2, \ldots$.
So everything it proves is true of them.
If it proved "some number has property $P$", then some actual number, say $5$, would have $P$.
Then it cannot also prove "$5$ does not have $P$", because that would be false.

### L2 human

We trace the argument on $\varphi(x) := x \cdot x = \underline{4}$.
$\mathsf{PA}$ proves $\exists x \, \varphi(x)$, because $\mathsf{Q}$ already proves $\underline{2} \cdot \underline{2} = \underline{4}$ by computing
$$\underline{2} \cdot \underline{2} = \underline{2} \cdot \underline{1} + \underline{2} = (\underline{2} \cdot \underline{0} + \underline{2}) + \underline{2} = \underline{2} + \underline{2} = \underline{4}.$$
For each $n \ne 2$, the sentence $\underline{n} \cdot \underline{n} = \underline{4}$ is false, and $\mathsf{Q}$ refutes it by a similar computation.
At $n = 2$ the sentence is true, so $\mathsf{PA}$ cannot refute it, and $\varphi$ is not a witness of $\omega$-inconsistency.
In every case the same thing happens: the witness that exists in $\mathbb{N}$ blocks one of the refutations.
