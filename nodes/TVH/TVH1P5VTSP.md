---
tag: TVH1P5VTSP
kind: example
name: Burke–Schumann flame
msc: [80A25, 76V05]
illustrates: [SXSCYXH068]
uses: [SXSCYXH068, DG49VBBT91]
sources:
  - url: https://en.wikipedia.org/wiki/Burke–Schumann_flame
same_as:
  wikidata: Q30674079
  wikipedia: Burke–Schumann flame
---

## Example

Consider a fuel stream, in which the fuel mass fraction is $Y_{F,1}$, and an oxidiser stream, in which the oxidiser mass fraction is $Y_{O,2}$.
The streams meet and react in one step in which $s$ units of mass of oxidiser burn one unit of mass of fuel.
Assume that fuel and oxidiser have the same diffusivity $D$, and let $\mathbf{u}$ be the velocity field.
The reaction removes oxidiser at $s$ times the rate at which it removes fuel, so the *mixture fraction*
$$Z = \frac{s Y_F - Y_O + Y_{O,2}}{s Y_{F,1} + Y_{O,2}}$$
solves the reaction-free [[advection–diffusion equation|DG49VBBT91]] $\partial_t Z + \mathbf{u} \cdot \nabla Z = D \Delta Z$.
It equals $1$ in the fuel stream and $0$ in the oxidiser stream.

The *Burke–Schumann flame* is the limit of infinitely fast chemistry, in which fuel and oxidiser cannot coexist: $Y_F Y_O = 0$ everywhere.
Then the flame is the surface $Z = Z_{st}$, with
$$Z_{st} = \frac{Y_{O,2}}{s Y_{F,1} + Y_{O,2}}.$$
On the fuel side $Z > Z_{st}$ one has $Y_O = 0$ and $Y_F = Y_{F,1} (Z - Z_{st}) / (1 - Z_{st})$.
On the oxidiser side $Z < Z_{st}$ one has $Y_F = 0$ and $Y_O = Y_{O,2} (1 - Z / Z_{st})$.
Check: at $Z = Z_{st}$ the numerator $s Y_F - Y_O$ vanishes, and with $Y_F Y_O = 0$ this forces $Y_F = Y_O = 0$; at $Z = 1$ the formula gives $Y_F = Y_{F,1}$, and at $Z = 0$ it gives $Y_O = Y_{O,2}$.

## Remarks

The whole reacting problem reduces to one linear equation for $Z$ and the choice of a level set.
S. P. Burke and T. E. W. Schumann used this idea in 1928 to compute the shape of the flame of a fuel jet surrounded by a coflowing air stream.
With finite reaction rates the flame becomes a thin reaction zone around the surface $Z = Z_{st}$ instead of a sheet.

## Explanations

### L1 human

In a candle or a lighter, fuel and air are not mixed in advance: they meet and burn where they touch.
Burke and Schumann assumed that burning is instant, so fuel and air can never be at the same place.
Then the flame is a thin sheet, located exactly where fuel and air arrive in the right proportion to burn each other completely.
To find the sheet, one only has to solve a mixing problem without any chemistry, which is much easier.
