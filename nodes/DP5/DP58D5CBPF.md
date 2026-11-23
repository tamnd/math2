---
tag: DP58D5CBPF
kind: example
name: Givens and goals for the composition of surjections
msc: ["00A35", "03E20"]
topics: [STSM6PR7TX]
audience: ug1
instance_of: [872K5XB580]
uses: [872K5XB580, 01RVCMSN5N, 0THBK9V825, 07EH4R3RVQ]
sources:
  - book: isbn:9781108439534
    locator: Section 3.3
  - url: https://en.wikipedia.org/wiki/Surjective_function
    locator: Composition and decomposition
---

## Example

Let $f \colon A \to B$ and $g \colon B \to C$ be functions, and let $(g \circ f)(a) = g(f(a))$ be their [[composition|0THBK9V825]].
The claim is that [[the composition of surjections is surjective|07EH4R3RVQ]]: if $f$ and $g$ are [[surjective|01RVCMSN5N]], then $g \circ f$ is surjective.
We build the proof only from the logical forms of the givens and the goal, by the method of [[proof strategies by logical form|872K5XB580]].

In logical form, the two givens and the goal read as follows.

1. Given 1: $\forall b \in B \; \exists a \in A \; f(a) = b$.
2. Given 2: $\forall c \in C \; \exists b \in B \; g(b) = c$.
3. Goal: $\forall c \in C \; \exists a \in A \; g(f(a)) = c$.

We apply one move at each stage.

| Stage | Form of the goal or given | Move | Text of the proof | Lean tactic |
|---|---|---|---|---|
| 1 | goal $\forall c$ | take an arbitrary element | "Let $c \in C$." | `intro c` |
| 2 | given 2 at $c$, an $\exists$ | apply the given to $c$ and name the witness | "By given 2, there is $b \in B$ with $g(b) = c$." | `obtain ⟨b, hb⟩ := hg c` |
| 3 | given 1 at $b$, an $\exists$ | apply the given to $b$ and name the witness | "By given 1, there is $a \in A$ with $f(a) = b$." | `obtain ⟨a, ha⟩ := hf b` |
| 4 | goal $\exists a$ | name a witness | "We show that $a$ works." | `use a` |
| 5 | goal $g(f(a)) = c$ | compute | "$g(f(a)) = g(b) = c$." | `simp [ha, hb]` |

The final proof collects the texts of the stages.

> Let $c \in C$.
> Since $g$ is surjective, there is $b \in B$ with $g(b) = c$.
> Since $f$ is surjective, there is $a \in A$ with $f(a) = b$.
> Then $(g \circ f)(a) = g(f(a)) = g(b) = c$.
> Since $c$ was arbitrary, $g \circ f$ is surjective.
> $\square$

We check that each move was applied correctly.

1. At stage 1 the letter $c$ is new, and nothing is assumed about it except $c \in C$, so the conclusion holds for all $c$.
2. At stage 2 the given is used at the element $c$ that the proof already has, so $b$ depends on $c$.
3. At stage 3 the given is used at $b$, so $a$ depends on $b$ and hence on $c$.
   This is allowed, because the goal has the form "$\forall c \, \exists a$".
4. At stage 4 the witness $a$ comes after $c$, as the order of the quantifiers permits.

## Remarks

The proof needs no idea beyond the logical forms, since each sentence is forced by the form of the current goal or of a given.
The order "first $c$, then $b$, then $a$" runs against the arrows $A \to B \to C$.
The goal "$\forall c \, \exists a$" forces the proof to start at the far end.

In Lean the goal of stage 5 is `(g ∘ f) a = c`, and `simp` unfolds the composition and then rewrites with `ha` and `hb`.
Mathlib states the result as `Function.Surjective.comp`.

If we change "surjective" to "injective", the goal becomes $\forall a_1, a_2 \; (g(f(a_1)) = g(f(a_2)) \Rightarrow a_1 = a_2)$.
Then the move for "implies" starts the proof with "Suppose $g(f(a_1)) = g(f(a_2))$", as in [[proving injectivity and surjectivity|DD2P85Y8E9]].

## Explanations

### L1 human

Think of three towns $A$, $B$ and $C$, a bus line from $A$ to $B$, and a bus line from $B$ to $C$.
"Surjective" says that every stop in the target town is reached by some bus.
To show that every stop in $C$ can be reached from $A$, we pick a stop $c$ in $C$.
We find a stop $b$ in $B$ with a bus to $c$, and then a stop $a$ in $A$ with a bus to $b$.
So from $a$ we reach $c$ by changing buses at $b$.
Each step of this plan comes from the words "for every" and "there is" in the claim.

### L2 human

We plan a proof of "if $g \circ f$ is surjective, then $g$ is surjective" with the same tables.
The given is $\forall c \in C \; \exists a \in A \; g(f(a)) = c$, and the goal is $\forall c \in C \; \exists b \in B \; g(b) = c$.
The goal starts with "for all", so we write "Let $c \in C$".
The given at $c$ yields "there is $a \in A$ with $g(f(a)) = c$".
The goal now asks for a witness in $B$, and $f(a)$ is in $B$, so we write "Let $b = f(a)$".
Then $g(b) = g(f(a)) = c$, so $g$ is surjective.

The witness $b = f(a)$ is the only step that needed a thought.
Watch out: the witness of an $\exists$ goal may depend on the element of an earlier $\forall$, so choose it after that element, never before.
