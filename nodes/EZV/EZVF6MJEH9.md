---
tag: EZVF6MJEH9
kind: example
name: The word normal in "normal subgroup" is a defined term
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug1
not_instance_of:
  - target: 4M1FGQ0HNZ
    note: the word normal in normal subgroup has an exact definition, so it is a defined term and not jargon
uses: [4M1FGQ0HNZ, 0CB0DX5BVV, 0515A6D2Y1, 0X1JXT47GA]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: lead section
---

## Example

In everyday English, "normal" means "usual" or "ordinary", and it has no exact meaning.
In group theory, the phrase "normal subgroup" has an exact definition.
A [[subgroup|0X1JXT47GA]] $N$ of a group $G$ is [[normal|0CB0DX5BVV]] when $gng^{-1} \in N$ for every $g \in G$ and every $n \in N$.
We show that this use of "normal" is a defined term and not [[jargon|4M1FGQ0HNZ]].

1. A defined term has a definition that decides each case.
   The definition above decides, for each subgroup, whether it is normal.
2. Test it on the [[symmetric group|0515A6D2Y1]] $S_3$ and the subgroup $H = \{e, (1\,2)\}$.
3. Take $g = (1\,3)$ and $n = (1\,2)$.
   Conjugation by $g$ renames the points by $g$, and $g$ sends $1 \mapsto 3$ and $2 \mapsto 2$, so
   $$g \, (1\,2) \, g^{-1} = (g(1)\; g(2)) = (3\,2) = (2\,3).$$
4. The element $(2\,3)$ is not in $H$.
   So $H$ is not normal in $S_3$, and the claim "$H$ is normal" is false.
5. Test the subgroup $A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$.
   It has index $6 / 3 = 2$ in $S_3$, and a subgroup of index $2$ is normal, so $A_3$ is normal.
6. Both answers follow from the definition alone, with no appeal to taste or context.
   So "normal" in "normal subgroup" is a defined term.

## Remarks

A jargon word such as "nice" fails step 1.
No definition decides whether a given function is nice, and the answer changes from one lecture to the next.

The same English word can be a defined term in one phrase and an everyday word in another.
"Normal subgroup", "normal matrix" and "normal distribution" each have an exact definition, and the three definitions are unrelated.
"A normal reader would expect this result" uses "normal" in its everyday sense.
So the test is not the word but the phrase: look for the definition that goes with the whole phrase in its field.

## Explanations

### L1 human

Some words have a special, exact meaning in mathematics.
"Normal" in "normal subgroup" is one of them: there is a precise test, and every subgroup either passes it or fails it.
This is different from a word like "nice", where two mathematicians can disagree.
So "normal" here is a technical term, like "prime" in "prime number", and not jargon.

### L2 human

To decide whether a word in a sentence is a defined term or jargon, look first for a definition in the text or in a standard source for its field.
If you find one, test it on an example and a non-example, as with $A_3$ and $\{e, (1\,2)\}$ above.
If no definition exists, the word is jargon, and a careful writer replaces it by the exact condition.
For "normal subgroup" the test found both a normal and a non-normal subgroup of $S_3$, so the word draws a real line.
Watch out: a defined term can have different definitions in different fields, so "normal" must be read with its field in mind.
