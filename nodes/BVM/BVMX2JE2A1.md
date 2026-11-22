---
tag: BVMX2JE2A1
kind: example
name: The therefore sign marks a step, not the end of a proof
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: school
not_instance_of:
  - target: ET9J6R9T5C
    note: the sign introduces a conclusion inside an argument, and more steps can follow it
uses: [0B94TKFQJX, ET9J6R9T5C]
sources:
  - url: https://en.wikipedia.org/wiki/Therefore_sign
    locator: lead section
---

## Example

The *therefore sign* $\therefore$ is written `\therefore` in TeX, and it is the Unicode character U+2234.
We check, on a short argument, that it marks a step and not the [[end of a proof|ET9J6R9T5C]].

1. Let $n$ be an odd integer, so $n = 2k + 1$ for an integer $k$.
2. Square it:
   $$n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1.$$
3. $\therefore$ $n^2$ is odd.
4. $\therefore$ $n^2 + 1$ is even. $\square$

The sign appears twice, at steps 3 and 4, and the argument continues after its first use.
Only the square after step 4 marks the end of the [[proof|0B94TKFQJX]].

Check with $k = 3$: $n = 7$, $n^2 = 49 = 2 \cdot 24 + 1$, and $n^2 + 1 = 50$ is even.

## Remarks

The sign means "so" or "hence", and it can appear many times in one proof.
An end of proof mark appears once, after the last step.
The related sign $\because$, written `\because`, means "because".

Both signs are common in school mathematics and rare in research papers, where authors write the words instead.
If you delete the square after step 4, the argument still reads correctly, but the reader can no longer be sure that the proof is over, since a third $\therefore$ could follow.

## Explanations

### L1 human

The sign $\therefore$ means "so".
You write it before a conclusion, and you can write it many times in one proof.
The end of a proof gets a different mark, such as a square.

### L2 human

To find the end of a proof, look for the end mark, not for the last $\therefore$.
In the argument above, $\therefore$ at step 3 is followed by step 4, so it cannot be the end.
The square follows step 4, and nothing in the proof comes after it.
So a proof that ends with "$\therefore$ $n^2$ is odd" and no mark leaves its reader to guess whether more steps are coming.
