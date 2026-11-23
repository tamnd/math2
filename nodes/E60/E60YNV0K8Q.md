---
tag: E60YNV0K8Q
kind: example
name: A rope around the Earth made one meter longer
msc: ["00A35", "97G40"]
topics: [X1NSTVGDNQ]
audience: research
not_instance_of:
  - target: 4BT08RE4CR
    note: intuition about sizes predicts a gap much smaller than a centimeter, while the gap is about 16 centimeters and does not depend on the radius
uses: [4BT08RE4CR, 060W5CBZP6, 0C1VYVNV2N]
sources:
  - url: https://en.wikipedia.org/wiki/Circumference
    locator: Circle
---

## Example

A rope is wrapped tightly around the equator of a perfectly round Earth, of radius about $6371$ kilometers.
The rope is made $1$ meter longer and raised evenly all around, so that it forms a larger [[circle|060W5CBZP6]] with the same center.
How high above the ground is the rope?

1. The usual intuitive answer is that the rope is about $40\,000$ kilometers long, so $1$ extra meter is a tiny fraction, and the gap is microscopic.
2. We compute instead, with $R$ the radius of the Earth and $h$ the gap: the old length is $2\pi R$ and the new length is $2\pi (R + h)$.
3. The difference is
   $$2\pi (R + h) - 2\pi R = 2\pi h,$$
   and it equals $1$ meter.
4. So $h = \frac{1}{2\pi} \approx 0.159$ meters, about $16$ centimeters.
5. The radius $R$ canceled in step 3, so the gap is the same for a rope around a football, around the Earth or around the Sun.

Here [[intuition|4BT08RE4CR]] misleads, and we name what went wrong.

1. Intuition judges the change by the relative change, $1$ meter out of $40\,000$ kilometers, which is $2.5 \times 10^{-8}$.
2. The question asks for an absolute change, and the circumference $2\pi R$ is a linear function of $R$ with slope $2\pi$.
3. For a linear function, a given change in the output needs the same change in the input from every starting point, so the size of the Earth does not matter.

## Remarks

The relative change of the radius is indeed tiny, $\frac{0.159}{6\,371\,000} \approx 2.5 \times 10^{-8}$, the same as the relative change of the length.
So the intuition answers a different question, about proportions, and answers it correctly.
A trained intuition gets the right answer at once: since $C = 2\pi R$, a change $\Delta C$ in the length gives $\Delta R = \Delta C / (2\pi)$ for every $R$.

The puzzle changes when the rope is pulled up at one point instead of raised evenly.
Then the height at that point grows with $R$, roughly like $R^{1/3}$, and for the Earth it is about $121$ meters.

## Explanations

### L1 human

Tie a rope tightly around the middle of the Earth.
Now add one meter to the rope, and lift it so that it floats at the same height all around.
Most people guess that the gap is too thin to see.
In fact a cat could crawl under it, since the gap is about $16$ centimeters.
The same extra meter lifts a rope around a tennis ball by the same $16$ centimeters.
Our feeling for size misleads us here, because the size of the ball does not matter.

### L2 human

Check that the gap does not depend on the radius.
Around a ball of radius $0.1$ meters, the rope has length $2\pi \cdot 0.1 \approx 0.628$ meters.
With $1$ meter added it is $1.628$ meters, so its radius is $1.628 / (2\pi) \approx 0.259$ meters, and the gap is $0.259 - 0.1 = 0.159$ meters.
Around the Earth, the new radius is $R + \frac{1}{2\pi}$, so the gap is again about $0.159$ meters.
The two gaps agree because, for every $R$,
$$\frac{2\pi R + 1}{2\pi} - R = \frac{1}{2\pi}.$$
Before you trust a sense of scale, write the quantity as a function and look at what it depends on.
Watch out: the lesson is not that intuition about proportions is always wrong, since the relative change really is tiny.
