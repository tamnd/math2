---
records:
    - id: D4V1GXWFVD
      kind: monograph
      title: Die Approximationseigenschaft lokaler Ringe
      creators:
        - name: Herbert Kurke
          role: author
        - name: Gerhard Pfister
          role: author
        - name: Dorin Popescu
          role: author
        - name: Marco Roczen
          role: author
        - name: Tadeusz Mostowski
          role: author
      date: "1978"
      expressions:
        - key: e1
          kind: edition
          date: "1978"
          ids:
            doi: 10.1007/bfb0068283
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1978"
              ids:
                isbn:
                    - "9783540086567"
                    - "9783540359289"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0068283
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: D4VDVX74FT
      kind: preprint
      title: Mathematical Analysis of Autonomous and Nonautonomous Hepatitis B Virus Transmission Models
      creators:
        - name: Abdallah Alsammani
          role: author
      date: "2023-05-14"
      subjects:
        - system: arxiv
          code: math.DS
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2023-05-14"
          ids:
            arxiv: "2305.08210"
            doi: 10.1007/978-3-031-37108-0_21
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2305.08210"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
