---
tag: 6FQKMC0PB2
kind: example
name: A written argument alone is not a proof scheme
msc: ["97E50", "97C30"]
topics: [VHGA6J4NZK]
audience: research
not_instance_of:
  - target: YVNRVXJR68
    note: a proof scheme is a standard of conviction of a person; a text with no reader and no writer has no such standard
uses: [YVNRVXJR68, GA27MSTQQD]
sources:
  - url: https://doi.org/10.1090/cbmath/007/07
    locator: pages 234-283
---

## Example

A textbook prints the text below, with no information about who wrote it or who reads it.

> Let $a$ and $b$ be integers.
> Then $(2a + 1) + (2b + 1) = 2(a + b + 1)$, which is even.

We check the text against the definition of a [[proof scheme|YVNRVXJR68]] and find that the definition does not apply.

1. A proof scheme of a person is what makes a claim certain for that person and what the person uses to persuade others.
2. The text is an argument, and a correct proof.
   No person is named whose conviction it describes, so it is not yet a standard of conviction.
3. Consider two readers.
   Reader R1 checks each step and is convinced.
   Reader R2 is convinced only after testing $a = 1$ and $b = 2$, which give $3 + 5 = 8$.
4. The same text serves a deductive episode for R1 and an empirical episode for R2, so the text alone does not fix a scheme.
5. The condition "belongs to a person" fails, and the text is not a proof scheme.

## Remarks

The example separates three notions that are easy to mix up.
A proof is a text with a logical property, a proof method is a form of text, and a proof scheme is a property of a person.
The same lines appear in [[the transformational example|GA27MSTQQD]], where a named student writes them to convince a classmate, and there a scheme can be inferred.
If the textbook adds that the text must be learned by heart for an examination, its readers may still hold different schemes, so the text still fixes none.

## Explanations

### L1 human

A proof on a page is like a recipe in a book.
The recipe is the same for all readers, but each reader trusts it for a different reason.
One reader understands each step, and another trusts it only after cooking it once.
A proof scheme describes the reader, not the page.

### L2 human

The test has three steps.
First identify the object, here a text with no writer and no reader.
Then recall that a scheme belongs to a person.
Finally show that two readers can hold different schemes with the same text, as R1 and R2 do.
Watch out: in research this mistake appears as classifying students only from their written answers, without asking what convinced them.
