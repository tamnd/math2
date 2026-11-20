---
tag: 6NANBCYMG2
kind: example
name: Change of basis in signal and image processing
msc: ["15A04", "94A08", "42C40"]
topics: [K0FNC6CWZN]
audience: ug2
instance_of: [0MKRHZB3WS]
illustrates: [GZ7NG7J3J8, 047RFCNVSK]
uses: [0MKRHZB3WS, 0S9GGTR0EX, 0AR68JTMDT, GZ7NG7J3J8, 047RFCNVSK, TST0GH66A5]
sources:
  - url: https://en.wikipedia.org/wiki/DFT_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Haar_wavelet
    locator: lead section
  - url: https://en.wikipedia.org/wiki/YCbCr
    locator: JPEG conversion
  - url: https://en.wikipedia.org/wiki/JPEG
    locator: JPEG codec example
---

## Example

A digital signal of length $n$ is a vector in $\mathbb C^n$, written in the standard basis of single samples.
Signal and image processing rewrite it in another basis, where the important part needs few coordinates.
We work out three such bases: the Fourier basis, the Haar basis and the YCbCr basis of colors.

**Part 1: the discrete Fourier transform as a unitary change of basis.**
Let $\omega = e^{-2\pi i / 4} = -i$.
The [[discrete Fourier transform|TST0GH66A5]] of $x \in \mathbb C^4$ is $X = F x$ with $F_{jk} = \omega^{jk}$:
$$F = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & -i & -1 & i \\ 1 & -1 & 1 & -1 \\ 1 & i & -1 & -i \end{pmatrix}.$$

1. The columns of $F$ are orthogonal, and each has squared length $4$. For example, columns $2$ and $3$ give $\overline{1} \cdot 1 + \overline{(-i)} \cdot (-1) + \overline{(-1)} \cdot 1 + \overline{i} \cdot (-1) = 1 - i - 1 + i = 0$.
2. So $F^* F = 4 I$, and $U = \frac12 F$ is a [[unitary matrix|0AR68JTMDT]].
3. Since $F^{-1} = \frac14 F^*$, we have $x = F^{-1} X$. So $X$ holds the coordinates of $x$ in the basis of the columns of $F^{-1}$, the sampled waves $\frac14 (1, \bar\omega^k, \bar\omega^{2k}, \bar\omega^{3k})$. In the language of [[change of basis matrices|0MKRHZB3WS]], $F^{-1}$ changes Fourier coordinates to standard coordinates, and $F$ changes them back.
4. For $x = (1, 2, 3, 4)$: $X_0 = 10$, $X_1 = 1 - 2i - 3 + 4i = -2 + 2i$, $X_2 = 1 - 2 + 3 - 4 = -2$ and $X_3 = -2 - 2i$.
5. Energy: $\norm{X}^2 = 100 + 8 + 4 + 8 = 120$ and $\norm{x}^2 = 1 + 4 + 9 + 16 = 30$. So $\norm{X}^2 = 4 \norm{x}^2$, which is [[Parseval's identity|047RFCNVSK]] for $U$, by the [[properties of a unitary matrix|GZ7NG7J3J8]].
6. The large coefficient $X_0 = 10$ is $4$ times the mean value $2.5$. The other coefficients measure the oscillation.

**Part 2: the Haar basis.**
The Haar vectors of length $4$ are
$$h_0 = \tfrac12 (1, 1, 1, 1), \quad h_1 = \tfrac12 (1, 1, -1, -1), \quad h_2 = \tfrac{1}{\sqrt 2} (1, -1, 0, 0), \quad h_3 = \tfrac{1}{\sqrt 2} (0, 0, 1, -1).$$

1. They form an [[orthonormal basis|0S9GGTR0EX]] of $\mathbb R^4$: each has length $1$, and each pair has dot product $0$, because their supports are disjoint or one is constant on the support of the other.
2. So the coordinates of $x = (6, 4, 5, 1)$ are the dot products: $x \cdot h_0 = 8$, $x \cdot h_1 = 2$, $x \cdot h_2 = \sqrt 2$ and $x \cdot h_3 = 2 \sqrt 2$.
3. Check: $8^2 + 2^2 + (\sqrt 2)^2 + (2 \sqrt 2)^2 = 78 = 36 + 16 + 25 + 1$.
4. Compression: drop the smallest coefficient $\sqrt 2$. The result is $x - \sqrt 2\, h_2 = (5, 5, 5, 1)$, and the error has length $\sqrt 2$, exactly the dropped coefficient.
5. Without the normalization, the Haar transform is "averages and half-differences" of neighbors: $(6, 4, 5, 1) \to (5, 3 \mid 1, 2)$, and then $(5, 3) \to (4 \mid 1)$. The result $(4, 1, 1, 2)$ needs only additions and halvings.

**Part 3: the color spaces RGB and YCbCr.**
A color pixel is a vector $(R, G, B)$ with entries from $0$ to $255$.
JPEG files use the coordinates
$$\begin{pmatrix} Y \\ C_B \\ C_R \end{pmatrix} = \begin{pmatrix} 0 \\ 128 \\ 128 \end{pmatrix} + \begin{pmatrix} 0.299 & 0.587 & 0.114 \\ -0.168736 & -0.331264 & 0.5 \\ 0.5 & -0.418688 & -0.081312 \end{pmatrix} \begin{pmatrix} R \\ G \\ B \end{pmatrix}.$$

1. The matrix $C$ is invertible: $\det C \approx 0.2363 \ne 0$. So $(Y, C_B, C_R)$ is a new coordinate system on the color space, shifted by the vector $(0, 128, 128)$.
2. The rows of $C$ sum to $1$, $0$ and $0$. So a grey pixel $(g, g, g)$ goes to $(g, 128, 128)$: the brightness $Y$ carries all the information, and the two color coordinates are neutral.
3. For the orange pixel $(200, 100, 50)$: $Y = 59.8 + 58.7 + 5.7 = 124.2$, $C_B = 128 - 33.7472 - 33.1264 + 25 = 86.1264$ and $C_R = 128 + 100 - 41.8688 - 4.0656 = 182.0656$.
4. The eye sees detail in brightness better than in color. So JPEG may store $C_B$ and $C_R$ at a lower resolution than $Y$.

**Part 4: JPEG as a chain of changes of basis.**

1. Convert each pixel from RGB to YCbCr, as in part 3.
2. Split each of the three channels into blocks of $8 \times 8$ pixels. Each block is a vector in $\mathbb R^{64}$.
3. Apply the two-dimensional discrete cosine transform to each block. This is a change to an orthonormal basis of $64$ cosine patterns, a real relative of the Fourier basis of part 1.
4. Quantize: round the coefficients, with coarser steps for the high frequencies. Many small coefficients become $0$. Apart from the lower resolution of the color channels, only this step loses information.
5. Encode the result without further loss. Decoding inverts the changes of basis.

## Remarks

The example shows the main idea of transform coding: the change of basis itself loses nothing, but in a good basis most coordinates are small.
Because the bases are orthonormal, the error after dropping coefficients has the length of the dropped part, as in step 4 of part 2.

The choice of basis depends on the signal.
For the smooth ramp $x = (1, 2, 3, 4)$, the Fourier coefficients do not decay fast, because the periodic extension of a ramp jumps from $4$ back to $1$.
For $x = (6, 4, 5, 1)$ with a jump at the end, the Haar coefficient $2 \sqrt 2$ of the jump is large, and the smooth part costs little.
Change the last entry of $x$ from $1$ to $5$: then $x = (6, 4, 5, 5)$, with the coefficients $10$, $0$, $\sqrt 2$ and $0$, and two coefficients suffice.

The theory of the Fourier transform and of wavelets belongs to harmonic analysis and signal processing.
The [[Fourier matrix of size three|SF3EBT2Z4F]] and the [[Haar wavelet|JW5PA9XA7F]] give more detail.

## Explanations

### L1 human

A sound or a picture is a long list of numbers.
The same information can be written as a mixture of simple patterns, such as waves or blocks.
For example, the list $6, 4, 5, 1$ has the average $4$, and the rest is a few up-and-down steps.
In a good choice of patterns, most patterns have tiny weights.
A file format can store only the large weights, and the picture still looks almost the same.

### L2 human

To compress a signal by a change of basis, do these steps.

1. Choose an orthonormal basis that fits the signal: cosines for smooth images, Haar vectors for signals with jumps.
2. Compute the coordinates as dot products, or by a fast transform.
3. Keep the large coordinates and drop or round the small ones.
4. Rebuild the signal from the kept coordinates.

The error of step 3 is the length of the dropped part, by Parseval's identity.
The typical use is JPEG and MP3 compression, and noise removal, where noise spreads over many small coefficients.
The trap is to forget the normalization: with the unnormalized Fourier matrix $F$, the energy grows by the factor $n$.

### L3 human

The discrete Fourier transform diagonalizes every circulant matrix, because the Fourier vectors are the characters of the cyclic group $\mathbb Z / n \mathbb Z$.
This is why it turns cyclic convolution, a linear filter, into pointwise multiplication.
The Haar basis is the simplest wavelet basis, and wavelets give bases adapted to both position and scale.
The fast Fourier transform and the fast wavelet transform factor these change-of-basis matrices into $O(\log n)$ sparse factors, and so need $O(n \log n)$ and $O(n)$ operations.
