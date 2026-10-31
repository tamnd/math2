---
records:
    - id: MVQ1AKPK21
      kind: monograph
      title: Permutation Groups
      creators:
        - name: John D. Dixon
          role: author
        - name: Brian Mortimer
          role: author
      date: "1996"
      expressions:
        - key: e1
          kind: edition
          date: "1996"
          ids:
            doi: 10.1007/978-1-4612-0731-3
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1996"
              ids:
                isbn:
                    - "9781461268857"
                    - "9781461207313"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-0731-3
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: MVQWXFXWM7
      kind: preprint
      title: The sixth moment of the Riemann zeta function
      creators:
        - name: Alexandre de Faveri
          role: author
        - name: Mayank Pandey
          role: author
      date: "2026-10-01"
      subjects:
        - system: arxiv
          code: math.NT
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-01"
          ids:
            arxiv: "2610.01035"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.01035"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
