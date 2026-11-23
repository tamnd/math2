---
tag: PXJSRNZ5TS
kind: example
name: Toulmin layout of a proof that the sum of two odd numbers is even
msc: ["97E50", "97C70"]
topics: [VHGA6J4NZK]
audience: research
instance_of: [RVZCSFDB2Y]
uses: [RVZCSFDB2Y, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Stephen_Toulmin
    locator: Toulmin model of argument
  - url: https://doi.org/10.1007/s10649-006-9059-8
    locator: pages 3-21
---

## Example

A student gives this argument in class.

> Take two odd numbers, $2a + 1$ and $2b + 1$.
> Their sum is $2a + 2b + 2$, which is $2(a + b + 1)$.
> So the sum is even.

We lay out the main step in the [[Toulmin model|RVZCSFDB2Y]] and check each part.

1. Claim $C$: for all integers $a$ and $b$, the sum $(2a + 1) + (2b + 1)$ is even.
2. Data $D$: the identity
   $$(2a + 1) + (2b + 1) = 2(a + b + 1),$$
   which follows from the commutative, associative and distributive laws, together with the fact that $a + b + 1$ is an integer.
3. Warrant $W$: an integer of the form $2k$, with $k$ an integer, is even.
   This is the definition of an even integer, and the student does not say it.
4. Backing $B$: the definition of "even" used in the course, and the laws of arithmetic in $\mathbb{Z}$.
5. Qualifier $Q$: "certainly", because the warrant is a definition and has no exceptions.
6. Rebuttal $R$: none, because every odd integer has the form $2a + 1$, so no pair of odd integers escapes the argument.

## Remarks

The example shows the model applied to a valid [[direct proof|0NTF6DMVAP]]: every part is present, the warrant is deductive, and the qualifier is "certainly".
The layout also brings a hidden step to light, the warrant of step 3, which a teacher can ask the student to state aloud.

Change the data and the layout changes with them.
If the student had argued "$3 + 5 = 8$ and $7 + 9 = 16$, so the sum is always even", the data would be two cases.
The warrant would then be inductive, and an honest qualifier would be "probably".

## Explanations

### L1 human

The student's argument has a claim (the sum is even), a fact ($2a + 2b + 2 = 2(a + b + 1)$) and a rule that the student does not say (twice a whole number is even).
The Toulmin model writes the rule down.
Because the rule always holds, the claim is certain.

### L2 human

To lay out any argument, start with the claim, which is usually the last sentence.
Then find the data, here the computation just before the claim.
Next ask which general rule links the data to the claim; here it is the definition of "even".
Finally ask how strong the link is, and since a definition has no exceptions, the qualifier is "certainly".
Watch out: the definition of "even" belongs in the warrant, not the data, because the data are particular facts about $a$ and $b$ and the definition is a general rule.
