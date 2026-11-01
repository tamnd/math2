---
records:
    - id: G8ZBAYRTJB
      kind: monograph
      title: Nonstandard Asymptotic Analysis
      creators:
        - name: Imme van den Berg
          role: author
      date: "1987"
      expressions:
        - key: e1
          kind: edition
          date: "1987"
          ids:
            doi: 10.1007/bfb0077577
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1987"
              ids:
                isbn:
                    - "9783540177678"
                    - "9783540478102"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0077577
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: G8ZEBKZY8M
      kind: preprint
      title: On Surjective Max-Phase Isometries of Schatten p-Classes (0<p<1)
      creators:
        - name: Wenwen Zhang
          role: author
        - name: Qi Liu
          role: author
      date: "2026-10-09"
      msc:
        - code: 46-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.FA
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-10-09"
          ids:
            arxiv: "2610.13271"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.13271"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2610.13271"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
