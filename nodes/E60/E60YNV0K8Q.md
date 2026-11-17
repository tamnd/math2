---
tag: E60YNV0K8Q
kind: example
name: A rope around the Earth made one metre longer
msc: ["00A35", "97G40"]
topics: [X1NSTVGDNQ]
audience: research
not_instance_of:
  - target: 4BT08RE4CR
    note: intuition about sizes predicts a gap much smaller than a centimetre, while the gap is about 16 centimetres and does not depend on the radius
uses: [4BT08RE4CR, 060W5CBZP6, 0C1VYVNV2N]
sources:
  - url: https://en.wikipedia.org/wiki/Circumference
    locator: Circle
---

## Example

A rope is wrapped tightly around the equator of a perfectly round Earth, of radius about $6371$ kilometres.
The rope is made $1$ metre longer and raised evenly all around, so that it forms a larger [[circle|060W5CBZP6]] with the same centre.
Question: how high above the ground is the rope?

1. The common intuitive answer: the rope is about $40\,000$ kilometres long, so $1$ extra metre is a tiny fraction, and the gap is microscopic.
2. Computation. Let $R$ be the radius of the Earth and $h$ the gap. The old length is $2\pi R$, and the new length is $2\pi (R + h)$.
3. The difference is $2\pi (R + h) - 2\pi R = 2\pi h$, and it equals $1$ metre.
4. So $h = \frac{1}{2\pi} \approx 0.159$ metres, about $16$ centimetres.
5. The radius $R$ cancels in step 3. The gap is the same for a rope around a football, around the Earth or around the Sun.

This is a case where [[intuition|4BT08RE4CR]] misleads, and we name the condition that fails.

1. Intuition judges the change by the relative change: $1$ metre out of $40\,000$ kilometres, that is $2.5 \times 10^{-8}$.
2. The question asks for an absolute change, and the circumference $2\pi R$ is a linear function of $R$ with slope $2\pi$.
3. For a linear function, a given change in the output needs the same change in the input from every starting point. The size of the Earth is irrelevant.

## Remarks

The relative change of the radius is indeed tiny: $\frac{0.159}{6\,371\,000} \approx 2.5 \times 10^{-8}$, the same as the relative change of the length.
So the intuition answers a different question, about proportions, correctly.
The puzzle is old and appears in many collections of recreational mathematics.
A trained intuition gives the right answer at once: since $C = 2\pi R$, we have $\Delta C = 2\pi \Delta R$ for any $R$.
The puzzle changes when the rope is pulled up at one point instead of raised evenly: then the height at that point grows with $R$, roughly like $R^{1/3}$, and for the Earth it is about $121$ metres.

## Explanations

### L1 human

Tie a rope tightly around the middle of the Earth.
Now add one metre to the rope, and lift it so it floats at the same height all around.
Most people guess that the gap is too thin to see.
In fact a cat could crawl under it: the gap is about $16$ centimetres.
The same extra metre lifts a rope around a tennis ball by the same $16$ centimetres.
Our feeling about size misleads us here, because the size of the ball does not matter.

### L2 human

We check the claim that the gap does not depend on the radius.

1. Around a ball of radius $0.1$ metres, the rope has length $2\pi \cdot 0.1 \approx 0.628$ metres. With $1$ metre added, it is $1.628$ metres, so its radius is $\frac{1.628}{2\pi} \approx 0.259$ metres. The gap is $0.259 - 0.1 = 0.159$ metres.
2. Around the Earth, $R = 6\,371\,000$ metres. The new radius is $R + \frac{1}{2\pi}$, so the gap is again $\frac{1}{2\pi} \approx 0.159$ metres.
3. The two gaps are equal, because $\frac{2\pi R + 1}{2\pi} - R = \frac{1}{2\pi}$ for each $R$.

The typical use: before trusting a sense of scale, write the quantity as a function and look at what it depends on.

A trap: concluding that intuition about proportions is always wrong; the relative change is tiny, and the intuition is right about it.
