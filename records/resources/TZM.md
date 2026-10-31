---
records:
    - id: TZM08VJAQT
      kind: preprint
      title: The Brakke-BV structure of flat flows
      creators:
        - name: Daniele De Gennaro
          role: author
        - name: Salvatore Stuvard
          role: author
      date: "2026-10-11"
      subjects:
        - system: arxiv
          code: math.AP
        - system: arxiv
          code: math.DG
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-11"
          ids:
            arxiv: "2610.15511"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.15511"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
    - id: TZM3NG05C8
      kind: monograph
      title: Numerical Methods in Matrix Computations
      creators:
        - name: Åke Björck
          role: author
      date: "2015"
      expressions:
        - key: e1
          kind: edition
          date: "2015"
          ids:
            doi: 10.1007/978-3-319-05089-8
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2015"
              ids:
                isbn:
                    - "9783319050881"
                    - "9783319050898"
      relations:
        - kind: part_of
          to: 7B8JKAVW9F
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-05089-8
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
