---
tag: WMQTJQDMC8
kind: example
name: A structured proof that a composition of injective functions is injective
msc: ["00A35", "03E20"]
topics: [STSM6PR7TX]
audience: research
instance_of: [H2W8D7BMSW]
uses: [H2W8D7BMSW, 09NWETVTNY, 0THBK9V825]
sources:
  - doi: 10.1080/00029890.1995.12004627
    locator: pages 600-608
  - url: https://en.wikipedia.org/wiki/Lean_(proof_assistant)
    locator: Examples (Lean 4)
---

## Example

*Theorem.* Let $f \colon A \to B$ and $g \colon B \to C$ be [[injective functions|09NWETVTNY]].
Then the [[composition|0THBK9V825]] $g \circ f \colon A \to C$ is injective.

Recall that $h \colon X \to Y$ is injective when, for all $x_1, x_2 \in X$, $h(x_1) = h(x_2)$ implies $x_1 = x_2$.
Recall also that $(g \circ f)(a) = g(f(a))$ for each $a \in A$.

*Structured proof.*

- `<1>1.` ASSUME: $a_1, a_2 \in A$ and $g(f(a_1)) = g(f(a_2))$. PROVE: $a_1 = a_2$.
    - `<2>1.` $f(a_1) = f(a_2)$. PROOF: $f(a_1)$ and $f(a_2)$ are elements of $B$, and $g$ is injective, so the assumption of `<1>1` gives the equality.
    - `<2>2.` Q.E.D. PROOF: by `<2>1`, since $f$ is injective.
- `<1>2.` Q.E.D. PROOF: by `<1>1` and the definition of an injective function, since $(g \circ f)(a) = g(f(a))$.

We check the structure.

1. The top level has two steps. Step `<1>1` is the definition of injectivity of $g \circ f$, written as ASSUME/PROVE. Step `<1>2` concludes the theorem from it.
2. The assumption of `<1>1` holds only inside the proof of `<1>1`, that is, in the steps `<2>1` and `<2>2`.
3. Step `<2>1` uses the injectivity of $g$, and step `<2>2` uses the injectivity of $f$. Each hypothesis of the theorem is used exactly once, and the citations show where.
4. Each leaf proof is one sentence that names its facts. A reader can check each leaf without reading the rest.

The same proof in Lean 4 with Mathlib has the same tree, written backward from the goal.
The goal is `Function.Injective (g ∘ f)`, with the hypotheses `hf : Function.Injective f` and `hg : Function.Injective g`.

1. `intro a₁ a₂ h`: this is step `<1>1`. It introduces $a_1$, $a_2$ and the hypothesis `h : (g ∘ f) a₁ = (g ∘ f) a₂`, and the goal becomes `a₁ = a₂`.
2. `apply hf`: this is step `<2>2`, read backward. The goal becomes `f a₁ = f a₂`, the statement of step `<2>1`.
3. `apply hg`: this is the proof of `<2>1`, read backward. The goal becomes `g (f a₁) = g (f a₂)`.
4. `exact h`: the hypothesis `h` is this goal, because `(g ∘ f) a` unfolds to `g (f a)`.

Mathlib states the theorem as `Function.Injective.comp`.

## Remarks

1. The example shows that a structured proof makes the use of each hypothesis visible. The citation of $g$ is in `<2>1`, and the citation of $f$ is in `<2>2`.
2. For a surjective $f$ and $g$, the same format gives the proof that $g \circ f$ is surjective. Step `<1>1` takes $c \in C$, and `<2>1` picks $b$ with $g(b) = c$. Then `<2>2` picks $a$ with $f(a) = b$, and `<2>3` concludes $g(f(a)) = c$.
3. If $f$ is not injective, step `<2>2` fails. For $A = \{1, 2\}$, $B = \{0\}$, $C = \{0\}$ and the constant maps, $g \circ f$ maps $1$ and $2$ to $0$, so it is not injective.
4. If only $f$ is injective, the proof breaks at step `<2>1`, but the conclusion can still hold. For $f \colon \{1\} \to \{1, 2\}$ with $f(1) = 1$ and $g$ constant on $\{1, 2\}$, the map $g \circ f$ is injective, because its domain has one element.

## Explanations

### L1 human

Two machines are joined: the first turns each input into a code, and the second turns each code into a label.
Each machine sends different inputs to different outputs.
Then the joined machine also sends different inputs to different labels.
The structured proof writes this in two levels.
The top step says what has to be shown.
The lower steps go back one machine at a time: equal labels give equal codes, and equal codes give equal inputs.

### L2 human

We test the proof on $f \colon \{1, 2, 3\} \to \{1, \dots, 6\}$ with $f(a) = 2a$, and $g \colon \{1, \dots, 6\} \to \mathbb{Z}$ with $g(b) = b + 10$.

1. Both maps are injective: $2a_1 = 2a_2$ gives $a_1 = a_2$, and $b_1 + 10 = b_2 + 10$ gives $b_1 = b_2$.
2. Here $(g \circ f)(a) = 2a + 10$, with the values $12$, $14$, $16$ at $a = 1, 2, 3$.
3. Step `<1>1`: let $a_1, a_2 \in \{1, 2, 3\}$ with $2a_1 + 10 = 2a_2 + 10$.
4. Step `<2>1`: the injectivity of $g$ removes the $+10$, so $2a_1 = 2a_2$, that is, $f(a_1) = f(a_2)$.
5. Step `<2>2`: the injectivity of $f$ removes the factor $2$, so $a_1 = a_2$.

The typical use of the format is for a proof that will be checked by a machine.
Each step then becomes a tactic or a lemma.
A trap is to cite $f$ in step `<2>1`.
The equation in `<1>1` is about values of $g$, so only the injectivity of $g$ can remove $g$ from it.
